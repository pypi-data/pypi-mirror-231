from setuptools import setup
from setuptools import find_packages


VERSION = '1.0.6'

setup(
    name='pytestCollectInfoPlugin',  # package name
    version=VERSION,  # package version
    description='Get executed interface information in pytest interface automation framework',  # package description
    packages=find_packages(),
    install_requires=[
        "pytest",
        "importlib-metadata",
        "requests",
    ],
)