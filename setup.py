from setuptools import setup, find_packages

with open("README.md", "r") as fp:
  long_description = fp.read()

setup(
  name="...",
  version="...",
  author="Smartmediq",
  author_email="dev@smartmediq.com",
  description="...",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/SmartMediQ/...",
  packages=find_packages(
    where="src",
  ),
  classifiers=[
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Medical Science Apps.",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  python_requires=">=3.11",
  install_requires=[
    ...
  ],
)
