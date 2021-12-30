from setuptools import setup
import os

here = os.path.dirname(os.path.abspath(__file__))
version_ns = {}
with open(os.path.join(here, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name='gee-extraction',
    version=version_ns['__version__'],
    py_modules=['gee-extraction'],
    install_requires=[
        'Click',
        'pyshp'
    ],
    entry_points='''
        [console_scripts]
        gee-extraction=main:main
    ''',
)