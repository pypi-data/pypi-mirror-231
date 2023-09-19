from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme = file.read()

VERSION = "0.0.1"

setup(
    name="marzpy",
    version=VERSION,
    author="Mewhrzad",
    description="a simple application with python to manage Marzban panel",
    long_description="text/markdown",
    url="https://github.com/Mewhrzad/marzpy",
    keywords=["marzpy", "Marzban", "Gozargah", "Marzban python", "Marzban API"],
    packages=find_packages(),
    requires=["requests"],
    classifiers=["Programming Language :: Python :: 3"],
)
