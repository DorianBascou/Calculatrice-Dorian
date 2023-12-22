from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

#Génération des boutons et de la fenêtre
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.boutonUn = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("1"))
        self.boutonUn.setGeometry(QtCore.QRect(230, 360, 93, 28))
        self.boutonUn.setObjectName("boutonUn")
        
        self.boutonDeux = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("2"))
        self.boutonDeux.setGeometry(QtCore.QRect(330, 360, 93, 28))
        self.boutonDeux.setObjectName("boutonDeux")
        
        self.boutonTrois = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("3"))
        self.boutonTrois.setGeometry(QtCore.QRect(430, 360, 93, 28))
        self.boutonTrois.setProperty("3", "")
        self.boutonTrois.setObjectName("boutonTrois")
        
        self.boutonQuatre = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("4"))
        self.boutonQuatre.setGeometry(QtCore.QRect(230, 330, 93, 28))
        self.boutonQuatre.setObjectName("boutonQuatre")
        
        self.boutonCinq = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("5"))
        self.boutonCinq.setGeometry(QtCore.QRect(330, 330, 93, 28))
        self.boutonCinq.setObjectName("boutonCinq")
        
        self.boutonSix = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("6"))
        self.boutonSix.setGeometry(QtCore.QRect(430, 330, 93, 28))
        self.boutonSix.setObjectName("boutonSix")
        
        self.boutonSept = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("7"))
        self.boutonSept.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.boutonSept.setObjectName("boutonSept")
        
        self.boutonHuit = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("8"))
        self.boutonHuit.setGeometry(QtCore.QRect(330, 300, 93, 28))
        self.boutonHuit.setObjectName("boutonHuit")
        
        self.boutonNeuf = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("9"))
        self.boutonNeuf.setGeometry(QtCore.QRect(430, 300, 93, 28))
        self.boutonNeuf.setObjectName("boutonNeuf")
        
        self.boutonZero = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("0"))
        self.boutonZero.setGeometry(QtCore.QRect(230, 390, 93, 28))
        self.boutonZero.setObjectName("boutonZero")
        
        self.boutonResultat = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("="))
        self.boutonResultat.setGeometry(QtCore.QRect(430, 390, 93, 28))
        self.boutonResultat.setObjectName("boutonResultat")
        
        self.boutonC = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("C"))
        self.boutonC.setGeometry(QtCore.QRect(330, 390, 93, 28))
        self.boutonC.setObjectName("boutonC")
        
        self.boutonPlus = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("+"))
        self.boutonPlus.setGeometry(QtCore.QRect(230, 270, 93, 28))
        self.boutonPlus.setObjectName("boutonPlus")
        
        self.boutonMoins = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("-"))
        self.boutonMoins.setGeometry(QtCore.QRect(330, 270, 93, 28))
        self.boutonMoins.setObjectName("boutonMoins")
        
        self.boutonFois = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("*"))
        self.boutonFois.setGeometry(QtCore.QRect(430, 270, 93, 28))
        self.boutonFois.setObjectName("boutonFois")
        
        self.boutonExposant = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("**"))
        self.boutonExposant.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.boutonExposant.setObjectName("boutonExposant")
        
        self.boutonDiviser = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("/"))
        self.boutonDiviser.setGeometry(QtCore.QRect(330, 240, 93, 28))
        self.boutonDiviser.setObjectName("boutonDiviser")
        
        self.boutonRacine = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("sqrt("))
        self.boutonRacine.setGeometry(QtCore.QRect(430, 240, 93, 28))
        self.boutonRacine.setObjectName("boutonRacine")
        
        self.outputLabel = QtWidgets.QLabel(Dialog)
        self.outputLabel.setGeometry(QtCore.QRect(130, 180, 491, 41))
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setObjectName("outputLabel")
        
        self.boutonTan = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("tan("))
        self.boutonTan.setGeometry(QtCore.QRect(130, 300, 93, 28))
        self.boutonTan.setObjectName("boutonTan")
        
        self.boutonSin = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("sin("))
        self.boutonSin.setGeometry(QtCore.QRect(130, 240, 93, 28))
        self.boutonSin.setObjectName("boutonSin")
        
        self.boutonCos = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("cos("))
        self.boutonCos.setGeometry(QtCore.QRect(130, 270, 93, 28))
        self.boutonCos.setObjectName("boutonCos")
        
        self.boutonLog = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("log("))
        self.boutonLog.setGeometry(QtCore.QRect(130, 330, 93, 28))
        self.boutonLog.setObjectName("boutonLog")
        
        self.boutonParantheseFerme = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre(")"))
        self.boutonParantheseFerme.setGeometry(QtCore.QRect(530, 360, 93, 28))
        self.boutonParantheseFerme.setProperty("3", "")
        self.boutonParantheseFerme.setObjectName("boutonParantheseFerme")
        
        self.boutonRetour = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("suppr"))
        self.boutonRetour.setGeometry(QtCore.QRect(530, 240, 93, 28))
        self.boutonRetour.setObjectName("boutonRetour")
        
        self.boutonVirgule = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("."))
        self.boutonVirgule.setGeometry(QtCore.QRect(530, 390, 93, 28))
        self.boutonVirgule.setObjectName("boutonVirgule")
        
        self.boutonParantheseOuvre = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("("))
        self.boutonParantheseOuvre.setGeometry(QtCore.QRect(530, 330, 93, 28))
        self.boutonParantheseOuvre.setObjectName("boutonParantheseOuvre")
        
        self.boutonPourcent = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("/100"))
        self.boutonPourcent.setGeometry(QtCore.QRect(530, 270, 93, 28))
        self.boutonPourcent.setObjectName("boutonPourcent")
        
        self.boutonPi = QtWidgets.QPushButton(Dialog, clicked= lambda: self.entre("pi"))
        self.boutonPi.setGeometry(QtCore.QRect(530, 300, 93, 28))
        self.boutonPi.setObjectName("boutonPi")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #Ce qui se passe lorsque l'on appui sur un bouton,
    #soit on rénitialise avec C,
    #soit on calcule avec =(en testant les erreurs),
    #soit on supprime le dernier caractère
    #ou bien on écrit
    def entre(self,entre):
        if entre == "C":
            self.outputLabel.setText("0")
        elif entre == "=":
            try:
                resultat=self.outputLabel.text()
                reponse = eval(resultat)
                self.outputLabel.setText(str(reponse))
            except:
                self.outputLabel.setText("Erreur Syntaxe Veuillez appuyer sur C")
        elif entre == "suppr":
            grabbed=self.outputLabel.text()
            grabbed = grabbed[:-1]
            self.outputLabel.setText(grabbed)
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText(entre)
            else:
                self.outputLabel.setText(f' {self.outputLabel.text()}{entre}')

           
    #Affichage de la fenêtre et des boutons avec leur noms d'affichage
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.boutonUn.setText(_translate("Dialog", "1"))
        self.boutonDeux.setText(_translate("Dialog", "2"))
        self.boutonTrois.setText(_translate("Dialog", "3"))
        self.boutonQuatre.setText(_translate("Dialog", "4"))
        self.boutonCinq.setText(_translate("Dialog", "5"))
        self.boutonSix.setText(_translate("Dialog", "6"))
        self.boutonSept.setText(_translate("Dialog", "7"))
        self.boutonHuit.setText(_translate("Dialog", "8"))
        self.boutonNeuf.setText(_translate("Dialog", "9"))
        self.boutonZero.setText(_translate("Dialog", "0"))
        self.boutonResultat.setText(_translate("Dialog", "="))
        self.boutonC.setText(_translate("Dialog", "C"))
        self.boutonPlus.setText(_translate("Dialog", "+"))
        self.boutonMoins.setText(_translate("Dialog", "-"))
        self.boutonFois.setText(_translate("Dialog", "x"))
        self.boutonExposant.setText(_translate("Dialog", "^"))
        self.boutonDiviser.setText(_translate("Dialog", "/"))
        self.boutonRacine.setText(_translate("Dialog", "√"))
        self.outputLabel.setText(_translate("Dialog", "0"))
        self.boutonTan.setText(_translate("Dialog", "tan"))
        self.boutonSin.setText(_translate("Dialog", "sin"))
        self.boutonCos.setText(_translate("Dialog", "cos"))
        self.boutonLog.setText(_translate("Dialog", "log"))
        self.boutonParantheseFerme.setText(_translate("Dialog", ")"))
        self.boutonRetour.setText(_translate("Dialog", "Retour"))
        self.boutonVirgule.setText(_translate("Dialog", "."))
        self.boutonParantheseOuvre.setText(_translate("Dialog", "("))
        self.boutonPourcent.setText(_translate("Dialog", "%"))
        self.boutonPi.setText(_translate("Dialog", "π"))

#Execution de l'application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
