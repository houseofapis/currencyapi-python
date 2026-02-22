# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-02-22

### Changed
- OHLC endpoint: renamed `currency()` to `quote()` and request parameter from `currency` to `quote` to align with API response field names.

## [2.0.0] - 2026-02-19

### Added
- OHLC endpoint (`currency.ohlc()`) for Open, High, Low, Close price data (Tier 3+)
  - Parameters: `currency` (required), `date` (required), `base` (optional), `interval` (optional)
  - Supported intervals: `5m`, `15m`, `30m`, `1h`, `4h`, `12h`, `1d`

### Changed
- **Breaking:** Updated to API v2 (`https://currencyapi.net/api/v2/`)
- Updated README with OHLC endpoint documentation and usage examples

### Removed
- **Breaking:** API v1 support dropped; all requests now use v2

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
