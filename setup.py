import setuptools
import os
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "SHeD-Subspace-for-Heterogeneous-Domains"

AUTHOR_USER_NAME = "ArunavoDey"
SRC_REPO = "SHED"
AUTHOR_EMAIL = "arunavo071@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A repor for SHeD paper",
    long_description=long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/",
    project_urs={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where="src")
)