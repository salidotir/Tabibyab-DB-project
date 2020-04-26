# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import dbms
from db.dbms import *
from ui.main_window import *

def get_pasword_text(text):
    global password
    password = text

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



class Ui_user_edit_window(object):
    def setupUi(self, user_edit_window):
        user_edit_window.setObjectName("user_edit_window")
        user_edit_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(user_edit_window)
        self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(70, 53, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        #self.label.setFont(font)
        #self.label.setObjectName("label")
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.first_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_input.setGeometry(QtCore.QRect(210, 110, 381, 31))
        self.first_name_input.setObjectName("first_name_input")
        self.last_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_input.setGeometry(QtCore.QRect(210, 170, 381, 31))
        self.last_name_input.setObjectName("last_name_input")
        self.bith_day_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bith_day_input.setGeometry(QtCore.QRect(210, 240, 381, 31))
        self.bith_day_input.setObjectName("bith_day_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(210, 300, 381, 31))
        self.password_input.setObjectName("password_input")
        self.insurance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.insurance_input.setGeometry(QtCore.QRect(210, 360, 381, 31))
        self.insurance_input.setObjectName("insurance_input")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 420, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.unknown_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.unknown_btn.setGeometry(QtCore.QRect(430, 430, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.unknown_btn.setFont(font)
        self.unknown_btn.setObjectName("unknown_btn")
        self.female_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.female_btn.setGeometry(QtCore.QRect(210, 430, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.female_btn.setFont(font)
        self.female_btn.setObjectName("female_btn")
        self.male_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.male_btn.setGeometry(QtCore.QRect(330, 430, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.male_btn.setFont(font)
        self.male_btn.setObjectName("male_btn")
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(600, 460, 75, 23))
        self.edit_btn.setObjectName("edit_btn")
        user_edit_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(user_edit_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        user_edit_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(user_edit_window)
        self.statusbar.setObjectName("statusbar")
        user_edit_window.setStatusBar(self.statusbar)

        self.retranslateUi(user_edit_window)
        QtCore.QMetaObject.connectSlotsByName(user_edit_window)
        ###################
        self.password_input.textChanged.connect(get_pasword_text)
        self.first_name_input.textChanged.connect(get_first_name)
        self.last_name_input.textChanged.connect(get_last_name)
        self.bith_day_input.textChanged.connect(get_birth_day)
        self.insurance_input.textChanged.connect(get_insurance)

        self.edit_btn.clicked.connect(self.update_user)

    def retranslateUi(self, user_edit_window):
        _translate = QtCore.QCoreApplication.translate
        user_edit_window.setWindowTitle(_translate("user_edit_window", "MainWindow"))
        #self.label.setText(_translate("user_edit_window", "phone number:"))
        self.label_2.setText(_translate("user_edit_window", "first name:"))
        self.label_3.setText(_translate("user_edit_window", "last name:"))
        self.label_4.setText(_translate("user_edit_window", "birth day:"))
        self.label_5.setText(_translate("user_edit_window", "password:"))
        self.label_7.setText(_translate("user_edit_window", "insurance:"))
        self.label_6.setText(_translate("user_edit_window", "gender:"))
        self.unknown_btn.setText(_translate("user_edit_window", "unknown"))
        self.female_btn.setText(_translate("user_edit_window", "female"))
        self.male_btn.setText(_translate("user_edit_window", "male"))
        self.edit_btn.setText(_translate("user_edit_window", "edit"))


    def update_user(self):
        conn = create_connection("db.sqlite")

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
        #print(gender_id,insurance_id)
        print(dbms.current_logged_in)
        res = edit_profile(conn, dbms.current_logged_in, first_name, last_name, password, birth_day, gender_id, insurance_id)
        print("edit is called")

        close_connection(conn)
        print("connection is closed ")
        if res == True:
            print("profile updated sucessfully.")
        else:
            print("could not update profile.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_edit_window = QtWidgets.QMainWindow()
    ui = Ui_user_edit_window()
    ui.setupUi(user_edit_window)
    user_edit_window.show()
    sys.exit(app.exec_())
