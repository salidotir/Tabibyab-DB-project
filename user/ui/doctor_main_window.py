# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctor_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import dbms
from db.dbms import *
from ui import *


class Ui_doctor_main_window(object):
    def setupUi(self, doctor_main_window):
        doctor_main_window.setObjectName("doctor_main_window")
        doctor_main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(doctor_main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(20, 30, 731, 331))
        self.result_label.setObjectName("result_label")
        self.see_profile_info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.see_profile_info_btn.setGeometry(QtCore.QRect(550, 500, 201, 23))
        self.see_profile_info_btn.setObjectName("see_profile_info_btn")
        self.see_patients_info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.see_patients_info_btn.setGeometry(QtCore.QRect(550, 470, 201, 23))
        self.see_patients_info_btn.setObjectName("see_patients_info_btn")
        doctor_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(doctor_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        doctor_main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(doctor_main_window)
        self.statusbar.setObjectName("statusbar")
        doctor_main_window.setStatusBar(self.statusbar)
        self.actionedit_doctor_profile = QtWidgets.QAction(doctor_main_window)
        self.actionedit_doctor_profile.setObjectName("actionedit_doctor_profile")
        self.actionadd_insurance = QtWidgets.QAction(doctor_main_window)
        self.actionadd_insurance.setObjectName("actionadd_insurance")
        self.actiondelete_insurance = QtWidgets.QAction(doctor_main_window)
        self.actiondelete_insurance.setObjectName("actiondelete_insurance")
        self.actionedit_work_hour = QtWidgets.QAction(doctor_main_window)
        self.actionedit_work_hour.setObjectName("actionedit_work_hour")
        self.menuedit.addAction(self.actionedit_doctor_profile)
        self.menuedit.addAction(self.actionadd_insurance)
        self.menuedit.addAction(self.actiondelete_insurance)
        self.menuedit.addAction(self.actionedit_work_hour)
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(doctor_main_window)
        QtCore.QMetaObject.connectSlotsByName(doctor_main_window)
        ##############################################################
        print(dbms.current_logged_in)
        conn=create_connection("db.sqlite")
        text =see_patients_of_a_doctor(conn,dbms.current_logged_in)
        text2 =show_doctor_profile(conn,dbms.current_logged_in)
        print(text,text2)
        self.see_patients_info_btn.clicked.connect(lambda :self.Clicked(text))
        self.see_profile_info_btn.clicked.connect(lambda :self.Clicked(text2))



    def retranslateUi(self, doctor_main_window):
        _translate = QtCore.QCoreApplication.translate
        doctor_main_window.setWindowTitle(_translate("doctor_main_window", "MainWindow"))
        self.result_label.setText(_translate("doctor_main_window", "click bottons to see info"))
        self.see_profile_info_btn.setText(_translate("doctor_main_window", "see profile info"))
        self.see_patients_info_btn.setText(_translate("doctor_main_window", "see patients info"))
        self.menuedit.setTitle(_translate("doctor_main_window", "edit"))
        self.actionedit_doctor_profile.setText(_translate("doctor_main_window", "edit doctor profile"))
        self.actionadd_insurance.setText(_translate("doctor_main_window", "add insurance"))
        self.actiondelete_insurance.setText(_translate("doctor_main_window", "delete insurance"))
        self.actionedit_work_hour.setText(_translate("doctor_main_window", "edit work hour"))

    def Clicked(self, text):

        self.result_label.setText(text)
        self.result_label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    doctor_main_window = QtWidgets.QMainWindow()
    ui = Ui_doctor_main_window()
    ui.setupUi(doctor_main_window)
    doctor_main_window.show()
    sys.exit(app.exec_())
