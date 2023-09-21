from setuptools import setup, find_packages

# Package metadata
NAME = 'example_emmo00'
VERSION = '0.0.5'
DESCRIPTION = 'A brief description of my package'
AUTHOR = 'Your Name'
AUTHOR_EMAIL = 'your@email.com'
URL = 'https://github.com/yourusername/mypackage'
LICENSE = 'MIT'

# Read the long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# List of required packages
INSTALL_REQUIRES = [
    # List your dependencies here, e.g., 'numpy', 'requests'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    # Other package metadata (e.g., classifiers, entry_points, etc.) can be added here.
)
