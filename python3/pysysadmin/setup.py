"""
setup.py contains the module/package that will be installed
has been packaged and distributed with Distutils
"""
from setuptools import setup

setup(
    name = 'pysysadmin',
    description = 'Python system admin scripts',
    author = 'Tony Li Xu',
    author_email = 'tonylixu@gmail.com',
    license = 'Apache',
    packages=['pysysadmin'],
    setup_requires = (
        'pytest-runner',
    ),
    tests_require = (
        'pytest',
        'pytest-datafiles',
    ),
)