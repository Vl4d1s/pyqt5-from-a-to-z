# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lstomsl/PycharmProjects/PyQt5_course/ui/sql.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgSql(object):
    def setupUi(self, dlgSql):
        dlgSql.setObjectName("dlgSql")
        dlgSql.resize(862, 523)
        self.widget = QtWidgets.QWidget(dlgSql)
        self.widget.setGeometry(QtCore.QRect(11, 14, 841, 501))
        self.widget.setObjectName("widget")
        self.lytMain = QtWidgets.QHBoxLayout(self.widget)
        self.lytMain.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.lytMain.setContentsMargins(0, 0, 0, 0)
        self.lytMain.setObjectName("lytMain")
        self.lytLeft = QtWidgets.QVBoxLayout()
        self.lytLeft.setObjectName("lytLeft")
        self.lstTables = QtWidgets.QListWidget(self.widget)
        self.lstTables.setObjectName("lstTables")
        self.lytLeft.addWidget(self.lstTables)
        self.btnAdd = QtWidgets.QPushButton(self.widget)
        self.btnAdd.setObjectName("btnAdd")
        self.lytLeft.addWidget(self.btnAdd)
        self.btnUpdate = QtWidgets.QPushButton(self.widget)
        self.btnUpdate.setObjectName("btnUpdate")
        self.lytLeft.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(self.widget)
        self.btnDelete.setObjectName("btnDelete")
        self.lytLeft.addWidget(self.btnDelete)
        self.lytMain.addLayout(self.lytLeft)
        self.lytTable = QtWidgets.QVBoxLayout()
        self.lytTable.setObjectName("lytTable")
        self.tblEmployees = QtWidgets.QTableWidget(self.widget)
        self.tblEmployees.setColumnCount(7)
        self.tblEmployees.setObjectName("tblEmployees")
        self.tblEmployees.setRowCount(0)
        self.lytTable.addWidget(self.tblEmployees)
        self.lytMain.addLayout(self.lytTable)

        self.retranslateUi(dlgSql)
        QtCore.QMetaObject.connectSlotsByName(dlgSql)

    def retranslateUi(self, dlgSql):
        _translate = QtCore.QCoreApplication.translate
        dlgSql.setWindowTitle(_translate("dlgSql", "Dialog"))
        self.btnAdd.setText(_translate("dlgSql", "Add Employee"))
        self.btnUpdate.setText(_translate("dlgSql", "Update Employee"))
        self.btnDelete.setText(_translate("dlgSql", "Delete Employee"))
