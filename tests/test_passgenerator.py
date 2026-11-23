import os.path
import sys

import pytest

import passgenerator
from passgenerator import passgenerator as pg

TEST_WORD_LIST = os.path.join(os.path.dirname(__file__), 'test_word_list.txt')


def _word_file(tmp_path, *words):
    path = tmp_path / 'words.txt'
    path.write_text('\n'.join(words) + '\n')
    return str(path)


def _run_cli(monkeypatch, *argv):
    monkeypatch.setattr(sys, 'argv', ['passgenerator', *argv])
    pg.__run_main()


# -----------------------------------------------------------------------------
# generate / complexpass
# -----------------------------------------------------------------------------
def test_complexpass():
    assert len(passgenerator.complexpass()) == 32
    assert len(passgenerator.complexpass(length=24)) == 24


def test_generate_length():
    assert len(passgenerator.generate()) == 32
    assert len(passgenerator.generate(23)) == 23


@pytest.mark.parametrize('flag, charset', [
    ('upper', pg.upper_chars),
    ('lower', pg.lowers_chars),
    ('numbers', pg.number_chars),
    ('special', pg.special_chars),
])
def test_generate_excludes_disabled_charset(flag, charset):
    password = passgenerator.generate(**{flag: False})
    assert not any(c in charset for c in password)


def test_generate_includes_every_enabled_charset():
    for _ in range(50):
        password = passgenerator.generate(4)
        for charset in (pg.upper_chars, pg.lowers_chars, pg.number_chars, pg.special_chars):
            assert any(c in charset for c in password)


def test_generate_single_charset():
    password = passgenerator.generate(10, upper=False, lower=False, special=False)
    assert password.isdigit()


def test_generate_all_charsets_disabled_raises():
    with pytest.raises(ValueError):
        passgenerator.generate(upper=False, lower=False, numbers=False, special=False)


@pytest.mark.parametrize('length', [-1, 0, 3])
def test_generate_length_too_short_raises(length):
    # 4 charsets enabled, so fewer than 4 characters can never satisfy them all
    with pytest.raises(ValueError):
        passgenerator.generate(length)


# -----------------------------------------------------------------------------
# phoenetic
# -----------------------------------------------------------------------------
def test_phoenetic_defaults():
    words = passgenerator.phoenetic().split('-')
    assert len(words) == 4
    assert all(len(w) >= 6 for w in words)


def test_phoenetic_number_words():
    assert len(passgenerator.phoenetic(number_words=6).split('-')) == 6


def test_phoenetic_delimiter():
    assert len(passgenerator.phoenetic(delimiter=' ').split(' ')) == 4
    assert '-' not in passgenerator.phoenetic(word_list=TEST_WORD_LIST, delimiter='')


def test_phoenetic_uses_word_list():
    with open(TEST_WORD_LIST) as f:
        allowed = {line.strip() for line in f}
    words = passgenerator.phoenetic(word_list=TEST_WORD_LIST).split('-')
    assert set(words) <= allowed
    assert len(set(words)) == len(words)


def test_phoenetic_substring_words_allowed(tmp_path):
    # Regression: 'ab' was rejected once 'abc' was picked, hanging forever.
    word_list = _word_file(tmp_path, 'abc', 'ab')
    for _ in range(20):
        assert sorted(passgenerator.phoenetic(2, word_list=word_list).split('-')) == ['ab', 'abc']


def test_phoenetic_ignores_blank_and_duplicate_lines(tmp_path):
    word_list = _word_file(tmp_path, 'alpha', '', 'beta', '  ', 'alpha')
    for _ in range(20):
        assert sorted(passgenerator.phoenetic(2, word_list=word_list).split('-')) == ['alpha', 'beta']


def test_phoenetic_too_many_words_raises(tmp_path):
    with pytest.raises(ValueError):
        passgenerator.phoenetic(3, word_list=_word_file(tmp_path, 'alpha', 'beta'))


@pytest.mark.parametrize('number_words', [-1, 0])
def test_phoenetic_non_positive_raises(number_words):
    with pytest.raises(ValueError):
        passgenerator.phoenetic(number_words)


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------
def test_cli_default(monkeypatch, capsys):
    _run_cli(monkeypatch)
    assert len(capsys.readouterr().out.strip()) == 32


def test_cli_length_and_disable_special(monkeypatch, capsys):
    _run_cli(monkeypatch, '-S', '14')
    password = capsys.readouterr().out.strip()
    assert len(password) == 14
    assert not any(c in pg.special_chars for c in password)


def test_cli_phoenetic(monkeypatch, capsys):
    _run_cli(monkeypatch, '-p', '3', '-d', '.')
    assert len(capsys.readouterr().out.strip().split('.')) == 3


def test_cli_no_delimiter(monkeypatch, capsys):
    _run_cli(monkeypatch, '-w', TEST_WORD_LIST, '-D')
    assert '-' not in capsys.readouterr().out


def test_cli_word_list_implies_phoenetic(monkeypatch, capsys):
    _run_cli(monkeypatch, '-w', TEST_WORD_LIST, '2')
    assert len(capsys.readouterr().out.strip().split('-')) == 2


@pytest.mark.parametrize('argv', [
    ['abc'],
    ['-p', 'abc'],
    ['-L', '-U', '-N', '-S'],
    ['2'],
    ['-w', '/nonexistent/words.txt'],
])
def test_cli_errors_exit_nonzero(monkeypatch, capsys, argv):
    with pytest.raises(SystemExit) as exc:
        _run_cli(monkeypatch, *argv)
    assert exc.value.code not in (0, None)
    assert capsys.readouterr().out == ''
