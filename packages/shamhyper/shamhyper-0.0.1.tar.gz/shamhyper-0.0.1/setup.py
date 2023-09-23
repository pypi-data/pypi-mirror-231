from setuptools import setup, find_packages

def readme():
    with open("README.md", "r") as f:
        return f.read()

setup(
    name="shamhyper",
    version="0.0.1",
    author="ShamHyper",
    author_email="makar.shatc@gmail.com",
    description="ShamHyper functions and quality of life things.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShamHyper/shamhyper-lib",
    packages=find_packages(),
    install_requires=["colorama"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="shamhyper help lib ",
    project_urls={"GitHub": "https://github.com/ShamHyper/shamhyper-lib"},
    python_requires=">=3.6",
)
