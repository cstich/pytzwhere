import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='tzwhere',
    version='1.0',
    packages=['tzwhere'],
    package_data={
        'tzwhere': ['tz_world.json', 'tz_world_compact.json',
                    'tz_world.pickle', 'tz_world.csv']
        },
    install_requires=['shapely']
    include_package_data=True,
    license='MIT License',
    description='Python library to look up timezone from lat / long offline',
    long_description=README,
    url='https://github.com/cstich/pytzwhere3',
    download_url='https://github.com/cstich/pytzwhere3/tarball/1.0',
    author='Christoph Stich',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Localization',
    ],
)
