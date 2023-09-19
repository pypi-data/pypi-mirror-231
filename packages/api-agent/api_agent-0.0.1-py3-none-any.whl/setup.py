"""Package setup File for the db copilot tool."""
import os

from setuptools import find_packages, setup

setup(
    name="api_agent",
    version="0.0.1"
    if not os.environ.get("RELEASE_VERSION")
    else os.environ.get("RELEASE_VERSION"),
    packages=find_packages(),
    install_requires=[
    ],
    author="Microsoft Corporation",
    author_email="qiangli@microsoft.com",
    description="API Agent. Enables copilot to use thousands of APIs.",
    long_description=open("../README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
)
