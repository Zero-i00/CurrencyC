from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


from forex_python.converter import CurrencyRates

c = CurrencyRates()

def USD(c):
    value = c.get_rate('USD', 'RUB')
    return value
print(USD(c))

def Convent(c):
    return c.get_rate(input_currency, output_currency)

input_currency = input('From the currency:').upper()
amount = int(input('The Amount:'))
output_currency = input('To the currency:').upper()
will_amount = Convent(c)

print(round(will_amount * amount, 2))

