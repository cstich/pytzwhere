pytzwhere
=========

pytzwhere is a Python 3 library to lookup the timezone for a given lat/lng entirely offline

It is a port from https://github.com/pegler/pytzwhere with a few improvements. It is faster (in the order of 100s) and uses less memory (150MB vs 750MB). Initialization is slower though and the library now requires the shapely package. This also means you need 'geos_c'.
The original library does not seem to be maintaned anymore. If that changes in the future, I am happy to merge the codebase, but I couldn't get hold of the original author. 

If used as a library, basic usage is as follows:

    >>> from tzwhere import tzwhere
    >>> tz = tzwhere.tzwhere()
    Reading csv input file: tz_world_compact.csv
    >>> print(tz.tzNameAt(35.29, -89.66))
    America/Chicago


The polygons used for building the timezones are based on VMAP0. Sometimes points are outside a VMAP0 polygon, but are clearly within a certain timezone (see also this [discussion](https://github.com/mattbornski/tzwhere/issues/8)). As a somewhat 'hacky' workaround you can tell the library to return the closest timezone if it doesn't find a proper timezone. This costs you another 80MB of RAM or so.

    >>> tz = tzwhere.tzwhere(closest=True)
    Reading csv input file: tz_world_compact.csv
    >>> tz.tzNameAt(40.7271, -73.98)
    >>> tz.tzNameAt(40.7271, -73.98, closest=True)
    'America/New_York'


The module can also be run as a script. Instructions and usage information can be seen by running:

    tzwhere.py --help

Dependencies (both optional):

  * `docopt` - if you want to use `tzwhere.py` as a script (e.g. as shown above).

  * `numpy` - if you want to save about 200MB of RAM.
