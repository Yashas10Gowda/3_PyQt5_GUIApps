from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 450)
        MainWindow.setStyleSheet("color: rgb(0, 130, 153);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "C:/Users/HOME/Desktop/Workspace/GUI_Code/picicon.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 130, 153, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(35)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(110, 120, 141, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.status.setFont(font)
        self.status.setStyleSheet("color: rgb(0, 130, 153);")
        self.status.setObjectName("status")
        self.filepicker = QtWidgets.QPushButton(self.centralwidget)
        self.filepicker.setGeometry(QtCore.QRect(40, 150, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filepicker.setFont(font)
        self.filepicker.setAutoFillBackground(False)
        self.filepicker.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 130, 153);\n"
                                      "border: 2px solid rgb(0, 130, 153);")
        self.filepicker.setDefault(False)
        self.filepicker.setObjectName("filepicker")
        self.filepicker.clicked.connect(self.getimg)
        self.inputlocation = QtWidgets.QLineEdit(self.centralwidget)
        self.inputlocation.setGeometry(QtCore.QRect(10, 200, 331, 20))
        self.inputlocation.setStyleSheet("color: rgb(0, 130, 153);")
        self.inputlocation.setText("")
        self.inputlocation.setObjectName("inputlocation")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 271, 20))
        self.label_3.setObjectName("label_3")
        self.quality = QtWidgets.QScrollBar(self.centralwidget)
        self.quality.setGeometry(QtCore.QRect(40, 270, 271, 16))
        self.quality.setStyleSheet("background-color:rgb(0, 130, 153);")
        self.quality.setSliderPosition(50)
        self.quality.setOrientation(QtCore.Qt.Horizontal)
        self.quality.setInvertedAppearance(True)
        self.quality.setInvertedControls(True)
        self.quality.setObjectName("quality")
        self.shrink = QtWidgets.QPushButton(self.centralwidget)
        self.shrink.setGeometry(QtCore.QRect(40, 330, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shrink.setFont(font)
        self.shrink.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(0, 130, 153);\n"
                                  "border: 3px solid rgb(0, 130, 153);\n"
                                  "")
        self.shrink.setObjectName("shrink")
        self.shrink.clicked.connect(self.putimg)
        self.outputlocation = QtWidgets.QLineEdit(self.centralwidget)
        self.outputlocation.setGeometry(QtCore.QRect(10, 380, 331, 20))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.outputlocation.setFont(font)
        self.outputlocation.setText("")
        self.outputlocation.setDragEnabled(True)
        self.outputlocation.setReadOnly(True)
        self.outputlocation.setObjectName("outputlocation")
        self.outputlocation.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Shrinker"))
        self.label.setStatusTip(_translate(
            "MainWindow", "Shrink the image size without losing much of it\'s quality."))
        self.label_2.setStatusTip(_translate(
            "MainWindow", "Shrink the image size without losing much of it\'s quality."))
        self.label_2.setText(_translate("MainWindow", "ImageShrink"))
        self.status.setText(_translate(
            "MainWindow", "Choose an Image to \"Shrink\"."))
        self.filepicker.setText(_translate("MainWindow", "BROWSE"))
        self.inputlocation.setPlaceholderText(_translate(
            "MainWindow", "The specified file\'s location shall appear here."))
        self.label_3.setText(_translate(
            "MainWindow", "Quality--> The lower the quality, the smaller the file size."))
        self.shrink.setText(_translate("MainWindow", "SHRINK-IT"))
        self.outputlocation.setPlaceholderText(_translate(
            "MainWindow", "The output file\'s location shall appear here."))

    def getimg(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            directory=os.getcwd())
        self.inputlocation.setText(fileName)
        self.status.setText('Now set the prefered quality.')
        self.status.adjustSize()

    def putimg(self):
        pic = Image.open(self.inputlocation.text())
        savloc = '/'.join(self.inputlocation.text().split('/')
                          [:-1])+'/imgshrinker-'+self.inputlocation.text().split('/')[-1]
        pic.save(savloc, quality=100-self.quality.value())
        self.outputlocation.setText(savloc)
        self.status.setText('Image is successfully shrinked.')
        self.status.adjustSize()
        alert = QtWidgets.QMessageBox()
        alert.setWindowTitle('ImageShrink')
        alert.setText(
            'Image is successfully shrinked and\n saved in the location shown below.\nThank you for using ImageShrink \n\t\t~Yashas Gowda')
        alert.setIcon(QtWidgets.QMessageBox.Information)
        alert.setStandardButtons(QtWidgets.QMessageBox.Ok)
        alert.exec_()
        # print('/'.join(self.inputlocation.text().split('/')[:-1]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
