from setuptools import setup, find_packages

VERSION = '0.0.13'
DESCRIPTION = 'A package for interacting with the Microsoft Blob storage'
LONG_DESCRIPTION = 'Within this package you can upload/download files and/or stream files directly into dataframes'

# Setting up
setup(
    name="azure_blob_connector",
    version=VERSION,
    author="dave_the_noob",
    author_email="dave.dawson86@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['azure.storage.blob', 'pandas','typing'],
    keywords=['python', 'blob', 'azure', 'azure blob', 'storage container', 'blob storage container'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)