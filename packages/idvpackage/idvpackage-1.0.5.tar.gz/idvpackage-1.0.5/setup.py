from setuptools import setup, find_packages

with open("/Users/fahadpatel/Downloads/OCRProofID copy/requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="idvpackage",
    version="1.0.5",
    author="Fahad Patel",
    author_email="fahadpatel1403@gmail.com",
    description=("This repository contains a Python program designed to execute Optical Character Recognition (OCR)"
                 " and Facial Recognition on images."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=required,
    include_package_data=True,
)