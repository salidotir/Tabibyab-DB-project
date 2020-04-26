# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from db.dbms import *
from ui.main_window import *
from ui.user_register_window import *
from ui.doctor_main_window import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtWidgets import QMessageBox
# from PyQt5.QtCore import QSize

def get_pasword_text(text):
    global password
    password = text

def get_username_text(text):
    global username
    username = text

class Ui_login_register_window(object):
    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_register_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =user_register_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_doctor_main_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_doctor_main_window()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, login_register_window):
        login_register_window.setObjectName("login_register_window")
        login_register_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(login_register_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 140, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.user_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.user_login_btn.setGeometry(QtCore.QRect(220, 310, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_login_btn.setFont(font)
        self.user_login_btn.setObjectName("user_login_btn")
        self.doctor_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.doctor_login_btn.setGeometry(QtCore.QRect(410, 310, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doctor_login_btn.setFont(font)
        self.doctor_login_btn.setObjectName("doctor_login_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 410, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.register_btn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(280, 410, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.register_btn.setFont(font)
        self.register_btn.setObjectName("register_btn")
        self.user_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name_input.setGeometry(QtCore.QRect(170, 150, 441, 31))
        self.user_name_input.setObjectName("user_name_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(170, 220, 441, 31))
        self.password_input.setObjectName("password_input")
        login_register_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_register_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        login_register_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login_register_window)
        self.statusbar.setObjectName("statusbar")
        login_register_window.setStatusBar(self.statusbar)

        self.retranslateUi(login_register_window)
        QtCore.QMetaObject.connectSlotsByName(login_register_window)

        self.user_login_btn.clicked.connect(self.ui_user_login)
        self.user_name_input.textChanged.connect(get_username_text)
        self.password_input.textChanged.connect(get_pasword_text)
        self.user_name_input.textChanged.connect(get_username_text)
        self.password_input.textChanged.connect(get_pasword_text)

        self.register_btn.clicked.connect(self.ui_user_register)
        self.doctor_login_btn.clicked.connect(self.ui_doctor_login)


    def retranslateUi(self, login_register_window):
        _translate = QtCore.QCoreApplication.translate
        login_register_window.setWindowTitle(_translate("login_register_window", "MainWindow"))
        self.label.setText(_translate("login_register_window", "Username:"))
        self.label_2.setText(_translate("login_register_window", "Password:"))
        self.user_login_btn.setText(_translate("login_register_window", "User login"))
        self.doctor_login_btn.setText(_translate("login_register_window", "Doctor login"))
        self.label_3.setText(_translate("login_register_window", "Don\'t have an account? Create "))
        self.register_btn.setText(_translate("login_register_window", "one."))

    def ui_user_login(self):
        conn = create_connection("db.sqlite")
        res = user_login(conn, password,username)
        close_connection(conn)
        if res == True:
            print("user logged in.")
            self.open_window()
        else:
            print("wrong username or password.")
            # QMessageBox.about(self, "Login page", "Wrong username or password")
            pass

    def ui_doctor_login(self):
        conn = create_connection("db.sqlite")
        view_table(conn,'doctor')
        res = doctor_login(conn, username, password)
        close_connection(conn)
        if res == True:
            print("doctor logged in.")
            print(dbms.current_logged_in)
            self.open_doctor_main_window()
        else:
            print("wrong username or password.")
            # QMessageBox.about(self, "Login page", "Wrong username or password")
            pass

    def ui_user_register(self):
        self.open_register_window()

def run_login_register_window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_register_window = QtWidgets.QMainWindow()
    ui = Ui_login_register_window()
    ui.setupUi(login_register_window)
    login_register_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_register_window = QtWidgets.QMainWindow()
    ui = Ui_login_register_window()
    ui.setupUi(login_register_window)
    login_register_window.show()
    sys.exit(app.exec_())
