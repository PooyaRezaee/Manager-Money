import sys
import json
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from Add_information.add import Ui_Dialog as page_add
from Setting_Programm.Setting import Ui_Dialog as page_setting
from Info_Programm.Info import Ui_Dialog as page_info
from Data_Base import Func_DataBase
from Windows_passwords.page_unloock import Ui_Dialog as page_unlook_password
from Setting_Programm import Words
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 455)
        MainWindow.setMinimumSize(620, 455)
        MainWindow.setMaximumSize(620, 455)
        MainWindow.setMinimumSize(QtCore.QSize(620, 455))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/Money_Manager.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON FOR WINDOW
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info.setGeometry(QtCore.QRect(330, 5, 60, 60))
        self.btn_info.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/info.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON INFO
        self.btn_info.setIcon(icon3)
        self.btn_info.setIconSize(QtCore.QSize(55, 55))
        self.btn_info.setFlat(True)
        self.btn_info.setObjectName("btn_info")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 65, 621, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.btn_setting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting.setGeometry(QtCore.QRect(250, 5, 60, 60))
        self.btn_setting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/setting.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON SETTING
        self.btn_setting.setIcon(icon2)
        self.btn_setting.setIconSize(QtCore.QSize(55, 55))
        self.btn_setting.setFlat(True)
        self.btn_setting.setObjectName("btn_setting")

        self.btn_s_g = QtWidgets.QPushButton(self.centralwidget)
        self.btn_s_g.setGeometry(QtCore.QRect(170, 5, 60, 60))
        self.btn_s_g.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/s_g.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON s_g
        self.btn_s_g.setIcon(icon4)
        self.btn_s_g.setIconSize(QtCore.QSize(50, 50))
        self.btn_s_g.setFlat(True)
        self.btn_s_g.setObjectName("btn_s_g")

        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(90, 5, 60, 60))
        self.btn_delete.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/Delate.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON DELATE
        self.btn_delete.setIcon(icon5)
        self.btn_delete.setIconSize(QtCore.QSize(55, 55))
        self.btn_delete.setFlat(True)
        self.btn_delete.setObjectName("btn_delete")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 120, 601, 301))

        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(10, 5, 60, 60))
        self.btn_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/Add.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON ADD
        self.btn_add.setIcon(icon1)
        self.btn_add.setIconSize(QtCore.QSize(55, 55))
        self.btn_add.setFlat(True)
        self.btn_add.setObjectName("btn_add")
        # ----------------------
        font = QtGui.QFont()
        font.setPointSize(9)
        self.treeWidget.setFont(font)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(110)
        self.txt_inventory = QtWidgets.QLabel(self.centralwidget)
        self.txt_inventory.setGeometry(QtCore.QRect(330, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_inventory.setFont(font)
        self.txt_inventory.setObjectName("txt_inventory")
        self.txtline_inventory = QtWidgets.QLineEdit(self.centralwidget)
        self.txtline_inventory.setGeometry(QtCore.QRect(450, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtline_inventory.setFont(font)
        self.txtline_inventory.setAlignment(QtCore.Qt.AlignCenter)
        self.txtline_inventory.setReadOnly(True)
        self.txtline_inventory.setObjectName("txtline_inventory")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 291, 19))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdb_all = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_all.setChecked(True)
        self.rdb_all.setObjectName("rdb_all")
        self.horizontalLayout.addWidget(self.rdb_all)
        self.rdb_received = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_received.setObjectName("rdb_received")
        self.horizontalLayout.addWidget(self.rdb_received)
        self.rdb_Payments = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_Payments.setObjectName("rdb_Payments")
        self.horizontalLayout.addWidget(self.rdb_Payments)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # ================== Coding ==================
        # Try for if not exists setting.json not give error
        try:
            with open("setting.json", 'r') as File:
                File = json.load(File)
                if File["language_Programm"] != "English":
                    self.centralwidget.setLayoutDirection(QtCore.Qt.RightToLeft)
                    
                self.them = File["them"]
        except:
            pass

        # Set Settig on the programm
        Func_DataBase.set_setting(MainWindow)

        try:
            Func_DataBase.get_password_in_database()
            self.status_password = True
        except:
            self.status_password = False

        # for if enable password first Enter password to open programm
        self.unlook()

        # Update Tabel inforamtion
        self.update_table_inventory()

        self.btn_add.clicked.connect(self.add_item)
        self.btn_delete.clicked.connect(self.remove_item)
        self.btn_s_g.clicked.connect(self.s_g)
        self.btn_setting.clicked.connect(self.win_setting)
        self.btn_info.clicked.connect(self.win_info)

        self.rdb_all.clicked.connect(self.update_table_inventory)
        self.rdb_received.clicked.connect(self.update_table_inventory)
        self.rdb_Payments.clicked.connect(self.update_table_inventory)

        # ==================== Status Bar ==========================
        self.btn_add.setStatusTip("Add Item")
        self.btn_delete.setStatusTip("Delete Item")
        self.btn_setting.setStatusTip("Setting program")
        self.btn_s_g.setStatusTip("This Create Comming Soon ")
        self.btn_info.setStatusTip("Info Programm And Developer")
        self.rdb_received.setStatusTip("Filter On Table")
        self.rdb_Payments.setStatusTip("Filter On Table")
        self.rdb_all.setStatusTip("Filter On Table")
        self.treeWidget.setStatusTip(f" {str(datetime.now())[0:10]} | {self.treeWidget.topLevelItemCount()} ")
        self.txtline_inventory.setStatusTip("Your Money Inventory")
        MainWindow.setStatusTip("Manager Money")
        
        # ==========================================================

    def unlook(self):
        if self.status_password:
            dialog = QtWidgets.QDialog()
            dialog.ui = page_unlook_password()
            dialog.ui.setupUi(dialog)
            dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

            def unlook():
                if dialog.ui.check_for_unlook():
                    dialog.close()

            dialog.ui.btn_unloock.clicked.connect(unlook)
            dialog.ui.btn_exit.clicked.connect(sys.exit)

            dialog.exec_()
# ========================================
    def convert_number_to_sort(self,number):
        if len(str(number)) <= 3:
            return str(number)
        i = 0
        s = ""
        b = len(str(number)) % 3
        c = True
        d = 0

        for n in str(number):
            i += 1
            s += n
            d += 1
            if b == i and c:
                s += ","
                i = 0
                c = False
            elif i % 3 == 0 and d < len(str(number)):
                s += ","

        return s


        


# ==============================================
    def update_table_inventory(self):
        self.treeWidget.clear()

        Payments = 0
        Recives = 0
        try:
            for i in Func_DataBase.Search_in_DataBase():
                if self.rdb_all.isChecked():
                    item = QtWidgets.QTreeWidgetItem(
                        self.treeWidget, [str(i[1]), i[2], i[3], i[4], i[5]])
                    self.treeWidget.addTopLevelItem(item)
                elif self.rdb_Payments.isChecked():
                    if i[2] == "Payment":
                        item = QtWidgets.QTreeWidgetItem(
                            self.treeWidget, [str(i[1]), i[2], i[3], i[4], i[5]])
                        self.treeWidget.addTopLevelItem(item)
                elif self.rdb_received.isChecked():
                    if i[2] == "Received":
                        item = QtWidgets.QTreeWidgetItem(
                            self.treeWidget, [str(i[1]), i[2], i[3], i[4], i[5]])
                        self.treeWidget.addTopLevelItem(item)

                if i[2] == "Payment":
                    Payments += i[1]
                elif i[2] == "Received":
                    Recives += i[1]
                else:
                    print(f"Error Not Found !!! {i[2]}")

            amount = Recives - Payments
            self.txtline_inventory.setText(self.convert_number_to_sort(amount))
        except:
            self.txtline_inventory.setText("0")

    def add_item(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = page_add()
        dialog.ui.setupUi(dialog)

        dialog.ui.btn_cancel.clicked.connect(dialog.close)

        def done_adn_close():
            if dialog.ui.command_btn_ok():
                dialog.close()
                self.update_table_inventory()

        dialog.ui.btn_ok.clicked.connect(done_adn_close)

        dialog.exec_()

    def remove_item(self):
        for currentItem in self.treeWidget.selectedItems():
            Func_DataBase.Delate_item_in_DataBase(currentItem.text(0), currentItem.text(
                1), currentItem.text(2), currentItem.text(3), currentItem.text(4))
        self.update_table_inventory()

    def s_g(self):
        # Comming Soon !!!
        self.win_aleart = QtWidgets.QMessageBox()
        self.win_aleart.setWindowTitle("Option")
        self.win_aleart.setText(Words.translate_words(Words.comming_soon))
        self.win_aleart.show()

    def win_setting(self):
        def command_btn_save():
            self.win_aleart = QtWidgets.QMessageBox()
            self.win_aleart.setWindowTitle("Restart")
            self.win_aleart.setText(Words.translate_words(Words.restart_Programm))
            self.win_aleart.show()

            dialog.close()
            MainWindow.close()

        dialog = QtWidgets.QDialog()
        dialog.ui = page_setting()
        dialog.ui.setupUi(dialog)
        dialog.ui.btn_close.clicked.connect(dialog.close)
        dialog.ui.btn_save.clicked.connect(command_btn_save)

        dialog.exec_()

        self.update_table_inventory()
        Func_DataBase.set_setting(MainWindow)

    def win_info(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = page_info()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", Words.translate_words(Words.Manager_money)))
        self.treeWidget.headerItem().setText(0, _translate(
            "MainWindow", Words.translate_words(Words.Amount_t)))
        self.treeWidget.headerItem().setText(1, _translate(
            "MainWindow", Words.translate_words(Words.Type_t)))
        self.treeWidget.headerItem().setText(2, _translate(
            "MainWindow", Words.translate_words(Words.From_To_t)))
        self.treeWidget.headerItem().setText(3, _translate(
            "MainWindow", Words.translate_words(Words.Date_t)))
        self.treeWidget.headerItem().setText(4, _translate(
            "MainWindow", Words.translate_words(Words.Description)))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.txt_inventory.setText(_translate(
            "MainWindow", Words.translate_words(Words.Money_inventory)))
        self.txtline_inventory.setText(_translate("MainWindow", "0"))
        self.rdb_all.setText(_translate(
            "MainWindow", Words.translate_words(Words.All)))
        self.rdb_received.setText(_translate(
            "MainWindow", Words.translate_words(Words.Received)))
        self.rdb_Payments.setText(_translate(
            "MainWindow", Words.translate_words(Words.Payment)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    try:
        if ui.them == "dark":
            app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
    except :
        pass
    MainWindow.show()
    sys.exit(app.exec_())
