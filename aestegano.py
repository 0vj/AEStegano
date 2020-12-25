# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from res.ui import aestegano_ui
from res.logic import messages
from stegano import lsb
import pyaes
import pathlib


def init(dialog, self):
    self.source = ''
    self.filter = ("Images (*.png *.jpg *.PNG *.JPG *.jpeg *.JPEG)"
                   ";;All files(*)")
    self.encrypt_pushButton.clicked.connect(
        lambda: encrypt(dialog, self)
        )
    self.decrypt_pushButton.clicked.connect(
        lambda: decrypt(dialog, self)
        )
    self.about_pushButton.clicked.connect(
        lambda: about(dialog, self)
        )
    self.source_toolButton.clicked.connect(
        lambda: get_source(dialog, self)
        )
    self.exit_pushButton.clicked.connect(dialog.close)


def encrypt(dialog, self):
    try:
        key = self.key_lineEdit.text()
        key_len = len(key)
        if key_len in (16, 24, 32):
            aes = pyaes.AESModeOfOperationCTR(key.encode())
            plaintext = self.textEdit.toPlainText()
            if plaintext.strip() != '':
                ciphertext = aes.encrypt(plaintext)
                if self.source != '':
                    dest = get_destination(dialog, self)
                    if dest != '':
                        secret = lsb.hide(self.source, ciphertext.hex())
                        secret.save(dest)
                elif self.source == '':
                    message = 'Please select an image!'
                    messages.warning(dialog, 'Warning', message)
            else:
                message = 'Text length is zero!'
                messages.warning(dialog, 'Warning', message)
        else:
            message = 'The lenght of the key must be 16, 24 or 32'
            messages.warning(dialog, 'Warning', message)
    except Exception as error:
        messages.error(dialog, 'Error', str(error))


def decrypt(dialog, self):
    try:
        key = self.key_lineEdit.text()
        key_len = len(key)
        if key_len in (16, 24, 32):
            if self.source != '':
                clear_message = lsb.reveal(self.source).strip()
                clear_message = bytes.fromhex(clear_message)
                key = key.encode()
                aes = pyaes.AESModeOfOperationCTR(key)
                decrypted = aes.decrypt(clear_message).decode()
                self.textEdit.setText(decrypted)
            else:
                message = 'Please select an image!'
                messages.warning(dialog, 'Warning', message)
        else:
            message = 'The lenght of the key must be 16, 24 or 32'
            messages.warning(dialog, 'Warning', message)
    except Exception as error:
        messages.error(dialog, 'Error', str(error))


def about(dialog, self):
    message = 'AEStegano\nDeveloped by @ArefDev\nGPLv2'
    messages.info(dialog, 'About...', message)


def get_source(dialog, self):
    self.source = QtWidgets.QFileDialog.getOpenFileName(
        dialog, 
        caption='Open Image',
        filter=self.filter,
        )[0].strip()
    if self.source != '':
        self.source_lineEdit.setText(self.source)


def get_destination(dialog, self):
    destination = QtWidgets.QFileDialog.getSaveFileName(
        dialog, 
        caption='Save...',
        directory='newfile',
        filter=self.filter,
        )[0].strip()
    if destination != '':
        suffix = pathlib.Path(destination).suffix
        if suffix == '':
            destination = '{}.png'.format(destination)
    return destination


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    ui = aestegano_ui.Ui_dialog()
    ui.setupUi(dialog)
    init(dialog, ui)
    dialog.show()
    sys.exit(app.exec_())
