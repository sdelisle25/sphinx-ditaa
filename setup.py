#!/usr/bin/env python

from setuptools import setup, find_packages

PACKAGES = find_packages()

INSTALL_REQUIRES = [
        'setuptools',
        'Sphinx >=1.0.7',
    ]

KEYWORDS = ['sphinx', 'ditaa', 'reST']

CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: System :: Installation/Setup',
        'License :: OSI Approved :: BSD License',
    ]

PLATEFORMS = 'any'
LICENSE = 'BSD'
VERSION = '1.0'

setup(
    name='sphinxcontrib-ditaa',
    author='Arthur Gautier',
    url='https://github.com/baloo/sphinx-ditaa',
    description='Sphinx contribution plugin for rendering Ditaa diagrams',
    namespace_packages=['sphinxcontrib'],
    version=VERSION,
    license=LICENSE,
    platforms=PLATEFORMS,
    packages=PACKAGES,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.5',
)
