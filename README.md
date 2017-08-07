# Ultimate-API

:guitar: *An API for ultimate-guitar.com*

![Python-Version](https://img.shields.io/badge/Python-3.6.1-blue.svg)

## Setup
1. Install python3 from https://www.python.org/downloads/

1. Create a virtual environment of python3:

    ```Python
    # Install virtualenv:
    # pip install virtualenv
    virtualenv -p /usr/local/bin/python3 venv
    source venv/bin/activate
    ```

1. Install dependancies:

    ```Python
    pip install -r requirements.txt
    ```

1. Usage:

    ```Python
    export FLASK_DEBUG=1 // Export for debug
    python run.py
    ```

## Endpoints

| Method | Endpoint |  Parameters | Result |
| ------ | -------- | ---------- | ------ |
| `GET`  | `/tab`   | `url`: A full (including protocol) url for an ultimate-guitar.com tab. | JSON response containing tab info as well as each tab line

## Running Tests
To run the full test suite execute the following from the top level directory.
```Python
python test.py
```
