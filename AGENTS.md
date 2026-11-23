# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

`passgenerator` is a small, dependency-free Python library and CLI that generates random complex passwords and
word-based ("phoenetic") passphrases. Published to PyPI as `passgenerator`.

## Layout

- `passgenerator/passgenerator.py` — all logic: `generate`, `complexpass` (alias of `generate`), `phoenetic`, and
  the argparse CLI (`__run_main`, the `passgenerator` console script).
- `passgenerator/__init__.py` — public API re-exports. Anything not in `__all__` is internal.
- `passgenerator/dictionary/words_english_6_char_plus.txt` — bundled word list (~314k ASCII words, one per line).
  Shipped as package data; do not hand-edit.
- `tests/` — pytest suite. `test_word_list.txt` is a small fixture list. Shipped in the sdist (via `MANIFEST.in`),
  not the wheel.
- `pyproject.toml` — packaging (setuptools), dev dependency group, pytest and ruff config.
- `.github/workflows/ci.yml` — lint, test matrix, build smoke test.

## Commands

```
uv run --group dev pytest        # tests
uv run --group dev ruff check    # lint (must be clean; CI enforces it)
uv build                         # sdist + wheel
```

## Conventions

- Supported Python: 3.11+ (see `requires-python`). Keep CI matrix, classifiers, and README in sync when this changes.
- No runtime dependencies. Standard library only.
- Match the existing style: single quotes, section-banner comments, 120-column lines.
- The public names `phoenetic` and the `-p/--phoenetic` flag are misspelled but are public API; do not rename them
  without a deprecation path.
- Library functions raise `ValueError` for impossible inputs; the CLI turns those (and `OSError` from word lists)
  into a stderr message and a non-zero exit. Never print errors to stdout or exit 0 on failure.
- Add or update tests alongside every behavior change. Bump `version` in `pyproject.toml` for releases only.

## Trust boundaries

This is a password generator, so the randomness and selection logic is the security-critical surface. Changes to
any of the following must pass `/security-review` before being considered complete:

- Source of randomness: always `random.SystemRandom` (or `secrets`). Never `random.random`, `random.choice` on the
  module-level RNG, seeding, or anything deterministic.
- Character sets and the alphabet construction in `generate`, and the per-set inclusion guarantee.
- Word selection in `phoenetic` (uniform, without replacement) and the bundled dictionary contents.
- Anything that could log, cache, or persist generated passwords.
