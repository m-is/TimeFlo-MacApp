# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("TimeFlo")
        Dialog.resize(400, 300)
        self.start_timer = QtWidgets.QPushButton(Dialog)
        self.start_timer.setGeometry(QtCore.QRect(40, 220, 150, 32))
        self.start_timer.setObjectName("StartTimer")

        self.end_timer = QtWidgets.QPushButton(Dialog)
        self.end_timer.setGeometry(QtCore.QRect(220, 220, 112, 32))
        self.end_timer.setObjectName("endTimer")

        self.lcd_number = QtWidgets.QLCDNumber(Dialog)
        self.lcd_number.setGeometry(QtCore.QRect(60, 40, 251, 141))
        self.lcd_number.setObjectName("lcdNumber")

        self.change_timer = QtWidgets.QPushButton(Dialog)
        self.change_timer.setGeometry(QtCore.QRect(40, 260, 150, 32)) 
        self.change_timer.setObjectName("changeTimer")

        self.change_break = QtWidgets.QPushButton(Dialog)
        self.change_break.setGeometry(QtCore.QRect(220, 260, 150, 32)) 
        self.change_break.setObjectName("changeBreak")

        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TimeFlo"))
        self.start_timer.setText(_translate("Dialog", "Start Timer"))
        self.end_timer.setText(_translate("Dialog", "Quit Timer"))
        self.change_timer.setText(_translate("Dialog", "Change Timer"))
        self.change_break.setText(_translate("Dialog", "Change Break"))
