#!/usr/bin/env python

from __future__ import absolute_import
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name=u'fastjsonschema',
    version=u'1.1',
    packages=[u'fastjsonschema'],

    install_requires=[
        u'requests',
    ],
    extras_require={
        u"test": [
            u"colorama",
            u"jsonschema",
            u"json-spec",
            u"pytest",
            u"validictory",
        ],
    },

    url=u'https://github.com/seznam/python-fastjsonschema',
    author=u'Michal Horejsek',
    author_email=u'horejsekmichal@gmail.com',
    description=u'Fastest Python implementation of JSON schema',
    license=u'BSD',

    classifiers=[
        u'Programming Language :: Python',
        u'Programming Language :: Python :: 2.7',
        u'License :: OSI Approved :: BSD License',
        u'Operating System :: OS Independent',
        u'Development Status :: 5 - Production/Stable',
        u'Intended Audience :: Developers',
        u'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
