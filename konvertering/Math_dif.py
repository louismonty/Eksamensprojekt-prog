# -*- coding: utf-8 -*-

# window implementation generated from reading ui file 'Mat2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


math_type = ""

class Ui_Math(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(421, 344)
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(110, 60, 171, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Multiply)
        
        self.pushButton_2 = QtWidgets.QPushButton(window)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 140, 171, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.substracting)
        
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(110, 10, 161, 41))
        self.label.setObjectName("label")
        
        self.pushButton_5 = QtWidgets.QPushButton(window)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 220, 171, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.multiplication)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def Multiply(self):
        math_type = "multiply"
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Math()
        self.ui.setupUi(self.window)
        self.window.show()
        
    
    def substracting(self):
        math_type = "Subtracting"
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Math()
        self.ui.setupUi(self.window)
        self.window.show()

    def multiplication(self):
        math_type ="Multiplication"
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Math()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "window"))
        self.pushButton.setText(_translate("window", "Easy"))
        self.pushButton_2.setText(_translate("window", ""))
        self.label.setText(_translate("window", "Chose you ..."))
        self.pushButton_5.setText(_translate("window", "Multiplication"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Math()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
