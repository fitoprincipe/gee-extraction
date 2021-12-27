# gee-extraction
## Extract Features from Google Earth Engine Scripts

Google Earth Engine's code editor brings you the possibility to create Features (Points, Lines, Polygons) and Feature Collections, which can even be a mix of Points, Lines and Polygons, and save it "in the code". But, sometimes you need to download those Features to your local drive, to use it with your preferred local software.

This code aims to make that process easy and automatic.

This code will be pure python, using simple libraries for file managements and [pyshp](https://github.com/GeospatialPython/pyshp) for exporting to shapefiles format.

WIP