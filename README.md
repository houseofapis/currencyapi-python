# CurrencyApi Python wrapper 


[![PyPI version](https://badge.fury.io/py/currencyapinet.svg)](https://pypi.org/project/currencyapinet/) [![Coverage Status](https://coveralls.io/repos/github/houseofapis/currencyapi-python/badge.svg?branch=main)](https://coveralls.io/github/houseofapis/currencyapi-python?branch=main) 


<a href="https://currencyapi.net" title="CurrencyApi">CurrencyApi.net</a> provides live currency rates via a REST API. A live currency feed for over 152 currencies, including physical (USD, GBP, EUR + more) and cryptos (Bitcoin, Litecoin, Ethereum + more). A JSON and XML currency api updated every 60 seconds. 

Features:

- Live exchange rates (updated every 60 seconds).
- 152 currencies world currencies.
- Popular cryptocurrencies included; Bitcoin, Litecoin etc.
- Convert currencies on the fly with the convert endpoint.
- Historical currency rates back to year 2000.
- Easy to follow <a href="https://currencyapi.net/documentation" title="currency-api-documentation">documentation</a>

Signup for a free or paid account <a href="https://currencyapi.net/#pricing-sec" title="currency-api-pricing">here</a>.

## This package

Python wrapper for <a href="https://currencyapi.net" title="CurrencyApi">CurrencyApi.net</a> endpoints.

#### Prerequisites

- Minimum Python version 3.5
- Last tested and working on Python 3.11.5
- Free or Paid account with CurrencyApi.net

#### Test Coverage

- 100% coverage

## Installation

```bash
pip install currencyapinet
```
then import the package with:

```python
from currencyapinet.currency import Currency
```

## Usage

### Instantiating

```python
currency = Currency('API_KEY')
```

### Live rates:

```python
result = currency.rates().get()
```

Example with all available methods (methods can be chained):
```python
result = currency
            .rates()
            .base('USD')
            .output('JSON')
            .get()
```
**Available methods for rates endpoint**

| Methods | Description |
| --- | --- |
| `base()` | The base currency you wish you receive the currency conversions for. This will output all currency conversions for that currency. **Default: USD**. |
| `output()` | Response output in either JSON or XML. **Default: JSON**. |

<br>

### List of available currencies:

```python
result = currency.currencies().get()
```

Example with all available methods:
```python
result = currency
            .currencies()
            .output('XML')
            .get()
```

**Available methods for currencies endpoint**

| Methods | Description |
| --- | --- |
| `output()` | Response output in either JSON or XML. **Default: JSON**. |

<br>

### Convert:

```python
result = currency
            .convert()
            .from_currency('BTC')
            .to_currency('USD')
            .amount(100)
            .get()
```

**Available methods for convert endpoint**

| Methods | Description |
| --- | --- |
| `amount()` | The value of the currency you want to convert from. This should be a number and can contain a decimal place. **Required**. |
| `from_currency()` | The currency you want to convert. This will be a three letter ISO 4217 currency code from one of the currencies we have rates for. **Required**. |
| `to_currency()` | The currency you want to convert the amount 'to'. Again this will be a three letter currency code from the ones we offer. **Required**. |
| `output()` | Response output in either JSON or XML. **Default: JSON**. |

<br>

### Historical:

```python
result = currency.history().date('2019-01-01').get()
```

Example with all available methods:

```python
result = currency
            .history()
            .date('2019-01-01')
            .base('GBP')
            .output('JSON')
            .get()
```

**Available methods for historical endpoint**

| Methods | Description |
| --- | --- |
| `date()` | The historical date you wish to receive the currency conversions for. This should be formatted as YYYY-MM-DD. **Required**. |
| `base()` | The base currency you wish you receive the currency conversions for. This will output all currency conversions for that currency. **Default: USD**. |
| `output()` | Response output in either JSON or XML. **Default: JSON**. |

<br>

### Timeframe:

```python
result = currency.timeframe().start_date('2019-01-01').end_date('2019-01-05').get()
```

Example with all available methods:

```python
result = currency
            .timeframe()
            .start_date('2019-01-01')
            .end_date('2019-01-05')
            .base('GBP')
            .output('JSON')
            .get()
```

**Available methods for timeframe endpoint**

| Methods | Description |
| --- | --- |
| `start_date()` | The historical date you wish to receive the currency conversions from. This should be formatted as YYYY-MM-DD. **Required**. |
| `end_date()` | The historical date you wish to receive the currency conversions until. This should be formatted as YYYY-MM-DD. **Required**. |
| `base()` | The base currency you wish you receive the currency conversions for. This will output all currency conversions for that currency. **Default: USD**. |
| `output()` | Response output in either JSON or XML. **Default: JSON**. |
