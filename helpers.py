""" Helper functions """
import os.path
import re
import pycrs

WGS84 = """
GEOGCS[
  "GCS_WGS_1984",
  DATUM[
    "D_WGS_1984", 
    SPHEROID["WGS_1984",6378137,298.257223563]
  ],
  PRIMEM["Greenwich",0],
  UNIT["Degree",0.017453292519943295]
]
"""


def write_prj(fn, datum=WGS84):
    """ Write the .prj file """
    crs = pycrs.parse.from_esri_wkt(datum)
    base = os.path.basename(fn)
    filename = base.split('.')[0]
    folder = os.path.dirname(fn)
    prj = os.path.join(folder, '{}.prj'.format(filename))
    with open(prj, "w") as writer:
        writer.write(crs.to_esri_wkt())
    return prj

def extract_color(text):
    """ Extract color from parsed text """
    pattern = '\#[\d\w]+'
    return re.search(pattern, text).group()


def convert_multipoint_coords(text):
    """ convert multipoint coords in a string into a list of points """
    pattern = '(\d+\.\d+)|(-\d+\.\d+)'
    allcords = re.findall(pattern, text)
    final = []
    for i in range(0, len(allcords)-1, 2):
        coord0 = allcords[i]
        coord0 = coord0[0] if coord0[0] else coord0[1]
        coord1 = allcords[i+1]
        coord1 = coord1[0] if coord1[0] else coord1[1]
        final.append([float(coord0), float(coord1)])
    return final


def extract_color_multipoints(text):
    """ Extract points from text """
    color_pattern = "(\/\*\s*color:\s*#\w+\s*\*\/)"
    with_color = "(\s+)(\w+)(\s*=\s*){}ee.Geometry.MultiPoint\(([\s\S]+?)\)".format(color_pattern)

    match = re.findall(with_color, text)

    result = []
    for m in match:
        midres = dict()
        midres['name'] = m[1]
        midres['color'] = extract_color(m[3])
        coords = m[4].replace('\n', '').replace(' ', '')
        midres['coords'] = convert_multipoint_coords(coords)
        result.append(midres)

    return result