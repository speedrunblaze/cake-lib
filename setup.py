from setuptools import setup, find_packages

setup(
    name="cake",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    description="Cake: A fast security scanning library.",
    author="speedrunblaze",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
