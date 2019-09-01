# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Department.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_Dialog(object):
    connection = sqlite3.connect('NewEmployee.db')
    c = connection.cursor()
    def modify(self):
        try:
            row = self.listWidget_DepartView.currentRow()
            #item = self.listWidget_DepartView.takeItem(row)
            iten = self.listWidget_DepartView.setCurrentItem(row)
            print(iten)
            self.lineEdit_AddDepart.setText(str(iten))
            self.listWidget_DepartView.insertItem(row,self.lineEdit_AddDepart.text())
            #self.c.execute("SELECT Department FROM Department")
        except Exception as err:
            print(err)

    def add_depart(self):
        try:

            item = self.lineEdit_AddDepart.text()
            sql = "INSERT INTO Department VALUES('{item}')".format(item = item)
            self.c.execute(sql)
            self.listWidget_DepartView.addItem(item)
            self.listWidget_DepartView.sortItems()
            self.connection.commit()
            self.connection.close()
        except Exception as err:
            print(err)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 304)
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
" }\n"
" QListView {\n"
"     selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                 stop: 0 #FF92BB, stop: 1 white);\n"
"border:10px;\n"
"border-radius: 10px;\n"
" }")
        self.groupBox_Depart = QtWidgets.QGroupBox(Dialog)
        self.groupBox_Depart.setGeometry(QtCore.QRect(0, 0, 541, 301))
        self.groupBox_Depart.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
" padding: 5px 5px 5px 20px;\n"
"font: 75 10pt \"MS Sans Serif\";\n"
"background-color: rgb(22, 200, 94);\n"
"border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border: 3px solid blue;\n"
"    color: white;\n"
"}")
        self.groupBox_Depart.setObjectName("groupBox_Depart")
        self.PushBotton_Add_Depart = QtWidgets.QPushButton(self.groupBox_Depart)
        self.PushBotton_Add_Depart.setGeometry(QtCore.QRect(220, 240, 71, 41))
        self.PushBotton_Add_Depart.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 255, 0);")
        self.PushBotton_Add_Depart.setObjectName("PushBotton_Add_Depart")
        self.PushButton_ModifyDepart = QtWidgets.QPushButton(self.groupBox_Depart)
        self.PushButton_ModifyDepart.setGeometry(QtCore.QRect(300, 240, 71, 41))
        self.PushButton_ModifyDepart.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.PushButton_ModifyDepart.setObjectName("PushButton_ModifyDepart")
        self.PushBotton_CancelDepart = QtWidgets.QPushButton(self.groupBox_Depart)
        self.PushBotton_CancelDepart.setGeometry(QtCore.QRect(380, 240, 71, 41))
        self.PushBotton_CancelDepart.setStyleSheet("color: rgb(255, 255, 255);\n"
";\n"
"background-color: rgb(255, 85, 0);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.PushBotton_CancelDepart.setObjectName("PushBotton_CancelDepart")
        self.PushBotton_close = QtWidgets.QPushButton(self.groupBox_Depart)
        self.PushBotton_close.setGeometry(QtCore.QRect(460, 240, 71, 41))
        self.PushBotton_close.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.PushBotton_close.setObjectName("PushBotton_close")
        self.lineEdit_AddDepart = QtWidgets.QLineEdit(self.groupBox_Depart)
        self.lineEdit_AddDepart.setGeometry(QtCore.QRect(230, 10, 301, 31))
        self.lineEdit_AddDepart.setObjectName("lineEdit_AddDepart")
        self.listWidget_DepartView = QtWidgets.QListWidget(self.groupBox_Depart)
        self.listWidget_DepartView.setGeometry(QtCore.QRect(0, 20, 201, 281))
        self.listWidget_DepartView.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-size:(10px)")
        self.listWidget_DepartView.setObjectName("listWidget_DepartView")
        connection = sqlite3.connect('NewEmployee.db')
        c = connection.cursor()
        c.execute('SELECT Department FROM Department')
        for row in c.fetchall():
            item = QtWidgets.QListWidgetItem()
            self.listWidget_DepartView.addItem(item)
            #item = QtWidgets.QListWidgetItem()
            #self.listWidget_DepartView.addItem(item)
        self.PushBotton_Add_Depart.clicked.connect(self.add_depart)
        self.PushButton_ModifyDepart.clicked.connect(self.modify)
        self.PushBotton_close.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_Depart.setTitle(_translate("Dialog", "Department"))
        self.PushBotton_Add_Depart.setText(_translate("Dialog", "Add"))
        self.PushButton_ModifyDepart.setText(_translate("Dialog", "Modify"))
        self.PushBotton_CancelDepart.setText(_translate("Dialog", "Cancel"))
        self.PushBotton_close.setText(_translate("Dialog", "Close"))
        __sortingEnabled = self.listWidget_DepartView.isSortingEnabled()
        self.listWidget_DepartView.setSortingEnabled(False)
        connection = sqlite3.connect('NewEmployee.db')
        c = connection.cursor()
        c.execute('SELECT Department FROM Department')
        count = 0
        for row in c.fetchall():
            item = self.listWidget_DepartView.item(count)
            raw = str(row).replace("('", "").replace("',)", "")
            item.setText(_translate("Dialog", raw))
            count = count + 1
            self.listWidget_DepartView.setSortingEnabled(__sortingEnabled)
        self.listWidget_DepartView.sortItems()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

