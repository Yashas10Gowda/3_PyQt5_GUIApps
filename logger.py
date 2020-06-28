import csv
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.priority = QtWidgets.QComboBox(self.centralwidget)
        self.priority.setGeometry(QtCore.QRect(280, 100, 201, 21))
        self.priority.setEditable(False)
        self.priority.setObjectName("priority")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(60, 100, 201, 21))
        self.user.setObjectName("user")
        self.log = QtWidgets.QLineEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(60, 70, 421, 21))
        self.log.setDragEnabled(False)
        self.log.setObjectName("log")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.logit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 170, 421, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.logs = []
        self.findlogsandsave(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logit by Yashas"))
        self.priority.setStatusTip(_translate(
            "MainWindow", "Select the priority of your log."))
        self.priority.setCurrentText(
            _translate("MainWindow", "Select Priority"))
        self.priority.setPlaceholderText(
            _translate("MainWindow", "Select Priority"))
        self.priority.setItemText(0, _translate("MainWindow", "HIGH"))
        self.priority.setItemText(1, _translate("MainWindow", "MEDIUM"))
        self.priority.setItemText(2, _translate("MainWindow", "LOW"))
        self.user.setStatusTip(_translate("MainWindow", "User\'s name"))
        self.user.setPlaceholderText(_translate("MainWindow", "User"))
        self.log.setStatusTip(_translate(
            "MainWindow", "Your log message goes there."))
        self.log.setPlaceholderText(_translate("MainWindow", "Log"))
        self.pushButton.setStatusTip(
            _translate("MainWindow", "Click to log it."))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "LOGGER"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Log Text"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Logged On"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Person Logged"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Priority"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Test your log here"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate(
            "MainWindow", datetime.datetime.now().__str__()))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Your name"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Priority:Medium"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def findlogsandsave(self, mybool):
        if os.path.exists('./logs.csv'):
            with open('logs.csv', 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                j = 0
                for log in csvreader:
                    self.tableWidget.setRowCount(j+1)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(j+1))
                    self.tableWidget.setVerticalHeaderItem(j, item)
                    if mybool:
                        self.logs.append(log)
                    for i in range(4):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(log[i])
                        self.tableWidget.setItem(j, i, item)
                    j += 1

        else:
            with open('logs.csv', 'w') as csvfile:
                pass

    def logit(self):
        self.logs.append([self.log.text(), datetime.datetime.now().__str__(),
                          self.user.text(), self.priority.currentText()])
        with open('logs.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(self.logs)
        self.findlogsandsave(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
