# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self,mesg,parent=None):
        self.message = mesg
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 109)
        Dialog.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  border-style:outset;\n"
"  padding: 0 5px;\n"
"  background: yellow;\n"
"}\n"
" QPushButton:pressed {\n"
"     background-color: rgb(224, 0, 0);\n"
"     border-style: inset;\n"
" }")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 70, 61, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 19, 321, 61))
        self.label.setStyleSheet("font: 10pt 75pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.label.setText(_translate("Dialog",self.message))
        #self.label.setWindowIcon(QtWidgets.QSystemTrayIcon.Warning)
        self.pushButton.setText(_translate("Dialog", "Ok"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

