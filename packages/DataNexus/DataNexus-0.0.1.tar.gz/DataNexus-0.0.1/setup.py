from setuptools import setup, find_packages

setup(
    name='DataNexus',
    version='0.0.1',
    description='A dataset module for your projects',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Ethan Barr',
    author_email='ethanwbarr07@gmail.com',
    url='https://github.com/Ethan-Barr/DataNexus',
    packages=find_packages(),
    install_requires=[
    "Requests==2.28.2"
    ],
)