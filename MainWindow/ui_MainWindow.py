
# Main Window of the program

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


import sys

class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 610)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 791, 541))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.LblHead = QLabel(self.frame)
        self.LblHead.setObjectName(u"LblHead")
        self.LblHead.setGeometry(QRect(260, 10, 280, 61))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        self.LblHead.setFont(font)
        self.LblHead.setLayoutDirection(Qt.LeftToRight)
        self.LblHead.setAlignment(Qt.AlignCenter)
        self.BtnMat = QPushButton(self.frame)
        self.BtnMat.setObjectName(u"BtnMat")
        self.BtnMat.setGeometry(QRect(310, 160, 180, 51))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(16)
        self.BtnMat.setFont(font1)
        self.BtnMat.clicked.connect(self.Mat_clicked)
        
        self.BtnProg = QPushButton(self.frame)
        self.BtnProg.setObjectName(u"BtnProg")
        self.BtnProg.setGeometry(QRect(310, 260, 180, 51))
        self.BtnProg.setFont(font1)
        self.BtnProg.clicked.connect(self.Prog_clicked)
        
        self.BtnDansk = QPushButton(self.frame)
        self.BtnDansk.setObjectName(u"BtnDansk")
        self.BtnDansk.setGeometry(QRect(310, 360, 180, 51))
        self.BtnDansk.setFont(font1)
        self.BtnDansk.clicked.connect(self.Dansk_clicked)
        
        self.BtnForlad = QPushButton(self.frame)
        self.BtnForlad.setObjectName(u"BtnForlad")
        self.BtnForlad.setGeometry(QRect(310, 460, 180, 51))
        self.BtnForlad.setFont(font1)
        self.BtnForlad.clicked.connect(self.Forlad_clicked)
        self.LblDato = QLabel(self.centralwidget)
        self.LblDato.setObjectName(u"LblDato")
        self.LblDato.setGeometry(QRect(10, 550, 781, 20))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(14)
        self.LblDato.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LblHead.setText(QCoreApplication.translate("MainWindow", u"L\u00e6ringsplatform", None))
        self.BtnMat.setText(QCoreApplication.translate("MainWindow", u"Matematik", None))
        self.BtnProg.setText(QCoreApplication.translate("MainWindow", u"Programmering", None))
        self.BtnDansk.setText(QCoreApplication.translate("MainWindow", u"Dansk", None))
        self.BtnForlad.setText(QCoreApplication.translate("MainWindow", u"Forlad", None))
        self.LblDato.setText(QCoreApplication.translate("MainWindow", u"Dato: ", None))
    # retranslateUi
    
    def Mat_clicked(self):
        print("start Mattematik")
        
    def Prog_clicked(self):
        print("start Proggramering")
        
    def Dansk_clicked(self):
        print("start Dansk")
        
    def Forlad_clicked(self):
        print("stop")
        
        
    
