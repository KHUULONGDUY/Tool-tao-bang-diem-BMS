# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KLday.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_KLday(object):
    def setupUi(self, KLday):
        KLday.setObjectName("KLday")
        KLday.setWindowIcon(QIcon('logo.ico'))
        KLday.resize(669, 642)
        self.centralwidget = QtWidgets.QWidget(KLday)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 10, 101, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.A1 = QtWidgets.QLineEdit(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(410, 160, 141, 31))
        self.A1.setObjectName("A1")
        self.A2 = QtWidgets.QLineEdit(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(410, 210, 141, 31))
        self.A2.setObjectName("A2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.A3 = QtWidgets.QLineEdit(self.centralwidget)
        self.A3.setGeometry(QtCore.QRect(410, 260, 141, 31))
        self.A3.setObjectName("A3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.A4 = QtWidgets.QLineEdit(self.centralwidget)
        self.A4.setGeometry(QtCore.QRect(410, 310, 141, 31))
        self.A4.setObjectName("A4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.A5 = QtWidgets.QLineEdit(self.centralwidget)
        self.A5.setGeometry(QtCore.QRect(410, 360, 141, 31))
        self.A5.setObjectName("A5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 360, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.A6 = QtWidgets.QLineEdit(self.centralwidget)
        self.A6.setGeometry(QtCore.QRect(410, 410, 141, 31))
        self.A6.setObjectName("A6")
        self.A7 = QtWidgets.QLineEdit(self.centralwidget)
        self.A7.setGeometry(QtCore.QRect(410, 460, 141, 31))
        self.A7.setObjectName("A7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 410, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 460, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(570, 210, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(570, 260, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(570, 310, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(570, 360, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(570, 410, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(570, 460, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(460, 520, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(60, 520, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        KLday.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KLday)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 26))
        self.menubar.setObjectName("menubar")
        KLday.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KLday)
        self.statusbar.setObjectName("statusbar")
        KLday.setStatusBar(self.statusbar)

        self.retranslateUi(KLday)
        QtCore.QMetaObject.connectSlotsByName(KLday)

    def retranslateUi(self, KLday):
        _translate = QtCore.QCoreApplication.translate
        KLday.setWindowTitle(_translate("KLday", "DỰ TOÁN KHỐI LƯỢNG DÂY"))
        self.label.setText(_translate("KLday", "DỰ TOÁN KHỐI LƯỢNG DÂY"))
        self.label_3.setText(_translate("KLday", "Tủ ĐK đến tủ ĐL :"))
        self.label_4.setText(_translate("KLday", "Tủ ĐK đến tủ AHU :"))
        self.label_5.setText(_translate("KLday", "Tủ ĐK đến tủ phòng :"))
        self.label_6.setText(_translate("KLday", "HS ống điện/dây điện: Tủ>>Tủ"))
        self.label_7.setText(_translate("KLday", "HS ống điện/dây điện : Tủ>>AHU"))
        self.label_8.setText(_translate("KLday", "HS ống điện/dây điện : Tủ>>phòng"))
        self.label_9.setText(_translate("KLday", "Định mức dây CAT6 tủ ĐK"))
        self.label_10.setText(_translate("KLday", "A1"))
        self.label_11.setText(_translate("KLday", "A2"))
        self.label_12.setText(_translate("KLday", "A3"))
        self.label_13.setText(_translate("KLday", "A4"))
        self.label_14.setText(_translate("KLday", "A5"))
        self.label_15.setText(_translate("KLday", "A6"))
        self.label_16.setText(_translate("KLday", "A7"))
        self.next_button.setText(_translate("KLday", "NEXT"))
        self.back_button.setText(_translate("KLday", "BACK"))