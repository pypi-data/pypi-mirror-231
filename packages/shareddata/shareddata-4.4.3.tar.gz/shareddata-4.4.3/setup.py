from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="shareddata",
    version="4.4.3",
    author="Jose Carlito de Oliveira Filho",
    author_email="jcarlitooliveira@gmail.com",
    description="Shared Memory Database with S3 repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcarlitooliveira/SharedData",
    project_urls={
        "Bug Tracker": "https://github.com/jcarlitooliveira/SharedData/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["shareddata"],
    package_dir={"shareddata": "src/SharedData"},
    package_data={"shareddata": ["SharedData.dll"]},
    python_requires=">=3.9",
    install_requires=[
        "ipykernel==6.23.3",
        "boto3==1.26.160",
        "python-json-logger==2.0.7",
        "python-dotenv==1.0.0",
        "numba==0.57.1",
        "numpy==1.24.3",
        "pandas==2.0.2",
        "XlsxWriter==3.1.2",
        "openpyxl==3.1.2",
        "tqdm==4.65.0",
        "cffi==1.15.1",
    ],
)
