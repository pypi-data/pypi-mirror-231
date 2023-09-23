from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="TransCipherTools",
    version="0.1",
    author="Fluffy_Debuger",
    author_email="a69247199@gmail.com",
    description="A Python library for the Transposition Cipher techniques  ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fluffy-debuger/Transposition_Cipher",
    packages=["TransCipherTools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
