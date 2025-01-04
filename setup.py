from setuptools import setup, find_packages

setup(
    name="data-processor",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyspark>=3.5.0",
        "pytest>=7.4.3",
        "pytest-spark>=0.6.0",
        "chispa>=0.9.2"
    ],
)