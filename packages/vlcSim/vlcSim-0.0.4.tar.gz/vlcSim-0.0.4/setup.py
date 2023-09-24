from setuptools import find_packages, setup
from distutils.core import setup, Extension

SETUP_REQUIRES = ["setuptools", "wheel"]

INSTALL_REQUIRES = ["numpy", "enum34"]

setup(
    name="vlcSim",
    version="0.0.4",
    license="MIT",
    description="Python Package of Event-Oriented Simulation for visible light communication",
    author="Danilo Bórquez-Paredes",
    author_email="danilo.borquez.p@uai.cl",
    url="https://gitlab.com/DaniloBorquez/simvlc/",
    packages=["vlcsim"],
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,  # to prevent Cython fail: Note also that if you use setuptools instead of distutils, the default action when running python setup.py install is to create a zipped egg file which will not work with cimport for pxd files when you try to use them from a dependent package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
