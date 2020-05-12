# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Opgave_Variable_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Udviklingsfase import Ui_Udviklingsfase

class Ui_Variabel_Opgave2(object):
        
    def rightAnswer(self):
        Answer1 = "hej"
        Answer2 = "hej"
        if self.Answer_1.text() == Answer1 and self.Answer_2.text() == Answer2:
            #Variabel.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Udviklingsfase()
            self.ui.setupUi(self.window)
            self.window.show()

    def setupUi(self, Variabel):
        Variabel.setObjectName("Variabel")
        Variabel.resize(800, 600)

        # Head label "Variabel - Opgave 1"
        self.label = QtWidgets.QLabel(Variabel)
        self.label.setGeometry(QtCore.QRect(230, 10, 360, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Button "Forlad"
        self.btnForlad = QtWidgets.QPushButton(Variabel)
        self.btnForlad.setGeometry(QtCore.QRect(352, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btnForlad.setFont(font)
        self.btnForlad.setObjectName("btnForlad")

        # Button "Næste"
        self.btnNst = QtWidgets.QPushButton(Variabel)
        self.btnNst.setGeometry(QtCore.QRect(654, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btnNst.setFont(font)
        self.btnNst.setObjectName("btnNst")
        self.btnNst.clicked.connect(self.rightAnswer)

        # Button Tilbage
        self.btnTilbage = QtWidgets.QPushButton(Variabel)
        self.btnTilbage.setGeometry(QtCore.QRect(50, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btnTilbage.setFont(font)
        self.btnTilbage.setObjectName("btnTilbage")

        # Label 1 for opgave 1.1
        self.Lbl_Head_1 = QtWidgets.QLabel(Variabel)
        self.Lbl_Head_1.setGeometry(QtCore.QRect(200, 110, 400, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Lbl_Head_1.setFont(font)
        self.Lbl_Head_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Lbl_Head_1.setObjectName("Lbl_Head_1")

        # Textbrowser for opgave 1.1
        self.textBrowser_1 = QtWidgets.QTextBrowser(Variabel)
        self.textBrowser_1.setGeometry(QtCore.QRect(200, 140, 400, 31))
        self.textBrowser_1.setObjectName("textBrowser_1")
        
        # Lineedit for opgave 1.1
        self.Answer_1 = QtWidgets.QLineEdit(Variabel)
        self.Answer_1.setGeometry(QtCore.QRect(350, 180, 251, 22))
        self.Answer_1.setObjectName("Answer_1")
        
        # Label 2 for opgave 1.1
        self.Lbl_answer_1 = QtWidgets.QLabel(Variabel)
        self.Lbl_answer_1.setGeometry(QtCore.QRect(210, 180, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Lbl_answer_1.setFont(font)
        self.Lbl_answer_1.setObjectName("Lbl_answer_1")

        # Label 1 for opgave 1.2
        self.Lbl_Head_2 = QtWidgets.QLabel(Variabel)
        self.Lbl_Head_2.setGeometry(QtCore.QRect(200, 250, 400, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Lbl_Head_2.setFont(font)
        self.Lbl_Head_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Lbl_Head_2.setObjectName("Lbl_Head_2")

        # Textbrowser for opgave 1.2
        self.textBrowser_2 = QtWidgets.QTextBrowser(Variabel)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 280, 400, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        # Label 2 for opgave 1.2
        self.Lbl_answer_2 = QtWidgets.QLabel(Variabel)
        self.Lbl_answer_2.setGeometry(QtCore.QRect(210, 320, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Lbl_answer_2.setFont(font)
        self.Lbl_answer_2.setObjectName("Lbl_answer_2")

        # Lineedit for opgave 1.2
        self.Answer_2 = QtWidgets.QLineEdit(Variabel)
        self.Answer_2.setGeometry(QtCore.QRect(350, 320, 251, 22))
        self.Answer_2.setObjectName("Answer_2")


        self.retranslateUi(Variabel)
        QtCore.QMetaObject.connectSlotsByName(Variabel)

    def retranslateUi(self, Variabel):
        _translate = QtCore.QCoreApplication.translate
        Variabel.setWindowTitle(_translate("Variabel", "Form"))
        self.label.setText(_translate("Variabel", "Variabel - Opgave 2"))
        self.btnForlad.setText(_translate("Variabel", "Forlad"))
        self.btnNst.setText(_translate("Variabel", "Næste"))
        self.btnTilbage.setText(_translate("Variabel", "Tilbage"))
        self.Lbl_Head_1.setText(_translate("Variabel", "Værdien af variablen skal være \"Hej\", hvad magler der"))
        self.textBrowser_1.setHtml(_translate("Variabel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Venlig = &quot;___&quot;</span></p></body></html>"))
        self.Lbl_answer_1.setText(_translate("Variabel", "Indsæt svar her:"))
        self.Lbl_Head_2.setText(_translate("Variabel", "Hvad bliver der printet i konsollen?"))
        self.textBrowser_2.setHtml(_translate("Variabel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa5500;\">print</span><span style=\" font-size:14pt;\">(Venlig)</span></p></body></html>"))
        self.Lbl_answer_2.setText(_translate("Variabel", "Indsæt svar her:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Variabel = QtWidgets.QWidget()
    ui = Ui_Variabel_Opgave2()
    ui.setupUi(Variabel)
    Variabel.show()
    sys.exit(app.exec_())
