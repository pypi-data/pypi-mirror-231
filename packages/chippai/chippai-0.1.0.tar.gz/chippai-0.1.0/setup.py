from setuptools import setup, find_packages

setup(
    name="chippai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Andre Lacke",
    author_email="andre@chipp.ai",
    description="A Python wrapper for the Chipp API",
    url="https://github.com/yourusername/chipp-pip",  # If you host it on GitHub or any other platform
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
