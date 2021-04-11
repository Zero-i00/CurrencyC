from forex_python.converter import CurrencyRates

c = CurrencyRates()

def USD(c):
    value = c.get_rate('USD', 'RUB')
    return value
print(USD(c))

