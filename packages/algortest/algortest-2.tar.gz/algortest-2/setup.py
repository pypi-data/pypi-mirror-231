import setuptools
from pathlib import Path

setuptools.setup(
    name="algortest",
    version="2",
    author="Alex Gorji",
    author_email="aligorji@hotmail.com",
    description="testing test files.",
    packages=setuptools.find_packages(),
    install_requires=['quicktions'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
