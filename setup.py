#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='extract_trajectory_elevation_matrix',
      version='0.1',
      description='Algorithm of elevation matrix extraction for the particular trajectory.',
      long_description='Algorithm of elevation matrix extraction for the particular trajectory.',
      classifiers=[
        'Programming Language :: Python :: 3.7',
      ],
      keywords='elevation_matrix, pyphased',
      url='https://github.com/KrepakVitaly/extract_trajectory_elevation_matrix',
      author='Vitaliy Krepak',
      author_email='krepakvitaliy@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
