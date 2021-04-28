from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from style_venv_for_currency_liver import Ui_MainWindow
import sys, time, json, lxml
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
import requests
from bs4 import BeautifulSoup
from pyowm import OWM
import pyowm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
import openpyxl

c = CurrencyRates()
b = BtcConverter()
l_time = time.localtime()
current_time = time.strftime('%H:%M', l_time)
dict_of_changes = {
    'USD': [],
    'GBP': [],
    'EUR': [],
    'TRY': [],
    'JPY': [],
    'AUD': [],
    'BTC': [],
    'ETH': [],
    'OilBrent': [],
    'OilWTI': [],
    'Gold': [],
    'Silver': [],
    'Platinum': [],
    'Palladium': [],
    'Gas': [],
    'Sberbank': [],
    'Gazprom': [],
    'Lukoil': [],
    'Yandex': [],
    'Tesla': [],
    'Apple': [],
    'time': []

}




def currency_difference_USD(c):
    value = c.get_rate('USD', 'RUB')
    value = round(value, 2)
    return value


def currency_difference_GBP(c):
    value = c.get_rate('GBP', 'RUB')
    value = round(value, 2)
    return value


def currency_difference_EUR(c):
    value = c.get_rate('EUR', 'RUB')
    value = round(value, 2)
    return value


def currency_difference_TRY(c):
    value = c.get_rate('TRY', 'RUB')
    value = round(value, 2)
    return value


def currency_difference_JPY(c):
    value = c.get_rate('JPY', 'RUB')
    value = round(value, 2)
    return value


def currency_difference_AUD(c):
    value = c.get_rate('AUD', 'RUB')
    value = round(value, 2)
    return value


def currency_difference_BTC(b):
    value = b.get_latest_price('RUB')
    value = round(value, 2)
    return value


def currency_difference_ETH(c):
    url = 'https://ru.investing.com/crypto/ethereum/chart'

    HEADERS = {
        'accept': 'q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    }
    req = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")
    price_ETH_to_USD = soup.find('span', {'class': 'inlineblock', 'dir': 'ltr'}, ).find('span', {
        'id': 'last_last'}).text.replace('.', '').replace(',', '.')
    value_RUB = c.get_rate('USD', 'RUB')
    price_ETH_to_RUB = round(float(price_ETH_to_USD) * value_RUB, 2)

    return [price_ETH_to_RUB, price_ETH_to_USD]


class Products:
    def __init__(self):
        self.url = 'https://ru.investing.com/news/forex-news'
        self.HEADERS = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }

        self.req = requests.get(self.url, headers=self.HEADERS)
        self.soup = BeautifulSoup(self.req.text, 'lxml')

    def OilBrent(self):
        price_Brent = self.soup.find('td', {'id': 'sb_last_8833'}).text.replace('.', '').replace(',', '.')
        price_Brent = round(float(price_Brent), 2)
        return price_Brent

    def OilWTI(self):
        price_WTI = self.soup.find('td', {'id': 'sb_last_8849'}).text.replace('.', '').replace(',', '.')
        price_WTI = round(float(price_WTI), 2)
        return price_WTI

    def Gold(self):
        price_Gold = self.soup.find('td', {'id': 'sb_last_8830'}).text.replace('.', '').replace(',', '.')
        price_Gold = round(float(price_Gold), 2)
        return price_Gold

    def Silver(self):
        price_Silver = self.soup.find('td', {'id': 'sb_last_8836'}).text.replace('.', '').replace(',', '.')
        price_Silver = round(float(price_Silver), 2)
        return price_Silver

    def Platinum(self):
        price_Platinum = self.soup.find('td', {'id': 'sb_last_8910'}).text.replace('.', '').replace(',', '.')
        price_Platinum = round(float(price_Platinum), 2)
        return price_Platinum

    def Palladium(self):
        price_Palladium = self.soup.find('td', {'id': 'sb_last_8883'}).text.replace('.', '').replace(',', '.')
        price_Palladium = round(float(price_Palladium), 2)
        return price_Palladium

    def Gas(self):
        price_Gas = self.soup.find('td', {'id': 'sb_last_8862'}).text.replace('.', '').replace(',', '.')
        price_Gas = round(float(price_Gas), 2)
        return price_Gas


class Stocks:
    def __init__(self):
        self.url = 'https://ru.investing.com/news/forex-news'
        self.HEADERS = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }
        self.req = requests.get(self.url, headers=self.HEADERS)
        self.soup = BeautifulSoup(self.req.text, 'lxml')

    def Sberbank(self):
        stocks_Sberbank = self.soup.find('td', {'id': 'sb_last_39214'}).text.replace('.', '').replace(',', '.')
        stocks_Sberbank = round(float(stocks_Sberbank), 2)
        return stocks_Sberbank

    def Gazprom(self):
        stocks_Gazprom = self.soup.find('td', {'id': 'sb_last_13684'}).text.replace('.', '').replace(',', '.')
        stocks_Gazprom = round(float(stocks_Gazprom), 2)
        return stocks_Gazprom

    def Lukoil(self):
        stocks_Lukoil = self.soup.find('td', {'id': 'sb_last_13689'}).text.replace('.', '').replace(',', '.')
        stocks_Lukoil = round(float(stocks_Lukoil), 2)
        return stocks_Lukoil

    def Yandex(self):
        stocks_Yandex = self.soup.find('td', {'id': 'sb_last_102063'}).text.replace('.', '').replace(',', '.')
        stocks_Yandex = round(float(stocks_Yandex), 2)
        return stocks_Yandex

    def Tesla(self):
        stocks_Tesla = self.soup.find('td', {'id': 'sb_last_13994'}).text.replace('.', '').replace(',', '.')
        stocks_Tesla = round(float(stocks_Tesla), 2)
        return stocks_Tesla

    def Apple(self):
        stocks_Apple = self.soup.find('td', {'id': 'sb_last_6408'}).text.replace('.', '').replace(',', '.')
        stocks_Apple = round(float(stocks_Apple), 2)
        return stocks_Apple


products = Products()
stocks = Stocks()


def weather():
    owm = OWM('f53ec5e445bf9fde80baa7338611fe61')
    city = input('city')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature_celsius = w.temperature('celsius')
    temperature_fahrenheit = w.temperature('fahrenheit')

    return temperature_celsius, temperature_fahrenheit


def convent_currency():
    global c

    input_currency = ui.Input_currency.text().upper()  # Из какой
    amount = float(ui.Input_amount.text())  # Сумма
    output_currency = ui.Output_currency.text().upper()  # В какую
    if output_currency == 'BTC':
        output_amount = round(b.convert_to_btc(amount, input_currency), 2)  # Получу
        ui.Output_amount.setText(str(output_amount))
    elif input_currency == 'BTC':
        output_amount = round(b.convert_btc_to_cur(amount, output_currency), 2)
        ui.Output_amount.setText(str(output_amount))
    elif input_currency == 'ETH':
        convert = c.get_rate('USD', output_currency)
        output_amount = round(float(currency_difference_ETH(c)[1]) * float(amount) * float(convert), 2)
        ui.Output_amount.setText(str(output_amount))
    elif output_currency == 'ETH':
        convert = c.get_rate(input_currency, 'USD')
        output_amount = round(float(currency_difference_ETH(c)[1]) / (float(convert) * float(amount)), 2)
        ui.Output_amount.setText(str(output_amount))
    else:
        convert = c.get_rate(input_currency, output_currency)
        output_amount = round(convert * amount, 2)
        print()
        ui.Output_amount.setText(str(output_amount))


def email():
    server = 'smtp.gmail.com'
    user = 'currencycgraduation@gmail.com'  # Email нашей программы
    password = 'CyCGn1605'  # Пороль

    recipients = ['user@gmail.com']  # Сюда надо получателя вписывать
    sender = 'currencycgraduation@gmail.com'
    subject = 'CurrencyC'
    text = '<b>Тестовое сообщение</b>'  # Само сообщение
    html = '<html><head></head><body><p>' + text + '</p></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


def excel():
    book = openpyxl.Workbook()
    time = [12, 13, 14, 15]
    Currency = ['USD', 'EUR', "GBP", '']
    USD = [77, 78, 79, 76]
    EUR = [90, 91, 92, 93]

    count = 0
    count_number = 2
    count_res_time = 0
    count_column = 2
    count_res_Currency = 0
    sheet = book.active

    while count != len(USD):
        sheet['A{0}'.format(count_number)] = Currency[count_res_Currency]
        sheet.cell(row=1, column=count_column).value = time[count_res_time]
        sheet.cell(row=2, column=count_column).value = USD[count]
        sheet.cell(row=3, column=count_column).value = EUR[count]
        count_number += 1
        count_column += 1
        count_res_time += 1
        count_res_Currency += 1
        if count_res_Currency >= len(USD) - 1:
            count_res_Currency = 3
        count += 1

    else:
        book.save('test.xlsx')
        book.close()


def update():
    global c, b, l_time, current_time

    c = CurrencyRates()
    b = BtcConverter()
    l_time = time.localtime()
    current_time = time.strftime('%H:%M', l_time)

    ui.Currency_USD.setText(str(currency_difference_USD(c)) + '  ₽')
    ui.Currency_GBP.setText(str(currency_difference_GBP(c)) + '  ₽')
    ui.Currency_EUR.setText(str(currency_difference_EUR(c)) + '  ₽')
    ui.Currency_TRY.setText(str(currency_difference_TRY(c)) + '  ₽')
    ui.Currency_JPY.setText(str(currency_difference_JPY(c)) + '  ₽')
    ui.Currency_AUD.setText(str(currency_difference_AUD(c)) + '  ₽')
    ui.Currency_BTC.setText(str(currency_difference_BTC(b)) + '  ₽')
    ui.Currency_ETH.setText(str(currency_difference_ETH(c)[0]) + '  ₽')
    ui.Course_Gold.setText(str(products.Gold()) + '  ₽')
    ui.Course_Silver.setText(str(products.Silver()) + '  ₽')
    ui.Course_Platinum.setText(str(products.Platinum()) + '  ₽')
    ui.Course_Palladium.setText(str(products.Palladium()) + '  ₽')
    ui.Course_Brent.setText(str(products.OilBrent()) + '  ₽')
    ui.Course_WTI.setText(str(products.OilWTI()) + '  ₽')
    ui.Course_Gas.setText(str(products.Gas()) + '  ₽')
    ui.Stocks_Sberbank.setText(str(stocks.Sberbank()) + '  ₽')
    ui.Stocks_Gazprom.setText(str(stocks.Gazprom()) + '  ₽')
    ui.Stocks_Lukoil.setText(str(stocks.Lukoil()) + '  ₽')
    ui.Stocks_Yandex.setText(str(stocks.Yandex()) + '  ₽')
    ui.Stocks_Tesla.setText(str(stocks.Tesla()) + '  ₽')
    ui.Stocks_Apple.setText(str(stocks.Apple()) + '  ₽')

    dict_of_changes['USD'].append(currency_difference_USD(c))
    dict_of_changes['GBP'].append(currency_difference_GBP(c))
    dict_of_changes['EUR'].append(currency_difference_EUR(c))
    dict_of_changes['TRY'].append(currency_difference_TRY(c))
    dict_of_changes['JPY'].append(currency_difference_JPY(c))
    dict_of_changes['AUD'].append(currency_difference_AUD(c))
    dict_of_changes['BTC'].append(currency_difference_BTC(b))
    dict_of_changes['ETH'].append(currency_difference_ETH(c)[0])
    dict_of_changes['Gold'].append(products.Gold())
    dict_of_changes['OilBrent'].append(products.OilBrent())
    dict_of_changes['OilWTI'].append(products.OilWTI())
    dict_of_changes['Silver'].append(products.Silver())
    dict_of_changes['Platinum'].append(products.Platinum())
    dict_of_changes['Palladium'].append(products.Palladium())
    dict_of_changes['time'].append(current_time)
    print(dict_of_changes)



# def percentage():
#     if min(list_of_changes_USD) < list_of_changes_USD[0] - (
#             list_of_changes_USD[0] / 100 * int(ui.Enter_percentage.text())):
#         print('yes')
#     else:
#         print('ere')


if __name__ == "__main__":
    # Main
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('CurrencyC')
    update()


    ui.Convert_Button.clicked.connect(convent_currency)


    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(60000)


    MainWindow.show()
    sys.exit(app.exec_())
