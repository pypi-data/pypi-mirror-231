from setuptools import setup, find_packages

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geometry_shapes",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Saurav Upreti",
    author_email="upretisaurav7@gmail.com",
    description="A simple package to work with geometric shapes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="geometry shapes",
    url="https://github.com/upretisaurav7/geometry_shapes",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
