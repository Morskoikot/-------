# Form implementation generated from reading ui file 'Main_s.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 557)
        MainWindow.setMaximumSize(QtCore.QSize(790, 557))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(790, 557))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, -1, 771, 491))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Main_page = QtWidgets.QWidget()
        self.Main_page.setMaximumSize(QtCore.QSize(790, 557))
        self.Main_page.setObjectName("Main_page")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.Main_page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1, 158, 771, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Zapolnit = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Button_Zapolnit.setMaximumSize(QtCore.QSize(270, 180))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_Zapolnit.setFont(font)
        self.Button_Zapolnit.setStyleSheet("#Button_Zapolnit{\n"
"background-color: rgb(133, 114, 85);\n"
"border-top-left-radius: 30px;\n"
"border-bottom-right-radius: 30px;\n"
"border: 2px solid;\n"
"}\n"
"#Button_Zapolnit:hover {\n"
"background:#dabb8b;\n"
"}\n"
"#Button_Zapolnit:pressed {\n"
"background-color: rgb(133, 114, 85);\n"
"}")
        self.Button_Zapolnit.setObjectName("Button_Zapolnit")
        self.horizontalLayout.addWidget(self.Button_Zapolnit)
        self.Button_Spisok = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Button_Spisok.setMaximumSize(QtCore.QSize(270, 180))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_Spisok.setFont(font)
        self.Button_Spisok.setStyleSheet("#Button_Spisok{\n"
"background-color: rgb(133, 114, 85);\n"
"border-top-right-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"border: 2px solid;\n"
"}\n"
"#Button_Spisok:hover {\n"
"background:#dabb8b;\n"
"}\n"
"#Button_Spisok:pressed {\n"
"background-color: rgb(133, 114, 85);\n"
"}")
        self.Button_Spisok.setObjectName("Button_Spisok")
        self.horizontalLayout.addWidget(self.Button_Spisok)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.Main_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 771, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Glavnaya = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.Glavnaya.setMaximumSize(QtCore.QSize(760, 142))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.Glavnaya.setFont(font)
        self.Glavnaya.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Glavnaya.setStyleSheet("border: 2px solid;\n"
"border-top-left-radius: 55px;\n"
"border-top-right-radius: 55px;\n"
"border-bottom-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.505682, y1:0, x2:0.501, y2:0.511, stop:0 rgba(19, 19, 19, 255), stop:0.0227273 rgba(89, 67, 42, 239), stop:1 rgba(249, 179, 96, 200));")
        self.Glavnaya.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Glavnaya.setObjectName("Glavnaya")
        self.horizontalLayout_5.addWidget(self.Glavnaya)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.Main_page)
        self.Add_Page = QtWidgets.QWidget()
        self.Add_Page.setMaximumSize(QtCore.QSize(790, 557))
        self.Add_Page.setObjectName("Add_Page")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.Add_Page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 771, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Dobavochnoe_pole = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.Dobavochnoe_pole.setMaximumSize(QtCore.QSize(777, 112))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.Dobavochnoe_pole.setFont(font)
        self.Dobavochnoe_pole.setStyleSheet("border: 2px solid;\n"
"background-color: qlineargradient(spread:pad, x1:0.505682, y1:0, x2:0.501, y2:0.511, stop:0 rgba(19, 19, 19, 255), stop:0.0227273 rgba(89, 67, 42, 239), stop:1 rgba(249, 179, 96, 200));\n"
"border-top-left-radius: 55px;\n"
"border-top-right-radius: 55px;\n"
"border-bottom-left-radius: 22px;\n"
"border-bottom-right-radius: 22px;\n"
"\n"
"")
        self.Dobavochnoe_pole.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Dobavochnoe_pole.setObjectName("Dobavochnoe_pole")
        self.horizontalLayout_14.addWidget(self.Dobavochnoe_pole)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Dobavit_dokument_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.Dobavit_dokument_label.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Dobavit_dokument_label.setFont(font)
        self.Dobavit_dokument_label.setObjectName("Dobavit_dokument_label")
        self.horizontalLayout_2.addWidget(self.Dobavit_dokument_label)
        self.Button_Dok = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.Button_Dok.setMaximumSize(QtCore.QSize(120, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Dok.setFont(font)
        self.Button_Dok.setStyleSheet("#Button_Dok {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Dok:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Dok:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Dok.setObjectName("Button_Dok")
        self.horizontalLayout_2.addWidget(self.Button_Dok)
        self.Button_Forma_plus = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.Button_Forma_plus.setMaximumSize(QtCore.QSize(157, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Forma_plus.setFont(font)
        self.Button_Forma_plus.setStyleSheet("#Button_Forma_plus {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Forma_plus:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Forma_plus:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Forma_plus.setObjectName("Button_Forma_plus")
        self.horizontalLayout_2.addWidget(self.Button_Forma_plus)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.frame.setMaximumSize(QtCore.QSize(729, 284))
        self.frame.setStyleSheet("#frame {\n"
"border: 4px solid;\n"
"border-radius: 10px;\n"
"border-color: #8E8080;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 731, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Vopros = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_3)
        self.Vopros.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Vopros.setFont(font)
        self.Vopros.setStyleSheet("#Vopros {\n"
"background-color: rgb(181, 173, 173);\n"
"}\n"
"#Vopros:Focus {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
        self.Vopros.setObjectName("Vopros")
        self.horizontalLayout_8.addWidget(self.Vopros)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Odin_iz_spiska = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Odin_iz_spiska.setMaximumSize(QtCore.QSize(141, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Odin_iz_spiska.setFont(font)
        self.Odin_iz_spiska.setStyleSheet("#Odin_iz_spiska {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Odin_iz_spiska:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Odin_iz_spiska:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Odin_iz_spiska.setObjectName("Odin_iz_spiska")
        self.horizontalLayout_9.addWidget(self.Odin_iz_spiska)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Kratki_otvet = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_3)
        self.Kratki_otvet.setMaximumSize(QtCore.QSize(425, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Kratki_otvet.setFont(font)
        self.Kratki_otvet.setStyleSheet("#Kratki_otvet {\n"
"background-color: rgb(181, 173, 173);\n"
"}\n"
"#Kratki_otvet:Focus {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
        self.Kratki_otvet.setObjectName("Kratki_otvet")
        self.horizontalLayout_12.addWidget(self.Kratki_otvet)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Button_Teg = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Button_Teg.setMaximumSize(QtCore.QSize(100, 48))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Teg.setFont(font)
        self.Button_Teg.setStyleSheet("#Button_Teg {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Teg:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Teg:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Teg.setObjectName("Button_Teg")
        self.horizontalLayout_11.addWidget(self.Button_Teg)
        self.Button_Question = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Button_Question.setMaximumSize(QtCore.QSize(37, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Question.setFont(font)
        self.Button_Question.setStyleSheet("#Button_Question {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Question:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Question:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Question.setObjectName("Button_Question")
        self.horizontalLayout_11.addWidget(self.Button_Question)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Button_Copy = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Button_Copy.setMaximumSize(QtCore.QSize(43, 41))
        self.Button_Copy.setStyleSheet("#Button_Copy {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4;\n"
"image: url(:/Copycopycopy/Copycopycopy.png);\n"
"}\n"
"#Button_Copy:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Copy:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Copy.setText("")
        self.Button_Copy.setObjectName("Button_Copy")
        self.horizontalLayout_13.addWidget(self.Button_Copy)
        self.Button_Trash = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Button_Trash.setMaximumSize(QtCore.QSize(43, 41))
        self.Button_Trash.setStyleSheet("#Button_Trash {\n"
"image: url(:/Trashcan/trashcan.png);\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Trash:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Trash:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Trash.setText("")
        self.Button_Trash.setObjectName("Button_Trash")
        self.horizontalLayout_13.addWidget(self.Button_Trash)
        self.Obyazatelny_vopros = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.Obyazatelny_vopros.setMaximumSize(QtCore.QSize(400, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Obyazatelny_vopros.setFont(font)
        self.Obyazatelny_vopros.setObjectName("Obyazatelny_vopros")
        self.horizontalLayout_13.addWidget(self.Obyazatelny_vopros)
        self.Button_Galka = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Button_Galka.setMaximumSize(QtCore.QSize(43, 41))
        self.Button_Galka.setStyleSheet("#Button_Galka {\n"
"border: 3px solid;\n"
"image: url(:/Galka/galka.png);\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Galka:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Galka:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Galka.setText("")
        self.Button_Galka.setObjectName("Button_Galka")
        self.horizontalLayout_13.addWidget(self.Button_Galka)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Button_Save = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.Button_Save.setMaximumSize(QtCore.QSize(157, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Save.setFont(font)
        self.Button_Save.setStyleSheet("#Button_Save {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Save:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Save:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Save.setObjectName("Button_Save")
        self.horizontalLayout_4.addWidget(self.Button_Save)
        self.Button_Back = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.Button_Back.setMaximumSize(QtCore.QSize(157, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Back.setFont(font)
        self.Button_Back.setStyleSheet("#Button_Back {\n"
"border: 3px solid;\n"
"border-radius: 9px;\n"
"border-color: #7A6D6D;\n"
"background-color: #BBB4B4\n"
"}\n"
"#Button_Back:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"#Button_Back:pressed { \n"
"background-color: #BBB4B4;\n"
"}")
        self.Button_Back.setObjectName("Button_Back")
        self.horizontalLayout_4.addWidget(self.Button_Back)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.Add_Page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_Zapolnit.setText(_translate("MainWindow", " ЗАПОЛНИТЬ\n"
"ДОКУМЕНТ"))
        self.Button_Spisok.setText(_translate("MainWindow", "СПИСОК\n"
"ФОРМ"))
        self.Glavnaya.setText(_translate("MainWindow", "ГЛАВНАЯ"))
        self.Dobavochnoe_pole.setText(_translate("MainWindow", "ДОБАВОЧНОЕ ПОЛЕ"))
        self.Dobavit_dokument_label.setText(_translate("MainWindow", "ДОБАВИТЬ ДОКУМЕНТ"))
        self.Button_Dok.setText(_translate("MainWindow", "ДОК."))
        self.Button_Forma_plus.setText(_translate("MainWindow", "+ ФОРМА"))
        self.Vopros.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Vopros.setPlaceholderText(_translate("MainWindow", "ВОПРОС"))
        self.Odin_iz_spiska.setText(_translate("MainWindow", "ОДИН ИЗ\n"
"СПИСКА"))
        self.Kratki_otvet.setPlaceholderText(_translate("MainWindow", "КРАТКИЙ ОТВЕТ"))
        self.Button_Teg.setText(_translate("MainWindow", "ТЭГ"))
        self.Button_Question.setText(_translate("MainWindow", "?"))
        self.Obyazatelny_vopros.setText(_translate("MainWindow", "ОБЯЗАТЕЛЬНЫЙ ВОПРОС"))
        self.Button_Save.setText(_translate("MainWindow", "Сохранить"))
        self.Button_Back.setText(_translate("MainWindow", "Назад"))
