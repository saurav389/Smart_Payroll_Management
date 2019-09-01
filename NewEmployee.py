# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogNewEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MessageBox import Ui_Dialog
import sqlite3
import csv
import os
from colorama import Fore,Back,Style

class Ui_DialogNewEmployee(object):
    Fieldname = ['WkNo', 'Name', 'Father', 'Gender', 'Dob', 'Mstatus', 'Address', 'Mno', 'UanNo', 'PfNo', 'EsiNo',
                 'Site','Department','Designation','Catagory','PF_Allowance','ESI_Allowance','ESI_Location','Attendence_Award']
    get_file_path = os.path.join(os.path.dirname(__file__), "EmployeDetails.csv")
    Filename = get_file_path
    get_file_pat = os.path.join(os.path.dirname(__file__), "NewEmployee.db")
    database = get_file_pat
    def clearform(self):
        try:
            self.lineEdit_name.setText("")
            self.lineEdit_FatherName.setText("")
            self.comboBox_Gender.setCurrentText("")
            self.dateEdit_Dob.setDateTime(QtCore.QDateTime.currentDateTime())
            self.comboBox_Mstatus.setCurrentText("")
            self.lineEdit_Address.setText("")
            self.lineEdit_MobileNo.setText("")
            self.lineEdit_UanNo.setText("")
            self.lineEdit_PfNo.setText("")
            self.lineEdit_EsiNo.setText("")
            self.comboBox_site.setCurrentText("")
            self.comboBox_Depart.setCurrentText("")
            self.comboBox_Desig.setCurrentText("")
            self.comboBox_Categ.setCurrentText("")
            self.comboBox_PFAllow.setCurrentText("")
            self.comboBox_ESIAllow.setCurrentText("")
            self.comboBox_EsiLocation.setCurrentText("")
            self.comboBox_AttnAwar_2.setCurrentText("")
        except Exception as err:
            mesg = "{err}".format(err = err)
            DialogNewEmployee.show()
            self.NewEmployeeWindow = QtWidgets.QDialog()
            # self.NewEmployeeWindow = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog(mesg)
            self.ui.setupUi(self.NewEmployeeWindow)
            self.NewEmployeeWindow.show()
    def getdb_length(self):
        connection = sqlite3.connect('NewEmployee.db')
        c = connection.cursor()
        c.execute('SELECT * FROM NewEmployees')
        count = 1
        for raw in c.fetchall():
            count = count + 1
        return count
    def Insert_to_Database(self):
        if not os.path.isfile(self.database):
            # create Database NewEmployee
            print(0)
            connection = sqlite3.connect('NewEmployee.db')
            c = connection.cursor()
            '''Fieldname = ['WkNo', 'Name', 'Father', 'Gender', 'Dob', 'Mstatus', 'Address', 'Mno', 'UanNo', 'PfNo', 'EsiNo',
                     'Site', 'Department', 'Designation', 'Catagory', 'PF_Allowance', 'ESI_Allowance', 'ESI_Location',
                     'Attendence_Award']'''
            c.execute("CREATE TABLE NewEmployees (WkNo text, Name text, Father text, Gender text, Dob text, Mstatus text,Address text, Mno real, UanNo real, PfNo real, EsiNo real, Site text, Department text, Designation text,Catagory text, PF_Allowance text, ESI_Allowance text, ESI_Location text, Attendance_Award text)")
        else:
            connection = sqlite3.connect('NewEmployee.db')
            c = connection.cursor()
            # Create a Dictionary Named as employeeData
            try:
                employeeData = {
                    "wkno": self.LineEdit_WkNo.text(),
                    "name": self.lineEdit_name.text(),
                    "father": self.lineEdit_FatherName.text(),
                    "gender": self.comboBox_Gender.currentText(),
                    "dob": self.dateEdit_Dob.text(),
                    "mstatus": self.comboBox_Mstatus.currentText(),
                    "address": self.lineEdit_Address.text(),
                    "mno": self.lineEdit_MobileNo.text(),
                    "UanNO": self.lineEdit_UanNo.text(),
                    "PfNo": self.lineEdit_PfNo.text(),
                    "EsiNo": self.lineEdit_EsiNo.text(),
                    "Site": self.comboBox_site.currentText(),
                    "Department": self.comboBox_Depart.currentText(),
                    "Designation": self.comboBox_Desig.currentText(),
                    "Catagory": self.comboBox_Categ.currentText(),
                    "PF_Allowance": self.comboBox_PFAllow.currentText(),
                    "Esi_Allowance": self.comboBox_ESIAllow.currentText(),
                    "Esi_Location": self.comboBox_EsiLocation.currentText(),
                    "Attendance_Award": self.comboBox_AttnAwar_2.currentText()
                }
            except Exception as Dict_err:
                print("Please check dictionary")
                return Dict_err
            # insert into Database NewEmployee
            try:
                columns = ','.join("'" + str(x).replace('/', '_') + "'" for x in employeeData.keys())
                values = ','.join("'" + str(x).replace('/', '_') + "'" for x in employeeData.values())
                sql = "INSERT INTO %s( %s ) VALUES (%s);" % ('NewEmployees', columns, values)
                #print(sql)
                c.execute(sql)
                connection.commit()
                connection.close()
                #print("Databasse Created")
            except Exception as err:
                return err
    def Message(self):
        var = self.inputvalidator()
        if var is not None:
                mesg = "{var} Required".format(var=var)
                self.NewEmployeeWindow = QtWidgets.QDialog()
                self.ui = Ui_Dialog(mesg)
                self.ui.setupUi(self.NewEmployeeWindow)
                self.NewEmployeeWindow.show()
        else:
                Value = self.Insert_to_Database()
                if Value is None:
                    mesg = "Data Inserted Succesfully"
                    self.NewEmployeeWindow = QtWidgets.QDialog()
                    self.ui = Ui_Dialog(mesg)
                    self.ui.setupUi(self.NewEmployeeWindow)
                    self.NewEmployeeWindow.show()
                    self.clearform()
                    WKNO = self.getdb_length()
                    next = str(WKNO)
                    self.LineEdit_WkNo.setText(next)
                else:
                    msg = "error ?\n{Value}".format(Value = Value)
                    self.NewEmployeeWindow = QtWidgets.QDialog()
                    self.ui = Ui_Dialog(msg)
                    self.ui.setupUi(self.NewEmployeeWindow)
                    self.NewEmployeeWindow.show()
    def inputvalidator(self):
        name = self.lineEdit_name.text()
        nameln=len(name)
        father = self.lineEdit_FatherName.text()
        fatherln = len(father)
        gender = self.comboBox_Gender.currentText()
        genderln = len(gender)
        dob = self.dateEdit_Dob.text()
        dobln = len(dob)
        mstatus = self.comboBox_Mstatus.currentText()
        mstatusln = len(mstatus)
        address = self.lineEdit_Address.text()
        addressln = len(address)
        Mno = self.lineEdit_MobileNo.text()
        Mnoln = len(Mno)
        uan = self.lineEdit_UanNo.text()
        uanln = len(uan)
        pf = self.lineEdit_PfNo.text()
        pfln = len(pf)
        esi = self.lineEdit_EsiNo.text()
        esiln= len(esi)
        # Departmental Details
        site = self.comboBox_site.currentText()
        siteln = len(site)
        dept = self.comboBox_Depart.currentText()
        deptln = len(dept)
        desig = self.comboBox_Desig.currentText()
        designl= len(desig)
        cat = self.comboBox_Categ.currentText()
        catln = len(cat)
        pfall = self.comboBox_PFAllow.currentText()
        pfallln = len(pfall)
        esiall = self.comboBox_ESIAllow.currentText()
        esiallln = len(esiall)
        esiloc = self.comboBox_EsiLocation.currentText()
        esilocln = len(esiloc)
        attawrd = self.comboBox_AttnAwar_2.currentText()
        attawrdln = len(attawrd)
        if(nameln == 0):
                var = "Name"
                return var
        if(fatherln == 0):
                # print("Father name is required")
                var = "Father Name"
                return var
        if(genderln == 0):
                # print("Gender is required")
                var = "Gender"
                return var
        if(dobln == 0):
                # print(Date of Birth is required")
                var = "Date OF Birth"
                return var
        if(mstatusln == 0):
                # print("Marital Status is required")
                var = "Merital Status"
                return var
        if(addressln == 0):
                # print("Address is required")
                var = "Address"
                return var
        if(Mnoln == 0):
                # print("Mobile No is required")
                var = "Mobile No"
                return var
        if(uanln == 0):
                # print("UAN NO is required")
                var = "Uan No "
                return var
        if(pfln == 0):
                # print("PF NO is required")
                var = "PF No "
                return var
        if(esiln == 0):
                # print("ESI NO  is required")
                var = "Esic No"
                return var
        if (siteln == 0):
                # print("ESI NO  is required")
                var = "SITE"
                return var
        if (deptln == 0):
                # print("ESI NO  is required")
                var = "DEPARTMENT"
                return var
        if (designl == 0):
                # print("ESI NO  is required")
                var = "DESIGNATION"
                return var
        if (catln == 0):
                # print("ESI NO  is required")
                var = "CATAGORY"
                return var
        if (pfallln == 0):
                # print("ESI NO  is required")
                var = "PF ALLOWANCE"
                return var
        if (esiallln == 0):
                # print("ESI NO  is required")
                var = "ESIC ALLOWANCE"
                return var
        if (esilocln == 0):
                # print("ESI NO  is required")
                var = "ESIC LOCATION"
                return var
        if (attawrdln == 0):
                # print("ESI NO  is required")
                var = "ATTENDENCE REWARD"
                return var
        else:
                pass

    def get_length(self):
        if not os.path.isfile(self.Filename):
                print(Back.RED + "")
                print(self.Filename, "Not present")
                with open(self.Filename, "w", newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=self.Fieldname)
                        writer.writeheader()
                return 0
        else:
                with open(self.Filename, "r") as csvfile:
                        reader = csv.reader(csvfile)
                        reader_list = list(reader)
                        return len(reader_list)
    def get_empdetails(self):
        # personal Details
        wkno = self.get_length()
        Next = str(wkno)
        #self.LineEdit_WkNo.setText(Next)
        name = self.lineEdit_name.text()

        father = self.lineEdit_FatherName.text()
        gender = self.comboBox_Gender.currentText()
        dob = self.dateEdit_Dob.text()
        mstatus = self.comboBox_Mstatus.currentText()
        address = self.lineEdit_Address.text()
        Mno = self.lineEdit_MobileNo.text()
        uan = self.lineEdit_UanNo.text()
        pf = self.lineEdit_PfNo.text()
        esi = self.lineEdit_EsiNo.text()
        # Departmental Details
        site = self.comboBox_site.currentText()
        dept = self.comboBox_Depart.currentText()
        desig = self.comboBox_Desig.currentText()
        categ = self.comboBox_Categ.currentText()
        PF_Allow = self.comboBox_PFAllow.currentText()
        ESI_Allow = self.comboBox_ESIAllow.currentText()
        ESI_Locat = self.comboBox_EsiLocation.currentText()
        attawrd = self.comboBox_AttnAwar_2.currentText()
        employeeData = {
                "wkno":wkno,
                "name":name,
                "father":father,
                "gender":gender,
                "dob":dob,
                "mstatus":mstatus,
                "address":address,
                "mno":Mno,
                "uan":uan,
                "pf":pf,
                "esi":esi,
                "site":site,
                "dept":dept,
                "desig":desig,
                "categ":categ,
                "pfallw":PF_Allow,
                "esiallw":ESI_Allow,
                "esiloc":ESI_Locat,
                "attawrd":attawrd
        }
        #print(self.Fieldname)
        #print(employeeData)

        return employeeData
    def Insert_emp(self):
            empdata = self.get_empdetails()
            print(1)
            print(empdata['wkno'])
            print(Fore.LIGHTMAGENTA_EX + "")
            if not os.path.isfile(self.Filename):
                    message = "Error {Filename} not present".format(Filename=self.Filename)
                    print(Fore.RED + message.center(30, '_'))
            if empdata['wkno'] > 0:
                    with open(self.Filename, "a", newline='') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=self.Fieldname)
                            print("data")
                            writer.writerow({
                                    "WkNo": empdata['wkno'],
                                    "Name": empdata['name'],
                                    "Father": empdata['father'],
                                    "Gender": empdata['gender'],
                                    "Dob": empdata['dob'],
                                    "Mstatus": empdata['mstatus'],
                                    "Address": empdata['address'],
                                    "Mno": empdata['mno'],
                                    "UanNo": empdata['uan'],
                                    "PfNo": empdata['pf'],
                                    "EsiNo": empdata['esi'],
                                    "Site":empdata['site'],
                                    "Department":empdata['dept'],
                                    "Designation":empdata['desig'],
                                    "Catagory":empdata['categ'],
                                    "PF_Allowance":empdata['pfallw'],
                                    "ESI_Allowance":empdata['esiallw'],
                                    "ESI_Location":empdata['esiloc'],
                                    "Attendence_Award":empdata['attawrd']
                            })
                    print("data inserted")
            else:
                    with open(self.Filename, "w", newline='') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=self.Fieldname)
                            writer.writeheader()
                            writer.writerow({
                                    "WkNo": empdata['wkno'],
                                    "Name": empdata['name'],
                                    "Father": empdata['father'],
                                    "Gender": empdata['gender'],
                                    "Dob": empdata['dob'],
                                    "Mstatus": empdata['mstatus'],
                                    "Address": empdata['address'],
                                    "Mno": empdata['mno'],
                                    "UanNo": empdata['uan'],
                                    "PfNo": empdata['pf'],
                                    "EsiNo": empdata['esi'],
                                    "Site":empdata['site'],
                                    "Department": empdata['dept'],
                                    "Designation": empdata['desig'],
                                    "Category": empdata['categ'],
                                    "PF_Allowance": empdata['pfallw'],
                                    "ESI_Allowance": empdata['esiallw'],
                                    "ESI_Location": empdata['esiloc'],
                                    "Attendence_Award": empdata['attawrd']
                            })
                    print("\n\t Data Inserted")
    def setupUi(self, DialogNewEmployee):
        DialogNewEmployee.setObjectName("DialogNewEmployee")
        DialogNewEmployee.resize(810, 553)
        DialogNewEmployee.setStyleSheet("QPushButton\n"
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
        self.groupBox_newemp = QtWidgets.QGroupBox(DialogNewEmployee)
        self.groupBox_newemp.setGeometry(QtCore.QRect(10, 10, 786, 529))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_newemp.setFont(font)
        self.groupBox_newemp.setStyleSheet("QDateEdit{\n"
" padding: 5px 5px 5px 20px;\n"
"font: 75 10pt \"MS Sans Serif\";\n"
"background-color: rgb(22, 200, 94);\n"
"border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"color: white;\n"
"}\n"
"QDateEdit:hover{\n"
" border: 3px solid blue;\n"
" color: white;\n"
"}\n"
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
"}\n"
"\n"
"QComboBox\n"
"{\n"
"font: 75 10pt \"MS Sans Serif\";\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: Blue;\n"
"    selection-color: yellow;\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 5px 5px 5px 20px;    \n"
"    background-color: rgb(22, 200, 94);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    border: 3px solid blue;\n"
"    color: white;\n"
"    padding:5px;\n"
"}\n"
"QComboBox::drop-down{\n"
"    border:none;\n"
"    background-color: rgb(255, 90, 14);\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"    padding:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.groupBox_newemp.setObjectName("groupBox_newemp")
        self.frame = QtWidgets.QFrame(self.groupBox_newemp)
        self.frame.setGeometry(QtCore.QRect(10, 120, 301, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Merital = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Merital.setFont(font)
        self.label_Merital.setObjectName("label_Merital")
        self.gridLayout.addWidget(self.label_Merital, 5, 0, 1, 1)
        self.dateEdit_Dob = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_Dob.setObjectName("dateEdit_Dob")
        self.gridLayout.addWidget(self.dateEdit_Dob, 4, 1, 1, 1)
        self.lineEdit_EsiNo = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_EsiNo.setClearButtonEnabled(True)
        self.lineEdit_EsiNo.setObjectName("lineEdit_EsiNo")
        self.gridLayout.addWidget(self.lineEdit_EsiNo, 10, 1, 1, 1)
        self.label_EsiNo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_EsiNo.setFont(font)
        self.label_EsiNo.setObjectName("label_EsiNo")
        self.gridLayout.addWidget(self.label_EsiNo, 10, 0, 1, 1)
        self.lineEdit_PfNo = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_PfNo.setClearButtonEnabled(True)
        self.lineEdit_PfNo.setObjectName("lineEdit_PfNo")
        self.gridLayout.addWidget(self.lineEdit_PfNo, 9, 1, 1, 1)
        self.label_PfNo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_PfNo.setFont(font)
        self.label_PfNo.setObjectName("label_PfNo")
        self.gridLayout.addWidget(self.label_PfNo, 9, 0, 1, 1)
        self.lineEdit_UanNo = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_UanNo.setClearButtonEnabled(True)
        self.lineEdit_UanNo.setObjectName("lineEdit_UanNo")
        self.gridLayout.addWidget(self.lineEdit_UanNo, 8, 1, 1, 1)
        self.label_UanNo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_UanNo.setFont(font)
        self.label_UanNo.setObjectName("label_UanNo")
        self.gridLayout.addWidget(self.label_UanNo, 8, 0, 1, 1)
        self.lineEdit_MobileNo = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_MobileNo.setClearButtonEnabled(True)
        self.lineEdit_MobileNo.setObjectName("lineEdit_MobileNo")
        self.gridLayout.addWidget(self.lineEdit_MobileNo, 7, 1, 1, 1)
        self.label_MobileNo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_MobileNo.setFont(font)
        self.label_MobileNo.setObjectName("label_MobileNo")
        self.gridLayout.addWidget(self.label_MobileNo, 7, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.label_Gender = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Gender.setFont(font)
        self.label_Gender.setObjectName("label_Gender")
        self.gridLayout.addWidget(self.label_Gender, 2, 0, 1, 1)
        self.lineEdit_FatherName = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_FatherName.setClearButtonEnabled(True)
        self.lineEdit_FatherName.setObjectName("lineEdit_FatherName")
        self.gridLayout.addWidget(self.lineEdit_FatherName, 1, 1, 1, 1)
        self.label_FatherName = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_FatherName.setFont(font)
        self.label_FatherName.setObjectName("label_FatherName")
        self.gridLayout.addWidget(self.label_FatherName, 1, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_name.setClearButtonEnabled(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.lineEdit_Address = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Address.setClearButtonEnabled(True)
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.gridLayout.addWidget(self.lineEdit_Address, 6, 1, 1, 1)
        self.label_Addres = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Addres.setFont(font)
        self.label_Addres.setObjectName("label_Addres")
        self.gridLayout.addWidget(self.label_Addres, 6, 0, 1, 1)
        self.comboBox_Mstatus = QtWidgets.QComboBox(self.frame)
        self.comboBox_Mstatus.setEditable(True)
        self.comboBox_Mstatus.setObjectName("comboBox_Gender_2")
        self.comboBox_Mstatus.addItem("")
        self.comboBox_Mstatus.addItem("")
        self.comboBox_Mstatus.addItem("")
        self.gridLayout.addWidget(self.comboBox_Mstatus, 5, 1, 1, 1)
        self.comboBox_Gender = QtWidgets.QComboBox(self.frame)
        self.comboBox_Gender.setEditable(True)
        self.comboBox_Gender.setObjectName("comboBox_Gender")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.gridLayout.addWidget(self.comboBox_Gender, 2, 1, 1, 1)
        self.label_Dob = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Dob.setFont(font)
        self.label_Dob.setObjectName("label_Dob")
        self.gridLayout.addWidget(self.label_Dob, 4, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_newemp)
        self.frame_2.setGeometry(QtCore.QRect(450, 130, 321, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_AttndAwrd_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_AttndAwrd_2.setFont(font)
        self.label_AttndAwrd_2.setObjectName("label_AttndAwrd_2")
        self.gridLayout_2.addWidget(self.label_AttndAwrd_2, 7, 0, 1, 1)
        self.comboBox_Categ = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_Categ.setEditable(True)
        self.comboBox_Categ.setObjectName("comboBox_Categ")
        self.comboBox_Categ.addItem("")
        self.comboBox_Categ.addItem("")
        self.comboBox_Categ.addItem("")
        self.comboBox_Categ.addItem("")
        self.comboBox_Categ.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Categ, 3, 1, 1, 1)
        self.comboBox_ESIAllow = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_ESIAllow.setEditable(True)
        self.comboBox_ESIAllow.setObjectName("comboBox_ESIAllow")
        self.comboBox_ESIAllow.addItem("")
        self.comboBox_ESIAllow.addItem("")
        self.comboBox_ESIAllow.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_ESIAllow, 5, 1, 1, 1)
        self.label_PfAllow = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_PfAllow.setFont(font)
        self.label_PfAllow.setObjectName("label_PfAllow")
        self.gridLayout_2.addWidget(self.label_PfAllow, 4, 0, 1, 1)
        self.comboBox_Desig = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_Desig.setEditable(True)
        self.comboBox_Desig.setObjectName("comboBox_Desig")
        self.comboBox_Desig.addItem("")
        self.comboBox_Desig.addItem("")
        self.comboBox_Desig.addItem("")
        self.comboBox_Desig.addItem("")
        self.comboBox_Desig.addItem("")
        self.comboBox_Desig.addItem("")
        self.comboBox_Desig.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Desig, 2, 1, 1, 1)
        self.label_Catagory = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Catagory.setFont(font)
        self.label_Catagory.setObjectName("label_Catagory")
        self.gridLayout_2.addWidget(self.label_Catagory, 3, 0, 1, 1)
        self.label_EsiAllow = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_EsiAllow.setFont(font)
        self.label_EsiAllow.setObjectName("label_EsiAllow")
        self.gridLayout_2.addWidget(self.label_EsiAllow, 5, 0, 1, 1)
        self.comboBox_PFAllow = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_PFAllow.setEditable(True)
        self.comboBox_PFAllow.setObjectName("comboBox_PFAllow")
        self.comboBox_PFAllow.addItem("")
        self.comboBox_PFAllow.addItem("")
        self.comboBox_PFAllow.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_PFAllow, 4, 1, 1, 1)
        self.label_EsiLocation = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_EsiLocation.setFont(font)
        self.label_EsiLocation.setObjectName("label_EsiLocation")
        self.gridLayout_2.addWidget(self.label_EsiLocation, 6, 0, 1, 1)
        self.comboBox_EsiLocation = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_EsiLocation.setEditable(True)
        self.comboBox_EsiLocation.setObjectName("comboBox_EsiLocation")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.comboBox_EsiLocation.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_EsiLocation, 6, 1, 1, 1)
        self.comboBox_Depart = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_Depart.setEditable(True)
        self.comboBox_Depart.setObjectName("comboBox_Depart")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.comboBox_Depart.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Depart, 1, 1, 1, 1)
        self.label_Designation = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Designation.setFont(font)
        self.label_Designation.setObjectName("label_Designation")
        self.gridLayout_2.addWidget(self.label_Designation, 2, 0, 1, 1)
        self.label_Depart = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Depart.setFont(font)
        self.label_Depart.setObjectName("label_Depart")
        self.gridLayout_2.addWidget(self.label_Depart, 1, 0, 1, 1)
        self.comboBox_site = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_site.setAutoFillBackground(False)
        self.comboBox_site.setStyleSheet("QComboBox:item {\n"
"    border-image: url(:/Resources/Images/Panel2_Normal.png);\n"
"    border-top: 4;\n"
"    border-left: 4;\n"
"    border-bottom: 4;\n"
"    border-right: 4;\n"
"    \n"
"    background-color: #C87020;\n"
"    \n"
"    font: url(:/Resources/Fonts/GameJam.ttf);\n"
"    color: #C87020;\n"
"}\n"
"\n"
"\n"
"QComboBox:item:selected {\n"
"    border-image: url(:/Resources/Images/Panel1_Normal.png);\n"
"    border-top: 4;\n"
"    border-left: 4;\n"
"    border-bottom: 4;\n"
"    border-right: 4;\n"
"    \n"
"    background-color: #C87020;\n"
"    \n"
"    font: url(:/Resources/Fonts/GameJam.ttf);\n"
"    color: #C87020;\n"
"}\n"
"\n"
"QComboBox:item::hover {\n"
"    border-image: url(:/Resources/Images/Panel2_Normal.png);\n"
"    border-top: 4;\n"
"    border-left: 4;\n"
"    border-bottom: 4;\n"
"    border-right: 4;\n"
"    \n"
"    background-color: #C87020;\n"
"    \n"
"    font: url(:/Resources/Fonts/GameJam.ttf);\n"
"    color: #C87020;\n"
"}\n"
"")
        self.comboBox_site.setEditable(True)
        self.comboBox_site.setObjectName("comboBox_site")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.comboBox_site.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_site, 0, 1, 1, 1)
        self.label_Site = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Site.setFont(font)
        self.label_Site.setObjectName("label_Site")
        self.gridLayout_2.addWidget(self.label_Site, 0, 0, 1, 1)
        self.comboBox_AttnAwar_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_AttnAwar_2.setEditable(True)
        self.comboBox_AttnAwar_2.setObjectName("comboBox_AttnAwar_2")
        self.comboBox_AttnAwar_2.addItem("")
        self.comboBox_AttnAwar_2.addItem("")
        self.comboBox_AttnAwar_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_AttnAwar_2, 7, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_newemp)
        self.line.setGeometry(QtCore.QRect(380, 130, 16, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_newemp)
        self.line_2.setGeometry(QtCore.QRect(0, 100, 786, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.PersonalDetails = QtWidgets.QLabel(self.groupBox_newemp)
        self.PersonalDetails.setGeometry(QtCore.QRect(100, 70, 151, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PersonalDetails.setFont(font)
        self.PersonalDetails.setObjectName("PersonalDetails")
        self.DepartDetails = QtWidgets.QLabel(self.groupBox_newemp)
        self.DepartDetails.setGeometry(QtCore.QRect(520, 70, 201, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.DepartDetails.setFont(font)
        self.DepartDetails.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DepartDetails.setIndent(0)
        self.DepartDetails.setObjectName("DepartDetails")
        self.LineEdit_WkNo = QtWidgets.QLineEdit(self.groupBox_newemp)
        self.LineEdit_WkNo.setGeometry(QtCore.QRect(300, 70, 184, 28))
        self.LineEdit_WkNo.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:2px solid blue;\n"
"}")
        self.LineEdit_WkNo.setInputMask("")
        wkno = self.getdb_length()
        ln = str(wkno)
        self.LineEdit_WkNo.setText(ln)
        self.LineEdit_WkNo.setClearButtonEnabled(True)
        self.LineEdit_WkNo.setObjectName("LineEdit_WkNo")
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_newemp)
        self.pushButton_Clear.setGeometry(QtCore.QRect(590, 470, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Clear.setFont(font)
        self.pushButton_Clear.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Save = QtWidgets.QPushButton(self.groupBox_newemp)
        self.pushButton_Save.setGeometry(QtCore.QRect(484, 471, 81, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Close = QtWidgets.QPushButton(self.groupBox_newemp)
        self.pushButton_Close.setGeometry(QtCore.QRect(690, 470, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_newemp)
        self.calendarWidget.setGeometry(QtCore.QRect(310, 260, 256, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton_calender = QtWidgets.QPushButton(self.groupBox_newemp)
        self.pushButton_calender.setGeometry(QtCore.QRect(268, 234, 36, 26))
        self.pushButton_calender.setObjectName("pushButton_calender")
        self.frame.raise_()
        self.frame_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.PersonalDetails.raise_()
        self.DepartDetails.raise_()
        self.LineEdit_WkNo.raise_()
        self.pushButton_Clear.raise_()
        self.pushButton_Save.raise_()
        self.pushButton_Close.raise_()
        self.calendarWidget.raise_()
        self.calendarWidget.raise_()
        self.pushButton_calender.raise_()
        #connecting all Push button or action button
        self.retranslateUi(DialogNewEmployee)
        #saving data on clicked of PushButton
        # ***************_________________________**************
        self.pushButton_Save.clicked.connect(self.Message)
        # ***************_________________________**************
        #**** Clear All Text on Click of PushButton_Clear *******
        self.pushButton_Clear.clicked.connect(self.clearform)
        #********************************************************
        self.pushButton_Close.clicked.connect(DialogNewEmployee.close)
        self.calendarWidget.clicked['QDate'].connect(self.dateEdit_Dob.setDate)
        #self.pushButton_calender.clicked.connect(self.calendarWidget.close)
        self.calendarWidget.clicked['QDate'].connect(self.calendarWidget.hide)
        self.pushButton_calender.clicked.connect(self.calendarWidget.show)
        self.groupBox_newemp.clicked.connect(self.calendarWidget.close)
        self.calendarWidget.hide()
        QtCore.QMetaObject.connectSlotsByName(DialogNewEmployee)
        DialogNewEmployee.setTabOrder(self.lineEdit_name, self.lineEdit_FatherName)
        DialogNewEmployee.setTabOrder(self.lineEdit_FatherName, self.comboBox_Gender)
        DialogNewEmployee.setTabOrder(self.comboBox_Gender, self.dateEdit_Dob)
        DialogNewEmployee.setTabOrder(self.dateEdit_Dob, self.comboBox_Mstatus)
        DialogNewEmployee.setTabOrder(self.comboBox_Mstatus, self.lineEdit_Address)
        DialogNewEmployee.setTabOrder(self.lineEdit_Address, self.lineEdit_MobileNo)
        DialogNewEmployee.setTabOrder(self.lineEdit_MobileNo, self.lineEdit_UanNo)
        DialogNewEmployee.setTabOrder(self.lineEdit_UanNo, self.lineEdit_PfNo)
        DialogNewEmployee.setTabOrder(self.lineEdit_PfNo, self.lineEdit_EsiNo)
        DialogNewEmployee.setTabOrder(self.lineEdit_EsiNo, self.comboBox_site)
        DialogNewEmployee.setTabOrder(self.comboBox_site, self.comboBox_Depart)
        DialogNewEmployee.setTabOrder(self.comboBox_Depart, self.comboBox_Desig)
        DialogNewEmployee.setTabOrder(self.comboBox_Desig, self.comboBox_Categ)
        DialogNewEmployee.setTabOrder(self.comboBox_Categ, self.comboBox_PFAllow)
        DialogNewEmployee.setTabOrder(self.comboBox_PFAllow, self.comboBox_ESIAllow)
        DialogNewEmployee.setTabOrder(self.comboBox_ESIAllow, self.comboBox_EsiLocation)
        DialogNewEmployee.setTabOrder(self.comboBox_EsiLocation, self.comboBox_AttnAwar_2)
        DialogNewEmployee.setTabOrder(self.comboBox_AttnAwar_2, self.pushButton_Save)
        DialogNewEmployee.setTabOrder(self.pushButton_Save, self.pushButton_Clear)
        DialogNewEmployee.setTabOrder(self.pushButton_Clear, self.pushButton_Close)
        DialogNewEmployee.setTabOrder(self.pushButton_Close, self.LineEdit_WkNo)
        DialogNewEmployee.setTabOrder(self.LineEdit_WkNo, self.calendarWidget)

    def retranslateUi(self, DialogNewEmployee):
        _translate = QtCore.QCoreApplication.translate
        DialogNewEmployee.setWindowTitle(_translate("DialogNewEmployee", "Dialog"))
        self.groupBox_newemp.setTitle(_translate("DialogNewEmployee", "New Emoloyee"))
        self.label_Merital.setText(_translate("DialogNewEmployee", "Merital Status"))
        self.label_EsiNo.setText(_translate("DialogNewEmployee", "ESI NO"))
        self.label_PfNo.setText(_translate("DialogNewEmployee", "PF NO"))
        self.label_UanNo.setText(_translate("DialogNewEmployee", "Uan NO"))
        self.label_MobileNo.setText(_translate("DialogNewEmployee", "Mobile No"))
        self.label_name.setText(_translate("DialogNewEmployee", "Name"))
        self.label_Gender.setText(_translate("DialogNewEmployee", "Gender"))
        self.label_FatherName.setText(_translate("DialogNewEmployee", "Father Name"))
        self.label_Addres.setText(_translate("DialogNewEmployee", "Address"))
        self.comboBox_Mstatus.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_Mstatus.setItemText(1, _translate("DialogNewEmployee", "Married"))
        self.comboBox_Mstatus.setItemText(2, _translate("DialogNewEmployee", "Un-Married"))
        self.comboBox_Gender.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_Gender.setItemText(1, _translate("DialogNewEmployee", "Male"))
        self.comboBox_Gender.setItemText(2,_translate("DialogNewEmployee","Female"))
        self.label_Dob.setText(_translate("DialogNewEmployee", "D O B"))
        self.label_AttndAwrd_2.setText(_translate("DialogNewEmployee", "Attendence Award"))
        self.comboBox_Categ.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_Categ.setItemText(1, _translate("DialogNewEmployee", "Un-Skilled"))
        self.comboBox_Categ.setItemText(2, _translate("DialogNewEmployee", "Semi-Skilled"))
        self.comboBox_Categ.setItemText(3, _translate("DialogNewEmployee", "Skilled"))
        self.comboBox_Categ.setItemText(4, _translate("DialogNewEmployee", "High-Skilled"))
        self.comboBox_ESIAllow.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_ESIAllow.setItemText(1, _translate("DialogNewEmployee", "Yes"))
        self.comboBox_ESIAllow.setItemText(2, _translate("DialogNewEmployee", "No"))
        self.label_PfAllow.setText(_translate("DialogNewEmployee", "PF Allowance"))
        self.comboBox_Desig.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_Desig.setItemText(1, _translate("DialogNewEmployee", "Helper"))
        self.comboBox_Desig.setItemText(2, _translate("DialogNewEmployee", "Operator"))
        self.comboBox_Desig.setItemText(3, _translate("DialogNewEmployee", "Supervisor"))
        self.comboBox_Desig.setItemText(4, _translate("DialogNewEmployee", "Crane-Operator"))
        self.comboBox_Desig.setItemText(5, _translate("DialogNewEmployee", "Computer-Operator"))
        self.comboBox_Desig.setItemText(6, _translate("DialogNewEmployee", "Hr"))
        self.label_Catagory.setText(_translate("DialogNewEmployee", "Catagory"))
        self.label_EsiAllow.setText(_translate("DialogNewEmployee", "ESI Allowance"))
        self.comboBox_PFAllow.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_PFAllow.setItemText(1, _translate("DialogNewEmployee", "Yes"))
        self.comboBox_PFAllow.setItemText(2, _translate("DialogNewEmployee", "No"))
        self.label_EsiLocation.setText(_translate("DialogNewEmployee", "ESI LOCATION"))
        self.comboBox_EsiLocation.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_EsiLocation.setItemText(1, _translate("DialogNewEmployee", "Aligarh"))
        self.comboBox_EsiLocation.setItemText(2, _translate("DialogNewEmployee", "Chennai"))
        self.comboBox_EsiLocation.setItemText(3, _translate("DialogNewEmployee", "Faridabad"))
        self.comboBox_EsiLocation.setItemText(4, _translate("DialogNewEmployee", "Jamshedpur"))
        self.comboBox_EsiLocation.setItemText(5, _translate("DialogNewEmployee", "Kalinganagar"))
        self.comboBox_EsiLocation.setItemText(6, _translate("DialogNewEmployee", "Pune"))
        self.comboBox_EsiLocation.setItemText(7, _translate("DialogNewEmployee", "Rudrapur"))
        self.comboBox_EsiLocation.setItemText(8, _translate("DialogNewEmployee", "Tada"))
        self.comboBox_Depart.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_Depart.setItemText(1, _translate("DialogNewEmployee", "Admin"))
        self.comboBox_Depart.setItemText(2, _translate("DialogNewEmployee", "CGL"))
        self.comboBox_Depart.setItemText(3, _translate("DialogNewEmployee", "Garden"))
        self.comboBox_Depart.setItemText(4, _translate("DialogNewEmployee", "Godawn"))
        self.comboBox_Depart.setItemText(5, _translate("DialogNewEmployee", "HR"))
        self.comboBox_Depart.setItemText(6, _translate("DialogNewEmployee", "Htk-Tech"))
        self.comboBox_Depart.setItemText(7, _translate("DialogNewEmployee", "Htk-NonTech"))
        self.label_Designation.setText(_translate("DialogNewEmployee", "Designation"))
        self.label_Depart.setText(_translate("DialogNewEmployee", "Department"))
        self.comboBox_site.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_site.setItemText(1, _translate("DialogNewEmployee", "Aligarh"))
        self.comboBox_site.setItemText(2, _translate("DialogNewEmployee", "Chennai"))
        self.comboBox_site.setItemText(3, _translate("DialogNewEmployee", "Faridabad"))
        self.comboBox_site.setItemText(4, _translate("DialogNewEmployee", "Jamshedpur"))
        self.comboBox_site.setItemText(5, _translate("DialogNewEmployee", "Kalinganagar"))
        self.comboBox_site.setItemText(6, _translate("DialogNewEmployee", "Pune"))
        self.comboBox_site.setItemText(7, _translate("DialogNewEmployee", "Rupdrapur"))
        self.comboBox_site.setItemText(8, _translate("DialogNewEmployee", "Tada"))
        self.label_Site.setText(_translate("DialogNewEmployee", "Site"))
        self.comboBox_AttnAwar_2.setItemText(0, _translate("DialogNewEmployee", ""))
        self.comboBox_AttnAwar_2.setItemText(1, _translate("DialogNewEmployee", "Yes"))
        self.comboBox_AttnAwar_2.setItemText(2, _translate("DialogNewEmployee", "No"))
        self.PersonalDetails.setText(_translate("DialogNewEmployee", "Personal Details"))
        self.DepartDetails.setText(_translate("DialogNewEmployee", "Departmental Details"))
        self.LineEdit_WkNo.setPlaceholderText(_translate("DialogNewEmployee", "Work Man NO"))
        self.pushButton_Clear.setText(_translate("DialogNewEmployee", "Clear"))
        self.pushButton_Save.setText(_translate("DialogNewEmployee", "Save"))
        self.pushButton_Close.setText(_translate("DialogNewEmployee", "Close"))
        self.pushButton_calender.setText(_translate("DialogNewEmployee", "Cal"))

#import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogNewEmployee = QtWidgets.QDialog()
    ui = Ui_DialogNewEmployee()
    ui.setupUi(DialogNewEmployee)
    DialogNewEmployee.show()
    sys.exit(app.exec_())
