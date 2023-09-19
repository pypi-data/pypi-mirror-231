from setuptools import setup, find_packages

s = setup(
    name="my_package",
    version="1.0",
    packages=find_packages(),
    package_data={"my_package": ["data/*.txt"]},
    install_requires=["numpy", "pandas"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# Create egg file
from setuptools.command.bdist_egg import bdist_egg
