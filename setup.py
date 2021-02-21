from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Real Time Track of ISS'
# Setting up
setup(
    name="isstrack_zilio",
    version=VERSION,
    author="Ziliotto Filippo",
    author_email="filippo.ziliotto1996@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['plotly', 'pandas'],
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
