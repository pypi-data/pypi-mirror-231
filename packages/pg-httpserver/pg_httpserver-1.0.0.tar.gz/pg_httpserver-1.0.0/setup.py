from setuptools import setup

DIST_NAME = "pg_httpserver"
DIST_VERSION = "1.0.0"
__author__ = "baozilaji@gmail.com"

setup(
	name=DIST_NAME,
	version=DIST_VERSION,
	description="python game: httpserver",
	packages=['pg_httpserver'],
	author=__author__,
	python_requires='>=3',
	install_requires=[
		'pg-environment>=0',
		'fastapi==0.65.3',
		'uvicorn==0.14.0'
	],
)
