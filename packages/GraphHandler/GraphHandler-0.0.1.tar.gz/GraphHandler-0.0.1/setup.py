from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Facebook Graph API Handler'
LONG_DESCRIPTION = 'A Facebook Graph API Handler to ease the use of Meta Graph APIs.'

# Setting up
setup(
    name="GraphHandler",
    version=VERSION,
    author="Ambar Rizvi",
    author_email="<brannstrom9911@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests==2.31.0', 'typing==3.7.4.3'],
    keywords=['python', 'facebook', 'graph api', 'social media', 'instagram', 'meta', 'meta api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
