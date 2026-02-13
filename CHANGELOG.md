# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-02-13

### Added
- Python 3.14 support
- Python version classifiers in package metadata (3.10-3.14)
- `python_requires` constraint in setup.py
- CHANGELOG.md

### Changed
- Minimum Python version raised from 3.5 to 3.10
- Dockerfile updated to use `python:3.14-alpine` base image
- GitHub Actions CI matrix updated to test Python 3.10, 3.12, and 3.14
- GitHub Actions updated to use `actions/checkout@v4` and `actions/setup-python@v5`
- Modernized class syntax (removed redundant `object` inheritance)
- Fixed `author_name` to `author` in setup.py (correct setuptools field)
- Fixed unclosed file handle in setup.py (now uses context manager)

### Removed
- Support for Python 3.5-3.9 (all EOL)

## [1.0.4] - Previous release

- Initial tracked version
