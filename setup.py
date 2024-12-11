from setuptools import setup, find_packages
import os


def get_version():
    init_file = os.path.join(os.path.dirname(__file__), "cellmate", "__init__.py")
    with open(init_file, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                parts = line.split("=")
                if len(parts) == 2:
                    return parts[1].strip().strip('"').strip("'")
    raise RuntimeError("Version string not found in cellmate/__init__.py")


setup(
    name="cellmate",
    version=get_version(),
    description="Excel formatting assistant.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Big Data & Intelegência de Mercado",
    author_email="bigdataim@ype.ind.br",
    url="https://github.com/yourusername/cellmate",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "openpyxl>=3.0,<4.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
