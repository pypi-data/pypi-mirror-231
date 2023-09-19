from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="playfairpolycipher",
    version="0.1",
    author="Fluffy_Debuger,SiddheshGanesh",
    author_email="a69247199@gmail.com",
    description="A Python library for the Playfair Cipher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fluffy-debuger/poly_playfair_cipher",
    packages=["PlayfairCipher"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
