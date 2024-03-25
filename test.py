import os, ast, sys

from tkinter import filedialog
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication,
    QFileDialog
)
import sys
import math
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QApplication
)
from Authorization import Ui_MainWindow as Register
from Main_Form import Ui_MainWindow as Form
KT = int(1)
import Pictures
from PyQt6.QtGui     import QFontDatabase, QFont
from PyQt6.QtCore    import Qt
from PyQt6 import QtCore, QtGui, QtWidgets

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        #загрузка шрифтов в приложение
        id = QFontDatabase.addApplicationFont('./Fonts/SFProText-Light.ttf')
        id2 = QFontDatabase.addApplicationFont('./Fonts/Lato-Light.ttf')
        # Если id равен -1, то шрифт не установлен
        if id == -1 or id2 == -1: 
            print('Ошибка подключения шрифтов')
        font = QFont('SFProText-Light', 70)
        font2 = QFont('Lato-Light', 28)
        font3 = QFont('SFProText-Light', 20)
        
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
        #добовление шрифтов
        global font,font2,font3,font4,font5,font6,font7
        font = QFont('SFProText-Light', 80)
        font2 = QFont('Lato-Light', 30)
        font3 = QFont('Lato-Light', 20)
        font4 = QFont('SFProText-Light', 50)
        font5 = QFont('SFProText-Light', 20)
        font6 = QFont('SFProText-Light', 30)
        font7 = QFont('Lato-Light', 22)
        font8 = QFont('SFProText-Light', 26)
        self.ui = Form()
        self.ui.setupUi(self)

        global a, b, d, e, f, g, h, j
        a = []
        b = 0
        d = []
        e = 0
        f = []
        g = 0
        h = []
        j = 0
        
        #присвоение шрифтов объектам
        self.ui.Kratki_otvet.setFont(font2)
        self.ui.Vopros.setFont(font2)
        self.ui.Glavnaya.setFont(font)
        self.ui.Button_Zapolnit.setFont(font6)
        self.ui.Button_Spisok.setFont(font6)
        self.ui.Button_Save.setFont(font5)
        self.ui.Button_Back.setFont(font5)
        self.ui.Obyazatelny_vopros.setFont(font3)
        self.ui.Button_Dok.setFont(font3)
        self.ui.Button_Forma_plus.setFont(font3)
        self.ui.Dobavit_dokument_label.setFont(font5)
        self.ui.Dobavochnoe_pole.setFont(font)
        self.ui.Obyazatelny_vopros.setFont(font7)
        self.ui.Button_Dok.setFont(font5)
        self.ui.Button_Forma_plus.setFont(font5)
        self.ui.Dobavit_dokument_label.setFont(font3)
        self.ui.Tag.setFont(font2)
        #self.ui..setFont(font5)
        self.ui.Dobavochnoe_pole.setFont(font4)
        self.ui.Button_Question.setFont(font5)
        self.ui.Button_Trash.setFont(font5)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        self.ui.label.setFont(font8)
        self.ui.label_2.setFont(font5)
        self.ui.Button_Back_Fill.setFont(font5)
        #self.ui.Button_Save_Fill.setFont(font5)
        self.ui.Button_Spisok.clicked.connect(self.transfer_page_add)
        self.ui.Button_Zapolnit.clicked.connect(self.transfer_Fill)
        # self.ui.Button_Save.clicked.connect(self.save_form)
        self.ui.Button_Dok.clicked.connect(self.Open_main_file_btn)
        
        
    #постороение пути к документу
    def Open_main_file_btn(self):
        res =QFileDialog.getOpenFileName(self, 'Open File', ".",'DOC file (*.doc*)')
        res = os.path.basename(res[0])
        self.ui.Dobavit_dokument_label.setText(res)
        global K, L
    #разделение названия файла от его расширения  
        K = res
        filename = K
        L, extension = os.path.splitext(filename)
        
    def transfer_page_add(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)
        self.ui.Button_Back.clicked.connect(self.transfer_back)
        self.ui.Button_Forma_plus.clicked.connect(self.add_field)
    def add_field(self):
        global KT
        global a, b, d, e, f, g, h, j
        _translate = QtCore.QCoreApplication.translate
        self.stackedWidget_t = QtWidgets.QStackedWidget ()
        self.ui.verticalLayout_7.addWidget(self.stackedWidget_t)
        
        
        
        self.page_t_1 = QtWidgets.QWidget()
        self.verticalLayout_t_1 = QtWidgets.QVBoxLayout(self.page_t_1)
        self.horizontalLayout_t_1 = QtWidgets.QHBoxLayout()
        self.widget_t_1 = QtWidgets.QWidget()
        self.widget_t_1.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_1.setObjectName(f"widget_t_1_{KT}")
        self.widget_t_1.setStyleSheet(f"#{self.widget_t_1.objectName()}" "{\n"
"background-color: rgb(228, 228, 228); \n"
"}")
        self.verticalLayout_w_1 = QtWidgets.QVBoxLayout(self.widget_t_1)
        self.verticalLayout_t_1.addLayout(self.horizontalLayout_t_1)
        self.horizontalLayout_t_1.addWidget(self.widget_t_1)
        self.horizontalLayout_f_100 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_100)
        self.horizontalLayout_f_110 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_100.addLayout(self.horizontalLayout_f_110)
        self.textField_vp_10 = QtWidgets.QLineEdit()
        self.textField_vp_10.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_vp_10.setFont(font)
        self.textField_vp_10.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_vp_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textField_vp_10.setPlaceholderText(_translate("MainWindow", "Вопрос"))
        self.horizontalLayout_f_110.addWidget(self.textField_vp_10)

        self.horizontalLayout_f_120 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_120.setContentsMargins(28, -1, -1, -1)
        self.horizontalLayout_f_110.addLayout(self.horizontalLayout_f_120)
        self.comboBox_f_1 = QtWidgets.QComboBox()
        self.comboBox_f_1.setMaximumSize(QtCore.QSize(220, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_f_1.setFont(font)
        self.comboBox_f_1.setObjectName(f"comboBox_f_1_{KT}")
        self.comboBox_f_1.setStyleSheet(f"#{self.comboBox_f_1.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190) ;\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.comboBox_f_1.objectName()}"":hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
f"#{self.comboBox_f_1.objectName()}"":pressed { \n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
"\n"
"")
        self.comboBox_f_1.addItem("ТЕКСТ (СТРОКА)")
        self.comboBox_f_1.addItem("ТЕКСТ (АБЗАЦ)")
        self.comboBox_f_1.addItem("ОДИН ИЗ СПИСКА")
        self.comboBox_f_1.addItem("МН. ИЗ СПИСКА")
        self.comboBox_f_1.addItem("РАСКР. СПИСОК")
        self.comboBox_f_1.addItem("ШКАЛА")
        self.comboBox_f_1.addItem("ДАТА")
        self.comboBox_f_1.addItem("ВРЕМЯ")
        self.horizontalLayout_f_120.addWidget(self.comboBox_f_1)
        # Среднее поле
        self.horizontalLayout_f_200 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_200)
        self.horizontalLayout_f_210 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_220 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_200.addLayout(self.horizontalLayout_f_210)
        self.horizontalLayout_f_200.addLayout(self.horizontalLayout_f_220)
        self.textField_low_1 = QtWidgets.QLineEdit()
        self.textField_low_1.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_low_1.setFont(font)
        self.textField_low_1.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_low_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_210.addWidget(self.textField_low_1)
        self.textField_low_1.setPlaceholderText(_translate("MainWindow", "Краткий ответ"))
        self.textField_tag_1 = QtWidgets.QLineEdit()
        self.textField_tag_1.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textField_tag_1.setFont(font)
        self.textField_tag_1.setStyleSheet("border-top: 0px solid;\n"
"border-bottom: 2px solid;\n"
"background-color: rgb(228, 228, 228);")
        self.textField_tag_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_f_220.addWidget(self.textField_tag_1)
        self.textField_tag_1.setPlaceholderText(_translate("MainWindow", "Тэг"))
        self.vertcalLayout_230 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_220.addLayout(self.vertcalLayout_230)
        spacer_1 = QtWidgets.QSpacerItem(45, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertcalLayout_230.addItem(spacer_1)
        self.Button_Question_1 = QtWidgets.QPushButton()
        self.Button_Question_1.setMaximumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question_1.setFont(font)
        self.Button_Question_1.setObjectName(f"Button_Question_1_{KT}")
        self.Button_Question_1.setStyleSheet(f"#{self.Button_Question_1.objectName()}" "{\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Question_1.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Question_1.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"\n"
"")
        self.vertcalLayout_230.addWidget(self.Button_Question_1)

        # Нижнее поле
        self.horizontalLayout_f_300 = QtWidgets.QHBoxLayout()
        self.verticalLayout_w_1.addLayout(self.horizontalLayout_f_300)
        self.horizontalLayout_f_310 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f_300.addLayout(self.horizontalLayout_f_310)
        self.Button_Copy_01 = QtWidgets.QPushButton()
        self.Button_Copy_01.setMaximumSize(QtCore.QSize(41, 41))
        self.Button_Copy_01.setObjectName(f"Button_Copy_0{KT}")
        self.Button_Copy_01.setStyleSheet(f"#{self.Button_Copy_01.objectName()}""{\n"
"border: 2px solid;\n"
"border-radius: 9px;\n"
"border-color:rgb(190, 190, 190);\n"
"background-color: rgb(228, 228, 228);\n"
"}\n"
f"#{self.Button_Copy_01.objectName()}"":hover {\n"
"background-color:rgb(219, 219, 219);\n"
"}\n"
f"#{self.Button_Copy_01.objectName()}"":pressed { \n"
"background-color:rgb(204, 204, 204);\n"
"}\n"
"")
        self.Button_Copy_01.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../1621635.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Copy_01.setIcon(icon2)
        self.horizontalLayout_f_300.addWidget(self.Button_Copy_01)
        self.Obyazatelny_vopros_f_01 = QtWidgets.QLabel()
        self.Obyazatelny_vopros_f_01.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros_f_01.setFont(font)
        self.Obyazatelny_vopros_f_01.setObjectName("Obyazatelny_vopros_f_01")
        self.Obyazatelny_vopros_f_01.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.horizontalLayout_f_310.addWidget(self.Obyazatelny_vopros_f_01)
        self.widget_f_01 = QtWidgets.QWidget()
        self.widget_f_01.setMinimumSize(QtCore.QSize(45, 45))
        self.widget_f_01.setMaximumSize(QtCore.QSize(45, 45))
        self.widget_f_01.setObjectName("widget_f_01")
        self.pushButton_f_01_on = QtWidgets.QPushButton(self.widget_f_01)
        self.pushButton_f_01_on.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_01_on.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_01_on.setText("")
        self.pushButton_f_01_on.setObjectName("pushButton_f_01_on")
        self.pushButton_f_01_off = QtWidgets.QPushButton(self.widget_f_01)
        self.pushButton_f_01_off.setGeometry(QtCore.QRect(0, 0, 45, 45))
        self.pushButton_f_01_off.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_f_01_off.setText("")
        self.pushButton_f_01_off.setObjectName("pushButton_f_01_off")
        self.horizontalLayout_f_310.addWidget(self.widget_f_01)

        
        
        
        self.page_t_2 = QtWidgets.QWidget()
        self.verticalLayout_t_2 = QtWidgets.QVBoxLayout(self.page_t_2)
        self.horizontalLayout_t_2 = QtWidgets.QHBoxLayout()
        self.widget_t_2 = QtWidgets.QWidget()
        self.widget_t_2.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_2.setObjectName(f"widget_t_2_{KT}")
        self.widget_t_2.setStyleSheet(f"#{self.widget_t_2.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_2 = QtWidgets.QVBoxLayout(self.widget_t_2)
        
        
        
        self.page_t_3 = QtWidgets.QWidget()
        self.verticalLayout_t_3 = QtWidgets.QVBoxLayout(self.page_t_3)
        self.horizontalLayout_t_3 = QtWidgets.QHBoxLayout()
        self.widget_t_3 = QtWidgets.QWidget()
        self.widget_t_3.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_3.setObjectName(f"widget_t_3_{KT}")
        self.widget_t_3.setStyleSheet (f"#{self.widget_t_3.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_3 = QtWidgets.QVBoxLayout(self.widget_t_3)
        
        
        
        self.page_t_4 = QtWidgets.QWidget()
        self.verticalLayout_t_4 = QtWidgets.QVBoxLayout(self.page_t_4)
        self.horizontalLayout_t_4 = QtWidgets.QHBoxLayout()
        self.widget_t_4 = QtWidgets.QWidget()
        self.widget_t_4.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_4.setObjectName(f"widget_t_4_{KT}")
        self.widget_t_4.setStyleSheet (f"#{self.widget_t_4.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_4 = QtWidgets.QVBoxLayout(self.widget_t_4)
        
        
        
        self.page_t_5 = QtWidgets.QWidget()
        self.verticalLayout_t_5 = QtWidgets.QVBoxLayout(self.page_t_5)
        self.horizontalLayout_t_5 = QtWidgets.QHBoxLayout()
        self.widget_t_5 = QtWidgets.QWidget()
        self.widget_t_5.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_5.setObjectName(f"widget_t_5_{KT}")
        self.widget_t_5.setStyleSheet (f"#{self.widget_t_5.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_5 = QtWidgets.QVBoxLayout(self.widget_t_5)
        
        
        
        self.page_t_6 = QtWidgets.QWidget()
        self.verticalLayout_t_6 = QtWidgets.QVBoxLayout(self.page_t_6)
        self.horizontalLayout_t_6 = QtWidgets.QHBoxLayout()
        self.widget_t_6 = QtWidgets.QWidget()
        self.widget_t_6.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_6.setObjectName(f"widget_t_6_{KT}")
        self.widget_t_6.setStyleSheet (f"#{self.widget_t_6.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_6 = QtWidgets.QVBoxLayout(self.widget_t_6)
        
        
        
        
        self.page_t_7 = QtWidgets.QWidget()
        self.verticalLayout_t_7 = QtWidgets.QVBoxLayout(self.page_t_7)
        self.horizontalLayout_t_7 = QtWidgets.QHBoxLayout()
        self.widget_t_7 = QtWidgets.QWidget()
        self.widget_t_7.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_7.setObjectName(f"widget_t_7_{KT}")
        self.widget_t_7.setStyleSheet (f"#{self.widget_t_7.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_7 = QtWidgets.QVBoxLayout(self.widget_t_7)
        
        
        
        
        
        
        self.page_t_8 = QtWidgets.QWidget()
        self.verticalLayout_t_8 = QtWidgets.QVBoxLayout(self.page_t_8)
        self.horizontalLayout_t_8 = QtWidgets.QHBoxLayout()
        self.widget_t_8 = QtWidgets.QWidget()
        self.widget_t_8.setMaximumSize(QtCore.QSize(900, 400))
        self.widget_t_8.setObjectName(f"widget_t_8_{KT}")
        self.widget_t_8.setStyleSheet (f"#{self.widget_t_8.objectName()}" "{\n"
"background-color: rgb(194, 194, 194); \n"
"}")
        self.verticalLayout_w_8 = QtWidgets.QVBoxLayout(self.widget_t_8)
       
       
       
        KT += 1
        self.stackedWidget_t.addWidget(self.page_t_1)
        self.stackedWidget_t.addWidget(self.page_t_2)
        self.stackedWidget_t.addWidget(self.page_t_3)
        self.stackedWidget_t.addWidget(self.page_t_4)
        self.stackedWidget_t.addWidget(self.page_t_5)
        self.stackedWidget_t.addWidget(self.page_t_6)
        self.stackedWidget_t.addWidget(self.page_t_7)
        self.stackedWidget_t.addWidget(self.page_t_8)
        
        
        
        
        
        
        
        
        # self.widget_t_1 = QtWidgets.QWidget()
#         self.widget_t_1.setStyleSheet ((self.widget_t_1) "{\n"
# "background-color: rgb(194, 194, 194); \n"
# "}")
#         self.verticalLayout_t = QtWidgets.QVBox Layout(self.widget_t_1)
#         self.verticalLayout_t.setObjectName("verticalLayout_t")
#         self.ui.verticalLayout_7.addWidget(self.widget_t_1)
#         # Основное размещение (верхнее)
#         self.horizontalLayout_01 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_01.setObjectName("horizontalLayout_01_")
#         self.verticalLayout_t.addLayout(self.horizontalLayout_01)
#         # Размещение текстового поля
#         self.horizontalLayout_04 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_04.setObjectName("horizontalLayout_04_")
#         self.horizontalLayout_01.addLayout(self.horizontalLayout_04)
#         # Размещение кнопки
#         self.horizontalLayout_05 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_05.setObjectName("horizontalLayout_05_")
#         self.horizontalLayout_01.addLayout(self.horizontalLayout_05)
#         # Текстовое поле
#         self.textField_01 = QtWidgets.QTextEdit()
#         self.textField_01.setMaximumSize(QtCore.QSize(425, 60))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.textField_01.setFont(font)
#         self.textField_01.setStyleSheet("#Vopros_0 {\n"
# "background-color: rgb(181, 173, 173);\n"
# "}\n"
# "#Vopros_0:Focus {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}")
#         self.textField_01.setObjectName("Vopros_0")
#         self.horizontalLayout_04.addWidget(self.textField_01)
#         self.textField_01.setPlaceholderText("ВОПРОС")
#         # Кнопка
#         self.pushButton_01 = QtWidgets.QPushButton()
#         self.pushButton_01.setMaximumSize(QtCore.QSize(141, 80))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.pushButton_01.setFont(font)
#         self.pushButton_01.setObjectName("pushButton_01")
#         self.pushButton_01.setStyleSheet("#pushButton_01 {\n"
# "border: 3px solid;\n"
# "border-radius: 9px;\n"
# "border-color: #7A6D6D;\n"
# "background-color: #BBB4B4\n"
# "}\n"
# "#pushButton_01:hover {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}\n"
# "#pushButton_01:pressed { \n"
# "background-color: #BBB4B4;\n"
# "}")
#         self.horizontalLayout_05.addWidget(self.pushButton_01)
#         self.pushButton_01.setText(_translate("MainWindow", "ОДИН ИЗ\nСПИСКА"))
#         ### Вторая часть, Основное размещение (середина)
#         self.horizontalLayout_02 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_02.setObjectName("horizontalLayout_02_")
#         self.verticalLayout_t.addLayout(self.horizontalLayout_02)
#         # Размещение текстового поля
#         self.horizontalLayout_06 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_06.setObjectName("horizontalLayout_06_")
#         self.horizontalLayout_02.addLayout(self.horizontalLayout_06)
#         # Текстовое поле
#         self.textField_02 = QtWidgets.QTextEdit()
#         self.textField_02.setMaximumSize(QtCore.QSize(425, 60))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.textField_02.setFont(font)
#         self.textField_02.setStyleSheet("#Answer_0 {\n"
# "background-color: rgb(181, 173, 173);\n"
# "}\n"
# "#Answer_0:Focus {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}")
#         self.textField_02.setObjectName("Answer_0")
#         self.horizontalLayout_06.addWidget(self.textField_02)
#         self.textField_02.setPlaceholderText("КРАТКИЙ ОТВЕТ")
#         # Размещение кнопок
#         self.horizontalLayout_07 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_07.setObjectName("horizontalLayout_07_")
#         self.horizontalLayout_02.addLayout(self.horizontalLayout_07)
#         ## Кнопки
#         self.pushButton_02 = QtWidgets.QPushButton()
#         self.pushButton_02.setMaximumSize(QtCore.QSize(100, 48))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.pushButton_02.setFont(font)
#         self.pushButton_02.setObjectName("pushButton_02")
#         self.pushButton_02.setStyleSheet("#pushButton_02 {\n"
# "border: 3px solid;\n"
# "border-radius: 9px;\n"
# "border-color: #7A6D6D;\n"
# "background-color: #BBB4B4\n"
# "}\n"
# "#pushButton_02:hover {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}\n"
# "#pushButton_02:pressed { \n"
# "background-color: #BBB4B4;\n"
# "}")
#         self.horizontalLayout_07.addWidget(self.pushButton_02)
#         self.pushButton_02.setText(_translate("MainWindow", "ТЭГ"))
#         # Кнопка вопроса
#         self.pushButton20 = QtWidgets.QPushButton()
#         self.pushButton20.setMaximumSize(QtCore.QSize(37, 33))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.pushButton20.setFont(font)
#         self.pushButton20.setObjectName("pushButton20")
#         self.pushButton20.setStyleSheet("#pushButton20 {\n"
# "border: 3px solid;\n"
# "border-radius: 9px;\n"
# "border-color: #7A6D6D;\n"
# "background-color: #BBB4B4\n"
# "}\n"
# "#pushButton20:hover {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}\n"
# "#pushButton20:pressed { \n"
# "background-color: #BBB4B4;\n"
# "}")
#         self.horizontalLayout_07.addWidget(self.pushButton20)
#         self.pushButton20.setText(_translate("MainWindow", "?"))
#         ### Третья часть
#         self.horizontalLayout_03 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_03.setObjectName("horizontalLayout_03_")
#         self.verticalLayout_t.addLayout(self.horizontalLayout_03)
#         # Кнопка копирования
#         self.pushButton_03 = QtWidgets.QPushButton()
#         self.pushButton_03.setMaximumSize(QtCore.QSize(43, 41))
#         self.pushButton_03.setObjectName("pushButton_03")
#         self.pushButton_03.setStyleSheet("#pushButton_03 {\n"
# "border: 3px solid;\n"
# "image: url(:/Copycopycopy/Copycopycopy.png);\n"
# "border-radius: 9px;\n"
# "border-color: #7A6D6D;\n"
# "background-color: #BBB4B4\n"
# "}\n"
# "#pushButton_03:hover {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}\n"
# "#pushButton_03:pressed { \n"
# "background-color: #BBB4B4;\n"
# "}")
#         self.horizontalLayout_03.addWidget(self.pushButton_03)
#         # Кнопка удаление
#         self.pushButton_04 = QtWidgets.QPushButton()
#         self.pushButton_04.setMaximumSize(QtCore.QSize(43, 41))
#         self.pushButton_04.setObjectName("pushButton_04")
#         self.pushButton_04.setStyleSheet("#pushButton_04 {\n"
# "border: 3px solid;\n"
# "image: url(:/Trashcan/trashcan.png);\n"
# "border-radius: 9px;\n"
# "border-color: #7A6D6D;\n"
# "background-color: #BBB4B4\n"
# "}\n"
# "#pushButton_04:hover {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}\n"
# "#pushButton_04:pressed { \n"
# "background-color: #BBB4B4;\n"
# "}")
#         self.horizontalLayout_03.addWidget(self.pushButton_04)
#         # Надпись
#         self.Label_01 = QtWidgets.QLabel()
#         self.Label_01.setMaximumSize(QtCore.QSize(400, 34))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.Label_01.setFont(font)
#         self.Label_01.setObjectName("Label_01")
        
#         self.horizontalLayout_03.addWidget(self.Label_01)
#         self.Label_01.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
#         # Кнопка галочка
#         self.pushButton_05 = QtWidgets.QPushButton()
#         self.pushButton_05.setMaximumSize(QtCore.QSize(43, 41))
#         self.pushButton_05.setObjectName("pushButton_05")
#         self.pushButton_05.setStyleSheet("#pushButton_05 {\n"
# "border: 3px solid;\n"
# "image: url(:/Galka/galka.png);\n"
# "border-radius: 9px;\n"
# "border-color: #7A6D6D;\n"
# "background-color: #BBB4B4\n"
# "}\n"
# "#pushButton_05:hover {\n"
# "background-color: rgb(219, 219, 219);\n"
# "}\n"
# "#pushButton_05:pressed { \n"
# "background-color: #BBB4B4;\n"
# "}")
#         self.horizontalLayout_03.addWidget(self.pushButton_05)



        
        
    def transfer_back(self):
        global KT
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
        KT = 1
    def transfer_Fill(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.Button_Back_Fill.clicked.connect(self.transfer_back)

app = QApplication([])
AppWindow_main = AppWindow_main()
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())
