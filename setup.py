#!/usr/bin/env python

from setuptools import setup, find_packages

requires = [
        'setuptools',
        'Sphinx >=1.0.7',
    ],

setup(
    name='sphinxcontrib-ditaa',
    author='Sylvain Delisle',
    author_email='sylvain.delisle25@gmail.com',
    url='https://github.com/sdelisle25/sphinxcontrib-ditaa',
    description='Sphinx contribution plugin for rendering Ditaa diagrams',
    version='1.0',
    license="BSD",
    platforms='any',
    install_requires=requires,
    packages=find_packages(),
    include_package_data=False,
    namespace_packages=['sphinxcontrib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: System :: Installation/Setup',
        'License :: OSI Approved :: BSD License',
    ],

)
