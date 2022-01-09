from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from db_connect import DbConnection
import requests
import time


class Ui_MainWindow(object):
    def setupUi(
        self,
        MainWindow,
    ):

        db_connect = DbConnection(
            "measuring", "postgres", "localhost", "_dataadmin1", "5432"
        )

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(230, 110)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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
                "background-color : #16F529;"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color : #85BB65;"
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

        # start_db_archieve
        self.pushButton_0.clicked.connect(lambda: db_connect.db_archieve_data())

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Archieve air pollution - DB Control Panel")
        )

        self.pushButton_0.setText(
            _translate("MainWindow", "Start DB archieve\nair pollution")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
