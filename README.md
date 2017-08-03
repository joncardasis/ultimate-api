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
  python tab_parser.py {ultimate-guitar-tab-url}
  ```

## Running Tests
To run the full test suite execute the following from the top level directory.
```Python
python test.py
```


## ToDo:
- [ ] Add Unit Tests
  - Test for Ed Sheeran - Perfect
  - Test for Jason Mraz - I'm Yours (because of the title parsing)
  - Test for Passenger - Let Her Go
