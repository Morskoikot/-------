import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from PyQt6.QtGui     import QFontDatabase, QFont
from PyQt6.QtCore    import Qt
from test_form import Ui_MainWindow as Register
from Main_s import Ui_MainWindow as Main
import Haha
#окно авторизации
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
        id = QFontDatabase.addApplicationFont('./Fonts/Gagarin Star Mix Cyrillic.ttf')
        id2 = QFontDatabase.addApplicationFont('./Fonts/NokiaKokia(RYS BY LYAJKA).ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1 or id2 == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('Gagarin Star Mix Cyrillic', 86)
        font2 = QFont('NokiaKokia(RYS BY LYAJKA)', 25)
        self.ui = Main()
        self.ui.setupUi(self)
       #переход на добвачное поле
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.pushButton_2.clicked.connect(self.transfer_page_add)
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())
