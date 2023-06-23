from setuptools import setup, find_packages

setup(
    name='scratch_getdata',
    version='0.0.6',
    author='kokofixcomputers',
    description='A Module to fetch scratch things from ScratchGetData',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={'': ['docs/*']},
    install_requires=['requests'],
)
