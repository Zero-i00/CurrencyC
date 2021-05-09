from main import *
from ui_main import *

class Currencies(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def currency_difference_USD(self, c):
        try:
            self.ui.USD.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_USD.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = c.get_rate('USD', 'RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.USD.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_USD.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_USD.setText('Unable to retrieve data')

    def currency_difference_GBP(self, c):
        try:
            self.ui.GBP.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_GBP.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = c.get_rate('GBP', 'RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.GBP.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_GBP.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_GBP.setText('Unable to retrieve data')

    def currency_difference_EUR(self, c):
        try:
            self.ui.EUR.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_EUR.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = c.get_rate('EUR', 'RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.EUR.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_EUR.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_EUR.setText('Unable to retrieve data')

    def currency_difference_TRY(self, c):
        try:
            self.ui.TRY.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_TRY.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = c.get_rate('TRY', 'RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.TRY.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_TRY.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_TRY.setText('Unable to retrieve data')

    def currency_difference_JPY(self, c):
        try:
            self.ui.JPY.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_JPY.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = c.get_rate('JPY', 'RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.JPY.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_JPY.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_JPY.setText('Unable to retrieve data')

    def currency_difference_AUD(self, c):
        try:
            self.ui.AUD.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_AUD.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = c.get_rate('AUD', 'RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.AUD.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_AUD.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_AUD.setText('Unable to retrieve data')

    def currency_difference_BTC(self, b):
        try:
            self.ui.BTC.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_BTC.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            value = b.get_latest_price('RUB')
            value = round(value, 2)
            return value
        except AttributeError:
            self.ui.BTC.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_BTC.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_BTC.setText('Unable to retrieve data')

    def currency_difference_ETH(self, c):
        try:
            self.ui.ETH.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_ETH.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
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
        except AttributeError:
            self.ui.ETH.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_ETH.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_ETH.setText('Unable to retrieve data')

    def OilBrent(self):
        try:
            self.ui.OilBrent.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "padding-left: 20px;\n"
                                           "font: 20pt \"Nirmala UI\";")
            self.ui.C_OilBrent.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_Brent = self.soup.find('td', {'id': 'sb_last_8833'}).text.replace('.', '').replace(',', '.')
            price_Brent = round(float(price_Brent), 2)
            return price_Brent
        except AttributeError:
            self.ui.OilBrent.setStyleSheet("color: rgb(215, 50, 75);\n"
                                           "padding-left: 20px;\n"
                                           "font: 20pt \"Nirmala UI\";")
            self.ui.C_OilBrent.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_OilBrent.setText('Unable to retrieve data')

    def OilWTI(self):
        try:
            self.ui.OilWTI.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_OilWTI.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_WTI = self.soup.find('td', {'id': 'sb_last_8849'}).text.replace('.', '').replace(',', '.')
            price_WTI = round(float(price_WTI), 2)
            return price_WTI
        except AttributeError:
            self.ui.OilWTI.setStyleSheet("color: rgb(215, 50, 75);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_OilWTI.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_OilWTI.setText('Unable to retrieve data')

    def Gold(self):
        try:
            self.ui.Gold.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "padding-left: 20px;\n"
                                       "font: 20pt \"Nirmala UI\";")
            self.ui.C_Gold.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_Gold = self.soup.find('td', {'id': 'sb_last_8830'}).text.replace('.', '').replace(',', '.')
            price_Gold = round(float(price_Gold), 2)
            return price_Gold
        except AttributeError:
            self.ui.Gold.setStyleSheet("color: rgb(215, 50, 75);\n"
                                       "padding-left: 20px;\n"
                                       "font: 20pt \"Nirmala UI\";")
            self.ui.C_Gold.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Gold.setText('Unable to retrieve data')

    def Silver(self):
        try:
            self.ui.Silver.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_Silver.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_Silver = self.soup.find('td', {'id': 'sb_last_8836'}).text.replace('.', '').replace(',', '.')
            price_Silver = round(float(price_Silver), 2)
            return price_Silver
        except AttributeError:
            self.ui.Silver.setStyleSheet("color: rgb(215, 50, 75);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_Silver.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Silver.setText('Unable to retrieve data')

    def Platinum(self):
        try:
            self.ui.Platinum.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "padding-left: 20px;\n"
                                           "font: 20pt \"Nirmala UI\";")
            self.ui.C_Platinum.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_Platinum = self.soup.find('td', {'id': 'sb_last_8910'}).text.replace('.', '').replace(',', '.')
            price_Platinum = round(float(price_Platinum), 2)
            return price_Platinum
        except AttributeError:
            self.ui.Platinum.setStyleSheet("color: rgb(215, 50, 75);\n"
                                           "padding-left: 20px;\n"
                                           "font: 20pt \"Nirmala UI\";")
            self.ui.C_Platinum.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Platinum.setText('Unable to retrieve data')

    def Palladium(self):
        try:
            self.ui.Palladium.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "padding-left: 20px;\n"
                                            "font: 20pt \"Nirmala UI\";")
            self.ui.C_Palladium.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_Palladium = self.soup.find('td', {'id': 'sb_last_8883'}).text.replace('.', '').replace(',', '.')
            price_Palladium = round(float(price_Palladium), 2)
            return price_Palladium
        except AttributeError:
            self.ui.Palladium.setStyleSheet("color: rgb(215, 50, 75);\n"
                                            "padding-left: 20px;\n"
                                            "font: 20pt \"Nirmala UI\";")
            self.ui.C_Palladium.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Palladium.setText('Unable to retrieve data')

    def Gas(self):
        try:
            self.ui.Gas.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_Gas.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            price_Gas = self.soup.find('td', {'id': 'sb_last_8862'}).text.replace('.', '').replace(',', '.')
            price_Gas = round(float(price_Gas), 2)
            return price_Gas
        except AttributeError:
            self.ui.Gas.setStyleSheet("color: rgb(215, 50, 75);\n"
                                      "padding-left: 20px;\n"
                                      "font: 20pt \"Nirmala UI\";")
            self.ui.C_Gas.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Gas.setText('Unable to retrieve data')

    def Sberbank(self):
        try:
            self.ui.Sberbank.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "padding-left: 20px;\n"
                                           "font: 20pt \"Nirmala UI\";")
            self.ui.C_Sberbank.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            stocks_Sberbank = self.soup.find('td', {'id': 'sb_last_13711'}).text.replace('.', '').replace(',', '.')
            stocks_Sberbank = round(float(stocks_Sberbank), 2)
            return stocks_Sberbank
        except AttributeError:
            self.ui.Sberbank.setStyleSheet("color: rgb(215, 50, 75);\n"
                                           "padding-left: 20px;\n"
                                           "font: 20pt \"Nirmala UI\";")
            self.ui.C_Sberbank.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Sberbank.setText('Unable to retrieve data')

    def Gazprom(self):
        try:
            self.ui.Gazprom.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "padding-left: 20px;\n"
                                          "font: 20pt \"Nirmala UI\";")
            self.ui.C_Gazprom.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            stocks_Gazprom = self.soup.find('td', {'id': 'sb_last_13684'}).text.replace('.', '').replace(',', '.')
            stocks_Gazprom = round(float(stocks_Gazprom), 2)
            return stocks_Gazprom
        except AttributeError:
            self.ui.Gazprom.setStyleSheet("color: rgb(215, 50, 75);\n"
                                          "padding-left: 20px;\n"
                                          "font: 20pt \"Nirmala UI\";")
            self.ui.C_Gazprom.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Gazprom.setText('Unable to retrieve data')

    def Lukoil(self):
        try:
            self.ui.Lukoil.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_Lukoil.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            stocks_Lukoil = self.soup.find('td', {'id': 'sb_last_13689'}).text.replace('.', '').replace(',', '.')
            stocks_Lukoil = round(float(stocks_Lukoil), 2)
            return stocks_Lukoil
        except AttributeError:
            self.ui.Lukoil.setStyleSheet("color: rgb(215, 50, 75);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_Lukoil.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Lukoil.setText('Unable to retrieve data')

    def Yandex(self):
        try:
            self.ui.Yandex.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_Yandex.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            stocks_Yandex = self.soup.find('td', {'id': 'sb_last_102063'}).text.replace('.', '').replace(',', '.')
            stocks_Yandex = round(float(stocks_Yandex), 2)
            return stocks_Yandex
        except AttributeError:
            self.ui.Yandex.setStyleSheet("color: rgb(215, 50, 75);\n"
                                         "padding-left: 20px;\n"
                                         "font: 20pt \"Nirmala UI\";")
            self.ui.C_Yandex.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Yandex.setText('Unable to retrieve data')

    def Tesla(self):
        try:
            self.ui.Tesla.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            self.ui.C_Tesla.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            stocks_Tesla = self.soup.find('td', {'id': 'sb_last_13994'}).text.replace('.', '').replace(',', '.')
            stocks_Tesla = round(float(stocks_Tesla), 2)
            return stocks_Tesla
        except AttributeError:
            self.ui.Tesla.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            self.ui.C_Tesla.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Tesla.setText('Unable to retrieve data')

    def Apple(self):
        try:
            self.ui.Apple.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            self.ui.C_Apple.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            stocks_Apple = self.soup.find('td', {'id': 'sb_last_6408'}).text.replace('.', '').replace(',', '.')
            stocks_Apple = round(float(stocks_Apple), 2)
            return stocks_Apple
        except AttributeError:
            self.ui.Apple.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 20pt \"Nirmala UI\";")
            self.ui.C_Apple.setStyleSheet("color: rgb(215, 50, 75);\n"
                                        "padding-left: 20px;\n"
                                        "font: 18pt \"Nirmala UI\";")
            self.ui.C_Apple.setText('Unable to retrieve data')