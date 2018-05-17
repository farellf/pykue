"""
This code contains my solutions for ISP Module 4 exercises
"""
import random
import math
import csv
import numpy as np
import matplotlib as mpb
import matplotlib.pyplot as plt
from xml.dom import minidom
import copy

#plt.style.use('plot_style.mplstyle')

def get_center(dim_tuple):
    """
    Get an image center with given dimensions in dim_tuple as a tuple
    (width, height).
    """

    return (dim_tuple[0] / float(2), dim_tuple[1] / float(2) )

def draw_USA_map(map_name):
    """
    Given the name of a PNG map of the USA (specified as a string),
    draw this map using matplotlib
    """
    with open(map_name, 'rb') as map_file:
        map = plt.imread(map_file)

    map_plot = plt.imshow(map)
    plt.pyplot.show()


# Parse the XMLin USA SVG file extract county attributes
# Derive from example code -
# https://stackoverflow.com/questions/15857818/python-svg-parser



def get_county_attributes(svg_file_name):
    """
    Given SVG file associate with string svg_file_name, extract county
    attributes from associated XML
    Return a list of tuples consisting of FIPS codes (strings) and
    county boundaries (strings)
    """

    filename = svg_file_name
    doc = minidom.parse(filename)  # parseString also exists
    path_strings = [(path.getAttribute('id'), path.getAttribute('d')) \
    for path in doc.getElementsByTagName('path')]
    doc.unlink()

    return path_strings


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def get_boundary_coordinates(boundary_data):
    """
    Given the country boundary data as a string,
    Return the county boundary as a list of coordinates
    Ignores 'M', 'L, 'z'
    """

    cmd = ['M', 'L', 'z'] # command to ignore

    boundary_data_list = list(filter(lambda a: "M" not in a, \
    boundary_data.split()))

    boundary_data_list = list(filter(lambda a: "L" not in a, \
    boundary_data_list))

    boundary_data_list = list(filter(lambda a: "z" not in a, \
    boundary_data_list))

    boundary_coordinates = []
    s = boundary_coordinates.append
    for coordinates_tup in boundary_data_list:
        x_coord, y_coord = coordinates_tup.split(",")
        s((float(x_coord), float(y_coord)))

    return boundary_coordinates

# Provided code to estimate a county center from a list of coordinates
# on county boundary

def dist(pt1, pt2):
    """
    Compute Euclidean distance between two points
    """
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def compute_county_center(boundary_coordinates):
    """
    Given a list of coordinates (tuples of two floats) on the county
    boundary, Return an estimate of the center of the county as a
    tuple of two floats. Assumes the list of coordinates forms a
    closed polygon with first and last point repeated
    """
    centroid = [0, 0]
    perimeter = 0
    for idx in range(len(boundary_coordinates) - 1):
        edge_length = dist(boundary_coordinates[idx], \
        boundary_coordinates[idx + 1])
        centroid[0] += 0.5 * (boundary_coordinates[idx][0] + \
        boundary_coordinates[idx + 1][0]) * edge_length
        centroid[1] += 0.5 * (boundary_coordinates[idx][1] + \
        boundary_coordinates[idx + 1][1]) * edge_length
        perimeter += edge_length
    return [(centroid[0] / perimeter), (centroid[1] / perimeter)]


def process_county_attributes(svg_file_name, csv_file_name):
    """
    Given SVG file name (as string), extract county attributes
    (FIPS code and county boundaries)
    Then compute county centers and write a CSV file with columns
    corresponding to FIPS code, x-coord of centers, y-coord of centers
    """

    # Extract county attributes from SVG file
    # List of counties in a list of tuples (id, d) where :
            # id corresponds to the county's FIPS code, and the
            # d attribute corresponds to path data (coordinates incl.)

    counties_attr = get_county_attributes(svg_file_name)

    with open(csv_file_name, 'wt', newline ='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Ouput CSV file
        for county in counties_attr:
            # Get boundary coordinates and compute centers
            boundary_coords = get_boundary_coordinates(county[1])
            center_coords = compute_county_center(boundary_coords)
            csvwriter.writerow([str(county[0]), center_coords[0], \
            center_coords[1]])

def make_dict(table, key_col):
    """
    takes a list 𝚝𝚊𝚋𝚕𝚎 and an integer 𝚔𝚎𝚢_𝚌𝚘𝚕 and returns a
    dictionary whose key/value pairs correspond to the rows in 𝚝𝚊𝚋𝚕𝚎.
    In particular, each key should correspond to the entry in column
    𝚔𝚎𝚢_𝚌𝚘𝚕 while the corresponding value is the rest of the row with
    the key deleted
    """
    output_dict = {}

    for dummy_row in copy.deepcopy(table):
        key = dummy_row.pop(key_col)
        output_dict[key] = dummy_row

    return output_dict

def read_csv_file(filename):
    """
    Given a file path specified as the string, 𝚏𝚒𝚕𝚎_𝚗𝚊𝚖𝚎 ,
    load the associated CSV file and return
    a nested list whose entries are the fields in the CSV file.
    Each entry in the returned table is of type 𝚜𝚝𝚛
    """
    nested_list = []
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for dummy_row in csvreader:
            nested_list.append(dummy_row)
    return nested_list

def write_csv_file(csv_table, filename):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated
    CSV file with the name file_name
    """
    with open(filename, 'wt', newline ='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter =',', quoting \
        = csv.QUOTE_MINIMAL)
        for dummy_row in csv_table:
            csvwriter.writerow(dummy_row)

def merge_csv_files(cancer_csv_file, center_csv_file, joined_csv_file):
    """
    Read two specified CSV files as tables
    Join the these tables by shared FIPS codes
    Write the resulting joined table as the specified file
    Analyze for problematic FIPS codes
    """

    # Read in both CSV files
    cancer_filename = cancer_csv_file
    center_filename = center_csv_file
    cancer_data = read_csv_file(cancer_filename)
    center_data = read_csv_file(center_filename)
    joined_data = []
    jd = joined_data.append

    cancer_dict = make_dict(cancer_data, 2)
    center_dict = make_dict(center_data, 0)
    # Remove lines that do not correspond to a FIPS code
    del center_dict['State_Lines']
    del center_dict['separator']

    # Join both dict in a table
    for fips in center_dict.keys():
        if fips in cancer_dict.keys():
            joined_row = [fips]
            joined_row.extend(list(center_dict[fips]))
            joined_row.extend(list((cancer_dict[fips])))
            jd(joined_row)
        else:
            print("==> FIPS {} in center data not in cancer data".\
            format(fips))

    for fips in cancer_dict.keys():
        if fips not in center_dict.keys():
            print("==> FIPS {} in cancer data not in center data".\
            format(fips))

    # Write joined table
    print("{:}".format("==" * 10))
    print("Writing data to : {}".format(joined_csv_file))
    write_csv_file(joined_data, joined_csv_file)

    # Print more information
    print("Wrote joined {} lines to file".format(len(joined_data)))
    print("Center data contained {} FIPS code".\
    format(len(center_dict)))
    print("Cancer data contained {} FIPS code".\
    format(len(cancer_dict)))


def compute_county_cirle(county_population):
    """
    Given county population as integer,
    Compute area of circle proportional to population for use as
    option to scatter() in matplotlib
    """
    scale = 7.5e-05 # Better result should normalize max and min
                # populations and before determining the scale factor.

    return   scale * county_population

# Part 2 - use colormap to define a function that takes risk and
# returns an RGB color

MAX_LOG_RISK = math.log(1.50E-04, 10)   # maximum cancer risk in table
MIN_LOG_RISK = math.log(8.60E-06, 10)   # minimum cancer risk in table

# This helper function has been copied from provided solution
def create_riskmap(colormap):
    """
    Initialize the colormap "jet" from matplotlib,
    Return function that takes risk and returns RGB color for use
    with scatter() in matplotlib
    """

    # Note that this code is tricky - remember to return a
    # lambda expression
    risk_norm = mpb.colors.Normalize(vmin = MIN_LOG_RISK, \
    vmax = MAX_LOG_RISK)
    color_mapper = mpb.cm.ScalarMappable(norm = risk_norm, \
    cmap = colormap)
    return lambda risk : color_mapper.to_rgba(math.log(risk, 10))

def draw_cancer_risk_map(joined_csv_file_name,map_name,num_counties):
    """
    This function takes the name of the joined cancer-risk CSV file
    and the name of the USA map and draws a scatter plot with scatter
    points of fixed size and color at the center of the
    num_counties counties with highest cancer risk.
    Omitting the final optional argument num_counties should default
    to drawing all counties.
    """

    joined_table = read_csv_file(joined_csv_file_name)
    joined_table.sort(
    key = lambda dummy_row : float(dummy_row[-1]), reverse = True)

    with open(map_name, 'rb') as map_file:
        map = mpb.pyplot.imread(map_file)

    #  Get dimensions of the map image
    y_pixels, x_pixels, bands = map.shape

    pixelization = 50
    x_size = x_pixels / pixelization
    y_size = y_pixels / pixelization
    plt.figure(figsize=(x_size,y_size))

    map_plot = mpb.pyplot.imshow(map)
    # Creat an RGB colormap
    risk_map = create_riskmap(mpb.cm.jet)

    for county_data in joined_table[:num_counties]:
        plt.scatter(float(county_data[1]) * x_pixels / 555,\
                    float(county_data[2]) * y_pixels / 352,\
                    s = compute_county_cirle(int(county_data[5])),\
                    c = risk_map(float(county_data[6])))

    plt.show()

# joined_csv_file_name = "/Users/ekue/github/pykue/ISP_exerc/cancer_risk_joined.csv"
# map_name = "/Users/ekue/github/pykue/ISP_exerc/USA_Counties_555x352.png"
# num_counties = 100

# if __name__ == "__main__":
#     process_county_attributes("USA_Counties_2014.svg", \
#     "USA_Counties_with_FIPS_and_centers_test.csv")
#    merge_csv_files("cancer_risk_trimmed_solution.csv", \
#"USA_Counties_with_FIPS_and_centers_test.csv", "cancer_risk_joined.csv")
#   draw_cancer_risk_map(joined_csv_file_name,map_name,num_counties)
