import sys
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from Data_Base import Func_DataBase
from Setting_Programm import Words


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 131)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/loock.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setMinimumSize(QtCore.QSize(317, 131))
        Dialog.setMaximumSize(QtCore.QSize(317, 131))
        self.btn_set = QtWidgets.QPushButton(Dialog)
        self.btn_set.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.btn_set.setAutoDefault(False)
        self.btn_set.setDefault(True)
        self.btn_set.setObjectName("btn_set")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 281, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_enter_password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_enter_password.setFont(font)
        self.txt_enter_password.setObjectName("txt_enter_password")
        self.gridLayout.addWidget(self.txt_enter_password, 0, 0, 1, 1)
        self.input_enter_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_enter_password.setMaxLength(16)
        self.input_enter_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_enter_password.setObjectName("input_enter_password")
        self.gridLayout.addWidget(self.input_enter_password, 0, 1, 1, 1)
        self.txt_enter_again_password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_enter_again_password.setFont(font)
        self.txt_enter_again_password.setObjectName("txt_enter_again_password")
        self.gridLayout.addWidget(self.txt_enter_again_password, 1, 0, 1, 1)
        self.input_enter_again_password = QtWidgets.QLineEdit(
            self.layoutWidget)
        self.input_enter_again_password.setMaxLength(16)
        self.input_enter_again_password.setEchoMode(
            QtWidgets.QLineEdit.Password)
        self.input_enter_again_password.setObjectName(
            "input_enter_again_password")
        self.gridLayout.addWidget(self.input_enter_again_password, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # ================== Coding ==================
        Func_DataBase.set_setting(Dialog)

    def set_password(self):
        self.password = self.input_enter_password.text()
        self.again_password = self.input_enter_again_password.text()

        if self.password != self.again_password:
            self.win_error = QtWidgets.QMessageBox()
            self.win_error.setWindowTitle("ERROR")
            self.win_error.setText("Password and again password are not like")
            self.win_error.show()
            return False
        elif self.password == "":
            self.win_error = QtWidgets.QMessageBox()
            self.win_error.setWindowTitle("ERROR")
            self.win_error.setText("You should not let the None password")
            self.win_error.show()
            return False

        password_hashed = hashlib.sha224()
        password_hashed.update(self.password.encode("utf-8"))

        Func_DataBase.Data_Base_Password(password_hashed.hexdigest())

        return True

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", Words.translate_words(Words.Set_password)))
        self.btn_set.setText(_translate(
            "Dialog", Words.translate_words(Words.set_)))
        self.btn_cancel.setText(_translate(
            "Dialog", Words.translate_words(Words.Cancel)))
        self.txt_enter_password.setText(_translate(
            "Dialog", Words.translate_words(Words.Enter_password)))
        self.txt_enter_again_password.setText(
            _translate("Dialog", Words.translate_words(Words.Enter_again_password)))
