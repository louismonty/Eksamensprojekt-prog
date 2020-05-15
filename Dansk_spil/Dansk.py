#Louis Monty-Krohn HTX Roskilde

#tilfældigt libarie 
import random 
#import PyQt5 som bliver brugt til QT
from PyQt5 import QtCore, QtGui, QtWidgets


#class for the UI
class Ui_Form(object):
    #Dansk spillet 
    def loop(self,dificulty):
        #filen med teksten der bliver taget fra 
        f = open("konvertering/tekst.txt", "r")
        #vokaler
        vokaler = ["a","e","i","o","u","y"]
        #stopper hvis et hvis antal vokaler er nået
        stop = False
        #renser listen
        tekst=[]
        #her splitter jeg ordene og gør dem alle lowercase 
        for i in f:
            i = i.lower()
            tekst += i.split()
        #starter while løkken 
        while stop == False:
            n = 0
            #vælger tilfældigt ord
            chosen = tekst[int(random.uniform(0,len(tekst)))]
            #renser chosen_p
            chosen_p=""
            
            #looper igenem oredets bogstaver
            for i in chosen:
                #hvis det er en vokal indsættes "_" og tæller n op 
                if i in vokaler:
                    chosen_p+="_"
                    n += 1
                else:
                    chosen_p += i
            #hvis antallet af vokaler er nået stopper loopet 
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
        #knap 2 til at give op
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.giv_op)
        
        #knap til sværhedsgrad nem
        self.pushButton_dif = QtWidgets.QPushButton(Form)
        self.pushButton_dif.setGeometry(QtCore.QRect(0, 0, 90, 20))
        self.pushButton_dif.setObjectName("pushButton_2")
        self.pushButton_dif.clicked.connect(self.nem)
 
        #knap til sværhedsgrad mellem        
        self.pushButton_dif_2 = QtWidgets.QPushButton(Form)
        self.pushButton_dif_2.setGeometry(QtCore.QRect(90, 0, 90, 20))
        self.pushButton_dif_2.setObjectName("pushButton_2")
        self.pushButton_dif_2.clicked.connect(self.normal)
        
        #knap til sværhedsgrad svær
        self.pushButton_dif_3 = QtWidgets.QPushButton(Form)
        self.pushButton_dif_3.setGeometry(QtCore.QRect(180, 0, 90, 20))
        self.pushButton_dif_3.setObjectName("pushButton_2")
        self.pushButton_dif_3.clicked.connect(self.sver)
        
         #knap 2 til at tjek svaret "ok"
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
        
        #tekstfelt 
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.ok)
        self.verticalLayout_2.addWidget(self.lineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #hvis svaret er rigtig så går den videre 
    def ok(self):
        if self.lineEdit.text() == self.right:
            self.text,self.right = self.loop(self.dificulty)
            self.label.setText(self.text)
            self.lineEdit.setText("")
     
    #giver op og går videre         
    def giv_op(self):
        self.text,self.right = self.loop(self.dificulty)
        self.label.setText(self.text)
        self.lineEdit.setText("")
    
    #sættersværhedsgraden til nem 1 vokal     
    def nem(self):
        self.dificulty = 1
    
    #sættersværhedsgraden til mellem 2 vokal      
    def normal(self):
        self.dificulty = 2
   
   #sættersværhedsgraden til svær 3 vokal          
    def sver(self):
        self.dificulty = 3
        
    #sætter navne på knapper og label
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "giv op"))
        self.pushButton.setText(_translate("Form", "svar"))
        self.label.setText(_translate("Form", self.text))
        self.pushButton_dif.setText(_translate("Form", "nem"))
        self.pushButton_dif_2.setText(_translate("Form", "mellem"))
        self.pushButton_dif_3.setText(_translate("Form", "svær"))

#starter programmet hvis det er main filen
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
