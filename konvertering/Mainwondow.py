# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog import Ui_Form
from Math_chose import Ui_Math
from Intro_Ui import Ui_Intro
from datetime import datetime

class Ui_MainWindow(object):
    def open_window_mat(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Math()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def open_window_dansk(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def open_window_prog(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Intro()
        self.ui.setupUi(self.window)
        self.window.show()

            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Head label "Læringsplatform"
        self.LblHead = QtWidgets.QLabel(self.frame)
        self.LblHead.setGeometry(QtCore.QRect(260, 10, 280, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.LblHead.setFont(font)
        self.LblHead.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LblHead.setAlignment(QtCore.Qt.AlignCenter)
        self.LblHead.setObjectName("LblHead")
        
        # Button "Matematik"
        self.BtnMat = QtWidgets.QPushButton(self.frame)
        self.BtnMat.setGeometry(QtCore.QRect(310, 160, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.BtnMat.setFont(font)
        self.BtnMat.setObjectName("BtnMat")
        self.BtnMat.clicked.connect(self.open_window_mat)
        
        # Button "Programmering"
        self.BtnProg = QtWidgets.QPushButton(self.frame)
        self.BtnProg.setGeometry(QtCore.QRect(310, 260, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.BtnProg.setFont(font)
        self.BtnProg.setObjectName("BtnProg")
        self.BtnProg.clicked.connect(self.open_window_prog)
        
        # Button "Dansk"
        self.BtnDansk = QtWidgets.QPushButton(self.frame)
        self.BtnDansk.setGeometry(QtCore.QRect(310, 360, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.BtnDansk.setFont(font)
        self.BtnDansk.setObjectName("BtnDansk")
        self.BtnDansk.clicked.connect(self.open_window_dansk)
        
        # Button "Folad"
        self.BtnForlad = QtWidgets.QPushButton(self.frame)
        self.BtnForlad.setGeometry(QtCore.QRect(310, 460, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.BtnForlad.setFont(font)
        self.BtnForlad.setObjectName("BtnForlad")
        
        # Date Label
        self.LblDato = QtWidgets.QLabel(self.centralwidget)
        self.LblDato.setGeometry(QtCore.QRect(10, 550, 781, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.LblDato.setFont(font)
        self.LblDato.setObjectName("LblDato")
        
        MainWindow.setCentralWidget(self.centralwidget)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    CurrentDate = datetime.now()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LblHead.setText(_translate("MainWindow", "Læringsplatform"))
        self.BtnMat.setText(_translate("MainWindow", "Matematik"))
        self.BtnProg.setText(_translate("MainWindow", "Programmering"))
        self.BtnDansk.setText(_translate("MainWindow", "Dansk"))
        self.BtnForlad.setText(_translate("MainWindow", "Forlad"))
        CurrentDate = datetime.now()
        self.LblDato.setText(_translate("MainWindow", "Dato: " + str(CurrentDate)))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
