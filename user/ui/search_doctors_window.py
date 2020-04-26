# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_doctors_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import  dbms
from db.dbms import *
from ui.get_appointment_window import *
def get_input(text):
    global input
    input = text

def get_medical_council_code(text):
    global medical_council
    medical_council = text



class Ui_search_doctors_window(object):
    
    def open_get_appointment_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_get_appointment()
        self.ui.setupUi(self.window)
        self.window.show()

    
    def setupUi(self, search_doctors_window):
        search_doctors_window.setObjectName("search_doctors_window")
        search_doctors_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(search_doctors_window)
        self.centralwidget.setObjectName("centralwidget")
        self.search_by_first_name = QtWidgets.QRadioButton(self.centralwidget)
        self.search_by_first_name.setGeometry(QtCore.QRect(0, 10, 121, 16))
        self.search_by_first_name.setObjectName("search_by_first_name")
        self.search_by_last_name = QtWidgets.QRadioButton(self.centralwidget)
        self.search_by_last_name.setGeometry(QtCore.QRect(130, 10, 131, 16))
        self.search_by_last_name.setObjectName("search_by_last_name")
        self.search_by_specialty = QtWidgets.QRadioButton(self.centralwidget)
        self.search_by_specialty.setGeometry(QtCore.QRect(250, 10, 131, 16))
        self.search_by_specialty.setObjectName("search_by_specialty")
        self.search_by_city = QtWidgets.QRadioButton(self.centralwidget)
        self.search_by_city.setGeometry(QtCore.QRect(370, 10, 121, 20))
        self.search_by_city.setObjectName("search_by_city")
        self.work_hour = QtWidgets.QRadioButton(self.centralwidget)
        self.work_hour.setGeometry(QtCore.QRect(0, 110, 181, 16))
        self.work_hour.setObjectName("work_hour")
        self.first_empty = QtWidgets.QRadioButton(self.centralwidget)
        self.first_empty.setGeometry(QtCore.QRect(180, 110, 251, 16))
        self.first_empty.setObjectName("first_empty")
        self.any_input = QtWidgets.QLineEdit(self.centralwidget)
        self.any_input.setGeometry(QtCore.QRect(660, 10, 113, 20))
        self.any_input.setObjectName("any_input")
        self.doctor_input = QtWidgets.QLineEdit(self.centralwidget)
        self.doctor_input.setGeometry(QtCore.QRect(660, 60, 113, 20))
        self.doctor_input.setObjectName("doctor_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.action_btn = QtWidgets.QPushButton(self.centralwidget)
        self.action_btn.setGeometry(QtCore.QRect(680, 130, 75, 23))
        self.action_btn.setObjectName("action_btn")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 200, 761, 381))
        self.result.setText("")
        self.result.setObjectName("result")
        self.all_empty = QtWidgets.QRadioButton(self.centralwidget)
        self.all_empty.setGeometry(QtCore.QRect(0, 140, 251, 16))
        self.all_empty.setObjectName("all_empty")
        self.add_to_saved = QtWidgets.QRadioButton(self.centralwidget)
        self.add_to_saved.setGeometry(QtCore.QRect(210, 140, 131, 17))
        self.add_to_saved.setObjectName("add_to_saved")
        self.search_by_insurance = QtWidgets.QRadioButton(self.centralwidget)
        self.search_by_insurance.setGeometry(QtCore.QRect(470, 10, 131, 17))
        self.search_by_insurance.setObjectName("search_by_insurance")
        self.search_by_health_care_system = QtWidgets.QRadioButton(self.centralwidget)
        self.search_by_health_care_system.setGeometry(QtCore.QRect(0, 40, 161, 17))
        self.search_by_health_care_system.setObjectName("search_by_health_care_system")
        self.show_all_doctors = QtWidgets.QRadioButton(self.centralwidget)
        self.show_all_doctors.setGeometry(QtCore.QRect(160, 40, 191, 17))
        self.show_all_doctors.setObjectName("show_all_doctors")
        self.appointment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.appointment_btn.setGeometry(QtCore.QRect(680, 100, 75, 23))
        self.appointment_btn.setObjectName("appointment_btn")
        search_doctors_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(search_doctors_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        search_doctors_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(search_doctors_window)
        self.statusbar.setObjectName("statusbar")
        search_doctors_window.setStatusBar(self.statusbar)

        self.retranslateUi(search_doctors_window)
        QtCore.QMetaObject.connectSlotsByName(search_doctors_window)
        ###############################################################
        self.any_input.textChanged.connect(get_input)
        self.doctor_input.textChanged.connect(get_medical_council_code)
        self.action_btn.clicked.connect(self.Clicked)
        self.appointment_btn.clicked.connect(lambda : self.open_get_appointment_window())



    def retranslateUi(self, search_doctors_window):
        _translate = QtCore.QCoreApplication.translate
        search_doctors_window.setWindowTitle(_translate("search_doctors_window", "MainWindow"))
        self.search_by_first_name.setText(_translate("search_doctors_window", "search by first name"))
        self.search_by_last_name.setText(_translate("search_doctors_window", "search by last name"))
        self.search_by_specialty.setText(_translate("search_doctors_window", "search by specialty"))
        self.search_by_city.setText(_translate("search_doctors_window", "search by city"))
        self.work_hour.setText(_translate("search_doctors_window", "see a specific doctor\'s work hour"))
        self.first_empty.setText(_translate("search_doctors_window", "see a specific doctor\'s first empty time"))
        self.label.setText(_translate("search_doctors_window", "doctor"))
        self.label_2.setText(_translate("search_doctors_window", "input"))
        self.action_btn.setText(_translate("search_doctors_window", "action"))
        self.all_empty.setText(_translate("search_doctors_window", "see a specific doctor\'s all empty times"))
        self.add_to_saved.setText(_translate("search_doctors_window", "add doctor to saved"))
        self.search_by_insurance.setText(_translate("search_doctors_window", "seardch by insurance"))
        self.search_by_health_care_system.setText(_translate("search_doctors_window", "search by health care center"))
        self.show_all_doctors.setText(_translate("search_doctors_window", "show all doctors"))
        self.appointment_btn.setText(_translate("search_doctors_window", "appointment"))


    def Clicked(self):
        conn = create_connection('db.sqlite')
        if self.search_by_first_name.isChecked():
            text = search_doctors_based_on_first_name(conn, input)
        elif self.search_by_last_name.isChecked():
            text = search_doctors_based_on_last_name(conn, input)
        elif self.search_by_city.isChecked():
            text = search_doctors_based_on_city(conn, input)
        elif self.search_by_specialty.isChecked():
            text = search_doctors_based_on_specialty_id(conn, input)
        elif self.work_hour.isChecked():
            text = get_working_hour(conn,medical_council)
        elif self.first_empty.isChecked():
            text = show_first_available_empty_time(conn,medical_council)
        elif self.all_empty.isChecked():
            text = show_all_available_empty_times(conn,medical_council)
        elif self.add_to_saved.isChecked():
            print(dbms.current_logged_in,medical_council)
            text =save_doctor(conn,dbms.current_logged_in,medical_council)
        elif self.search_by_insurance.isChecked():
            text =search_doctors_based_on_insurance(conn,input)
        elif self.search_by_health_care_system.isChecked():
            text= docotrs_of_a_medical_center(conn,input)
        elif self.show_all_doctors.isChecked():
            text = show_all_doctors(conn)
        self.result.setText(text)
        self.result.adjustSize()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search_doctors_window = QtWidgets.QMainWindow()
    ui = Ui_search_doctors_window()
    ui.setupUi(search_doctors_window)
    search_doctors_window.show()
    sys.exit(app.exec_())
