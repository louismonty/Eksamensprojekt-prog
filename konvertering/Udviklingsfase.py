# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Udviklingsfase.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Udviklingsfase(object):
    def setupUi(self, Variabel):
        Variabel.setObjectName("Variabel")
        Variabel.resize(800, 600)
        self.label = QtWidgets.QLabel(Variabel)
        self.label.setGeometry(QtCore.QRect(230, 220, 360, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Variabel)
        QtCore.QMetaObject.connectSlotsByName(Variabel)

    def retranslateUi(self, Variabel):
        _translate = QtCore.QCoreApplication.translate
        Variabel.setWindowTitle(_translate("Variabel", "Form"))
        self.label.setText(_translate("Variabel", "Udviklingsstadie..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Variabel = QtWidgets.QWidget()
    ui = Ui_Udviklingsfase()
    ui.setupUi(Variabel)
    Variabel.show()
    sys.exit(app.exec_())
