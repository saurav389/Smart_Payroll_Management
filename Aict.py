# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aict.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewEmployee import Ui_DialogNewEmployee
import csv
import os
from colorama import Fore,Back,Style

class Ui_MainWindow(object):
    def NewEmployee(self):
        self.NewEmployeeWindow = QtWidgets.QDialog()
        #self.NewEmployeeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_DialogNewEmployee()
        self.ui.setupUi(self.NewEmployeeWindow)
        self.NewEmployeeWindow.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 587)
        MainWindow.setStyleSheet(" QMenuBar {\n"
"background-color: rgb(19, 161, 255);\n"
"     \n"
"    font: 75 10pt \"MS Sans Serif\";\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"\n"
" QMenuBar::item {\n"
"     spacing: 15px; /* spacing between menu bar items */\n"
"     padding: 5px 10px;\n"
"     background: transparent;\n"
"     border-radius: 15px;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"     background-color: rgb(22, 143, 3);\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"    background-color: rgb(33, 122, 255);\n"
" }\n"
" QMenu {\n"
"     background-color: white;\n"
"     margin: 2px; /* some spacing around the menu */\n"
" }\n"
"\n"
" QMenu::item {\n"
"     padding: 2px 25px 2px 20px;\n"
"     border: 1px solid transparent; /* reserve space for selection border */\n"
" }\n"
"\n"
" QMenu::item:selected {\n"
"     border-color: darkblue;\n"
"     \n"
"    \n"
"    background-color: rgb(33, 122, 255);\n"
" }\n"
"\n"
" QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"     background: gray;\n"
"     border: 1px inset gray;\n"
"     position: absolute;\n"
"     top: 1px;\n"
"     right: 1px;\n"
"     bottom: 1px;\n"
"     left: 1px;\n"
" }\n"
"\n"
" QMenu::separator {\n"
"     height: 2px;\n"
"     background: lightblue;\n"
"     margin-left: 10px;\n"
"     margin-right: 5px;\n"
" }\n"
"\n"
" QMenu::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"QPushButton\n"
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
" QComboBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
"\n"
" ")
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTransanction = QtWidgets.QMenu(self.menuFile)
        self.menuTransanction.setObjectName("menuTransanction")
        self.menuNew_2 = QtWidgets.QMenu(self.menuFile)
        self.menuNew_2.setObjectName("menuNew_2")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuRegister = QtWidgets.QMenu(self.menuView)
        self.menuRegister.setObjectName("menuRegister")
        self.menuPF = QtWidgets.QMenu(self.menuView)
        self.menuPF.setObjectName("menuPF")
        self.menuEsi = QtWidgets.QMenu(self.menuView)
        self.menuEsi.setObjectName("menuEsi")
        self.menuLIN = QtWidgets.QMenu(self.menuView)
        self.menuLIN.setObjectName("menuLIN")
        self.menuDLC_Report = QtWidgets.QMenu(self.menuView)
        self.menuDLC_Report.setObjectName("menuDLC_Report")
        self.menuBonus = QtWidgets.QMenu(self.menuView)
        self.menuBonus.setObjectName("menuBonus")
        self.menuAdvance_Loans = QtWidgets.QMenu(self.menuView)
        self.menuAdvance_Loans.setObjectName("menuAdvance_Loans")
        self.menuUtility = QtWidgets.QMenu(self.menubar)
        self.menuUtility.setObjectName("menuUtility")
        self.menuChange_User = QtWidgets.QMenu(self.menuUtility)
        self.menuChange_User.setObjectName("menuChange_User")
        self.menuNew = QtWidgets.QMenu(self.menuChange_User)
        self.menuNew.setObjectName("menuNew")
        self.menuChange_Details = QtWidgets.QMenu(self.menuChange_User)
        self.menuChange_Details.setObjectName("menuChange_Details")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuEidt = QtWidgets.QMenu(self.menubar)
        self.menuEidt.setObjectName("menuEidt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWages = QtWidgets.QAction(MainWindow)
        self.actionWages.setObjectName("actionWages")
        self.actionSalary = QtWidgets.QAction(MainWindow)
        self.actionSalary.setObjectName("actionSalary")
        self.actionWages_To_Salary = QtWidgets.QAction(MainWindow)
        self.actionWages_To_Salary.setObjectName("actionWages_To_Salary")
        self.actionArear_To_Salary = QtWidgets.QAction(MainWindow)
        self.actionArear_To_Salary.setObjectName("actionArear_To_Salary")
        self.actionWages_Register_2 = QtWidgets.QAction(MainWindow)
        self.actionWages_Register_2.setObjectName("actionWages_Register_2")
        self.actionSalary_Register_2 = QtWidgets.QAction(MainWindow)
        self.actionSalary_Register_2.setObjectName("actionSalary_Register_2")
        self.actionArear_Register = QtWidgets.QAction(MainWindow)
        self.actionArear_Register.setObjectName("actionArear_Register")
        self.actionEmployee_Register = QtWidgets.QAction(MainWindow)
        self.actionEmployee_Register.setObjectName("actionEmployee_Register")
        self.actionEmployee_Ledger = QtWidgets.QAction(MainWindow)
        self.actionEmployee_Ledger.setObjectName("actionEmployee_Ledger")
        self.actionMisc_Report = QtWidgets.QAction(MainWindow)
        self.actionMisc_Report.setObjectName("actionMisc_Report")
        self.actionSettlement_Report = QtWidgets.QAction(MainWindow)
        self.actionSettlement_Report.setObjectName("actionSettlement_Report")
        self.actionEmployee_att_Register = QtWidgets.QAction(MainWindow)
        self.actionEmployee_att_Register.setObjectName("actionEmployee_att_Register")
        self.actionPF_Challan = QtWidgets.QAction(MainWindow)
        self.actionPF_Challan.setObjectName("actionPF_Challan")
        self.actionForm_12AR = QtWidgets.QAction(MainWindow)
        self.actionForm_12AR.setObjectName("actionForm_12AR")
        self.actionForm_12R = QtWidgets.QAction(MainWindow)
        self.actionForm_12R.setObjectName("actionForm_12R")
        self.actionMonthly_Report = QtWidgets.QAction(MainWindow)
        self.actionMonthly_Report.setObjectName("actionMonthly_Report")
        self.actionForm_5_10 = QtWidgets.QAction(MainWindow)
        self.actionForm_5_10.setObjectName("actionForm_5_10")
        self.actionReturn_Form_6 = QtWidgets.QAction(MainWindow)
        self.actionReturn_Form_6.setObjectName("actionReturn_Form_6")
        self.actionForm_3_AR = QtWidgets.QAction(MainWindow)
        self.actionForm_3_AR.setObjectName("actionForm_3_AR")
        self.actionForm_3AR_Data_File = QtWidgets.QAction(MainWindow)
        self.actionForm_3AR_Data_File.setObjectName("actionForm_3AR_Data_File")
        self.actionChallan = QtWidgets.QAction(MainWindow)
        self.actionChallan.setObjectName("actionChallan")
        self.actionForm_5_Return = QtWidgets.QAction(MainWindow)
        self.actionForm_5_Return.setObjectName("actionForm_5_Return")
        self.actionMonthly_Report_2 = QtWidgets.QAction(MainWindow)
        self.actionMonthly_Report_2.setObjectName("actionMonthly_Report_2")
        self.actionChallan_2 = QtWidgets.QAction(MainWindow)
        self.actionChallan_2.setObjectName("actionChallan_2")
        self.actionMonthly_Report_3 = QtWidgets.QAction(MainWindow)
        self.actionMonthly_Report_3.setObjectName("actionMonthly_Report_3")
        self.actionHalf_and_Yearly = QtWidgets.QAction(MainWindow)
        self.actionHalf_and_Yearly.setObjectName("actionHalf_and_Yearly")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionSettlement_Report_2 = QtWidgets.QAction(MainWindow)
        self.actionSettlement_Report_2.setObjectName("actionSettlement_Report_2")
        self.actionAdvance_Misc = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Misc.setObjectName("actionAdvance_Misc")
        self.actionAdvance_Register = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Register.setObjectName("actionAdvance_Register")
        self.actionAdvance_Issue = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Issue.setObjectName("actionAdvance_Issue")
        self.actionAdvance_Receipt = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Receipt.setObjectName("actionAdvance_Receipt")
        self.actionAdvance_Regist = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Regist.setObjectName("actionAdvance_Regist")
        self.actionSelect_Company = QtWidgets.QAction(MainWindow)
        self.actionSelect_Company.setObjectName("actionSelect_Company")
        self.actionUpdate_Bank_Info = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Bank_Info.setObjectName("actionUpdate_Bank_Info")
        self.actionSystem_Audit = QtWidgets.QAction(MainWindow)
        self.actionSystem_Audit.setObjectName("actionSystem_Audit")
        self.actionUpdate_PF_Cal = QtWidgets.QAction(MainWindow)
        self.actionUpdate_PF_Cal.setObjectName("actionUpdate_PF_Cal")
        self.actionUpdate_Data = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Data.setObjectName("actionUpdate_Data")
        self.actionUser = QtWidgets.QAction(MainWindow)
        self.actionUser.setObjectName("actionUser")
        self.actionManager = QtWidgets.QAction(MainWindow)
        self.actionManager.setObjectName("actionManager")
        self.actionName_2 = QtWidgets.QAction(MainWindow)
        self.actionName_2.setObjectName("actionName_2")
        self.actionPassword_2 = QtWidgets.QAction(MainWindow)
        self.actionPassword_2.setObjectName("actionPassword_2")
        self.actionCompany_Info = QtWidgets.QAction(MainWindow)
        self.actionCompany_Info.setObjectName("actionCompany_Info")
        self.actionPayroll_Parameter = QtWidgets.QAction(MainWindow)
        self.actionPayroll_Parameter.setObjectName("actionPayroll_Parameter")
        self.actionImport_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionExport_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionBank_Details = QtWidgets.QAction(MainWindow)
        self.actionBank_Details.setObjectName("actionBank_Details")
        self.actionEmployee_History = QtWidgets.QAction(MainWindow)
        self.actionEmployee_History.setObjectName("actionEmployee_History")
        self.actionEmployee = QtWidgets.QAction(MainWindow)
        self.actionEmployee.setObjectName("actionEmployee")
        self.actionDepartment = QtWidgets.QAction(MainWindow)
        self.actionDepartment.setObjectName("actionDepartment")
        self.actionCatagory = QtWidgets.QAction(MainWindow)
        self.actionCatagory.setObjectName("actionCatagory")
        self.actionDesignation = QtWidgets.QAction(MainWindow)
        self.actionDesignation.setObjectName("actionDesignation")
        self.actionSite_Master = QtWidgets.QAction(MainWindow)
        self.actionSite_Master.setObjectName("actionSite_Master")
        self.actionEsi_Location = QtWidgets.QAction(MainWindow)
        self.actionEsi_Location.setObjectName("actionEsi_Location")
        self.actionPayRoll_Year_Data = QtWidgets.QAction(MainWindow)
        self.actionPayRoll_Year_Data.setObjectName("actionPayRoll_Year_Data")
        self.actionBank_Details_2 = QtWidgets.QAction(MainWindow)
        self.actionBank_Details_2.setObjectName("actionBank_Details_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEmployee_Details = QtWidgets.QAction(MainWindow)
        self.actionEmployee_Details.setObjectName("actionEmployee_Details")
        self.actionUpdate_Esi_Cal = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Esi_Cal.setObjectName("actionUpdate_Esi_Cal")
        self.menuTransanction.addAction(self.actionWages)
        self.menuTransanction.addAction(self.actionSalary)
        self.menuTransanction.addAction(self.actionWages_To_Salary)
        self.menuTransanction.addAction(self.actionArear_To_Salary)
        self.menuNew_2.addAction(self.actionEmployee)
        self.menuNew_2.addAction(self.actionDepartment)
        self.menuNew_2.addAction(self.actionCatagory)
        self.menuNew_2.addAction(self.actionDesignation)
        self.menuNew_2.addAction(self.actionSite_Master)
        self.menuNew_2.addAction(self.actionEsi_Location)
        self.menuNew_2.addAction(self.actionPayRoll_Year_Data)
        self.menuNew_2.addAction(self.actionBank_Details_2)
        self.menuFile.addAction(self.menuNew_2.menuAction())
        self.menuFile.addAction(self.menuTransanction.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuRegister.addAction(self.actionWages_Register_2)
        self.menuRegister.addAction(self.actionSalary_Register_2)
        self.menuRegister.addAction(self.actionArear_Register)
        self.menuRegister.addAction(self.actionEmployee_Register)
        self.menuRegister.addAction(self.actionEmployee_Ledger)
        self.menuRegister.addAction(self.actionMisc_Report)
        self.menuRegister.addAction(self.actionSettlement_Report)
        self.menuRegister.addAction(self.actionEmployee_att_Register)
        self.menuRegister.addAction(self.actionAdvance_Regist)
        self.menuPF.addAction(self.actionPF_Challan)
        self.menuPF.addAction(self.actionForm_12AR)
        self.menuPF.addAction(self.actionForm_12R)
        self.menuPF.addAction(self.actionMonthly_Report)
        self.menuPF.addAction(self.actionForm_5_10)
        self.menuPF.addAction(self.actionReturn_Form_6)
        self.menuPF.addAction(self.actionForm_3_AR)
        self.menuPF.addAction(self.actionForm_3AR_Data_File)
        self.menuEsi.addAction(self.actionChallan)
        self.menuEsi.addAction(self.actionForm_5_Return)
        self.menuEsi.addAction(self.actionMonthly_Report_2)
        self.menuLIN.addAction(self.actionChallan_2)
        self.menuLIN.addAction(self.actionMonthly_Report_3)
        self.menuDLC_Report.addAction(self.actionHalf_and_Yearly)
        self.menuBonus.addAction(self.actionRegister)
        self.menuAdvance_Loans.addAction(self.actionAdvance_Misc)
        self.menuAdvance_Loans.addAction(self.actionAdvance_Register)
        self.menuAdvance_Loans.addAction(self.actionAdvance_Issue)
        self.menuAdvance_Loans.addAction(self.actionAdvance_Receipt)
        self.menuView.addAction(self.menuRegister.menuAction())
        self.menuView.addAction(self.menuPF.menuAction())
        self.menuView.addAction(self.menuEsi.menuAction())
        self.menuView.addAction(self.menuLIN.menuAction())
        self.menuView.addAction(self.menuDLC_Report.menuAction())
        self.menuView.addAction(self.menuBonus.menuAction())
        self.menuView.addAction(self.actionEmployee_History)
        self.menuView.addAction(self.actionSettlement_Report_2)
        self.menuView.addAction(self.menuAdvance_Loans.menuAction())
        self.menuNew.addAction(self.actionUser)
        self.menuNew.addAction(self.actionManager)
        self.menuChange_Details.addAction(self.actionName_2)
        self.menuChange_Details.addAction(self.actionPassword_2)
        self.menuChange_User.addAction(self.menuNew.menuAction())
        self.menuChange_User.addAction(self.menuChange_Details.menuAction())
        self.menuUtility.addAction(self.actionSelect_Company)
        self.menuUtility.addAction(self.actionCompany_Info)
        self.menuUtility.addAction(self.actionUpdate_Bank_Info)
        self.menuUtility.addAction(self.actionSystem_Audit)
        self.menuUtility.addAction(self.actionUpdate_PF_Cal)
        self.menuUtility.addAction(self.actionUpdate_Esi_Cal)
        self.menuUtility.addAction(self.actionUpdate_Data)
        self.menuUtility.addAction(self.menuChange_User.menuAction())
        self.menuUtility.addAction(self.actionPayroll_Parameter)
        self.menuUtility.addAction(self.actionImport_Data)
        self.menuUtility.addAction(self.actionExport_Data)
        self.menuUtility.addAction(self.actionBank_Details)
        self.menuUtility.addSeparator()
        self.menuEidt.addAction(self.actionEmployee_Details)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEidt.menuAction())
        self.menubar.addAction(self.menuUtility.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        #  opening new employee dialog box on click of new employee action button
        self.actionEmployee.triggered.connect(self.NewEmployee)
        #self.pushButton_Close.clicked.connect(self.NewEmployee)
        #self.pushButton_Save.clicked.connect(self.Insert_emp)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Add"))
        self.menuTransanction.setTitle(_translate("MainWindow", "Transanction"))
        self.menuNew_2.setTitle(_translate("MainWindow", "New"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuRegister.setTitle(_translate("MainWindow", "Register"))
        self.menuPF.setTitle(_translate("MainWindow", "PF"))
        self.menuEsi.setTitle(_translate("MainWindow", "Esi"))
        self.menuLIN.setTitle(_translate("MainWindow", "LIN"))
        self.menuDLC_Report.setTitle(_translate("MainWindow", "DLC  Report"))
        self.menuBonus.setTitle(_translate("MainWindow", "Misc Report"))
        self.menuAdvance_Loans.setTitle(_translate("MainWindow", "Advance/Loans"))
        self.menuUtility.setTitle(_translate("MainWindow", "Utility"))
        self.menuChange_User.setTitle(_translate("MainWindow", "User"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuChange_Details.setTitle(_translate("MainWindow", "Change Details"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuEidt.setTitle(_translate("MainWindow", "Edit"))
        self.actionWages.setText(_translate("MainWindow", "Wages"))
        self.actionSalary.setText(_translate("MainWindow", "Salary"))
        self.actionWages_To_Salary.setText(_translate("MainWindow", "Wages To Salary"))
        self.actionArear_To_Salary.setText(_translate("MainWindow", "Arear To Salary"))
        self.actionWages_Register_2.setText(_translate("MainWindow", "Wages Register"))
        self.actionSalary_Register_2.setText(_translate("MainWindow", "Salary Register"))
        self.actionArear_Register.setText(_translate("MainWindow", "Arear Register"))
        self.actionEmployee_Register.setText(_translate("MainWindow", "Employee Register"))
        self.actionEmployee_Ledger.setText(_translate("MainWindow", "Employee Ledger"))
        self.actionMisc_Report.setText(_translate("MainWindow", "Bonus Register"))
        self.actionSettlement_Report.setText(_translate("MainWindow", "Leave Register"))
        self.actionEmployee_att_Register.setText(_translate("MainWindow", "Attendence Register"))
        self.actionPF_Challan.setText(_translate("MainWindow", "PF Challan"))
        self.actionForm_12AR.setText(_translate("MainWindow", "Form 12AR"))
        self.actionForm_12R.setText(_translate("MainWindow", "Form 12R"))
        self.actionMonthly_Report.setText(_translate("MainWindow", "Monthly Report"))
        self.actionForm_5_10.setText(_translate("MainWindow", "Form 5/10"))
        self.actionReturn_Form_6.setText(_translate("MainWindow", "Return( Form 6 )"))
        self.actionForm_3_AR.setText(_translate("MainWindow", "Form 3AR"))
        self.actionForm_3AR_Data_File.setText(_translate("MainWindow", "Form 3AR (Data_File)"))
        self.actionChallan.setText(_translate("MainWindow", "Challan"))
        self.actionForm_5_Return.setText(_translate("MainWindow", "Form 5(Return)"))
        self.actionMonthly_Report_2.setText(_translate("MainWindow", "Monthly Report"))
        self.actionChallan_2.setText(_translate("MainWindow", "Challan "))
        self.actionMonthly_Report_3.setText(_translate("MainWindow", "Monthly Report"))
        self.actionHalf_and_Yearly.setText(_translate("MainWindow", "Half and Yearly"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionSettlement_Report_2.setText(_translate("MainWindow", "Settlement Report"))
        self.actionAdvance_Misc.setText(_translate("MainWindow", "Advance Misc"))
        self.actionAdvance_Register.setText(_translate("MainWindow", "Advance Ledger"))
        self.actionAdvance_Issue.setText(_translate("MainWindow", "Advance Issue"))
        self.actionAdvance_Receipt.setText(_translate("MainWindow", "Advance Receipt"))
        self.actionAdvance_Regist.setText(_translate("MainWindow", "Advance Register"))
        self.actionSelect_Company.setText(_translate("MainWindow", "Select Company"))
        self.actionUpdate_Bank_Info.setText(_translate("MainWindow", "Update Bank Info"))
        self.actionSystem_Audit.setText(_translate("MainWindow", "System Audit"))
        self.actionUpdate_PF_Cal.setText(_translate("MainWindow", "Update PF Cal"))
        self.actionUpdate_Data.setText(_translate("MainWindow", "Update Data"))
        self.actionUser.setText(_translate("MainWindow", "User"))
        self.actionManager.setText(_translate("MainWindow", "Manager"))
        self.actionName_2.setText(_translate("MainWindow", "Name"))
        self.actionPassword_2.setText(_translate("MainWindow", "Password"))
        self.actionCompany_Info.setText(_translate("MainWindow", "Company Info"))
        self.actionPayroll_Parameter.setText(_translate("MainWindow", "Payroll Parameter"))
        self.actionImport_Data.setText(_translate("MainWindow", "Import Data"))
        self.actionExport_Data.setText(_translate("MainWindow", "Export Data"))
        self.actionBank_Details.setText(_translate("MainWindow", "Bank Details"))
        self.actionEmployee_History.setText(_translate("MainWindow", "Employee History"))
        self.actionEmployee.setText(_translate("MainWindow", "Employee"))
        self.actionDepartment.setText(_translate("MainWindow", "Department"))
        self.actionCatagory.setText(_translate("MainWindow", "Catagory"))
        self.actionDesignation.setText(_translate("MainWindow", "Designation"))
        self.actionSite_Master.setText(_translate("MainWindow", "Site Master"))
        self.actionEsi_Location.setText(_translate("MainWindow", "Esi Location"))
        self.actionPayRoll_Year_Data.setText(_translate("MainWindow", "PayRoll Year "))
        self.actionBank_Details_2.setText(_translate("MainWindow", "Bank Details"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionEmployee_Details.setText(_translate("MainWindow", "Employee Details"))
        self.actionUpdate_Esi_Cal.setText(_translate("MainWindow", "Update Esi Cal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

