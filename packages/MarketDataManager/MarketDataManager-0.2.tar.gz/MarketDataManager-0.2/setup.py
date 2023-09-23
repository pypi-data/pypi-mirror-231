from setuptools import setup, find_packages

# Load long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MarketDataManager",
    version="0.2",
    packages=find_packages(where="."),
    install_requires=[
        'certifi>=2023.7.22',
        'charset-normalizer>=3.2.0',
        'requests>=2.31.0',
        'urllib3>=2.0.4',
    ],
    author="Anthony Baxter",
    author_email="anthonybaxter819@gmail.com",
    description="A client library to manage a postgresSQL database of financial market data, using a docker containerized api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    keywords="marketdata, postgresSQL, financial, docker",
    url="https://github.com/anthonyb8/MarketData",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python ',
        'Programming Language :: Python :: 3', 
    ],
    python_requires='>=3.10',
)
