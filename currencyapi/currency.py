from currencyapi.endpoints.rates import Rates
from currencyapi.endpoints.convert import Convert
from currencyapi.endpoints.history import History
from currencyapi.endpoints.timeframe import Timeframe
from currencyapi.endpoints.currencies import Currencies

class Currency(object):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def rates(self) -> Rates:
        return Rates(self._api_key)
    
    def convert(self) -> Convert:
        return Convert(self._api_key)
    
    def history(self) -> History:
        return History(self._api_key)
    
    def timeframe(self) -> Timeframe:
        return Timeframe(self._api_key)
    
    def currencies(self) -> Currencies:
        return Currencies(self._api_key)
