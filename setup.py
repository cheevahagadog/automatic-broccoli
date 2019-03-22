#!/usr/env/bin python

from setuptools import setup, find_packages


setup(name='autobroccoli',
      version='0.0.1',
      description='Make data analysis great again!',
      url='https://github.com/cheevahagadog/automatic-broccoli',
      author='Nathan Cheever',
      author_email='nathan.cheever12@gmail.com',
      license=None,
      packages=find_packages(exclude=['tests', '.idea', '.cache', '__pycache__']),
      include_package_data=True,
      zip_safe=False)
      
