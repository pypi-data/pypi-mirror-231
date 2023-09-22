from setuptools import setup, find_packages

setup(
    name='post-processing-library',
    version='0.1',
    description='A library for post-processing entities',
    author='Tushar',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'fuzzywuzzy',
    ],
)
