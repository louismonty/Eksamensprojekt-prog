# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teori_Variable_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Eksempel_Variable_1 import Ui_Variabel_Eksempel

class Ui_Variabel(object):

    def open_window_neaste(self):
        #Variabel.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Variabel_Eksempel()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Variabel):
        Variabel.setObjectName("Variabel")
        Variabel.resize(804, 610)

        self.label = QtWidgets.QLabel(Variabel)
        self.label.setGeometry(QtCore.QRect(230, 10, 360, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(Variabel)
        self.textBrowser.setGeometry(QtCore.QRect(90, 100, 620, 410))
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
        self.label.setText(_translate("Variabel", "Variabel "))
        self.textBrowser.setHtml(_translate("Variabel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Variabler er i det hele taget bare reseveret hukommelse og man skal derfor bare se det som at resevere noget plads i hukommelsen når du laver en variabel.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Der er forskellige typer af variabler og de bestemmer hvordan din data er reseveret i hukommelsen, python har fem standard data typer, som er: </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:11pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numbers </li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">String</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">List</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tuple</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dictonary </li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Når man skal lave variabler gør man det ved at skrive hvad man vil have variablen til at hedde, derefter sætter du tegnet = som vil sige at man sætte en værdi til variablen og til sidst sætter værdien af variablen.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Der vises et eksempel på næste side.</span></p></body></html>"))
        self.btnForlad.setText(_translate("Variabel", "Forlad"))
        self.btnNst.setText(_translate("Variabel", "Næste"))
        self.btnTilbage.setText(_translate("Variabel", "Tilbage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Variabel = QtWidgets.QWidget()
    ui = Ui_Variabel()
    ui.setupUi(Variabel)
    Variabel.show()
    sys.exit(app.exec_())
