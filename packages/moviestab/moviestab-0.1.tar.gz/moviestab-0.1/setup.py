'''
from distutils.core import setup
setup(
	name = 'nester',
	version = '1.0.0',
	py_modules = ['nester'],
	author = 'hfpython',
	author_email = '3175454707@qq.com',
	url = 'http://www.headfirstlabs.com',
	description = 'A simple printer of nested lists',)
'''
import setuptools

from setuptools import setup,find_packages
setuptools.setup(
    name = 'moviestab',
    version = '0.1',
    author = 'sgys_22',
    description = 'a tool of list to eval all figure',
    authour_email = '3175454707@qq.com',
    packages = find_packages(),
)
