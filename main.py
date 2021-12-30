import click
import os
import helpers
import shapefile as pyshp


@click.group()
def main():
    pass


@main.command()
@click.argument('fn')
@click.argument('result_fn')
def points2shape(fn, result_fn):
    """ Extract points from a GEE's code editor script and save them into a shapefile

    Parameters:

    - FN: Input filename. Must be a JavaScript code coming from GEE's code editor

    - RESULT_FN: The resulting filename for the shapefile
    """
    fpath = os.path.join(os.getcwd(), fn)
    with open(fpath, 'r') as thefile:
        content = thefile.read()
        multipoints = helpers.extract_color_multipoints(content)
        with pyshp.Writer(result_fn, 8) as writeshp:
            writeshp.field('Name', 'C', size=50)
            writeshp.field('Color', 'C', size=10)
            for data in multipoints:
                # print(data)
                writeshp.record(data['name'], data['color'])
                writeshp.multipoint(data['coords'])

    # PRJ
    helpers.write_prj(result_fn)
    return result_fn
