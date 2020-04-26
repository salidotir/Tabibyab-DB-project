# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_family_member.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import dbms
from db.dbms import *


def get_family_phone_number(text):
    global family_phone_number
    family_phone_number = text


def get_user_phone_number(text):
    global user_phone_number
    user_phone_number = text


def get_first_name(text):
    global first_name
    first_name = text


def get_last_name(text):
    global last_name
    last_name = text


def get_birth_day(text):
    global birth_day
    birth_day = text


def get_insurance(text):
    global insurance
    insurance = text


class Ui_add_family_member_window(object):
    def setupUi(self, add_family_member_window):
        add_family_member_window.setObjectName("add_family_member_window")
        add_family_member_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(add_family_member_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 53, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 310, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.family_phone_number = QtWidgets.QLineEdit(self.centralwidget)
        self.family_phone_number.setGeometry(QtCore.QRect(210, 59, 381, 31))
        self.family_phone_number.setObjectName("family_phone_number")
        self.first_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_input.setGeometry(QtCore.QRect(210, 110, 381, 31))
        self.first_name_input.setObjectName("first_name_input")
        self.last_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_input.setGeometry(QtCore.QRect(210, 170, 381, 31))
        self.last_name_input.setObjectName("last_name_input")
        self.bith_day_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bith_day_input.setGeometry(QtCore.QRect(210, 240, 381, 31))
        self.bith_day_input.setObjectName("bith_day_input")
        self.insurance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.insurance_input.setGeometry(QtCore.QRect(210, 310, 381, 31))
        self.insurance_input.setObjectName("insurance_input")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 370, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.unknown_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.unknown_btn.setGeometry(QtCore.QRect(430, 380, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.unknown_btn.setFont(font)
        self.unknown_btn.setObjectName("unknown_btn")
        self.female_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.female_btn.setGeometry(QtCore.QRect(210, 380, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.female_btn.setFont(font)
        self.female_btn.setObjectName("female_btn")
        self.male_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.male_btn.setGeometry(QtCore.QRect(330, 380, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.male_btn.setFont(font)
        self.male_btn.setObjectName("male_btn")
        self.add_family_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_family_btn.setGeometry(QtCore.QRect(600, 412, 121, 21))
        self.add_family_btn.setObjectName("add_family_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 430, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.user_phone_number = QtWidgets.QLineEdit(self.centralwidget)
        self.user_phone_number.setGeometry(QtCore.QRect(210, 460, 381, 31))
        self.user_phone_number.setObjectName("user_phone_number")
        add_family_member_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_family_member_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        add_family_member_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_family_member_window)
        self.statusbar.setObjectName("statusbar")
        add_family_member_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_family_member_window)
        QtCore.QMetaObject.connectSlotsByName(add_family_member_window)

        self.family_phone_number.textChanged.connect(get_family_phone_number)
        self.first_name_input.textChanged.connect(get_first_name)
        self.last_name_input.textChanged.connect(get_last_name)
        self.bith_day_input.textChanged.connect(get_birth_day)
        self.insurance_input.textChanged.connect(get_insurance)
        self.user_phone_number.textChanged.connect(get_user_phone_number)

        self.add_family_btn.clicked.connect(self.add_family_member)

    def retranslateUi(self, add_family_member_window):
        _translate = QtCore.QCoreApplication.translate
        add_family_member_window.setWindowTitle(_translate("add_family_member_window", "MainWindow"))
        self.label.setText(_translate("add_family_member_window", "phone number:"))
        self.label_2.setText(_translate("add_family_member_window", "first name:"))
        self.label_3.setText(_translate("add_family_member_window", "last name:"))
        self.label_4.setText(_translate("add_family_member_window", "birth day:"))
        self.label_7.setText(_translate("add_family_member_window", "insurance:"))
        self.label_6.setText(_translate("add_family_member_window", "gender:"))
        self.unknown_btn.setText(_translate("add_family_member_window", "unknown"))
        self.female_btn.setText(_translate("add_family_member_window", "female"))
        self.male_btn.setText(_translate("add_family_member_window", "male"))
        self.add_family_btn.setText(_translate("add_family_member_window", "add family member"))
        self.label_5.setText(_translate("add_family_member_window", "repeat your own phone number"))

    def add_family_member(self):
        ## get texts from text boxes and add family
        conn = create_connection("db.sqlite")
        print(user_phone_number,family_phone_number,insurance,first_name,last_name)
        gender = ""
        if self.female_btn.isChecked():
            print("female is checked")
            gender = 'female'
        elif self.male_btn.isChecked():
            gender = 'male'
        elif self.unknown_btn.isChecked():
            gender = 'other'

        gender_id = get_gender_id(conn, gender)
        insurance_id = get_insurance_id(conn, insurance)
        print(gender_id,insurance_id)
        add_family(conn, user_phone_number, family_phone_number, first_name, last_name, birth_day, gender_id,
                   insurance_id)
        print("family member added")
        close_connection(conn)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    add_family_member_window = QtWidgets.QMainWindow()
    ui = Ui_add_family_member_window()
    ui.setupUi(add_family_member_window)
    add_family_member_window.show()
    sys.exit(app.exec_())
