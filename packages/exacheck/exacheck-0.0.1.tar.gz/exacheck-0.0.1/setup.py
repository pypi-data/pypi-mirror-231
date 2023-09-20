import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "exacheck",
    version = "0.0.1",
    author = "gbe0",
    author_email = "development@exacheck.net",
    description = "Pure Python health check implementation for ExaBGP",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://exacheck.net",
    project_urls = {
        "Bug Tracker": "https://github.com/exacheck/exacheck/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10"
)
