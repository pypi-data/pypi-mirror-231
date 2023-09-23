from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: MacOS",
    "Operating System :: Microsoft",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

setup(
    name="loadsure_data",
    version="0.1.1",
    description="This package contains all the classes we use on the data team to complete API integrations and also classes to update, create and delete things related to BigQuery and Firebase",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="https://github.com/Loadsure/packages-py.git",
    author="Loadsure Data Team",
    author_email="data-team@loadsure.net",
    license="MIT",
    classifiers=classifiers,
    package_dir={"": "packages"},
    packages=find_packages(where='packages'),
)
