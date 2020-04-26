# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 781, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.set_appointment = QtWidgets.QPushButton(self.centralwidget)
        self.set_appointment.setGeometry(QtCore.QRect(644, 490, 111, 21))
        self.set_appointment.setObjectName("set_appointment")
        self.search_doctors = QtWidgets.QPushButton(self.centralwidget)
        self.search_doctors.setGeometry(QtCore.QRect(644, 463, 111, 20))
        self.search_doctors.setObjectName("search_doctors")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menumy_orofile = QtWidgets.QMenu(self.menubar)
        self.menumy_orofile.setObjectName("menumy_orofile")
        self.menusee_my_appointments = QtWidgets.QMenu(self.menumy_orofile)
        self.menusee_my_appointments.setObjectName("menusee_my_appointments")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionby_name = QtWidgets.QAction(MainWindow)
        self.actionby_name.setObjectName("actionby_name")
        self.actionby_family = QtWidgets.QAction(MainWindow)
        self.actionby_family.setObjectName("actionby_family")
        self.actionby_specialty = QtWidgets.QAction(MainWindow)
        self.actionby_specialty.setObjectName("actionby_specialty")
        self.actionby_place = QtWidgets.QAction(MainWindow)
        self.actionby_place.setObjectName("actionby_place")
        self.actionshow = QtWidgets.QAction(MainWindow)
        self.actionshow.setObjectName("actionshow")
        self.actionedit = QtWidgets.QAction(MainWindow)
        self.actionedit.setObjectName("actionedit")
        self.actionadd_family_member = QtWidgets.QAction(MainWindow)
        self.actionadd_family_member.setObjectName("actionadd_family_member")
        self.actionsee_my_family_appointments = QtWidgets.QAction(MainWindow)
        self.actionsee_my_family_appointments.setObjectName("actionsee_my_family_appointments")
        self.actionmy_reservations = QtWidgets.QAction(MainWindow)
        self.actionmy_reservations.setObjectName("actionmy_reservations")
        self.actionmy_family_reservations = QtWidgets.QAction(MainWindow)
        self.actionmy_family_reservations.setObjectName("actionmy_family_reservations")
        self.menusee_my_appointments.addAction(self.actionmy_reservations)
        self.menusee_my_appointments.addAction(self.actionmy_family_reservations)
        self.menumy_orofile.addAction(self.actionshow)
        self.menumy_orofile.addAction(self.actionedit)
        self.menumy_orofile.addAction(self.actionadd_family_member)
        self.menumy_orofile.addSeparator()
        self.menumy_orofile.addAction(self.menusee_my_appointments.menuAction())
        self.menumy_orofile.addAction(self.actionsee_my_family_appointments)
        self.menubar.addAction(self.menumy_orofile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.set_appointment.setText(_translate("MainWindow", "get appointment"))
        self.search_doctors.setText(_translate("MainWindow", "search doctors"))
        self.menumy_orofile.setTitle(_translate("MainWindow", "my profile"))
        self.menusee_my_appointments.setTitle(_translate("MainWindow", "see my appointments"))
        self.actionby_name.setText(_translate("MainWindow", "by name"))
        self.actionby_name.setStatusTip(_translate("MainWindow", "choose your doctor by name"))
        self.actionby_name.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionby_family.setText(_translate("MainWindow", "by family"))
        self.actionby_family.setStatusTip(_translate("MainWindow", "choose your doctor by family"))
        self.actionby_family.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionby_specialty.setText(_translate("MainWindow", "by specialty"))
        self.actionby_specialty.setStatusTip(_translate("MainWindow", "choose your doctor by specialty"))
        self.actionby_specialty.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionby_place.setText(_translate("MainWindow", "by place"))
        self.actionby_place.setStatusTip(_translate("MainWindow", "choose your doctor by place"))
        self.actionby_place.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionshow.setText(_translate("MainWindow", "show"))
        self.actionshow.setStatusTip(_translate("MainWindow", "show profile"))
        self.actionedit.setText(_translate("MainWindow", "edit"))
        self.actionedit.setStatusTip(_translate("MainWindow", "edit profile"))
        self.actionadd_family_member.setText(_translate("MainWindow", "add family member"))
        self.actionsee_my_family_appointments.setText(_translate("MainWindow", "see my family appointments"))
        self.actionmy_reservations.setText(_translate("MainWindow", "my reservations"))
        self.actionmy_family_reservations.setText(_translate("MainWindow", "my family reservations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
