# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eksempel_Variable_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Opgave_Variable_1 import Ui_Variabel_Opgave

class Ui_Variabel_Eksempel(object):
    
    def open_window_neaste(self):
        #Variabel.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Variabel_Opgave()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, Variabel):
        Variabel.setObjectName("Variabel")
        Variabel.resize(800, 600)

        self.label = QtWidgets.QLabel(Variabel)
        self.label.setGeometry(QtCore.QRect(230, 10, 360, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(Variabel)
        self.textBrowser.setGeometry(QtCore.QRect(100, 100, 620, 410))
        self.textBrowser.setObjectName("textBrowser")

        self.btnForlad = QtWidgets.QPushButton(Variabel)
        self.btnForlad.setGeometry(QtCore.QRect(352, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btnForlad.setFont(font)
        self.btnForlad.setObjectName("btnForlad")

        self.btnNst = QtWidgets.QPushButton(Variabel)
        self.btnNst.setGeometry(QtCore.QRect(654, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btnNst.setFont(font)
        self.btnNst.setObjectName("btnNst")
        self.btnNst.clicked.connect(self.open_window_neaste)

        self.btnTilbage = QtWidgets.QPushButton(Variabel)
        self.btnTilbage.setGeometry(QtCore.QRect(50, 540, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btnTilbage.setFont(font)
        self.btnTilbage.setObjectName("btnTilbage")

        self.retranslateUi(Variabel)
        QtCore.QMetaObject.connectSlotsByName(Variabel)

    def retranslateUi(self, Variabel):
        _translate = QtCore.QCoreApplication.translate
        Variabel.setWindowTitle(_translate("Variabel", "Form"))
        self.label.setText(_translate("Variabel", "Variabel - Ekempel"))
        self.textBrowser.setHtml(_translate("Variabel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Her laver vi en variabel x med en int værdi 11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Kode:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">x = </span><span style=\" font-size:12pt; color:#0000ff;\">11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Her laver vi en variabel y med en string værdi Jasper</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Kode:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">y = </span><span style=\" font-size:12pt; color:#0000ff;\">&quot;Jasper&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">Vi kan nu printe de to variabler til konsollen </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">Her printer vi x</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#aa5500;\">print</span><span style=\" font-size:12pt; color:#000000;\">(x)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">Her printer vi y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#aa5500;\">print</span><span style=\" font-size:12pt; color:#000000;\">(y)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">På næste side kommer du til en opgave, hvor du selv skal laver en variabel.</span></p></body></html>"))
        self.btnForlad.setText(_translate("Variabel", "Forlad"))
        self.btnNst.setText(_translate("Variabel", "Næste"))
        self.btnTilbage.setText(_translate("Variabel", "Tilbage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Variabel = QtWidgets.QWidget()
    ui = Ui_Variabel_Eksempel()
    ui.setupUi(Variabel)
    Variabel.show()
    sys.exit(app.exec_())
