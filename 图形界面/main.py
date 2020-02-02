# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from 图形界面.login import Ui_dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.menubar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menubar.setAccessibleName("")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.menu.setToolTipsVisible(True)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))

def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    ui_dialog = QtWidgets.QDialog(parent=main_window)
    ui = Ui_dialog()
    ui.setupUi(ui_dialog)
    ui_dialog.show()

    main_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    show_MainWindow()