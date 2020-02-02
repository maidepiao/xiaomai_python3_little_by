# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        dialog.setWhatsThis("")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 120, 113, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 170, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "小麦布局"))
        dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMaximizeButtonHint)
        self.label.setText(_translate("dialog", "账号"))
        self.label_2.setText(_translate("dialog", "密码"))
        self.lineEdit.setPlaceholderText(_translate("dialog", "请输入用户名"))
        self.pushButton.setText(_translate("dialog", "登录"))
        self.pushButton_2.setText(_translate("dialog", "取消"))

import sys
def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)

    ui_dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(ui_dialog)
    ui_dialog.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    show_MainWindow()
