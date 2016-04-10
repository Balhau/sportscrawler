from distutils.core import setup
import os
import codecs
from setuptools import setup, find_packages


pname="omxclient"

packages=[pname]+[pname+ "." + name
	for name in os.listdir(os.path.join(pname)) if os.path.isdir(os.path.join(pname, name))]

current_dir=os.path.dirname(__file__)

with codecs.open(os.path.join(current_dir,'README.md'),'r','utf8') as readme_file:
		long_description=readme_file.read()

setup(
	name='sportscrawler',
	author='Balhau',
	author_email='balhau@balhau.net',
	version='1.2.6',
	url='https://git.balhau.net/',
	license='MIT License',
	scripts=[],
	include_package_data = True ,
	description='A python crawler for sports events',
	long_description=__doc__,
    platforms='any',
	packages=packages,
    test_suite="tests",
    install_requires=[
	  	   #'lxml',
		   #'sqlalchemy'
      ]
)
