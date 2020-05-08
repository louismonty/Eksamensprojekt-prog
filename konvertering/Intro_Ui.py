# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Intro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from Teori_Variable_1 import Ui_Variabel

class Ui_Intro(object):
    def open_window_naeste(self):
        Form.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Variabel()
        self.ui.setupUi(self.window)
        self.window.show
    
    def close_window_Intro(self, event):
        reply = QMessageBox.question(Form, 'Window close', 'Are you sure you want to close the window?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 610)

        # Head Label "Programmering - Intro"
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 360, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Textbrowser with text 
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(90, 100, 620, 410))
        self.textBrowser.setObjectName("textBrowser")

        # Button "Næste" 
        self.BtnNst = QtWidgets.QPushButton(Form)
        self.BtnNst.setGeometry(QtCore.QRect(654, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.BtnNst.setFont(font)
        self.BtnNst.setObjectName("BtnNst")
        self.BtnNst.clicked.connect(self.open_window_naeste)

        # Button "Forlad"
        self.BtnForlad = QtWidgets.QPushButton(Form)
        self.BtnForlad.setGeometry(QtCore.QRect(352, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.BtnForlad.setFont(font)
        self.BtnForlad.setObjectName("BtnForlad")
        self.BtnForlad.clicked.connect(self.close_window_Intro)

        #Button "Tilbae"
        self.BtnTilbage = QtWidgets.QPushButton(Form)
        self.BtnTilbage.setGeometry(QtCore.QRect(50, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.BtnTilbage.setFont(font)
        self.BtnTilbage.setObjectName("BtnTilbage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Programmering - Intro"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><a name=\"docs-internal-guid-30bfc0a7-7fff-7a80-b7e2-b8786a257718\"></a><span style=\" font-family:\'Palatino Linotype\',\'serif\'; font-size:12pt; color:#000000; background-color:transparent;\">V</span><span style=\" font-family:\'Palatino Linotype\',\'serif\'; font-size:12pt; color:#000000; background-color:transparent;\">i vil starte med at lærer at programmere i Python. Python er det man kalder et objektorienteret programmeringssprog på højt niveau, hvilket vil sige at det er opbygget via objekter og klasser. Python bruges til at udarbejde mange forskellige opgaver:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\">Webudvikling</li>\n"
"<li style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\">Softwareudvikling</li>\n"
"<li style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\">Matematik</li>\n"
"<li style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" background-color:#ffffff;\">System scripting</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Palatino Linotype\',\'serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\">Vi vil komme til at arbejde med softwareudvikling, hvor i vil lærer de mest basale elementer og bruge det til at udføre små opgaver. I vil til sidst kunne udarbejde et lille projekt, som vil tage udgangspunkt i de elementer i har lært.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>"))
        self.BtnNst.setText(_translate("Form", "Næste"))
        self.BtnForlad.setText(_translate("Form", "Forlad"))
        self.BtnTilbage.setText(_translate("Form", "Tilbage"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Intro()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
