import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from Authorization import Ui_MainWindow as Register
from Main_t import Ui_MainWindow as Form
from docxtpl import DocxTemplate
import Pictures

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
        self.ui.Button_Save.clicked.connect(self.creatWord)
    def creatWord(self):
        Name = self.ui.textEdit.toPlainText()
        Name_value = self.ui.Kratki_otvet.toPlainText()
        Fam = self.ui.textEdit_8.toPlainText()
        Fam_value = self.ui.Kratki_otvet_8.toPlainText()
        Otс = self.ui.textEdit_18.toPlainText()
        Otс_value = self.ui.Kratki_otvet_18.toPlainText()
        reges = self.ui.textEdit_17.toPlainText()
        reges_value = self.ui.Kratki_otvet_17.toPlainText()
        adres = self.ui.textEdit_15.toPlainText()
        adres_value = self.ui.Kratki_otvet_15.toPlainText()
        fact = self.ui.textEdit_14.toPlainText()
        fact_value = self.ui.Kratki_otvet_14.toPlainText()
        tel = self.ui.textEdit_13.toPlainText()
        tel_value = self.ui.Kratki_otvet_13.toPlainText()
        pochta = self.ui.textEdit_11.toPlainText()
        pochta_value = self.ui.Kratki_otvet_11.toPlainText()
        date = self.ui.textEdit_10.toPlainText()
        date_value = self.ui.Kratki_otvet_10.toPlainText()
        mes = self.ui.textEdit_9.toPlainText()
        mes_value = self.ui.Kratki_otvet_9.toPlainText()
        god = self.ui.textEdit_20.toPlainText()
        god_value = self.ui.Kratki_otvet_20.toPlainText()
        doc = DocxTemplate('Test.docx')
        context = { Name : Name_value, Fam : Fam_value, Otс : Otс_value, reges : reges_value, adres : adres_value, fact : fact_value, tel : tel_value, pochta : pochta_value, date : date_value, mes : mes_value, god : god_value}
        # try:
        doc.render(context)
        doc.save("Test_final.docx")
        # except:
        #     print("Закройте документ - Test_final.docx")

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())
