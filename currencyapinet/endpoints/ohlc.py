from currencyapinet.endpoints.endpoint import Endpoint

OHLC_ENDPOINT = 'ohlc'

class Ohlc(Endpoint):
    def __init__(self, api_key: str):
        super().__init__(api_key, OHLC_ENDPOINT)

    def currency(self, currency: str):
        self.add_param('currency', currency.upper())
        return self

    def date(self, date: str):
        self.add_param('date', date)
        return self

    def base(self, currency: str):
        self._base(currency)
        return self

    def interval(self, interval: str):
        self.add_param('interval', interval)
        return self
