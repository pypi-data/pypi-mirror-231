from setuptools import setup, find_packages

setup(
    name='httpquest',
    version='1.0.0',
    description='A Python HTTP request library with advanced features, including error handling, exceptions, and proxy support.',
    author='cxstles',
    author_email='bio@fbi.ac',
    url='https://github.com/cxstles/httpquest',
    install_requires=[
        'brotli',
        'pysocks',
    ],
)