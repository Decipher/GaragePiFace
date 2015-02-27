#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def package_data_dirs(source, sub_folders):
	dirs = []

	for d in sub_folders:
		for dirname, _, files in os.walk(os.path.join(source, d)):
			dirname = os.path.relpath(dirname, source)
			for f in files:
				dirs.append(os.path.join(dirname, f))

	return dirs


def params():
	name = 'GaragePiFace'
	version = '0.1'
	description = '@TODO'
	author = "Stuart Clark"
	author_email = "stu@rtclark.net"
	url = "http://stuar.tc"

	packages = find_packages(where="src")
	package_dir = {"garagepiface": "src/garagepiface"}
	package_data = {"garagepiface": package_data_dirs('src/garagepiface', ['static', 'templates'])}

	include_package_data = True
	zip_safe = False
	install_requires = open("requirements.txt").read().split("\n")

	return locals()

setup(**params())