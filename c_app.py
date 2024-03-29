import sys
import PyQt5
import os
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QStatusBar
from ciphers import Ciphers
import od_encryption


import PIL
from tkinter import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 600, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.Cezarus = QtWidgets.QWidget()
        self.Cezarus.setObjectName("Cezarus")
        self.c_button = QtWidgets.QPushButton(self.Cezarus)
        self.c_button.setGeometry(QtCore.QRect(0, 220, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.c_button.setFont(font)
        self.c_button.setObjectName("c_button")
        self.c_input = QtWidgets.QLineEdit(self.Cezarus)
        self.c_input.setGeometry(QtCore.QRect(260, 10, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.c_input.setFont(font)
        self.c_input.setText("")
        self.c_input.setObjectName("c_input")
        self.c_label_1 = QtWidgets.QLabel(self.Cezarus)
        self.c_label_1.setGeometry(QtCore.QRect(0, 10, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.c_label_1.setFont(font)
        self.c_label_1.setObjectName("c_label_1")
        self.c_label_3 = QtWidgets.QLabel(self.Cezarus)
        self.c_label_3.setGeometry(QtCore.QRect(0, 150, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.c_label_3.setFont(font)
        self.c_label_3.setObjectName("c_label_3")
        self.c_result = QtWidgets.QLineEdit(self.Cezarus)
        self.c_result.setGeometry(QtCore.QRect(260, 150, 330, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.c_result.setFont(font)
        self.c_result.setText("")
        self.c_result.setObjectName("c_result")
        self.c_label_2 = QtWidgets.QLabel(self.Cezarus)
        self.c_label_2.setGeometry(QtCore.QRect(0, 80, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.c_label_2.setFont(font)
        self.c_label_2.setObjectName("c_label_2")
        self.c_shift = QtWidgets.QLineEdit(self.Cezarus)
        self.c_shift.setGeometry(QtCore.QRect(260, 70, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.c_shift.setFont(font)
        self.c_shift.setText("")
        self.c_shift.setObjectName("c_shift")
        self.c_encrypt = QtWidgets.QRadioButton(self.Cezarus)
        self.c_encrypt.setGeometry(QtCore.QRect(440, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.c_encrypt.setFont(font)
        self.c_encrypt.setObjectName("c_encrypt")
        self.c_decrypt = QtWidgets.QRadioButton(self.Cezarus)
        self.c_decrypt.setGeometry(QtCore.QRect(440, 100, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.c_decrypt.setFont(font)
        self.c_decrypt.setObjectName("c_decrypt")
        self.c_copy = QtWidgets.QPushButton(self.Cezarus)
        self.c_copy.setGeometry(QtCore.QRect(0, 270, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.c_copy.setFont(font)
        self.c_copy.setObjectName("c_copy")
        self.tabWidget.addTab(self.Cezarus, "")
        self.Polybium = QtWidgets.QWidget()
        self.Polybium.setObjectName("Polybium")
        self.p_label_1 = QtWidgets.QLabel(self.Polybium)
        self.p_label_1.setGeometry(QtCore.QRect(0, 10, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.p_label_1.setFont(font)
        self.p_label_1.setObjectName("p_label_1")
        self.p_input = QtWidgets.QLineEdit(self.Polybium)
        self.p_input.setGeometry(QtCore.QRect(260, 10, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.p_input.setFont(font)
        self.p_input.setText("")
        self.p_input.setObjectName("p_input")
        self.p_label_2 = QtWidgets.QLabel(self.Polybium)
        self.p_label_2.setGeometry(QtCore.QRect(0, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.p_label_2.setFont(font)
        self.p_label_2.setObjectName("p_label_2")
        self.p_russ = QtWidgets.QRadioButton(self.Polybium)
        self.p_russ.setGeometry(QtCore.QRect(120, 70, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p_russ.setFont(font)
        self.p_russ.setObjectName("p_russ")
        self.p_a = QtWidgets.QButtonGroup(MainWindow)
        self.p_a.setObjectName("p_a")
        self.p_a.addButton(self.p_russ)
        self.p_eng = QtWidgets.QRadioButton(self.Polybium)
        self.p_eng.setGeometry(QtCore.QRect(220, 70, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p_eng.setFont(font)
        self.p_eng.setObjectName("p_eng")
        self.p_a.addButton(self.p_eng)
        self.p_label_4 = QtWidgets.QLabel(self.Polybium)
        self.p_label_4.setGeometry(QtCore.QRect(340, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.p_label_4.setFont(font)
        self.p_label_4.setObjectName("p_label_4")
        self.p_encrypt = QtWidgets.QRadioButton(self.Polybium)
        self.p_encrypt.setGeometry(QtCore.QRect(460, 70, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p_encrypt.setFont(font)
        self.p_encrypt.setObjectName("p_encrypt")
        self.p_f = QtWidgets.QButtonGroup(MainWindow)
        self.p_f.setObjectName("p_f")
        self.p_f.addButton(self.p_encrypt)
        self.p_decrypt = QtWidgets.QRadioButton(self.Polybium)
        self.p_decrypt.setGeometry(QtCore.QRect(460, 100, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p_decrypt.setFont(font)
        self.p_decrypt.setObjectName("p_decrypt")
        self.p_f.addButton(self.p_decrypt)
        self.p_num = QtWidgets.QCheckBox(self.Polybium)
        self.p_num.setGeometry(QtCore.QRect(120, 100, 87, 20))
        self.p_num.setObjectName("p_num")
        self.p_spec = QtWidgets.QCheckBox(self.Polybium)
        self.p_spec.setGeometry(QtCore.QRect(220, 100, 121, 20))
        self.p_spec.setObjectName("p_spec")
        self.p_label_3 = QtWidgets.QLabel(self.Polybium)
        self.p_label_3.setGeometry(QtCore.QRect(0, 150, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.p_label_3.setFont(font)
        self.p_label_3.setObjectName("p_label_3")
        self.p_result = QtWidgets.QLineEdit(self.Polybium)
        self.p_result.setGeometry(QtCore.QRect(260, 150, 330, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.p_result.setFont(font)
        self.p_result.setText("")
        self.p_result.setObjectName("p_result")
        self.p_button = QtWidgets.QPushButton(self.Polybium)
        self.p_button.setGeometry(QtCore.QRect(0, 220, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.p_button.setFont(font)
        self.p_button.setObjectName("p_button")
        self.p_copy = QtWidgets.QPushButton(self.Polybium)
        self.p_copy.setGeometry(QtCore.QRect(0, 270, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.p_copy.setFont(font)
        self.p_copy.setObjectName("p_copy")
        self.tabWidget.addTab(self.Polybium, "")
        self.Vigenere = QtWidgets.QWidget()
        self.Vigenere.setObjectName("Vigenere")
        self.v_label_1 = QtWidgets.QLabel(self.Vigenere)
        self.v_label_1.setGeometry(QtCore.QRect(0, 10, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.v_label_1.setFont(font)
        self.v_label_1.setObjectName("v_label_1")
        self.v_input = QtWidgets.QLineEdit(self.Vigenere)
        self.v_input.setGeometry(QtCore.QRect(260, 10, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.v_input.setFont(font)
        self.v_input.setText("")
        self.v_input.setObjectName("v_input")
        self.v_label_3 = QtWidgets.QLabel(self.Vigenere)
        self.v_label_3.setGeometry(QtCore.QRect(160, 80, 91, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.v_label_3.setFont(font)
        self.v_label_3.setObjectName("v_label_3")
        self.v_clue = QtWidgets.QLineEdit(self.Vigenere)
        self.v_clue.setGeometry(QtCore.QRect(260, 70, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.v_clue.setFont(font)
        self.v_clue.setText("")
        self.v_clue.setObjectName("v_clue")
        self.v_encrypt = QtWidgets.QRadioButton(self.Vigenere)
        self.v_encrypt.setGeometry(QtCore.QRect(440, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v_encrypt.setFont(font)
        self.v_encrypt.setObjectName("v_encrypt")
        self.v_decrypt = QtWidgets.QRadioButton(self.Vigenere)
        self.v_decrypt.setGeometry(QtCore.QRect(440, 100, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v_decrypt.setFont(font)
        self.v_decrypt.setObjectName("v_decrypt")
        self.v_label_2 = QtWidgets.QLabel(self.Vigenere)
        self.v_label_2.setGeometry(QtCore.QRect(0, 80, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.v_label_2.setFont(font)
        self.v_label_2.setObjectName("v_label_2")
        self.v_result = QtWidgets.QLineEdit(self.Vigenere)
        self.v_result.setGeometry(QtCore.QRect(0, 150, 590, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.v_result.setFont(font)
        self.v_result.setText("")
        self.v_result.setObjectName("v_result")
        self.v_button = QtWidgets.QPushButton(self.Vigenere)
        self.v_button.setGeometry(QtCore.QRect(0, 220, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.v_button.setFont(font)
        self.v_button.setObjectName("v_button")
        self.v_copy = QtWidgets.QPushButton(self.Vigenere)
        self.v_copy.setGeometry(QtCore.QRect(0, 270, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.v_copy.setFont(font)
        self.v_copy.setObjectName("v_copy")
        self.tabWidget.addTab(self.Vigenere, "")
        self.private1 = QtWidgets.QWidget()
        self.private1.setObjectName("private1")
        self.ov_label_1 = QtWidgets.QLabel(self.private1)
        self.ov_label_1.setGeometry(QtCore.QRect(0, 10, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.ov_label_1.setFont(font)
        self.ov_label_1.setObjectName("ov_label_1")
        self.ov_input = QtWidgets.QLineEdit(self.private1)
        self.ov_input.setGeometry(QtCore.QRect(260, 10, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.ov_input.setFont(font)
        self.ov_input.setText("")
        self.ov_input.setObjectName("ov_input")
        self.ov_label_2 = QtWidgets.QLabel(self.private1)
        self.ov_label_2.setGeometry(QtCore.QRect(0, 80, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.ov_label_2.setFont(font)
        self.ov_label_2.setObjectName("ov_label_2")
        self.ov_clue = QtWidgets.QLineEdit(self.private1)
        self.ov_clue.setGeometry(QtCore.QRect(260, 70, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.ov_clue.setFont(font)
        self.ov_clue.setText("")
        self.ov_clue.setObjectName("ov_clue")
        self.ov_encrypt = QtWidgets.QRadioButton(self.private1)
        self.ov_encrypt.setGeometry(QtCore.QRect(440, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ov_encrypt.setFont(font)
        self.ov_encrypt.setObjectName("ov_encrypt")
        self.ov_decrypt = QtWidgets.QRadioButton(self.private1)
        self.ov_decrypt.setGeometry(QtCore.QRect(440, 100, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ov_decrypt.setFont(font)
        self.ov_decrypt.setObjectName("ov_decrypt")
        self.ov_label_3 = QtWidgets.QLabel(self.private1)
        self.ov_label_3.setGeometry(QtCore.QRect(0, 150, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.ov_label_3.setFont(font)
        self.ov_label_3.setObjectName("ov_label_3")
        self.ov_result = QtWidgets.QLineEdit(self.private1)
        self.ov_result.setGeometry(QtCore.QRect(260, 150, 330, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.ov_result.setFont(font)
        self.ov_result.setText("")
        self.ov_result.setObjectName("ov_result")
        self.ov_button = QtWidgets.QPushButton(self.private1)
        self.ov_button.setGeometry(QtCore.QRect(0, 220, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.ov_button.setFont(font)
        self.ov_button.setObjectName("ov_button")
        self.ov_copy = QtWidgets.QPushButton(self.private1)
        self.ov_copy.setGeometry(QtCore.QRect(0, 270, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.ov_copy.setFont(font)
        self.ov_copy.setObjectName("ov_copy")
        self.tabWidget.addTab(self.private1, "")
        self.private2 = QtWidgets.QWidget()
        self.private2.setObjectName("private2")
        self.os_label_1 = QtWidgets.QLabel(self.private2)
        self.os_label_1.setGeometry(QtCore.QRect(0, 10, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.os_label_1.setFont(font)
        self.os_label_1.setObjectName("os_label_1")
        self.os_input = QtWidgets.QLineEdit(self.private2)
        self.os_input.setGeometry(QtCore.QRect(270, 10, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.os_input.setFont(font)
        self.os_input.setText("")
        self.os_input.setObjectName("os_input")
        self.os_label_4 = QtWidgets.QLabel(self.private2)
        self.os_label_4.setGeometry(QtCore.QRect(270, 60, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.os_label_4.setFont(font)
        self.os_label_4.setObjectName("os_label_4")
        self.os_clue = QtWidgets.QLineEdit(self.private2)
        self.os_clue.setGeometry(QtCore.QRect(270, 100, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.os_clue.setFont(font)
        self.os_clue.setText("")
        self.os_clue.setObjectName("os_clue")
        self.os_encrypt = QtWidgets.QRadioButton(self.private2)
        self.os_encrypt.setGeometry(QtCore.QRect(130, 100, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.os_encrypt.setFont(font)
        self.os_encrypt.setObjectName("os_encrypt")
        self.k2_f = QtWidgets.QButtonGroup(MainWindow)
        self.k2_f.setObjectName("k2_f")
        self.k2_f.addButton(self.os_encrypt)
        self.os_decrypt = QtWidgets.QRadioButton(self.private2)
        self.os_decrypt.setGeometry(QtCore.QRect(130, 130, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.os_decrypt.setFont(font)
        self.os_decrypt.setObjectName("os_decrypt")
        self.k2_f.addButton(self.os_decrypt)
        self.os_label_3 = QtWidgets.QLabel(self.private2)
        self.os_label_3.setGeometry(QtCore.QRect(130, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.os_label_3.setFont(font)
        self.os_label_3.setObjectName("os_label_3")
        self.os_label_2 = QtWidgets.QLabel(self.private2)
        self.os_label_2.setGeometry(QtCore.QRect(0, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.os_label_2.setFont(font)
        self.os_label_2.setObjectName("os_label_2")
        self.os_russ = QtWidgets.QRadioButton(self.private2)
        self.os_russ.setGeometry(QtCore.QRect(0, 110, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.os_russ.setFont(font)
        self.os_russ.setObjectName("os_russ")
        self.k2_a = QtWidgets.QButtonGroup(MainWindow)
        self.k2_a.setObjectName("k2_a")
        self.k2_a.addButton(self.os_russ)
        self.os_eng = QtWidgets.QRadioButton(self.private2)
        self.os_eng.setGeometry(QtCore.QRect(0, 130, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.os_eng.setFont(font)
        self.os_eng.setObjectName("os_eng")
        self.k2_a.addButton(self.os_eng)
        self.os_label_5 = QtWidgets.QLabel(self.private2)
        self.os_label_5.setGeometry(QtCore.QRect(0, 150, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.os_label_5.setFont(font)
        self.os_label_5.setObjectName("os_label_5")
        self.os_button = QtWidgets.QPushButton(self.private2)
        self.os_button.setGeometry(QtCore.QRect(0, 250, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.os_button.setFont(font)
        self.os_button.setObjectName("os_button")
        self.os_copy = QtWidgets.QPushButton(self.private2)
        self.os_copy.setGeometry(QtCore.QRect(0, 300, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.os_copy.setFont(font)
        self.os_copy.setObjectName("os_copy")
        self.os_result = QtWidgets.QLineEdit(self.private2)
        self.os_result.setGeometry(QtCore.QRect(0, 190, 590, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.os_result.setFont(font)
        self.os_result.setText("")
        self.os_result.setObjectName("os_result")
        self.tabWidget.addTab(self.private2, "")
        self.private3 = QtWidgets.QWidget()
        self.private3.setObjectName("private3")
        self.od_label_1 = QtWidgets.QLabel(self.private3)
        self.od_label_1.setGeometry(QtCore.QRect(0, 10, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.od_label_1.setFont(font)
        self.od_label_1.setObjectName("od_label_1")
        self.od_input = QtWidgets.QLineEdit(self.private3)
        self.od_input.setGeometry(QtCore.QRect(260, 10, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.od_input.setFont(font)
        self.od_input.setText("")
        self.od_input.setObjectName("od_input")
        self.od_load_image = QtWidgets.QPushButton(self.private3)
        self.od_load_image.setGeometry(QtCore.QRect(0, 70, 260, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.od_load_image.setFont(font)
        self.od_load_image.setObjectName("od_load_image")
        self.od_label_2 = QtWidgets.QLabel(self.private3)
        self.od_label_2.setGeometry(QtCore.QRect(300, 60, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.od_label_2.setFont(font)
        self.od_label_2.setObjectName("od_label_2")
        self.od_encrypt = QtWidgets.QRadioButton(self.private3)
        self.od_encrypt.setGeometry(QtCore.QRect(450, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.od_encrypt.setFont(font)
        self.od_encrypt.setObjectName("od_encrypt")
        self.od_decrypt = QtWidgets.QRadioButton(self.private3)
        self.od_decrypt.setGeometry(QtCore.QRect(450, 110, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.od_decrypt.setFont(font)
        self.od_decrypt.setObjectName("od_decrypt")
        self.od_result = QtWidgets.QLineEdit(self.private3)
        self.od_result.setGeometry(QtCore.QRect(260, 160, 330, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(14)
        self.od_result.setFont(font)
        self.od_result.setText("")
        self.od_result.setObjectName("od_result")
        self.od_button = QtWidgets.QPushButton(self.private3)
        self.od_button.setGeometry(QtCore.QRect(0, 230, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.od_button.setFont(font)
        self.od_button.setObjectName("od_button")
        self.od_label_3 = QtWidgets.QLabel(self.private3)
        self.od_label_3.setGeometry(QtCore.QRect(0, 160, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(24)
        self.od_label_3.setFont(font)
        self.od_label_3.setObjectName("od_label_3")
        self.od_copy = QtWidgets.QPushButton(self.private3)
        self.od_copy.setGeometry(QtCore.QRect(0, 280, 591, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(18)
        self.od_copy.setFont(font)
        self.od_copy.setObjectName("od_copy")
        self.tabWidget.addTab(self.private3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приложение-шифровальщик"))
        self.c_button.setText(_translate("MainWindow", "Выполнить"))
        self.c_label_1.setText(_translate("MainWindow", "Исходные данные:"))
        self.c_label_3.setText(_translate("MainWindow", "Результат:"))
        self.c_label_2.setText(_translate("MainWindow", "Сдвиг:"))
        self.c_encrypt.setText(_translate("MainWindow", "Шифрование"))
        self.c_decrypt.setText(_translate("MainWindow", "Дешифрование"))
        self.c_copy.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cezarus), _translate("MainWindow", "Шифр Цезаря"))
        self.p_label_1.setText(_translate("MainWindow", "Исходные данные:"))
        self.p_label_2.setText(_translate("MainWindow", "Алфавит:"))
        self.p_russ.setText(_translate("MainWindow", "Кириллица"))
        self.p_eng.setText(_translate("MainWindow", "Латиница"))
        self.p_label_4.setText(_translate("MainWindow", "Функция:"))
        self.p_encrypt.setText(_translate("MainWindow", "Шифрование"))
        self.p_decrypt.setText(_translate("MainWindow", "Дешифрование"))
        self.p_num.setText(_translate("MainWindow", "Цифры"))
        self.p_spec.setText(_translate("MainWindow", "Спецсимволы"))
        self.p_label_3.setText(_translate("MainWindow", "Результат:"))
        self.p_button.setText(_translate("MainWindow", "Выполнить"))
        self.p_copy.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Polybium), _translate("MainWindow", "Шифр Полибия"))
        self.v_label_1.setText(_translate("MainWindow", "Исходные данные:"))
        self.v_label_3.setText(_translate("MainWindow", "Ключ:"))
        self.v_encrypt.setText(_translate("MainWindow", "Шифрование"))
        self.v_decrypt.setText(_translate("MainWindow", "Дешифрование"))
        self.v_label_2.setText(_translate("MainWindow", "Результат:"))
        self.v_button.setText(_translate("MainWindow", "Выполнить"))
        self.v_copy.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vigenere), _translate("MainWindow", "Шифр Виженера"))
        self.ov_label_1.setText(_translate("MainWindow", "Исходные данные:"))
        self.ov_label_2.setText(_translate("MainWindow", "Ключг:"))
        self.ov_encrypt.setText(_translate("MainWindow", "Шифрование"))
        self.ov_decrypt.setText(_translate("MainWindow", "Дешифрование"))
        self.ov_label_3.setText(_translate("MainWindow", "Результат:"))
        self.ov_button.setText(_translate("MainWindow", "Выполнить"))
        self.ov_copy.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.private1), _translate("MainWindow", "Кастом 1"))
        self.os_label_1.setText(_translate("MainWindow", "Исходные данные:"))
        self.os_label_4.setText(_translate("MainWindow", "Ключ:"))
        self.os_encrypt.setText(_translate("MainWindow", "Шифрование"))
        self.os_decrypt.setText(_translate("MainWindow", "Дешифрование"))
        self.os_label_3.setText(_translate("MainWindow", "Функция:"))
        self.os_label_2.setText(_translate("MainWindow", "Алфавит:"))
        self.os_russ.setText(_translate("MainWindow", "Кириллица"))
        self.os_eng.setText(_translate("MainWindow", "Латиница"))
        self.os_label_5.setText(_translate("MainWindow", "Результат:"))
        self.os_button.setText(_translate("MainWindow", "Выполнить"))
        self.os_copy.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.private2), _translate("MainWindow", "Кастом 2"))
        self.od_label_1.setText(_translate("MainWindow", "Исходные данные:"))
        self.od_load_image.setText(_translate("MainWindow", "Загрузить изображение"))
        self.od_label_2.setText(_translate("MainWindow", "Функция:"))
        self.od_encrypt.setText(_translate("MainWindow", "Шифрование"))
        self.od_decrypt.setText(_translate("MainWindow", "Дешифрование"))
        self.od_button.setText(_translate("MainWindow", "Выполнить"))
        self.od_label_3.setText(_translate("MainWindow", "Результат:"))
        self.od_copy.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.private3), _translate("MainWindow", "Кастом 3"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.Picture_crypt = od_encryption.Picture_encrypt()
        self.Ciphers_class = Ciphers()
        super().__init__()
        self.setupUi(self)
        self.connect_to()

    def print_message(self, text):
        QStatusBar.showMessage(self.statusbar, text)

    def c_to_clipboard(self):
        pyperclip.copy(self.c_result.text())

    def p_to_clipboard(self):
        pyperclip.copy(self.p_result.text())

    def v_to_clipboard(self):
        pyperclip.copy(self.v_result.text())

    def ov_to_clipboard(self):
         pyperclip.copy(self.ov_result.text())
    
    def os_to_clipboard(self):
         pyperclip.copy(self.os_result.text())

    def p_alpha_changed(self):
        n = ""
        s = ""
        if self.p_eng.isChecked():
            alpha = "abcdefghijklmnopqrstuvwxyz"
        else:
            alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        if self.p_num.isChecked():
            n = "0123456789"

        if self.p_spec.isChecked():
            s = "()[]{}.?!@#$%^&*_+-=/±<>"

        alpha += n
        alpha += s
        self.Ciphers_class.alphabet_polybium = alpha

    def os_alpha_changed(self):
        n = ""
        s = ""
        if self.os_eng.isChecked():
            alpha = "abcdefghijklmnopqrstuvwxyz"
        else:
            alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.Ciphers_class.alphabet_os = alpha

    def connect_to(self):
        self.c_button.clicked.connect(self.cezarus_work)
        self.c_copy.clicked.connect(self.c_to_clipboard)
        self.c_encrypt.setChecked(True)
        self.c_encrypt.toggled.connect(self.c_state_changed)

        self.p_button.clicked.connect(self.polybium_work)
        self.p_copy.clicked.connect(self.p_to_clipboard)
        self.p_encrypt.setChecked(True)
        self.p_eng.setChecked(True)
        self.p_num.setChecked(True)
        self.p_eng.toggled.connect(self.p_alpha_changed)
        self.p_num.toggled.connect(self.p_alpha_changed)
        self.p_spec.toggled.connect(self.p_alpha_changed)
        self.p_encrypt.toggled.connect(self.p_state_changed)

        self.v_button.clicked.connect(self.vigenere_work)
        self.v_copy.clicked.connect(self.v_to_clipboard)
        self.v_encrypt.setChecked(True)
        self.v_encrypt.toggled.connect(self.v_state_changed)

        self.ov_button.clicked.connect(self.ov_work)
        self.ov_copy.clicked.connect(self.ov_to_clipboard)
        self.ov_encrypt.setChecked(True)
        self.ov_encrypt.toggled.connect(self.ov_state_changed)
        self.os_button.clicked.connect(self.os_work)
        self.os_copy.clicked.connect(self.os_to_clipboard)
        self.os_encrypt.setChecked(True)
        self.os_eng.setChecked(True)
        self.os_eng.toggled.connect(self.os_alpha_changed)
        self.os_encrypt.toggled.connect(self.os_state_changed)

        self.od_load_image.clicked.connect(self.load_image)
        self.od_button.clicked.connect(self.od_work)
        self.od_encrypt.setChecked(True)
        self.od_encrypt.toggled.connect(self.od_state_changed)

    def c_state_changed(self):
        self.c_input.setText(self.c_result.text())
        self.c_shift.setText(str(int(self.c_shift.text()) * -1))
        self.c_result.setText("")

    def p_state_changed(self):
        self.p_input.setText(self.p_result.text())
        self.p_result.setText("")

    def v_state_changed(self):
        self.v_input.setText(self.v_result.text())
        self.v_result.setText("")

    def ov_state_changed(self):
        self.ov_input.setText(self.ov_result.text())
        self.ov_result.setText("")

    def os_state_changed(self):
        self.os_input.setText(self.os_result.text())
        self.os_result.setText("")

    def od_state_changed(self):
        self.od_input.setText(self.od_result.text())
        self.od_result.setText("")

    def cezarus_work(self):
        self.print_message("")
        text = self.c_input.text()
        shift = self.c_shift.text()
        if shift.isdigit() or shift[0] == "-":
            shift = int(shift)
        else:
            self.print_message("Ключ должен быть типа int!")
            shift = 0
            self.c_shift.setText("0")
        result = self.Ciphers_class.Cezarus_cipher(text, shift)
        self.c_result.setText(result)


    def polybium_work(self):
        self.print_message("")
        if self.p_input.text()[0] in self.Ciphers_class.alphabet_os:
            if self.p_encrypt.isChecked():
                text = self.p_input.text()
                result = self.Ciphers_class.Polybium_cipher_encrypt(text, 7)
                self.p_result.setText(result)
            else:
                text = self.p_input.text()
                result = self.Ciphers_class.Polybium_cipher_decrypt(text, 7)
                self.p_result.setText(result)
        else:
            self.print_message("Выбран неверный алфавит!")

    def vigenere_work(self):
        if self.v_encrypt.isChecked():
            text = self.v_input.text()
            key = self.v_clue.text()
            result = self.Ciphers_class.Vigenere_cipher_encrypt(text, key)
            self.v_result.setText(result)
        else:
            text = self.v_input.text()
            key = self.v_clue.text()
            result = self.Ciphers_class.Vigenere_cipher_decrypt(text, key)
            self.v_result.setText(result)

    def ov_work(self):
        if self.ov_encrypt.isChecked():
            text = self.ov_input.text()
            key = self.ov_clue.text()
            result = self.Ciphers_class.private_cipher_encrypt(text, key)
            self.ov_clue.setText(result[1])
            self.ov_result.setText(result[0])
        else:
            text = self.ov_input.text()
            key = self.ov_clue.text()
            result = self.Ciphers_class.private_cipher_decrypt(text, key)
            self.ov_result.setText(result)
            self.ov_clue.setText("")

    def os_work(self):
        if self.os_encrypt.isChecked():
            text = self.os_input.text()
            key = int(self.os_clue.text())
            result = self.Ciphers_class.os_encode(text, key)
            self.os_result.setText(result)
        else:
            text = self.os_input.text()
            key = int(self.os_clue.text())
            result = self.Ciphers_class.os_decode(text, key)
            self.os_result.setText(result)

    def load_image(self):
        wb_patch = QFileDialog.getOpenFileName()[0]
        self.Picture_crypt.take_image(wb_patch)

    def od_work(self):
        if self.od_decrypt.isChecked():
            text = self.od_input.text()
            result = self.Picture_crypt.image_crypt(text, action="encrypt")
            self.od_result.setText(result)
        else:
            text = self.od_input.text()
            result = self.Picture_crypt.image_crypt(text, action="decrypt")
            self.od_result.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
