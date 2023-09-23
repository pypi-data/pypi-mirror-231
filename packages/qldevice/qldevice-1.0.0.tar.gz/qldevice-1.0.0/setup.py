from setuptools import setup
from setuptools import find_packages

VERSION = '1.0.0'
AUTHOR='eegion'
EMAIL='hehuajun@eegion.com'

option = {
    "build_exe": {
        "excludes":["test", "main"]
    }
}

setup(
    name='qldevice',  # package name
    version=VERSION,  # package version
    author=AUTHOR,
    author_email=EMAIL,
    description='api for x7 box since v1.0',  # package description
    packages=find_packages(),
    package_data={
        "":["*.txt", "*.md"]
    },
    zip_safe=False
)