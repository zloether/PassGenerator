# passgenerator
[![Python](https://img.shields.io/badge/python-v3.4+-blue.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/zloether/passgenerator.svg?branch=master)](https://travis-ci.org/zloether/passgenerator)
[![Issues](https://img.shields.io/github/issues/zloether/passgenerator.svg)](https://github.com/zloether/passgenerator/issues)
[![License](https://img.shields.io/github/license/zloether/passgenerator.svg)](https://opensource.org/licenses/MIT)

`passgenerator` is a secure password generator written in Python. It can be imported or run by itself.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
    - [Standalone](#standalone)
    - [Importing](#importing)
- [License](#license)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed in order to run `passgenerator`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: `passgenerator` has not been tested with Python 2 and may not work without changing some things.*


## Installation
Download the latest version from GitHub using Git.
```
git clone https://github.com/zloether/passgenerator.git
```
This will create a directory called *passgenerator* and all the code will be in it.

## Usage
### Standalone
```
python passgenerator.py --help
usage: passgenerator.py [-h] [-l] [-L] [-n] [-N] [-s] [-S] [-u] [-U] [length]

Generates secure random passwords

positional arguments:
  length                number of characters of length (default=32)

optional arguments:
  -h, --help            show this help message and exit
  -l, --lower-enable    use lower case characters
  -L, --lower-disable   don't use lower case characters
  -n, --number-enable   use number characters
  -N, --number-disable  don't use number characters
  -s, --special-enable  use special characters
  -S, --special-disable
                        don't use special characters
  -u, --upper-enable    use upper case characters
  -U, --upper-disable   don't use upper case characters
```

Generating a default password
```
python passgenerator.py
zT0Q9tyfcAx.S2d8*pXGxen86ipSL_;E
```

Generating a 14 character password with no special characters
```
python passgenerator.py -S 14
pocUvtR0RyZ9jd
```
### Importing
`passgenerator` can also be imported into another Python script. It only provides a single method:
```
generate(length=32, upper=True, lower=True, numbers=True, special=True)
```

Sample code:
```
>>> import passgenerator
>>> passgenerator.generate()
'qq*6opDb45;o~;6jWy4U-A5V.*cbHp1Z'
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
