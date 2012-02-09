#!/usr/bin/env python

from distutils.core import setup

setup(
    name="toilet",
    version="0.1",
    author="Benjamin Grandfond",
    author_email="benjaming@theodo.fr",
    description="Theodo toilets availability status ubuntu indicator.",
    #packages=['os', 'gtk', 'appindicator', 'json', 'urllib2'],
    scripts=['toilet/indicator.py']
)