from setuptools import setup

setup(
    name='gee-extraction',
    version='0.0.1',
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