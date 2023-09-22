from setuptools import setup, find_packages

setup(
    name='post_processing_library_tushar',
    version='0.1',
    description='A library for post-processing entities',
    author='Tushar',
    author_email='mahuritushar@gmail.com',
    packages=find_packages(),
    install_requires=[
        'fuzzywuzzy',
    ],
)
