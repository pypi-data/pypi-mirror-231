"""Setup for aryahelpers modules"""
from setuptools import setup, find_packages

BASE_REPO = 'https://gitlab.leoforce.com/ratnadip.adhikari/arya-helpers'

setup(
    name='aryahelpers',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    version='0.0.1',
    description='Arya Helpers Modules',
    long_description='Global Intel using ML Lite + SJA',
    author='Ratnadip Adhikari',
    author_email='ratnadip.adhikari@leoforce.com',
    url=BASE_REPO + '.git',
    download_url=BASE_REPO,
    keywords=['utilities', 'arya', 'helper modules'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ],
    platforms=['any'],
    install_requires=[],
    # include_package_data=True
)
