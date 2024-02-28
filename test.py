import os
import sys
from tkinter import filedialog
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication,
    QFileDialog
)
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from Authorization import Ui_MainWindow as Register
from Main_Form import Ui_MainWindow as Form
import Pictures
from PyQt6.QtGui     import QFontDatabase, QFont
from PyQt6.QtCore    import Qt
from PyQt6 import QtCore, QtGui, QtWidgets

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        id = QFontDatabase.addApplicationFont('./Fonts/Gagarin Star Mix Cyrillic.ttf')
        id2 = QFontDatabase.addApplicationFont('./Fonts/NokiaKokia(RYS BY LYAJKA).ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1 or id2 == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('Gagarin Star Mix Cyrillic', 86)
        font2 = QFont('NokiaKokia(RYS BY LYAJKA)', 32)
        font3 = QFont('Gagarin Star Mix Cyrillic', 12)
        
        self.ui = Register()
        self.ui.setupUi(self)

        self.ui.label.setFont(font)
        self.ui.label_3.setFont(font2)
        self.ui.label_2.setFont(font2)
        self.ui.pushButton.setFont(font3)
        self.ui.pushButton.clicked.connect(self.transfer)
    def transfer(self):
        AppWindow_main.show()
        AppWindow.close()
       
#основное окно программы        
class AppWindow_main(QMainWindow):
    def __init__(self):
        super(AppWindow_main, self).__init__()
        global font,font2,font3,font5,font6
        id = QFontDatabase.addApplicationFont('./Fonts/Gagarin Star Mix Cyrillic.ttf')
        id2 = QFontDatabase.addApplicationFont('./Fonts/NokiaKokia(RYS BY LYAJKA).ttf')
        id3 = QFontDatabase.addApplicationFont('./Fonts/No Limits(FONT BY LYAJKA).ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1 or id2 == -1 or id3 == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('Gagarin Star Mix Cyrillic', 50)
        font2 = QFont('NokiaKokia(RYS BY LYAJKA)', 25)
        font3 = QFont('No Limits(FONT BY LYAJKA)', 20)
        font5 = QFont('No Limits(FONT BY LYAJKA)', 16)
        font6 = QFont('NokiaKokia(RYS BY LYAJKA)', 24)
        font4 = QFont('Gagarin Star Mix Cyrillic', 40)

        self.ui = Form()
        self.ui.setupUi(self)

        self.ui.Kratki_otvet.setFont(font6)
        self.ui.Vopros.setFont(font6)

        self.ui.Glavnaya.setFont(font)
        self.ui.Button_Zapolnit.setFont(font2)
        self.ui.Button_Spisok.setFont(font2)
        self.ui.Button_Save.setFont(font5)
        self.ui.Button_Back.setFont(font5)
        self.ui.Obyazatelny_vopros.setFont(font3)
        self.ui.Button_Dok.setFont(font3)
        self.ui.Button_Forma_plus.setFont(font3)
        self.ui.Dobavit_dokument_label.setFont(font5)

        self.ui.Odin_iz_spiska.setFont(font5)
        self.ui.Dobavochnoe_pole.setFont(font4)
        self.ui.Button_Question.setFont(font3)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.label.setFont(font)
        self.ui.label_2.setFont(font3)
        self.ui.Button_Back_Fill.setFont(font3)
        self.ui.Button_Spisok.clicked.connect(self.transfer_page_add)
        self.ui.Button_Zapolnit.clicked.connect(self.transfer_Fill)
        self.ui.Button_Dok.clicked.connect(self.Open_main_file_btn)
    
    def Open_main_file_btn(self):
        res =QFileDialog.getOpenFileName(self, 'Open File', ".",'DOC file (*.doc*)')
        res = os.path.basename(res[0])
        self.ui.Dobavit_dokument_label.setText(res)

    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)
        self.ui.Button_Back.clicked.connect(self.transfer_back)
        self.ui.Button_Forma_plus.clicked.connect(self.add_field)
    def add_field(self):
        
        _translate = QtCore.QCoreApplication.translate
        self.widget_t = QtWidgets.QWidget()
        self.widget_t.setStyleSheet("#widget_t {\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.widget_t.setObjectName("widget_t")
        self.verticalLayout_t = QtWidgets.QVBoxLayout(self.widget_t)
        self.verticalLayout_t.setObjectName("verticalLayout_t")
        self.ui.verticalLayout_7.addWidget(self.widget_t)
        # Основное размещение (верхнее)
        self.horizontalLayout_01 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_01.setObjectName("horizontalLayout_01_")
        self.verticalLayout_t.addLayout(self.horizontalLayout_01)
        # Размещение текстового поля
        self.horizontalLayout_04 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_04.setObjectName("horizontalLayout_04_")
        self.horizontalLayout_01.addLayout(self.horizontalLayout_04)
        # Размещение кнопки
        self.horizontalLayout_05 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_05.setObjectName("horizontalLayout_05_")
        self.horizontalLayout_01.addLayout(self.horizontalLayout_05)
        # Текстовое поле
        self.textField_01 = QtWidgets.QTextEdit()
        self.textField_01.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_01.setFont(font)
        self.textField_01.setStyleSheet("#Vopros_0 {\n"
"background-color: rgb(181, 173, 173);\n"
"}\n"
"#Vopros_0:Focus {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
        self.textField_01.setObjectName("Vopros_0")
        self.horizontalLayout_04.addWidget(self.textField_01)
        self.textField_01.setPlaceholderText("ВОПРОС")
        self.textField_01.setFont(font6)
        # Кнопка
        self.pushButton_01 = QtWidgets.QPushButton()
        self.pushButton_01.setMaximumSize(QtCore.QSize(141, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_01.setStyleSheet("#pushButton_01 {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#pushButton_01:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#pushButton_01:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.horizontalLayout_05.addWidget(self.pushButton_01)
        self.pushButton_01.setText(_translate("MainWindow", "ОДИН ИЗ\nСПИСКА"))
        self.pushButton_01.setFont(font5)
        ### Вторая часть, Основное размещение (середина)
        self.horizontalLayout_02 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_02.setObjectName("horizontalLayout_02_")
        self.verticalLayout_t.addLayout(self.horizontalLayout_02)
        # Размещение текстового поля
        self.horizontalLayout_06 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_06.setObjectName("horizontalLayout_06_")
        self.horizontalLayout_02.addLayout(self.horizontalLayout_06)
        # Текстовое поле
        self.textField_02 = QtWidgets.QTextEdit()
        self.textField_02.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_02.setFont(font)
        self.textField_02.setStyleSheet("#Answer_0 {\n"
"background-color: rgb(181, 173, 173);\n"
"}\n"
"#Answer_0:Focus {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
        self.textField_02.setObjectName("Answer_0")
        self.horizontalLayout_06.addWidget(self.textField_02)
        self.textField_02.setPlaceholderText("КРАТКИЙ ОТВЕТ")
        self.textField_02.setFont(font6)
        # Размещение кнопок
        self.horizontalLayout_07 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_07.setObjectName("horizontalLayout_07_")
        self.horizontalLayout_02.addLayout(self.horizontalLayout_07)
        ## Кнопки
        self.pushButton_02 = QtWidgets.QPushButton()
        self.pushButton_02.setMaximumSize(QtCore.QSize(100, 48))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_02.setStyleSheet("#pushButton_02 {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#pushButton_02:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#pushButton_02:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.horizontalLayout_07.addWidget(self.pushButton_02)
        self.pushButton_02.setText(_translate("MainWindow", "ТЭГ"))
        self.pushButton_02.setFont(font3)
        # Кнопка вопроса
        self.pushButton20 = QtWidgets.QPushButton()
        self.pushButton20.setMaximumSize(QtCore.QSize(37, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton20.setFont(font)
        self.pushButton20.setObjectName("pushButton20")
        self.pushButton20.setStyleSheet("#pushButton20 {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#pushButton20:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#pushButton20:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.horizontalLayout_07.addWidget(self.pushButton20)
        self.pushButton20.setText(_translate("MainWindow", "?"))
        self.pushButton20.setFont(font3)
        ### Третья часть
        self.horizontalLayout_03 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_03.setObjectName("horizontalLayout_03_")
        self.verticalLayout_t.addLayout(self.horizontalLayout_03)
        # Кнопка копирования
        self.pushButton_03 = QtWidgets.QPushButton()
        self.pushButton_03.setMaximumSize(QtCore.QSize(43, 41))
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_03.setStyleSheet("#pushButton_03 {\n"
"border: 3px solid;\n"
"image: url(:/Copycopycopy/Copycopycopy.png);\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#pushButton_03:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#pushButton_03:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.horizontalLayout_03.addWidget(self.pushButton_03)
        # Кнопка удаление
        self.pushButton_04 = QtWidgets.QPushButton()
        self.pushButton_04.setMaximumSize(QtCore.QSize(43, 41))
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_04.setStyleSheet("#pushButton_04 {\n"
"border: 3px solid;\n"
"image: url(:/Trashcan/trashcan.png);\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#pushButton_04:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#pushButton_04:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.horizontalLayout_03.addWidget(self.pushButton_04)
        # Надпись
        self.Label_01 = QtWidgets.QLabel()
        self.Label_01.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Label_01.setFont(font)
        self.Label_01.setObjectName("Label_01")
        
        self.horizontalLayout_03.addWidget(self.Label_01)
        self.Label_01.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.Label_01.setFont(font3)
        # Кнопка галочка
        self.pushButton_05 = QtWidgets.QPushButton()
        self.pushButton_05.setMaximumSize(QtCore.QSize(43, 41))
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_05.setStyleSheet("#pushButton_05 {\n"
"border: 3px solid;\n"
"image: url(:/Galka/galka.png);\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#pushButton_05:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#pushButton_05:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.horizontalLayout_03.addWidget(self.pushButton_05)

    def transfer_back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
    def transfer_Fill(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Fill_page)
        self.ui.Button_Back_Fill.clicked.connect(self.transfer_back)

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())
