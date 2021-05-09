from main import *
from ui_main import *

class Waether(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def weather(self):
        try:
            self.ui.lineEdit_City.setStyleSheet("QLineEdit{\n"
                                                "    border-radius: 10px;\n"
                                                "    color: #FFF;\n"
                                                "    border: 2px solid rgb(120, 230, 130);\n"
                                                "    padding-left:60px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "")
            self.ui.lineEdit_City.setPlaceholderText('City')

            owm = OWM('f53ec5e445bf9fde80baa7338611fe61')
            city = self.ui.lineEdit_City.text()
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temperature_celsius = w.temperature('celsius')['temp']
            temperature_fahrenheit = w.temperature('fahrenheit')['temp']
            weather = self.ui.label_inf_temperature.setText(
                '\n''{0}\n{1}'.format(temperature_celsius, temperature_fahrenheit))
            return weather

        except pyowm.commons.exceptions.NotFoundError:
            self.ui.lineEdit_City.setText('')
            self.ui.lineEdit_City.setStyleSheet("QLineEdit{\n"
                                                "    border-radius: 10px;\n"
                                                "    color: rgb(215, 50, 75);\n"
                                                "    border: 2px solid rgb(215, 50, 75);\n"
                                                "    padding-left:15px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "")
            self.ui.lineEdit_City.setPlaceholderText('the city doesnt exist')
        except pyowm.commons.exceptions.APIRequestError:
            self.ui.lineEdit_City.setStyleSheet("QLineEdit{\n"
                                                "    border-radius: 10px;\n"
                                                "    color: rgb(215, 50, 75);\n"
                                                "    border: 2px solid rgb(215, 50, 75);\n"
                                                "    padding-left:40px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "")
            self.ui.lineEdit_City.setPlaceholderText('enter the city')