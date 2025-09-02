
from setuptools import setup, find_packages

setup(
    name="rsee_controller",
    version="1.5.0",
    author="Rex Wu",
    description="A Python wrapper for the Rsee Light Controller SDK V1.5",
    packages=find_packages(),
    package_data={
        'rsee_controller': ['*.dll', '*.lib'],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
