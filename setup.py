import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()


REPO_NAME="kidney-disease-classification"
AUTHOR_USER_NAME="Arshp-svg"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="arshpatel213@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for kidney disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arshp-svg/kidney-disease-classification",
    
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)