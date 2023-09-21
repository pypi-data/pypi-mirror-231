import os

import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()


# Get the code version
version = {}
with open(os.path.join(here, "optiguide/version.py")) as fp:
    exec(fp.read(), version)
__version__ = version["__version__"]

install_requires = [
    "openai",
    "diskcache",
    "termcolor",
    "flaml",
    "autogen",
    "eventlet",
    "gurobipy"
]


setuptools.setup(
    name="OptiGuide",
    version=__version__,
    author="Beibin Li",
    author_email="beibin.li@microsoft.com",
    description="Large Language Models for Supply Chain Optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/optiguide",
    packages=setuptools.find_packages(include=["optiguide*"]),
    package_data={
        "optiguide.default": ["*/*.json"],
    },
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "test": [
            "pytest>=6.1.1",
            "pre-commit",
            "nbconvert",
            "nbformat",
            "ipykernel",
            "pydantic==1.10.9",
            "sympy",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
