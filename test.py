import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from test_form import Ui_MainWindow as Register
from Main_s import Ui_MainWindow as Form
import Haha

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Register()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.transfer)
    def transfer(self):
        AppWindow_main.show()
        AppWindow.close()
        
class AppWindow_main(QMainWindow):
    def __init__(self):
        super(AppWindow_main, self).__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.Button_Dobavit.clicked.connect(self.transfer_page_add)
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_Page)

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())
