# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMainWindow(object):
    def setupUi(self, frmMainWindow):
        frmMainWindow.setObjectName("frmMainWindow")
        frmMainWindow.resize(400, 129)
        self.lstItems = QtWidgets.QListWidget(frmMainWindow)
        self.lstItems.setGeometry(QtCore.QRect(205, 20, 181, 91))
        self.lstItems.setObjectName("lstItems")
        self.btnAdd = QtWidgets.QPushButton(frmMainWindow)
        self.btnAdd.setGeometry(QtCore.QRect(10, 90, 181, 25))
        self.btnAdd.setObjectName("btnAdd")
        self.txtInput = QtWidgets.QLineEdit(frmMainWindow)
        self.txtInput.setGeometry(QtCore.QRect(10, 50, 181, 25))
        self.txtInput.setObjectName("txtInput")
        self.lblAdd = QtWidgets.QLabel(frmMainWindow)
        self.lblAdd.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.lblAdd.setObjectName("lblAdd")

        self.retranslateUi(frmMainWindow)
        QtCore.QMetaObject.connectSlotsByName(frmMainWindow)

    def retranslateUi(self, frmMainWindow):
        _translate = QtCore.QCoreApplication.translate
        frmMainWindow.setWindowTitle(_translate("frmMainWindow", "Add to List"))
        self.btnAdd.setText(_translate("frmMainWindow", "Add"))
        self.lblAdd.setText(_translate("frmMainWindow", "Add Item"))

