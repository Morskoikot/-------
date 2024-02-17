import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from Authorization import Ui_MainWindow as Register
from Main_s import Ui_MainWindow as Form
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
        self.ui.Button_Teg.setFont(font3)
        self.ui.Odin_iz_spiska.setFont(font5)
        self.ui.Dobavochnoe_pole.setFont(font)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.Button_Spisok.clicked.connect(self.transfer_page_add)
        self.ui.Button_Zapolnit.clicked.connect(self.transfer_Fill)
        
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)
        self.ui.Button_Back.clicked.connect(self.transfer_back)
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
