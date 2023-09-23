![Code Ocean Logo](https://raw.githubusercontent.com/codeocean/branding/main/logo/CO_logo_135x72.png)
# codeoceanapi-py
Python api for capsules, data assets, etc. 

## Documentation
Documentation for the SDK can be found [here](https://codeocean.github.io/codeoceansdk-py/codeoceansdk.html) The documentation has been generated using pdoc by running the following command: 

`pdoc src/codeoceansdk/ -o docs/`

The original REST API documentation can be found in the [Code Ocean User Guide](https://docs.codeocean.com/user-guide/code-ocean-api)

## Version

This version is tested with the 2.13 release of the Code Ocean Platform.

## pytest

For pytests, please set the API_KEY environment variable.

In order to include slower tests include --slow as an argument to pytest

Install package as editable: 

`pip install --editable .`

Run pytest from codeoceansdk-py

`pytest`