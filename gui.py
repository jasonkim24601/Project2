# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(326, 277)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 40, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_url_info = QtWidgets.QLabel(self.centralwidget)
        self.label_url_info.setGeometry(QtCore.QRect(10, 70, 301, 31))
        self.label_url_info.setObjectName("label_url_info")
        self.label_output_info1 = QtWidgets.QLabel(self.centralwidget)
        self.label_output_info1.setGeometry(QtCore.QRect(10, 90, 301, 31))
        self.label_output_info1.setObjectName("label_output_info1")
        self.label_output_info2 = QtWidgets.QLabel(self.centralwidget)
        self.label_output_info2.setGeometry(QtCore.QRect(10, 110, 301, 31))
        self.label_output_info2.setObjectName("label_output_info2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 301, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 301, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 301, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project 2"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "Output File"))
        self.label_url_info.setText(_translate("MainWindow", "Please input a Magic: The Gathering Tournament decklists URL. "))
        self.label_output_info1.setText(_translate("MainWindow", "Please designate the Output csv file to append."))
        self.label_output_info2.setText(_translate("MainWindow", "If no output is set, results will be appended to default.csv"))
        self.label_6.setText(_translate("MainWindow", "ERROR MESSAGE YOU SHOULDN\'T BE SEEING THIS"))
        self.label_7.setText(_translate("MainWindow", "Done, results saved to ..."))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.label_8.setText(_translate("MainWindow", "Press Next to close program."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
