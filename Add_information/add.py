from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import Data_Base.Func_DataBase as Func_DataBase
from Setting_Programm import Words
import json

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 335)
        Dialog.setMinimumSize(553, 335)
        Dialog.setMaximumSize(553, 335)
        Dialog.setMinimumSize(QtCore.QSize(55, 335))
        Dialog.setMaximumSize(QtCore.QSize(555, 335))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/Add.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 531, 311))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_8 = QtWidgets.QFrame(self.widget)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 2, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 5, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_amount = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_amount.setFont(font)
        self.txt_amount.setObjectName("txt_amount")
        self.horizontalLayout.addWidget(self.txt_amount)
        self.input_amount = QtWidgets.QLineEdit(self.widget)
        self.input_amount.setObjectName("input_amount")
        self.horizontalLayout.addWidget(self.input_amount)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txt_description = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txt_description.setFont(font)
        self.txt_description.setObjectName("txt_description")
        self.horizontalLayout_6.addWidget(self.txt_description)
        self.input_description = QtWidgets.QTextEdit(self.widget)
        self.input_description.setObjectName("input_description")
        self.horizontalLayout_6.addWidget(self.input_description)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 3)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txt_date = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_date.setFont(font)
        self.txt_date.setObjectName("txt_date")
        self.horizontalLayout_5.addWidget(self.txt_date)
        self.input_date = QtWidgets.QDateEdit(self.widget)
        self.input_date.setObjectName("input_date")
        self.horizontalLayout_5.addWidget(self.input_date)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txt_fromorto = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_fromorto.setFont(font)
        self.txt_fromorto.setObjectName("txt_fromorto")
        self.horizontalLayout_4.addWidget(self.txt_fromorto)
        self.input_fromorto = QtWidgets.QLineEdit(self.widget)
        self.input_fromorto.setText("")
        self.input_fromorto.setObjectName("input_fromorto")
        self.horizontalLayout_4.addWidget(self.input_fromorto)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.txt_helper = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.txt_helper.setFont(font)
        self.txt_helper.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txt_helper.setLineWidth(2)
        self.txt_helper.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_helper.setObjectName("txt_helper")
        self.gridLayout.addWidget(self.txt_helper, 0, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txt_type = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_type.setFont(font)
        self.txt_type.setObjectName("txt_type")
        self.horizontalLayout_3.addWidget(self.txt_type)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rdb_payment = QtWidgets.QRadioButton(self.widget)
        self.rdb_payment.setObjectName("rdb_payment")
        self.horizontalLayout_2.addWidget(self.rdb_payment)
        self.rdb_received = QtWidgets.QRadioButton(self.widget)
        self.rdb_received.setObjectName("rdb_received")
        self.horizontalLayout_2.addWidget(self.rdb_received)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 3, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.btn_ok = QtWidgets.QPushButton(self.widget)
        self.btn_ok.setCheckable(False)
        self.btn_ok.setAutoRepeat(False)
        self.btn_ok.setAutoDefault(False)
        self.btn_ok.setDefault(True)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout_2.addWidget(self.btn_ok, 1, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # ================== Coding ==================
        try:
            with open("setting.json", 'r') as File:
                File = json.load(File)
                if File["language_Programm"] != "English":
                    self.widget.setLayoutDirection(QtCore.Qt.RightToLeft)  
        except:
            pass
        
        Func_DataBase.set_setting(Dialog)

    def check_amount(self):
        # Check for in line_edit just enter number no Charcter
        amount = self.input_amount.text()
        try:
            float(amount)
            return self.input_amount.text()
        except:
            return False

    def check_rdbs(self):
        # Check select one from received and rdb_payment
        if self.rdb_received.isChecked():
            return "Received"
        elif self.rdb_payment.isChecked():
            return "Payment"
        else:
            return False

    def check_Enter_from_or_to(self):
        # Check for Enter text in From/to
        if self.input_fromorto.text() == "":
            return False
        else:
            return self.input_fromorto.text()

    def command_btn_ok(self):
        Kes_for_information = ["amount", "Type Amount",
                               "From/To", "Date", "Description"]
        Values_for_information = []
        # ------------- Check True Enter Amount -----------
        if self.check_amount():
            Values_for_information.append(self.input_amount.text())
        else:
            self.win_error_amount = QtWidgets.QMessageBox()
            self.win_error_amount.setText(Words.translate_words(Words.M_Enter_amount))
            self.win_error_amount.show()
            return None
        # ------------- Check Enter recived or paymount ---------------
        if self.check_rdbs():
            Values_for_information.append(self.check_rdbs())
        else:
            self.win_error_amount = QtWidgets.QMessageBox()
            self.win_error_amount.setText(Words.translate_words(Words.M_Enter_type))
            self.win_error_amount.show()
            return None
        # ------------------- check Enter From Or To -----------------
        if self.check_Enter_from_or_to():
            Values_for_information.append(self.check_Enter_from_or_to())
        else:
            self.win_error_amount = QtWidgets.QMessageBox()
            self.win_error_amount.setText(Words.translate_words(Words.M_Enter_from_to))
            self.win_error_amount.show()
            return None
        # -------------- Get Date -----------------
        Values_for_information.append(self.input_date.text())
        # ---------- Get Descripton ---------------
        if self.input_description.toPlainText() == "":
            Values_for_information.append("Null")
        else:
            Values_for_information.append(self.input_description.toPlainText())

        # This code conver two lists to one dict
        information_for_add = dict(
            zip(Kes_for_information, Values_for_information))

        # ------------- Work With Database -------------------
        Func_DataBase.Create_DataBase()
        Func_DataBase.Add_in_DataBase(0, information_for_add['amount'], information_for_add['Type Amount'],
                                      information_for_add['From/To'], information_for_add['Date'], information_for_add['Description'])
        Func_DataBase.Search_in_DataBase()
        # ----------------------------------------------------
        return True

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", Words.translate_words(Words.Add)))
        self.txt_amount.setText(_translate(
            "Dialog", Words.translate_words(Words.Amount)))
        self.input_amount.setPlaceholderText(_translate(
            "Dialog", Words.translate_words(Words.Enter_amount)))
        self.txt_description.setText(_translate(
            "Dialog", Words.translate_words(Words.Description)))
        self.txt_date.setText(_translate(
            "Dialog", Words.translate_words(Words.Date)))
        self.txt_fromorto.setText(_translate(
            "Dialog", Words.translate_words(Words.From_To)))
        self.input_fromorto.setPlaceholderText(_translate(
            "Dialog", Words.translate_words(Words.From_or_To)))
        self.txt_helper.setText(_translate("Dialog", Words.translate_words(
            Words.Please_enter_information_and_select_ok)))
        self.txt_type.setText(_translate(
            "Dialog", Words.translate_words(Words.Type)))
        self.rdb_payment.setText(_translate(
            "Dialog", Words.translate_words(Words.Payment)))
        self.rdb_received.setText(_translate(
            "Dialog", Words.translate_words(Words.Received)))
        self.btn_ok.setText(_translate(
            "Dialog", Words.translate_words(Words.Ok)))
        self.btn_cancel.setText(_translate(
            "Dialog", Words.translate_words(Words.Cancel)))
