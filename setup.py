#!/usr/bin/env python

from distutils.core import setup
import os

toilet_dir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'toilet'

setup(
    name="toilet",
    version="0.1",
    author="Benjamin Grandfond",
    author_email="benjaming@theodo.fr",
    maintainer="Benjamin Grandfond",
    maintainer_email="benjaming@theodo.fr",
    url="http://github.com/theodo/toilet",
    description="Theodo toilets availability status ubuntu indicator.",
#    package_dir={'': 'toilet'},
#    package_dir={
#      toilet_dir: 'indicator',
#      toilet_dir: 'toilet',
#      toilet_dir: 'dataloader', 
#    },
    py_modules=['toilet.toilet', 'toilet.dataloader', 'toilet.indicator'],
    scripts=['app-toilet']
)
