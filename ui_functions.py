
from main import *



class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            width_Home = self.ui.btn_Home.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 50\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}\n"
"\n"
"\n"
"")

            width_Excel = self.ui.btn_Excel.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 54;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}")
            width_Converter = self.ui.btn_Converter.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 72;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}")


            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
                widthExtended_Home = self.ui.btn_Home.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: -20\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}\n"
"\n"
"\n"
"")

                widthExtended_Excel = self.ui.btn_Excel.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: -14;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}\n""")
                widthExtended_Converter = self.ui.btn_Converter.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 6;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}")


            else:
                widthExtended = standard
                widthExtended_Home = self.ui.btn_Home.setStyleSheet("QPushButton {\n"
"    color: rgb(35, 35, 35);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 50\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}\n"
"\n"
"\n"
"")

                widthExtended_Excel = self.ui.btn_Excel.setStyleSheet("QPushButton {\n"
"    color: rgb(35, 35, 35);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 54;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}")
                widthExtended_Converter = self.ui.btn_Converter.setStyleSheet("QPushButton {\n"
"    color: rgb(35, 35, 35);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    padding-left: 72;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 230, 130);\n"
"}")




            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(100)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

            self.animation_Home = QPropertyAnimation(self.ui.btn_Home, b"minimumWidth")
            self.animation_Home.setDuration(200)
            self.animation_Home.setStartValue(width_Home)
            self.animation_Home.setEndValue(widthExtended_Home)
            self.animation_Home.setEasingCurve(QtCore.QEasingCurve.InOutQuart)



            self.animation_Excel = QPropertyAnimation(self.ui.btn_Excel, b"minimumWidth")
            self.animation_Excel.setDuration(200)
            self.animation_Excel.setStartValue(width_Excel)
            self.animation_Excel.setEndValue(widthExtended_Excel)
            self.animation_Excel.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

            self.animation_Converter = QPropertyAnimation(self.ui.btn_Converter, b"minimumWidth")
            self.animation_Converter.setDuration(200)
            self.animation_Converter.setStartValue(width_Converter)
            self.animation_Converter.setEndValue(widthExtended_Converter)
            self.animation_Converter.setEasingCurve(QtCore.QEasingCurve.InOutQuart)


            self.animation.start()
            self.animation_Home.start()
            self.animation_Excel.start()
            self.animation_Converter.start()


    def toggleInformation(self, maxWidth, enable):

        if enable:
            # GET WIDTH
            width_Information = self.ui.frame_additional_information.width()
            maxExtend = maxWidth
            standard = 0

            if width_Information == 0:
                widthExtended_Information = maxExtend
            else:
                widthExtended_Information = standard

            self.animation_Information = QPropertyAnimation(self.ui.frame_additional_information, b"minimumWidth")
            self.animation_Information .setDuration(200)
            self.animation_Information .setStartValue(width_Information)
            self.animation_Information .setEndValue(widthExtended_Information)
            self.animation_Information .setEasingCurve(QtCore.QEasingCurve.InOutQuart)

            self.animation_Information.start()








