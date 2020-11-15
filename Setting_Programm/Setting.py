import json
from PyQt5 import QtCore, QtGui, QtWidgets
from Data_Base import Func_DataBase
from Setting_Programm import Words
from Windows_passwords.set_password import Ui_Dialog as page_set_password
from Windows_passwords.page_unloock import Ui_Dialog as page_unlook_password


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 255)
        Dialog.setMinimumSize(447, 255)
        Dialog.setMaximumSize(447, 255)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Icons/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 431, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 2, 401, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txt_languge = QtWidgets.QLabel(self.layoutWidget)
        self.txt_languge.setObjectName("txt_languge")
        self.horizontalLayout_3.addWidget(self.txt_languge)
        self.combo_languge = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_languge.setObjectName("combo_languge")
        self.combo_languge.addItem("")
        self.combo_languge.addItem("")
        self.combo_languge.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_languge)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_type_font = QtWidgets.QLabel(self.layoutWidget)
        self.txt_type_font.setObjectName("txt_type_font")
        self.horizontalLayout_2.addWidget(self.txt_type_font)
        self.combo_font = QtWidgets.QFontComboBox(self.layoutWidget)
        self.combo_font.setObjectName("combo_font")
        self.horizontalLayout_2.addWidget(self.combo_font)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_size_font = QtWidgets.QLabel(self.layoutWidget)
        self.txt_size_font.setObjectName("txt_size_font")
        self.horizontalLayout.addWidget(self.txt_size_font)
        self.input_num = QtWidgets.QSpinBox(self.layoutWidget)
        self.input_num.setWrapping(False)
        self.input_num.setFrame(True)
        self.input_num.setMaximum(14)
        self.input_num.setMinimum(6)
        self.input_num.setProperty("value", 8)
        self.input_num.setObjectName("input_num")
        self.horizontalLayout.addWidget(self.input_num)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.rdb_dark = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_dark.setObjectName("rdb_dark")
        self.horizontalLayout_4.addWidget(self.rdb_dark)
        self.rdb_light = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_light.setChecked(True)
        self.rdb_light.setObjectName("rdb_light")
        self.horizontalLayout_4.addWidget(self.rdb_light)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_reset_information = QtWidgets.QPushButton(self.tab_2)
        self.btn_reset_information.setGeometry(QtCore.QRect(10, 110, 121, 41))
        self.btn_reset_information.setAutoDefault(False)
        self.btn_reset_information.setObjectName("btn_reset_information")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 381, 81))
        self.groupBox.setObjectName("groupBox")
        self.btn_change_password = QtWidgets.QPushButton(self.groupBox)
        self.btn_change_password.setGeometry(QtCore.QRect(250, 30, 111, 41))
        self.btn_change_password.setAutoDefault(False)
        self.btn_change_password.setObjectName("btn_change_password")
        self.btn_disaable_password = QtWidgets.QPushButton(self.groupBox)
        # self.btn_disaable_password.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.btn_disaable_password.setGeometry(QtCore.QRect(130, 30, 111, 41))
        self.btn_disaable_password.setAutoDefault(False)
        self.btn_disaable_password.setObjectName("btn_disaable_password")
        self.btn_enable_password = QtWidgets.QPushButton(self.groupBox)
        self.btn_enable_password.setGeometry(QtCore.QRect(10, 30, 111, 41))
        self.btn_enable_password.setAutoDefault(False)
        self.btn_enable_password.setObjectName("btn_enable_password")
        self.btn_change_password.raise_()
        self.btn_disaable_password.raise_()
        self.btn_enable_password.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(170, 210, 81, 31))
        self.btn_save.setAutoDefault(False)
        self.btn_save.setDefault(True)
        self.btn_save.setObjectName("btn_save")
        self.btn_rest_setting = QtWidgets.QPushButton(Dialog)
        self.btn_rest_setting.setGeometry(QtCore.QRect(10, 210, 151, 31))
        self.btn_rest_setting.setAutoDefault(False)
        self.btn_rest_setting.setObjectName("btn_rest_setting")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(350, 210, 75, 30))
        self.btn_close.setAutoDefault(False)
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btn_save, self.btn_rest_setting)
        Dialog.setTabOrder(self.btn_rest_setting, self.btn_close)
        Dialog.setTabOrder(self.btn_close, self.combo_font)
        Dialog.setTabOrder(self.combo_font, self.combo_languge)
        Dialog.setTabOrder(self.combo_languge, self.btn_reset_information)
        Dialog.setTabOrder(self.btn_reset_information, self.input_num)
        Dialog.setTabOrder(self.input_num, self.tabWidget)
        # ================== Coding ==================
        try:
            with open("setting.json", 'r') as File:
                File = json.load(File)
                if File["language_Programm"] != "English":
                    self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        except:
            pass

        Func_DataBase.set_setting(Dialog)

        # Try for if not exist file setting.json
        try:
            self.set_setting()
        except:
            self.reset_setting()
            self.command_save()

        try:
            Func_DataBase.get_password_in_database()
            self.status_password = True
        except:
            self.status_password = False

        self.btn_save.clicked.connect(self.command_save)
        self.btn_rest_setting.clicked.connect(self.reset_setting)

        self.btn_enable_password.clicked.connect(self.enble_password)
        self.btn_disaable_password.clicked.connect(self.disable_password)
        self.btn_change_password.clicked.connect(self.change_password)
        self.btn_reset_information.clicked.connect(self.reset_information)

        if self.status_password:
            self.btn_enable_password.setEnabled(False)
            self.btn_change_password.setEnabled(True)
            self.btn_disaable_password.setEnabled(True)
        elif not self.status_password:
            self.btn_enable_password.setDisabled(False)
            self.btn_change_password.setDisabled(True)
            self.btn_disaable_password.setDisabled(True)

    def convert_information_setting_to_json(self):
        if self.rdb_light.isChecked():
            self.them = "light"
        else:
            self.them = "dark"

        settings_setting = {"language_Programm": self.combo_languge.currentText(), "type_font": self.combo_font.currentText(),
                            "size_font": self.input_num.text(), "them": self.them}
        json_file_setting = json.dumps(settings_setting)
        with open("setting.json", "w") as File:
            File.write(json_file_setting)

    def set_setting(self):
        with open("setting.json", "r") as File:
            setting = json.load(File)
            self.combo_languge.setCurrentText(setting["language_Programm"])
            self.combo_font.setCurrentText(setting["type_font"])
            self.input_num.setValue(int(setting["size_font"]))

            if setting["them"] == "light":
                self.rdb_light.setChecked(True)
            else:
                self.rdb_dark.setChecked(True)

    def enble_password(self):
        # ------------- open Diolog Set password------------
        dialog = QtWidgets.QDialog()
        dialog.ui = page_set_password()
        dialog.ui.setupUi(dialog)

        def set_password():
            if dialog.ui.set_password():
                self.btn_enable_password.setDisabled(True)
                self.btn_change_password.setDisabled(False)
                self.btn_disaable_password.setDisabled(False)

                dialog.close()

                self.status_password = True

        dialog.ui.btn_set.clicked.connect(set_password)
        dialog.ui.btn_cancel.clicked.connect(dialog.close)

        dialog.exec_()
        # ------------- ---------- ------------

    def disable_password(self):
        # ------------- open Diolog Unlook Password------------
        dialog = QtWidgets.QDialog()
        dialog.ui = page_unlook_password()
        dialog.ui.setupUi(dialog)

        def unlook():
            if dialog.ui.check_for_unlook():
                self.btn_enable_password.setDisabled(False)
                self.btn_change_password.setDisabled(True)
                self.btn_disaable_password.setDisabled(True)

                Func_DataBase.delate_password()
                dialog.close()

                self.status_password = False

        dialog.ui.btn_unloock.clicked.connect(unlook)
        dialog.ui.btn_exit.clicked.connect(dialog.close)

        dialog.exec_()
        # ------------- ---------- ------------

    def change_password(self):
        def set_for_change_password():
            dialog = QtWidgets.QDialog()
            dialog.ui = page_set_password()
            dialog.ui.setupUi(dialog)

            def set_password():
                if dialog.ui.set_password():
                    self.btn_enable_password.setDisabled(True)
                    self.btn_change_password.setDisabled(False)
                    self.btn_disaable_password.setDisabled(False)

                    dialog.close()

            dialog.ui.btn_set.clicked.connect(set_password)
            dialog.ui.btn_cancel.clicked.connect(dialog.close)

            dialog.exec_()

        dialog = QtWidgets.QDialog()
        dialog.ui = page_unlook_password()
        dialog.ui.setupUi(dialog)

        def unlook():
            if dialog.ui.check_for_unlook():
                self.btn_enable_password.setDisabled(False)
                self.btn_change_password.setDisabled(True)
                self.btn_disaable_password.setDisabled(True)

                Func_DataBase.delate_password()
                dialog.close()

                set_for_change_password()

        dialog.ui.btn_unloock.clicked.connect(unlook)
        dialog.ui.btn_exit.clicked.connect(dialog.close)

        dialog.exec_()
        # ------------- ---------- ------------

    def reset_information(self):
        if self.status_password:
            dialog = QtWidgets.QDialog()
            dialog.ui = page_unlook_password()
            dialog.ui.setupUi(dialog)

            def unlook():
                if dialog.ui.check_for_unlook():
                    try:
                        Func_DataBase.Delate_in_DataBase()
                    except:
                        pass

                    dialog.close()

            dialog.ui.btn_unloock.clicked.connect(unlook)
            dialog.ui.btn_exit.clicked.connect(dialog.close)

            dialog.exec_()
        else:
            try:
                Func_DataBase.Delate_in_DataBase()
            except:
                pass

    def reset_setting(self):
        # this is setting Defult
        self.btn_enable_password.setDisabled(False)
        self.btn_change_password.setDisabled(True)
        self.btn_disaable_password.setDisabled(True)

        self.combo_languge.setCurrentText("English")
        self.combo_font.setCurrentText("MS Shell Dlg 2")
        self.input_num.setValue(8)
        self.rdb_light.setChecked(True)

    def command_save(self):
        # this just save setting in json
        self.convert_information_setting_to_json()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", Words.translate_words(Words.Setting)))
        self.txt_languge.setText(_translate(
            "Dialog", Words.translate_words(Words.Languge)))
        self.combo_languge.setItemText(0, _translate("Dialog", "English"))
        self.combo_languge.setItemText(1, _translate("Dialog", "Persian"))
        self.combo_languge.setItemText(2, _translate("Dialog", "Arabic"))
        self.txt_type_font.setText(_translate(
            "Dialog", Words.translate_words(Words.Type_font)))
        self.txt_size_font.setText(_translate(
            "Dialog", Words.translate_words(Words.Size_font)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("Dialog", Words.translate_words(Words.General)))
        self.btn_reset_information.setText(
            _translate("Dialog", Words.translate_words(Words.Delete_all_information)))
        self.groupBox.setTitle(_translate(
            "Dialog", Words.translate_words(Words.Password_setting)))
        self.btn_enable_password.setText(
            _translate("Dialog", Words.translate_words(Words.Enable_password)))
        self.btn_disaable_password.setText(
            _translate("Dialog", Words.translate_words(Words.Disable_password)))
        self.btn_change_password.setText(
            _translate("Dialog", Words.translate_words(Words.Change_password)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("Dialog", Words.translate_words(Words.Security)))
        self.btn_save.setText(_translate(
            "Dialog", Words.translate_words(Words.Save)))
        self.btn_rest_setting.setText(_translate(
            "Dialog", Words.translate_words(Words.Reset_setting_to_defult)))
        self.btn_close.setText(_translate(
            "Dialog", Words.translate_words(Words.Close)))
        self.label.setText(_translate("Dialog", Words.translate_words(Words.them)))
        self.rdb_dark.setText(_translate("Dialog", Words.translate_words(Words.dark)))
        self.rdb_light.setText(_translate("Dialog", Words.translate_words(Words.light)))


if __name__ == "__main__":
    import sys
    Programm = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(Programm.exec_())
