
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="respy_test_package", # Replace with your own username
    version="0.0.2",
    author="Finn Upham",
    author_email="finn.upham@gmail.com",
    description="A library to evalute single belt respiration recordings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finn42/respy_test_package.git",
    packages=setuptools.find_packages(include=['respy_test', 'respy_test.*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)