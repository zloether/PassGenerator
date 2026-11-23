# PassGenerator

`PassGenerator` is a secure password generator with a CLI utility. It can generate random complex or phoenetic passwords.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
    - [Command Line Utility](#command-line-utility)
- [Development](#development)
- [License](#license)

## Prerequisites
`PassGenerator` requires [Python](https://www.python.org/downloads/) 3.11 or newer. It has no third-party dependencies.

> *Note: Version 1.1.1 is the last release that supports Python 2 and Python 3 versions older than 3.11.*


## Installation
Install the latest version directly from GitHub:
```
python -m pip install git+https://github.com/zloether/PassGenerator.git
```
> *Note: The `passgenerator` package on PyPI is an outdated release and is not currently maintained there.*

## Usage
`PassGenerator` provides the following methods:
```
passgenerator.generate(length=32, upper=True, lower=True, numbers=True, special=True)
passgenerator.complexpass(length=32, upper=True, lower=True, numbers=True, special=True)
passgenerator.phoenetic(number_words=4, word_list='path/to/list', delimiter='-')
```
> *Note: The `complexpass` method calls the `generate` method - both methods provide identical output*

All randomness comes from `random.SystemRandom` (the OS CSPRNG). Complex passwords always contain at least one
character from every enabled character set. Phoenetic passwords never repeat a word.

Both methods raise `ValueError` for impossible requests: `generate` when every character set is disabled or
`length` is shorter than the number of enabled sets, and `phoenetic` when `number_words` is less than 1 or greater
than the number of unique words in the word list. Blank and duplicate lines in a word list are ignored.

Sample code:
```
>>> import passgenerator
>>> passgenerator.generate()
'qq*6opDb45;o~;6jWy4U-A5V.*cbHp1Z'
>>> passgenerator.generate(14, numbers=False)
"N'VJXGQ'Sj)Cj-"
>>> passgenerator.phoenetic()
'endocondensation-chevance-electroless-quadrifurcation'
>>> passgenerator.phoenetic(3)
'inducibility-beheira-onoclea'
```


### Command Line Utility
`PassGenerator` includes a command line utility for generating passwords.
```
passgenerator --help
usage: passgenerator [-h] [-d [delimiter]] [-D] [-l] [-L] [-n] [-N] [-p] [-s]
                     [-S] [-u] [-U] [-w <word list>]
                     [length]

Generates secure random passwords

positional arguments:
  length                length of password (default is 32 characters for
                        complex and 4 words for phoenetic)

options:
  -h, --help            show this help message and exit
  -d [delimiter], --delimiter [delimiter]
                        delimiter between words in phoenetic password
  -D, --no-delimiter    no delimiter between words in phoenetic password
  -l, --lower-enable    use lower case characters
  -L, --lower-disable   don't use lower case characters
  -n, --number-enable   use number characters
  -N, --number-disable  don't use number characters
  -p, --phoenetic       create phoenetic password using English words
  -s, --special-enable  use special characters
  -S, --special-disable
                        don't use special characters
  -u, --upper-enable    use upper case characters
  -U, --upper-disable   don't use upper case characters
  -w <word list>, --word-list <word list>
                        use provided word list (plaintext format, newline
                        separated)

optional argument '-w/--word-list' assumes '-p/--phoenetic'
```

Generating a default complex password:
```
passgenerator
zT0Q9tyfcAx.S2d8*pXGxen86ipSL_;E
```

Generating a 14 character complex password with no special characters:
```
passgenerator -S 14
pocUvtR0RyZ9jd
```

Generating a phoenetic password:
```
passgenerator -p
taurocol-pandiabolism-alkalinuria-enfeeblish
```

Generating a phoenetic password using 3 words and a dot as a delimiter:
```
passgenerator -p 3 -d .
overdevotedly.evanesces.perceivers
```

Invalid input (for example, disabling every character set) prints an error to stderr and exits with a non-zero status.


## Development
This project uses [uv](https://docs.astral.sh/uv/).
```
uv run --group dev pytest        # run tests
uv run --group dev ruff check    # lint
uv build                         # build sdist and wheel
```
CI runs lint, tests on Python 3.11-3.15 (plus Windows and macOS), and a wheel build/smoke test on every push and pull request.


## License

This project is licensed under the MIT License
