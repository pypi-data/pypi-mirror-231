import os

from setuptools import find_packages, setup


def read(fname: str) -> str:
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="nincore",
    version="0.0.1",
    author="Ninnart Fuengfusin",
    author_email="ninnart.fuengfusin@yahoo.com",
    description="Core utilities nin's packages.",
    license="Apache License 2.0",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    classifier=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
