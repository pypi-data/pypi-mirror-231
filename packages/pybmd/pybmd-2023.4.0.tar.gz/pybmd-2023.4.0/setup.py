import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="pybmd",
    version="2023.4.0",
    author="wheheo",
    author_email="wheheohu@outlook.com",
    description="python library for Davinci Resolve(Repack)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WheheoHu/pybmd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],

)
