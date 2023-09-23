import csv
import fiona
import numpy as np
import os
import requests
import subprocess
from ebird.api import get_taxonomy
from pyproj import Transformer
from rasterio import features
from rasterio.windows import Window
from scgt import GeoTiff
from shapely.geometry import shape
from ecoscape_layers.constants import EBIRD_INDIV_RANGE_PATH, EBIRD_INDIV_RANGE_LAYER


class RedList():
    """
    A module of functions that involve interfacing with the IUCN Red List API.
    """

    def __init__(self, redlist_key, ebird_key):
        """
        Initializes a RedList object.
        API keys are required to access the IUCN Red List API and eBird API respectively; see the documentation for more information.
        """
        self.redlist_params = { "token": redlist_key }
        self.ebird_key = ebird_key

    def get_from_redlist(self, url):
        """
        Convenience function for sending GET request to Red List API with the key.

        :param url: the URL for the request.
        :return: response for the request.
        """
        res = requests.get(url, params=self.redlist_params).json()
        return res["result"]

    def get_scientific_name(self, species):
        """
        Translates eBird codes to scientific names for use in Red List.

        :param species: a 6-letter eBird code for a bird species.
        :return: the scientific name of the bird species.
        """
        return get_taxonomy(self.ebird_key, species=species)[0]["sciName"]

    def get_habitats(self, name, region=None):
        """
        Gets habitat assessments for suitability for a given species.
        This also adds the associated terrain map's code and resistance value to the API response, which are useful for creating resistance mappings and/or habitat layers.

        :param name: scientific name of the species.
        :param region: a specific region to assess habitats in (see https://apiv3.iucnredlist.org/api/v3/docs#regions).
        :return: a list of habitats identified by the IUCN Red List as suitable for the species.
        """
        url = "https://apiv3.iucnredlist.org/api/v3/habitats/species/name/{0}".format(name)
        if region is not None:
            url += "/region/{1}".format(region)

        habs = self.get_from_redlist(url)

        for hab in habs:
            code = hab["code"]
            sep = code.index(".")
            # only take up to level 2 (xx.xx), therefore truncating codes with more than 1 period separator
            if code.count(".") > 1:
                code = code[:code.index(".", sep+1)]
            hab["map_code"] = int(code[:sep] + code[sep+1:].zfill(2))
            hab["resistance"] = 0 if hab["majorimportance"] == "Yes" else 0.1

        return habs


class LayerGenerator(object):
    """
    For things like reprojecting, building resistance tables, and creating habitat layers and matrix (terrain) layers.
    This class maintains a common CRS, resolution, and resampling method for this purpose.
    """

    def __init__(self, terrain_path, terrain_codes_path, crs=None, resolution=None, resampling="near", bounds=None, padding=0):
        """
        Initializes a HabitatGenerator object.

        :param terrain_path: file path to the initial terrain raster.
        :param terrain_codes_path: file path to a CSV containing terrain resistance codes. If not generated, it may be generated from the terrain using the generate_resistance_table method.
        :param crs: desired common CRS of the layers as an ESRI WKT string.
        :param resolution: desired resolution of the layers in the units of the CRS as an integer.
        :param resampling: resampling method if resampling is necessary to produce layers with the desired CRS and/or resolution.
        """
        self.orig_terrain_path = os.path.abspath(terrain_path)
        self.terrain_path = self.orig_terrain_path
        self.terrain_codes_path = os.path.abspath(terrain_codes_path)
        self.crs = crs
        self.resolution = resolution
        self.resampling = resampling
        self.bounds = bounds
        self.padding = padding

        # rio_resampling accounts for rasterio's different resampling parameter names from gdal
        if self.resampling == "near":
            self.rio_resampling = "nearest"
        elif self.resampling == "cubicspline":
            self.rio_resampling = "cubic_spline"
        else:
            self.rio_resampling = self.resampling

    def generate_terrain(self):
        """
        Generates the terrain layer based on the paramters specified at initialization.
        If no reprojection or cropping is needed, it may not be necessary to generate a new layer file.
        If generation was already done before, then repeated generations start from the original file
        rather than any new ones that were created.
        """

        if self.orig_terrain_path != self.terrain_path:
            print("A new terrain layer has already been generated before. Generation will proceed with the original terrain that was inputted on initialization, which may overwrite any previously generated terrain layers.")
            self.terrain_path = self.orig_terrain_path

        # reproject/crop terrain if needed
        self.reproject_terrain()
        if self.bounds is not None:
            self.crop_terrain()
        if self.orig_terrain_path != self.terrain_path or not os.path.exists(self.terrain_codes_path):
            self.write_map_codes()

    def reproject_terrain(self):
        """
        Reprojects the terrain to the CRS and resolution desired if needed, creating a new file in doing so.
        terrain_path is reassigned to the path of this new file.
        The CRS and resolution are taken from the current class instance's settings if specified.
        If reprojection occurs, the resampling method used is taken from the current class instance.
        """
        with GeoTiff.from_file(self.terrain_path) as ter:
            if self.crs is None:
                self.crs = ter.dataset.crs
            if self.resolution is None:
                self.resolution = int(ter.dataset.transform[0])
            
            # reproject terrain if resolution and/or CRS attributes differ from current resolution and CRS
            if self.resolution != int(ter.dataset.transform[0]) or self.crs != ter.dataset.crs:
                reproj_terrain_path = self.append_settings_to_name(self.terrain_path)
                ter.reproject_from_crs(reproj_terrain_path, self.crs, (self.resolution, self.resolution), self.rio_resampling)
                self.terrain_path = reproj_terrain_path

    def crop_terrain(self):
        """
        Crops the terrain to the desired bounding rectangle with optional padding.
        This does not modify the existing file, but creates a new one that terrain_path is assigned to.
        """
        if not isinstance(self.bounds, tuple):
            raise TypeError("Bounds should be given as a tuple")
        if len(self.bounds) != 4:
            raise ValueError("Invalid bounding box")

        with GeoTiff.from_file(self.terrain_path) as file:
            cropped_terrain_path = self.terrain_path[:-4] + "_cropped.tif"
            cropped_file = file.crop_to_new_file(cropped_terrain_path, bounds=self.bounds, padding=self.padding)
            cropped_file.dataset.close()
            self.terrain_path = cropped_terrain_path

    def get_map_codes(self):
        """
        Obtains the list of unique terrain map codes from terrain_codes_path, if the file path exists.
        This is used to determine the map codes for which resistance values need to be defined.
        """
        if not os.path.isfile(self.terrain_codes_path):
            raise FileNotFoundError("Terrain codes file not found, generate with write_map_codes")

        all_map_codes = []
        with open(self.terrain_codes_path, newline="") as ter_codes:
            for row in csv.reader(ter_codes):
                all_map_codes.append(int(row[0]))
        return all_map_codes

    def write_map_codes(self):
        """
        Finds the unique map code values from the terrain tiff and writes them to a CSV located at terrain_codes_path, for creating resistance tables later.
        """
        all_map_codes = set()

        # find all map codes in the terrain
        with GeoTiff.from_file(self.terrain_path) as ter:
            reader = ter.get_reader(b=0, w=10000, h=10000)
            for tile in reader:
                tile.fit_to_bounds(width=ter.width, height=ter.height)
                window = Window(tile.x, tile.y, tile.w, tile.h)
                all_map_codes.update(np.unique(ter.dataset.read(window=window)))

        # write map codes to a csv file in a single column
        with open(self.terrain_codes_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for map_code in all_map_codes:
                writer.writerow([map_code])

    def get_ranges_from_ebird(self, species_list_path, species_range_folder):
        """
        Downloads range map shapefiles from eBird by using the ebirdst R package.
        This utilizes the R script "ebird_range_download.r" to download the ranges.
        An API key for eBird is required; see the documentation for more information.

        :param species_list_path: list of species to download range map shapefiles for, given as 6-letter eBird codes.
        :param species_range_folder: folder to which the downloaded range maps should be saved.
        """
        if not os.path.exists(species_range_folder):
            os.makedirs(species_range_folder)

        downloader_path = os.path.join(os.path.dirname(__file__), "ebird_range_download.r")
        result = subprocess.run(["Rscript", downloader_path, species_list_path, species_range_folder], capture_output=True, text=True)

        if result.returncode != 0:
            print(result)
            raise AssertionError("Problem occurred while downloading ranges")

    def generate_resistance_table(self, habitats, map_codes, output_path):
        """
        Generates the terrain-to-resistance table for a given species as a CSV file using habitat preference data from the IUCN Red List.
        - Major importance terrain is assigned a resistance of 0.
        - Suitable (but not major importance) terrain is assigned a resistance of 0.1.
        - All other terrains are assigned a resistance of 1.

        :param habitats: IUCN Red List habitat data for the species for which the table should be generated.
        :param map_codes: list of map codes to assign resistances to.
        :param output_path: path of CSV file to which the species' resistance table should be saved.
        """
        with open(output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(habitats[0].keys())
            # map codes from the terrain map
            for map_code in map_codes:
                h = next((hab for hab in habitats if hab["map_code"] == map_code), None)
                if h is not None:
                    writer.writerow(h.values())
                else:
                    writer.writerow([''] * 5 + [map_code] + [1])

    def refine_habitat(self, ter, habitats, shapes, output_path, refine_method="forest_add308"):
        """
        Creates the habitat layer for a given species based on the terrain and range map.

        :param ter: open instance of the terrain GeoTiff.
        :param habitats: IUCN Red List habitat data for the species for which the habitat layer should be generated.
        :param shapes: list of shapes to use as the range map, given in the same projection as the terrain.
        :param output_path: file path to save the habitat layer to.
        :param refine_method: used to decide what terrain should be considered for habitat.
        """

        shapes = [shape(shapes["geometry"])]

        with ter.clone_shape(output_path) as output:
            reader = output.get_reader(b=0, w=10000, h=10000)
            good_terrain_for_hab = self.get_good_terrain(habitats, refine_method)

            for tile in reader:
                # get window and fit to the tiff's bounds if necessary
                tile.fit_to_bounds(width=output.width, height=output.height)
                window = Window(tile.x, tile.y, tile.w, tile.h)

                # mask out pixels from terrain not within range of shapes
                window_data = ter.dataset.read(window=window, masked=True)
                shape_mask = features.geometry_mask(shapes, out_shape=(tile.h, tile.w), transform=ter.dataset.window_transform(window))
                window_data.mask = window_data.mask | shape_mask
                window_data = window_data.filled(0)

                # get pixels where terrain is good
                window_data = np.isin(window_data, good_terrain_for_hab)

                output.dataset.write(window_data, window=window)

            # remove old attribute table if it exists so that values can be updated
            if os.path.isfile(output_path + ".aux.xml"):
                os.remove(output_path + ".aux.xml")

    def get_good_terrain(self, habitats, refine_method="forest_add308"):
        """
        Determine the terrain deemed suitable for habitat based on the refining method.
        This decides what terrain map codes should be used to filter the habitat.

        :param habitats: IUCN Red List habitat data for the species for which suitable terrain is computed.
        :param refine_method: method by which habitat pixels should be selected ("forest", "forest_add308", "allsuitable", or "majoronly"). See documentation for detailed descriptions of each option.
        :return: list of terrain map codes filtered by refine_method.
        """

        if refine_method == "forest":
            return [x for x in range(100, 110)]
        elif refine_method == "forest_add308":
            return [x for x in range(100, 110)] + [308]
        elif refine_method == "allsuitable":
            return [hab["map_code"] for hab in habitats if hab["suitability"] == "Suitable"]
        elif refine_method == "majoronly":
            return [hab["map_code"] for hab in habitats if hab["majorimportance"] == "Yes"]

    def append_settings_to_name(self, file_path):
        """
        Adds the resolution and resampling settings to the file path name.
        If the old file name is "filename.ext", the new name is "filename_[resolution]_[resampling].ext".

        :param file_path: file path to modify.
        :return: modified version of the file path.
        """

        sep = file_path.index(".")
        return file_path[:sep] + "_" + str(self.resolution) + "_" + self.resampling + file_path[sep:]

def reproject_shapefile(shapes_path, dest_crs, shapes_layer=None, file_path=None):
    """
    Takes a specified shapefile or geopackage and reprojects it to a different CRS.

    :param shapes_path: file path to the shapefile or geopackage to reproject.
    :param dest_crs: CRS to reproject to as an ESRI WKT string.
    :param shapes_layer: if file is a geopackage, the name of the layer that should be reprojected.
    :param file_path: if specified, the file path to write the reprojected result to as a shapefile.
    :return: list of reprojected features.
    """

    myfeatures = []

    with fiona.open(shapes_path, 'r', layer=shapes_layer) as shp:
        # create a Transformer for changing from the current CRS to the destination CRS
        transformer = Transformer.from_crs(crs_from=shp.crs_wkt, crs_to=dest_crs, always_xy=True)

        # loop through polygons in each features, transforming all point coordinates within those polygons
        for feature in shp:
            for i, polygon in enumerate(feature['geometry']['coordinates']):
                for j, ring in enumerate(polygon):
                    if isinstance(ring, list):
                        feature['geometry']['coordinates'][i][j] = [transformer.transform(*point) for point in ring]
                    else:
                        # "ring" is really just a single point
                        feature['geometry']['coordinates'][i][j] = [transformer.transform(*ring)]
            myfeatures.append(feature)

        # if file_path is specified, write the result to a new shapefile
        if file_path is not None:
            meta = shp.meta
            meta.update({
                'driver': 'ESRI Shapefile',
                'crs_wkt': dest_crs
            })
            with fiona.open(file_path, 'w', **meta) as output:
                output.writerecords(myfeatures)

    return myfeatures

def generate_layers(redlist_key, ebird_key, species_list_path, terrain_path, terrain_codes_path=None,
                    species_range_folder=None, output_folder=None, crs=None, resolution=None, resampling="near", bounds=None, padding=0, refine_method="forest"):
    """
    Runner function for full process of habitat and matrix layer generation.

    :param redlist_key: IUCN Red List API key.
    :param ebird_key: eBird API key.
    :param species_list_path: file path to text file of the bird species for which habitat layers should be generated, formatted as 6-letter eBird species codes on individual lines.
    :param terrain_path: file path to initial terrain raster.
    :param terrain_codes_path: file path to a CSV containing terrain resistance codes. If not generated, it can be generated by setting reproject_inputs to True.
    :param species_range_folder: folder path for where downloaded eBird range maps should be saved.
    :param output_folder: folder path to place habitat layer output files and terrain-to-resistance CSV files into.
    :param crs: desired common CRS of the layers as an ESRI WKT string.
    :param resolution: desired resolution in the units of the chosen CRS, or None to use the resolution of the input terrain raster.
    :param resampling: resampling method if resampling is necessary to produce layers with the desired CRS and/or resolution; see https://gdal.org/programs/gdalwarp.html#cmdoption-gdalwarp-r for valid arguments.
    :param bounds: bounds to crop generated layers to in the units of the chosen CRS, specified as a bounding box (xmin, ymin, xmax, ymax).
    :param padding: padding in units of chosen CRS to add around the bounds.
    :param refine_method: method by which habitat pixels should be selected ("forest", "forest_add308", "allsuitable", or "majoronly"). See documentation for detailed descriptions of each option.
    """

    REDLIST_KEY = redlist_key
    EBIRD_KEY = ebird_key

    # Define some default output files and directories.
    current_dir = os.getcwd()
    if terrain_codes_path is None:
        terrain_codes_path = os.path.join(current_dir, "terrain_codes.csv")
    if species_range_folder is None:
        species_range_folder = os.path.join(current_dir, "ebird_ranges")
    if output_folder is None:
        output_folder = os.path.join(current_dir, "outputs")

    # Define eBird-specific range map path and gpkg layer.
    indiv_range_path = os.path.join(species_range_folder, EBIRD_INDIV_RANGE_PATH)
    indiv_range_layer = EBIRD_INDIV_RANGE_LAYER

    # Get the list of bird species from species_list_path.
    with open(species_list_path) as file:
        species_list = file.read().splitlines()

    # Generate output folder.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate species output folders.
    for species in species_list:
        species_output_folder = os.path.join(output_folder, species)
        if not os.path.exists(species_output_folder):
            os.makedirs(species_output_folder)
    
    # Initialize RedList and LayerGenerator instances.
    redlist = RedList(REDLIST_KEY, EBIRD_KEY)
    layer_generator = LayerGenerator(terrain_path, terrain_codes_path, crs, resolution, resampling,
                                        bounds, padding)

    # Generate terrain layer.
    print("Generating terrain layer...")
    layer_generator.generate_terrain()
    
    # Obtain species habitat information from the IUCN Red List.
    print("Gathering species habitat preferences...")
    species_data = []

    for species in species_list:
        sci_name = redlist.get_scientific_name(species)
        habs = redlist.get_habitats(sci_name)

        # Manual corrections for differences between eBird and IUCN Red List scientific names.
        if species == "whhwoo":
            sci_name = "Leuconotopicus albolarvatus"
            habs = redlist.get_habitats(sci_name)
        if species == "yebmag":
            sci_name = "Pica nutalli"
            habs = redlist.get_habitats(sci_name)

        if len(habs) == 0:
            print("Skipping", species, "due to not finding info on IUCN Red List (perhaps a name mismatch with eBird)?")
            continue
        else:
            species_data.append({
                "name": species,
                "sci_name": sci_name,
                "habitats": habs
            })

    # Download species ranges as shapefiles from eBird.
    print("Downloading species range maps...")
    layer_generator.get_ranges_from_ebird(species_list_path, species_range_folder)

    # Create the resistance table for each species.
    print("Creating resistance CSVs...")
    all_map_codes = layer_generator.get_map_codes()
    for species in species_data:
        code = species["name"]
        resistance_output_path = os.path.join(output_folder, code, f"{code}_resistance.csv")
        layer_generator.generate_resistance_table(species["habitats"], all_map_codes, resistance_output_path)

    # Perform the intersection between the range and habitable terrain.
    print("Generating habitat layers...")
    with GeoTiff.from_file(layer_generator.terrain_path) as ter:
        resolution = int(ter.dataset.transform[0])
        resampling = layer_generator.resampling

        for species in species_data:
            if species == "":
                break

            code = species["name"]

            if not os.path.isfile(indiv_range_path.format(code=code)):
                print("Skipping {code}, no associated range map found".format(code=code))
                continue

            range_shapes = reproject_shapefile(
                shapes_path=indiv_range_path.format(code=code),
                dest_crs=layer_generator.crs,
                shapes_layer=indiv_range_layer
            )

            if len(range_shapes) == 1:
                # not a seasonal bird
                path = os.path.join(output_folder, code, f"habitat_2020_{resolution}_{resampling}_{refine_method}.tif")
                layer_generator.refine_habitat(ter, species["habitats"], range_shapes[0], path, refine_method)
            else:
                # seasonal bird, different output for each shape
                for s in range_shapes:
                    season = str(s["properties"]["season"])
                    path = os.path.join(output_folder, code, f"{season}_habitat_2020_{resolution}_{resampling}_{refine_method}.tif")
                    layer_generator.refine_habitat(ter, species["habitats"], s, path, refine_method)
    
    print("Layers successfully generated in " + output_folder)