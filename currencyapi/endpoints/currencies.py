from currencyapi.endpoints.endpoint import Endpoint

CURRENCIES_ENDPOINT = 'currencies'

class Currencies(Endpoint):
    def __init__(self, api_key: str):
        super().__init__(api_key, CURRENCIES_ENDPOINT)
        self._base()

    def base(self, currency: str):
        self._base(currency)
        return self

