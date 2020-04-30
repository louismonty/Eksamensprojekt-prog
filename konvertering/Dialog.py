import random 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def loop(self):
        f = open("konvertering/tekst.txt", "r")
        vokaler = ["a","e","i","o","u","y"]
        tekst=[]

        for i in f:
            tekst += i.split()

        chosen = tekst[int(random.uniform(0,len(tekst)))]

        chosen_p=""

        for i in chosen:
            if i in vokaler:
                chosen_p+="_"
            else:
                chosen_p += i
        return(chosen_p,chosen)

    
    def setupUi(self, Form):
        self.text,self.right = self.loop()
        Form.setObjectName("Form")
        Form.resize(540, 413)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 380, 158, 25))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.giv_op)
        
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.ok)
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 521, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.ok)
        self.verticalLayout_2.addWidget(self.lineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ok(self):
        if self.lineEdit.text() == self.right:
            self.text,self.right = self.loop()
            self.label.setText(self.text)
            self.lineEdit.setText("")
            
    def giv_op(self):
        self.text,self.right = self.loop()
        self.label.setText(self.text)
        self.lineEdit.setText("")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "giv op"))
        self.pushButton.setText(_translate("Form", "svar"))
        self.label.setText(_translate("Form", self.text))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
