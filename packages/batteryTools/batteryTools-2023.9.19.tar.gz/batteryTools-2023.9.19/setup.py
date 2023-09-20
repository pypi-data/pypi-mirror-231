__version__ = '2023.09.19'
__author__ = 'PABLO PILA'
__author_email__ = "pablogonzalezpila@gmail.com"

''' 
NOTES:
TASK:
WARNINGS:
'''

from setuptools import setup, find_packages

setup(
    name = "batteryTools",
    # packages = find_packages(), # con find_pachages no conseguir hacerlo funcionar
    packages=["batteryTools"],
    include_package_data=True, # muy importante para que se incluyan archivos sin extension .py
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    url = "https://github.com/PaulFilms/battery-tools.git",
    long_description = "README.md",
    license = "www.unlicense.org",
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        ]
)
