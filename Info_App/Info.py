import os
from PyQt5 import QtCore, QtGui, QtWidgets
from Setting_app import Words
from Data_Base import Func_DataBase


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 186)
        Dialog.setMinimumSize(393, 186)
        Dialog.setMaximumSize(393, 186)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/info.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.txt_info = QtWidgets.QTextBrowser(Dialog)
        self.txt_info.setGeometry(QtCore.QRect(10, 10, 371, 101))
        self.txt_info.setObjectName("txt_info")
        self.txt_communicate = QtWidgets.QLabel(Dialog)
        self.txt_communicate.setGeometry(QtCore.QRect(10, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_communicate.setFont(font)
        self.txt_communicate.setObjectName("txt_communicate")
        self.link_GitHub = QtWidgets.QCommandLinkButton(Dialog)
        self.link_GitHub.setGeometry(QtCore.QRect(210, 120, 50, 51))
        self.link_GitHub.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/gitub.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon GitHub
        self.link_GitHub.setIcon(icon1)
        self.link_GitHub.setIconSize(QtCore.QSize(40, 40))
        self.link_GitHub.setObjectName("link_instagram")
        self.link_Linkin = QtWidgets.QCommandLinkButton(Dialog)
        self.link_Linkin.setGeometry(QtCore.QRect(260, 120, 51, 51))
        self.link_Linkin.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/Linkden.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON Linkin
        self.link_Linkin.setIcon(icon2)
        self.link_Linkin.setIconSize(QtCore.QSize(40, 40))
        self.link_Linkin.setObjectName("link_Linkin")
        self.link_gmail = QtWidgets.QCommandLinkButton(Dialog)
        self.link_gmail.setGeometry(QtCore.QRect(310, 125, 51, 51))
        self.link_gmail.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/Gmail.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # ICON GMAIL
        self.link_gmail.setIcon(icon3)
        self.link_gmail.setIconSize(QtCore.QSize(40, 40))
        self.link_gmail.setObjectName("link_gmail")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # ================== Coding ==================
        Func_DataBase.set_setting(Dialog)

        self.link_gmail.clicked.connect(lambda: self.send_gmail())
        
        # in windows with command start "target Site" open site in chrom
        self.link_GitHub.clicked.connect(lambda: os.system(
            "start https://github.com/PooyaRezaee"))
        self.link_Linkin.clicked.connect(lambda: os.system(
            "start https://www.linkedin.com/in/pooya-rezaee-moghadam-1700721b9"))

    def send_gmail(self):
        self.win_alert_gmail = QtWidgets.QMessageBox()
        self.win_alert_gmail.setWindowTitle("My Gmail")
        self.win_alert_gmail.setText(
            "My gmail is \npooyareaiy909@gmail.com \nYou can send a message for me to this address")
        self.win_alert_gmail.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", Words.translate_words(Words.info)))
        self.txt_info.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This Program Is for Save Information Received &amp; Payments</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is make with me(Pooya Rezaee)</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For communicate with me my email is 'pooyarezaiy909@gmail.com'</p></body></html>"))
        self.txt_communicate.setText(_translate(
            "Dialog", Words.translate_words(Words.Ways_communicate)))
