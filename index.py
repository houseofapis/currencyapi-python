from currencyapi.client import Client

c = Client('fake_api_key')
r = c.rates().get()