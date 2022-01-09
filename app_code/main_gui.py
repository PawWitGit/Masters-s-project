from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from api_response import Response
import requests
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        response = Response(
            requests.get(
                "https://api.thingspeak.com/channels/1569165/feeds.json?results=2"
            ).json(),
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )

        response.get_response_data()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(180, 100, 20, 20))
        self.label_0.setObjectName("WELCOME TEXT")

        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(20, 20, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_13")
        self.pushButton_0.setStyleSheet(
            (
                "QPushButton"
                "{"
                "border-radius : 15px;"
                "font-size : 22px;"
                "background-color : lightgreen;"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color : green;"
                "}"
            )
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RESEARCH OF AIR POLLUTION"))

        self.pushButton_0.setText(
            _translate("MainWindow", "Start DB archieve\nair pollution")
        )
        self.label_0.setText(_translate("MainWindow", "Temperatura:\n"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
