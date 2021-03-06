#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.argv[-1] == 'publish':
    # Clean existing build artifacts
    os.system('rm -rf dist')
    os.system('rm -rf build')
    os.system('rm -rf rdbms_subsetter.egg-info')

    # Build and publish
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')

    sys.exit()

curdir = os.path.dirname(os.path.realpath(__file__))
readme = open(os.path.join(curdir, 'README.rst')).read()

setup(
    name='rdbms-subsetter',
    version='0.2.6.2',
    description='Generate consistent subset of an RDBMS',
    long_description=readme,
    author='Catherine Devlin',
    author_email='catherine.devlin@gsa.gov',
    url='https://github.com/18F/rdbms-subsetter',
    install_requires=[
        "blinker",
        "sqlalchemy",
    ],
    license="CC0",
    keywords='database testing',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database',
        'Topic :: Software Development :: Testing',
    ],
    packages=find_packages(include=['dialects', 'rdbms_subsetter']),
    entry_points={
        'console_scripts': [
            'rdbms-subsetter = rdbms_subsetter.subsetter:generate',
        ]
    },
)
