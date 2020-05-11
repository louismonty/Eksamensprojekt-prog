import random 


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def loop(self,dificulty):
        f = open("konvertering/tekst.txt", "r")
        vokaler = ["a","e","i","o","u","y"]
        stop = False
        tekst=[]
        for i in f:
            i = i.lower()
            tekst += i.split()
        while stop == False:
            n = 0
            chosen = tekst[int(random.uniform(0,len(tekst)))]

            chosen_p=""

            for i in chosen:
                if i in vokaler:
                    chosen_p+="_"
                    n += 1
                else:
                    chosen_p += i
            if n == dificulty:
                stop = True
        return(chosen_p,chosen)

    
    def setupUi(self, Form):
        self.dificulty = 1
        self.text,self.right = self.loop(self.dificulty)
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
        
        self.pushButton_dif = QtWidgets.QPushButton(Form)
        self.pushButton_dif.setGeometry(QtCore.QRect(0, 0, 90, 20))
        self.pushButton_dif.setObjectName("pushButton_2")
        self.pushButton_dif.clicked.connect(self.nem)
        
        self.pushButton_dif_2 = QtWidgets.QPushButton(Form)
        self.pushButton_dif_2.setGeometry(QtCore.QRect(90, 0, 90, 20))
        self.pushButton_dif_2.setObjectName("pushButton_2")
        self.pushButton_dif_2.clicked.connect(self.normal)
        
        self.pushButton_dif_3 = QtWidgets.QPushButton(Form)
        self.pushButton_dif_3.setGeometry(QtCore.QRect(180, 0, 90, 20))
        self.pushButton_dif_3.setObjectName("pushButton_2")
        self.pushButton_dif_3.clicked.connect(self.sver)
        
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
            self.text,self.right = self.loop(self.dificulty)
            self.label.setText(self.text)
            self.lineEdit.setText("")
            
    def giv_op(self):
        self.text,self.right = self.loop(self.dificulty)
        self.label.setText(self.text)
        self.lineEdit.setText("")
        
    def nem(self):
        self.dificulty = 1
        
    def normal(self):
        self.dificulty = 2
        
    def sver(self):
        self.dificulty = 3
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "giv op"))
        self.pushButton.setText(_translate("Form", "svar"))
        self.label.setText(_translate("Form", self.text))
        self.pushButton_dif.setText(_translate("Form", "nem"))
        self.pushButton_dif_2.setText(_translate("Form", "normal"))
        self.pushButton_dif_3.setText(_translate("Form", "svær"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
