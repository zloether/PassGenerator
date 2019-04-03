# passgenerator
[![Python](https://img.shields.io/pypi/pyversions/passgenerator.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/zloether/passgenerator.svg?branch=master)](https://travis-ci.org/zloether/passgenerator)
[![Issues](https://img.shields.io/github/issues/zloether/passgenerator.svg)](https://github.com/zloether/passgenerator/issues)
[![License](https://img.shields.io/github/license/zloether/passgenerator.svg)](https://opensource.org/licenses/MIT)

`passgenerator` is a secure password generator with a CLI utility.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
    - [Command Line Utility](#command-line-utility)
- [License](#license)

## Prerequisites
You'll need to have Python installed in order to run `passgenerator`. Start by downloading and installing the [Python](https://www.python.org/downloads/).
> *Note: Python 3 is recommended, however `passgenerator` has been successfully tested with Python 2.6+*


## Installation
```
pip install passgenerator
```

## Usage
`passgenerator` provides a single method:
```
generate(length=32, upper=True, lower=True, numbers=True, special=True)
```

Sample code:
```
>>> import passgenerator
>>> passgenerator.generate()
'qq*6opDb45;o~;6jWy4U-A5V.*cbHp1Z'
>>> passgenerator.generate(14, numbers=False)
"N'VJXGQ'Sj)Cj-"
```


### Command Line Utility
`passgenerator` includes a command line utility for generating passwords.
```
passgenerator --help
usage: passgenerator [-h] [-l] [-L] [-n] [-N] [-s] [-S] [-u] [-U] [length]

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

Generating a default password:
```
python passgenerator.py
zT0Q9tyfcAx.S2d8*pXGxen86ipSL_;E
```

Generating a 14 character password with no special characters:
```
python passgenerator.py -S 14
pocUvtR0RyZ9jd
```



## License

This project is licensed under the MIT License
