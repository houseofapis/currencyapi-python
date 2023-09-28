from currencyapinet.currency import Currency

currency = Currency('')
print(currency.history().output('JSON').date('2013-01-02').get())