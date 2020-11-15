import sys
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Setting_app import Words
from Data_Base import Func_DataBase



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(219, 127)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Icons/loock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.btn_unloock = QtWidgets.QPushButton(Dialog)
        self.btn_unloock.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.btn_unloock.setAutoDefault(False)
        self.btn_unloock.setDefault(True)
        self.btn_unloock.setObjectName("btn_unloock")
        self.btn_exit = QtWidgets.QPushButton(Dialog)
        self.btn_exit.setGeometry(QtCore.QRect(120, 80, 75, 23))
        self.btn_exit.setAutoDefault(False)
        self.btn_exit.setObjectName("btn_exit")
        self.input_password = QtWidgets.QLineEdit(Dialog)
        self.input_password.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.input_password.setObjectName("input_password")
        self.btn_forgget_password = QtWidgets.QPushButton(Dialog)
        self.btn_forgget_password.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.btn_forgget_password.setAutoDefault(False)
        self.btn_forgget_password.setFlat(True)
        self.btn_forgget_password.setObjectName("btn_forgget_password")
        self.btn_unloock.raise_()
        self.btn_exit.raise_()
        self.btn_forgget_password.raise_()
        self.input_password.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # ================== Coding ==================
        Func_DataBase.set_setting(Dialog)
        self.btn_forgget_password.clicked.connect(self.forget_password)

    def check_passsword(self):
        self.password_entered = self.input_password.text()

        password_hashed = hashlib.sha224()
        password_hashed.update(self.password_entered.encode("utf-8"))

        try:
            self.password = Func_DataBase.get_password_in_database()
        except:
            pass

        if password_hashed.hexdigest() == self.password:
            return True
        else:
            return False

    def check_for_unlook(self):
        if self.check_passsword():
            return True
        else:
            self.win_error = QtWidgets.QMessageBox()
            self.win_error.setWindowTitle("ERROR")
            self.win_error.setText("Password is Wrong")
            self.win_error.show()
            self.input_password.clear()
            return False

    def forget_password(self):
        self.win_forget = QtWidgets.QMessageBox()
        self.win_forget.setWindowTitle("Forget Password")
        self.win_forget.setText(
            "If You Forget Your Password \nMust Clear All Data\n\nShud Delate File main_information.db")
        
        # I can't create button yes and no for if enter yes Delate File main_information.db

        # self.win_forget.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)

        # def status_button():
        #     if self.win_forget == self.win_forget.Yes:
        #         print("Yes")
        #     elif self.win_forget == self.win_forget.No:
        #         print("no")
        #     else:
        #         print(self.win_forget.buttonClicked)

        # self.win_forget.buttonClicked.connect(status_button)

        self.win_forget.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", Words.translate_words(Words.Enter_password)))
        self.btn_unloock.setText(_translate(
            "Dialog", Words.translate_words(Words.Unloock)))
        self.btn_exit.setText(_translate(
            "Dialog", Words.translate_words(Words.Exit)))
        self.input_password.setPlaceholderText(
            _translate("Dialog", Words.translate_words(Words.Enter_your_password)))
        self.btn_forgget_password.setText(
            _translate("Dialog", Words.translate_words(Words.Forget_password)))
