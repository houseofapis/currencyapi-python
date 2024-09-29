from currencyapinet.currency import Currency
currency = Currency("nZZSD96Obwjzfjfbgcff8NfkinMjHYP7r09A")
result = currency.rates().get()
print(currency.rates().get())


