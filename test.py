import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from Authorization import Ui_MainWindow as Register
from Main_s import Ui_MainWindow as Form
import Pictures

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
        font3 = QFont('Gagarin Star Mix Cyrillic', 16)
    
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
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.Button_Spisok.clicked.connect(self.transfer_page_add)
        self.ui.Button_Zapolnit.clicked.connect(self.transfer_page_fill)
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)
        self.ui.Button_Back.clicked.connect(self.transfer_page_back)
    def transfer_page_back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
    def transfer_page_fill(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Fill_page)
        self.ui.Button_Back_Fill.clicked.connect(self.transfer_page_back)




app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())
