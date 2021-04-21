import setuptools
from setuptools.command.install import install
import os

def getversion():
	'''
	read the version string from __init__
	
	'''
	#get the init file path
	thispath = os.path.abspath(os.path.dirname(__file__))+'/'
	initfile = thispath + 'PyFileIO/__init__.py'
	
	#read the file in
	f = open(initfile,'r')
	lines = f.readlines()
	f.close()
	
	#search for the version
	version = 'unknown'
	for l in lines:
		if '__version__' in l:
			s = l.split('=')
			version = s[-1].strip().strip('"').strip("'")
			break
	return version
	
version = getversion()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyFileIO",
    version=version,
    author="Matthew Knight James",
    author_email="mattkjames7@gmail.com",
    description="Some very basic  routines for file IO in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattkjames7/PyFileIO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    install_requires=[
		'numpy',
		'RecarrayTools',
	],
)



