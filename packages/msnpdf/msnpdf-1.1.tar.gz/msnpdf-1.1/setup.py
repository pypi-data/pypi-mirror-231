from pathlib import Path
import setuptools

setuptools.setup(
    name="msnpdf",
    version=1.1,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)