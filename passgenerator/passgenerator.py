#!/usr/bin/env python

###############################################################################################
# NAME: passgenerator.py
#
# Website: https://github.com/zloether/passgenerator
#
# Description: Simple password generator written in Python. Can be imported or run by itself.
###############################################################################################


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import argparse
import os.path
import sys
from random import SystemRandom

# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------
upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers_chars = 'abcdefghijklmnopqrstuvwxyz'
number_chars = '0123456789'
special_chars = "-._~()'!*:@,;"
bundled_dictionary = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'dictionary/words_english_6_char_plus.txt'))
default_phoenetic_length = 4
default_complex_length = 32



# -----------------------------------------------------------------------------
# help text
# -----------------------------------------------------------------------------
help_description = '''
Generates secure random passwords
'''

help_epilog = '''
optional argument '-w/--word-list' assumes '-p/--phoenetic'
'''

help_length_description = '''
length of password (default is 32 characters for complex and 4 words for phoenetic)
'''

# -----------------------------------------------------------------------------
# alternate method name for generating random complex password
# -----------------------------------------------------------------------------
def complexpass(length=32, upper=True, lower=True, numbers=True, special=True):
    return generate(length=length, upper=upper, lower=lower, numbers=numbers, special=special)



# -----------------------------------------------------------------------------
# generate complex password
# -----------------------------------------------------------------------------
def generate(length=32, upper=True, lower=True, numbers=True, special=True):
    alphabet = ''

    if upper:
        alphabet += upper_chars
    if lower:
        alphabet += lowers_chars
    if numbers:
        alphabet += number_chars
    if special:
        alphabet += special_chars

    if not alphabet:
        raise ValueError('at least one character set must be enabled')
    if length < sum((upper, lower, numbers, special)):
        raise ValueError('length must be at least the number of enabled character sets')

    rand = SystemRandom()

    while True:
        password = ''.join(rand.choice(alphabet) for i in range(length))
        if upper:
            if any(c in upper_chars for c in password):
                pass
            else:
                continue

        if lower:
            if any(c in lowers_chars for c in password):
                pass
            else:
                continue

        if numbers:
            if any(c in number_chars for c in password):
                pass
            else:
                continue

        if special:
            if any(c in special_chars for c in password):
                pass
            else:
                continue

        break

    return password



# -----------------------------------------------------------------------------
# generate phoenetic password
# -----------------------------------------------------------------------------
def phoenetic(number_words=4, word_list=bundled_dictionary, delimiter='-'):
    with open(word_list, encoding='utf-8') as f:
        words = list(dict.fromkeys(line.strip() for line in f if line.strip()))

    if number_words < 1:
        raise ValueError('number_words must be at least 1')
    if number_words > len(words):
        raise ValueError(f'word list has only {len(words)} unique words')

    return delimiter.join(SystemRandom().sample(words, number_words))



# -----------------------------------------------------------------------------
# Configure argument parser
# -----------------------------------------------------------------------------
def __parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description=help_description, epilog=help_epilog)

    # setup argument to store length
    parser.add_argument('length', nargs='?', default=None, type=int,
                        action='store', help=help_length_description)

    # setup argument to store length
    parser.add_argument('-d', '--delimiter', nargs='?', default='-',
                        metavar='delimiter', action='store',
                        help='delimiter between words in phoenetic password')

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-D', '--no-delimiter', dest='delimiter', default=False,
                        action='store_false', help="no delimiter between words in phoenetic password")

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-l', '--lower-enable', dest='lower', default=True,
                        action='store_true', help="use lower case characters")

    # setup arugment to explicitly disable upper characters
    parser.add_argument('-L', '--lower-disable', dest='lower', default=None,
                        action='store_false', help="don't use lower case characters")

    # setup arugment to explicitly enable number characters
    parser.add_argument('-n', '--number-enable', dest='numbers', default=True,
                        action='store_true', help="use number characters")

    # setup arugment to explicitly enable number characters
    parser.add_argument('-N', '--number-disable', dest='numbers', default=None,
                        action='store_false', help="don't use number characters")

    # setup argument for phoenetic password
    parser.add_argument('-p', '--phoenetic', dest='phoenetic', default=False,
                        action='store_true', help='create phoenetic password using English words')

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-s', '--special-enable', dest='special', default=True,
                        action='store_true', help="use special characters")

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-S', '--special-disable', dest='special', default=None,
                        action='store_false', help="don't use special characters")

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-u', '--upper-enable', dest='upper', default=True,
                        action='store_true', help="use upper case characters")

    # setup arugment to explicitly disable upper characters
    parser.add_argument('-U', '--upper-disable', dest='upper', default=None,
                        action='store_false', help="don't use upper case characters")

    # setup argument to use provided word list
    parser.add_argument('-w', '--word-list', dest='word_list', default=None,
                        action='store', metavar='<word list>',
                        help='use provided word list (plaintext ' + \
                        'format, newline separated)')

    # parse the arguments
    args = parser.parse_args()

    return args



# -----------------------------------------------------------------------------
# Run main
# -----------------------------------------------------------------------------
def __run_main():
    args = __parse_arguments()

    try:
        if args.phoenetic or args.word_list:
            password = phoenetic(
                number_words=default_phoenetic_length if args.length is None else args.length,
                word_list=args.word_list or bundled_dictionary,
                delimiter=args.delimiter or '')
        else:
            password = generate(
                length=default_complex_length if args.length is None else args.length,
                upper=args.upper, lower=args.lower,
                numbers=args.numbers, special=args.special)
    except (ValueError, OSError) as e:
        sys.exit(f'Error: {e}')

    print(password)



# -----------------------------------------------------------------------------
# Run interactively
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    __run_main()
