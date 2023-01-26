# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'case_db.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 228)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plunger/icons/plunger_logo_PFmZvE.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_open = QtWidgets.QPushButton(Dialog)
        self.btn_open.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plunger/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open.setIcon(icon1)
        self.btn_open.setIconSize(QtCore.QSize(24, 24))
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        self.btn_delete.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plunger/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setIconSize(QtCore.QSize(24, 24))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plunger/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon3)
        self.btn_cancel.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TUALP Transient Plunger Lift Simulator"))
        self.label.setText(_translate("Dialog", "Case name"))
        self.btn_open.setText(_translate("Dialog", "Open"))
        self.btn_delete.setText(_translate("Dialog", "Delete"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))

import plunger_ico_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

