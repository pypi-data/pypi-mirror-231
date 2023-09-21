from setuptools import setup, find_packages

readme = ""
license = ""

with open("README.MD", "r") as fh:
    readme = fh.read()
with open("LICENCE", "r") as fh:
    license = fh.read()
 
setup(
    name = "py_aaio",
    version = "1.1.3",
    keywords = ("aaio", ),
    description = "Simple library for AAIO API",
    long_description = readme,
    license = license,
    url = "https://github.com/DephPhascow/py_aaio",
    author = "DephPhascow",
    author_email = "d.sinisterpsychologist@gmail.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["strenum", "requirements"]
)