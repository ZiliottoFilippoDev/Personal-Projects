from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Tracking ISS '
LONG_DESCRIPTION = 'Tracks the International Space Station in real time and plots the location'

# Setting up
setup(
    name="iss_track",
    version=VERSION,
    author="Ziliotto Filippo",
    author_email="filippo.ziliotto1996@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['plotly', 'json', 'time', 'urllib.request', 'pandas'],
    keywords=['python', 'ISS', 'Tracking', 'Plotly', 'map'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)