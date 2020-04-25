# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Intro.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Intro(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(804, 610)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 291, 51))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(112, 100, 580, 410))
        self.BtnNst = QPushButton(Form)
        self.BtnNst.setObjectName(u"BtnNst")
        self.BtnNst.setGeometry(QRect(654, 540, 100, 50))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(20)
        self.BtnNst.setFont(font1)
        self.BtnForlad = QPushButton(Form)
        self.BtnForlad.setObjectName(u"BtnForlad")
        self.BtnForlad.setGeometry(QRect(352, 540, 100, 50))
        self.BtnForlad.setFont(font1)
        self.BtnTilbage = QPushButton(Form)
        self.BtnTilbage.setObjectName(u"BtnTilbage")
        self.BtnTilbage.setGeometry(QRect(50, 540, 100, 50))
        self.BtnTilbage.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Programmering - Intro", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><a name=\"docs-internal-guid-30bfc0a7-7fff-7a80-b7e2-b8786a257718\"></a><span style=\" font-family:'Palatino Linotype','serif'; font-size:12pt; color:#000000; background-color:transparent;\">V</span><span style=\" font-family:'Palatino Linotype','serif'; font-size:12pt; color:#000000; background-color:transparent;\">i vil starte med at l\u00e6rer at programmere i Python. Python er det man kalder et objektorienteret programmeringssprog p\u00e5 h\u00f8jt niveau, hvilket vil sige at det er opbygget via objekter og klasser. Python bruges til"
                        " at udarbejde mange forskellige opgaver:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'Courier New'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\">Webudvikling</li>\n"
"<li style=\" font-family:'Courier New'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\">Softwareudvikling</li>\n"
"<li style=\" font-family:'Courier New'; font-size:12pt; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\">Matematik</li>\n"
"<li style=\" font-family:'Courier New'; font-size:12pt; color:#000000; backg"
                        "round-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" background-color:#ffffff;\">System scripting</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:'Palatino Linotype','serif'; font-size:12pt; color:#000000; background-color:#ffffff;\">Vi vil komme til at arbejde med softwareudvikling, hvor i vil l\u00e6rer de mest basale elementer og bruge det til at udf\u00f8re sm\u00e5 opgaver. I vil til sidst kunne udarbejde et lille projekt, som vil tage udgangspunkt i de elementer i har l\u00e6rt.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>", None))
        self.BtnNst.setText(QCoreApplication.translate("Form", u"N\u00e6ste", None))
        self.BtnForlad.setText(QCoreApplication.translate("Form", u"Forlad", None))
        self.BtnTilbage.setText(QCoreApplication.translate("Form", u"Tilbage", None))
    # retranslateUi

