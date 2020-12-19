# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aestegano.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(359, 356)
        self.centralwidget = QtWidgets.QWidget(dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.about_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.about_pushButton.setObjectName("about_pushButton")
        self.gridLayout_3.addWidget(self.about_pushButton, 0, 2, 1, 1)
        self.exit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.gridLayout_3.addWidget(self.exit_pushButton, 0, 3, 1, 1)
        self.decrypt_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_pushButton.setObjectName("decrypt_pushButton")
        self.gridLayout_3.addWidget(self.decrypt_pushButton, 0, 1, 1, 1)
        self.encrypt_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_pushButton.setObjectName("encrypt_pushButton")
        self.gridLayout_3.addWidget(self.encrypt_pushButton, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setObjectName("text_label")
        self.gridLayout.addWidget(self.text_label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.source_label = QtWidgets.QLabel(self.centralwidget)
        self.source_label.setObjectName("source_label")
        self.gridLayout_2.addWidget(self.source_label, 1, 0, 1, 1)
        self.key_label = QtWidgets.QLabel(self.centralwidget)
        self.key_label.setObjectName("key_label")
        self.gridLayout_2.addWidget(self.key_label, 0, 0, 1, 1)
        self.key_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.key_lineEdit.setClearButtonEnabled(True)
        self.key_lineEdit.setObjectName("key_lineEdit")
        self.gridLayout_2.addWidget(self.key_lineEdit, 0, 2, 1, 1)
        self.source_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.source_toolButton.setObjectName("source_toolButton")
        self.gridLayout_2.addWidget(self.source_toolButton, 1, 3, 1, 1)
        self.source_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.source_lineEdit.setReadOnly(True)
        self.source_lineEdit.setPlaceholderText("")
        self.source_lineEdit.setObjectName("source_lineEdit")
        self.gridLayout_2.addWidget(self.source_lineEdit, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 22))
        self.menubar.setObjectName("menubar")
        dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dialog)
        self.statusbar.setObjectName("statusbar")
        dialog.setStatusBar(self.statusbar)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.textEdit, self.key_lineEdit)
        dialog.setTabOrder(self.key_lineEdit, self.source_lineEdit)
        dialog.setTabOrder(self.source_lineEdit, self.source_toolButton)
        dialog.setTabOrder(self.source_toolButton, self.encrypt_pushButton)
        dialog.setTabOrder(self.encrypt_pushButton, self.decrypt_pushButton)
        dialog.setTabOrder(self.decrypt_pushButton, self.about_pushButton)
        dialog.setTabOrder(self.about_pushButton, self.exit_pushButton)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "AEStegano"))
        self.about_pushButton.setText(_translate("dialog", "About..."))
        self.exit_pushButton.setText(_translate("dialog", "Exit"))
        self.decrypt_pushButton.setText(_translate("dialog", "Decrypt"))
        self.encrypt_pushButton.setText(_translate("dialog", "Encrypt"))
        self.text_label.setText(_translate("dialog", "Text:"))
        self.source_label.setText(_translate("dialog", "Image:"))
        self.key_label.setText(_translate("dialog", "AES Key:"))
        self.source_toolButton.setText(_translate("dialog", "..."))


