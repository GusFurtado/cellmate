from setuptools import setup
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
    author="Big Data & Intelegência de Mercado",
    author_email="bigdataim@ype.ind.br",
    packages=["cellmate"],
    install_requires=["openpyxl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.10",
)
