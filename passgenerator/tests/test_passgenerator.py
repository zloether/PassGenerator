#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import passgenerator



def test_generate():
    password_23 = passgenerator.generate(23)
    assert len(password_23) == 23

    password_upper = passgenerator.generate(upper=False)
    for c in password_upper:
        if c.isupper():
            assert False
    assert True

    password_lower = passgenerator.generate(lower=False)
    for c in password_lower:
        if c.islower():
            assert False
    assert True

    password_number = passgenerator.generate(numbers=False)
    for c in password_number:
        if c.isdigit():
            assert False
    assert True

    special_chars = "-._~()'!*:@,;"
    password_special = passgenerator.generate(special=False)
    for c in password_special:
        if c in special_chars:
            assert False
    assert True
