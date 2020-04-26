# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_appointment_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import dbms
from ui import search_doctors_window
from ui.search_doctors_window import *
from db.dbms import *


def get_patient_phone_number(text):
    global patient_phone_number
    patient_phone_number = text

def get_appointment_time(text):
    global appointment_time
    appointment_time = text

class Ui_get_appointment(object):
    def setupUi(self, get_appointment):
        get_appointment.setObjectName("get_appointment")
        get_appointment.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(get_appointment)
        self.centralwidget.setObjectName("centralwidget")
        self.get_appointment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_appointment_btn.setGeometry(QtCore.QRect(590, 340, 75, 23))
        self.get_appointment_btn.setObjectName("get_appointment_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 200, 121, 16))
        self.label_4.setObjectName("label_4")
        self.current_logged_in = QtWidgets.QLabel(self.centralwidget)
        self.current_logged_in.setGeometry(QtCore.QRect(230, 80, 141, 20))
        self.current_logged_in.setObjectName("current_logged_in")
        self.dhh_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.dhh_btn.setGeometry(QtCore.QRect(230, 200, 121, 17))
        self.dhh_btn.setObjectName("dhh_btn")
        self.doh_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.doh_btn.setGeometry(QtCore.QRect(360, 200, 141, 17))
        self.doh_btn.setObjectName("doh_btn")
        self.patient_phone_number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_phone_number_input.setGeometry(QtCore.QRect(230, 120, 113, 20))
        self.patient_phone_number_input.setObjectName("patient_phone_number_input")
        self.appointment_time_input = QtWidgets.QLineEdit(self.centralwidget)
        self.appointment_time_input.setGeometry(QtCore.QRect(230, 160, 113, 20))
        self.appointment_time_input.setObjectName("appointment_time_input")
        self.appointment_info = QtWidgets.QLabel(self.centralwidget)
        self.appointment_info.setGeometry(QtCore.QRect(40, 290, 351, 141))
        self.appointment_info.setObjectName("appointment_info")
        get_appointment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(get_appointment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        get_appointment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(get_appointment)
        self.statusbar.setObjectName("statusbar")
        get_appointment.setStatusBar(self.statusbar)

        self.retranslateUi(get_appointment)
        QtCore.QMetaObject.connectSlotsByName(get_appointment)
        ########################################################
        self.patient_phone_number_input.textChanged.connect(get_patient_phone_number)
        self.appointment_time_input.textChanged.connect(get_appointment_time)
        self.get_appointment_btn.clicked.connect(self.Clicked)


    def retranslateUi(self, get_appointment):
        _translate = QtCore.QCoreApplication.translate
        get_appointment.setWindowTitle(_translate("get_appointment", "MainWindow"))
        self.get_appointment_btn.setText(_translate("get_appointment", "get"))
        self.label.setText(_translate("get_appointment", "getter phone number"))
        self.label_2.setText(_translate("get_appointment", "patient phone number"))
        self.label_3.setText(_translate("get_appointment", "appointment time"))
        self.label_4.setText(_translate("get_appointment", "place"))
        self.current_logged_in.setText(_translate("get_appointment", dbms.current_logged_in))
        self.dhh_btn.setText(_translate("get_appointment", "health care center"))
        self.doh_btn.setText(_translate("get_appointment", "doctor office"))
        self.appointment_info.setText(_translate("get_appointment", "appointment info"))

    def Clicked(self):
        #print(search_doctors_window.medical_council,appointment_time, dbms.current_logged_in, patient_phone_number)
        conn = create_connection("db.sqlite")
        if self.doh_btn.isChecked():
            place = 'doh'
        if self.dhh_btn.isChecked():
            place = 'dhh'
        if is_start_hour_valid(conn,search_doctors_window.medical_council,place,appointment_time):
            text =make_appointment(conn,place,search_doctors_window.medical_council,patient_phone_number,dbms.current_logged_in,appointment_time)
        else:
            text = "invalid appointment time"
        self.appointment_info.setText(text)
        self.appointment_info.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    get_appointment = QtWidgets.QMainWindow()
    ui = Ui_get_appointment()
    ui.setupUi(get_appointment)
    get_appointment.show()
    sys.exit(app.exec_())
