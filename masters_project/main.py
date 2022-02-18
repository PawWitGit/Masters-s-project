from cProfile import label
from calendar import calendar
from msilib.schema import LaunchCondition
from sqlite3 import Timestamp
import sys
import datetime
import time
from xmlrpc.client import DateTime
from pytest import console_main
from plot_data import DataView
import requests
from turtle import right
from PySide6.QtCharts import QCandlestickSet
from PySide6.QtCore import QRect, Qt, QDateTime, QDate
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidgetItem,
    QTextEdit,
    QLineEdit,
    QCalendarWidget,
    QDateEdit,
    QDateTimeEdit,
    QComboBox,
)

from datetime import datetime

from database.db_connect import DbConnection


class MainWindow(QLabel):
    def __init__(self, parent=None):

        self.db_ip_adress = "192.168.55.111"
        self.date_string = "wpisz godzinę w formacie hh:mm"

        super(MainWindow, self).__init__()

        try:
            db_connection = DbConnection()
        except:
            print("Network Fault")
        MainWindow.setGeometry(self, 500, 300, 700, 700)

        def convert_data(data):

            time_convert = data
            day = data[0:1]
            month = data[3:4]
            year = data[6:9]

            time_convert = day + ":" + month + ":" + year
            return time_convert

        item_list = ["PM1", "PM2.5", "PM10", "Temperatura", "Ciśnienie", "Wilgotność"]
        menu_widget = QListWidget()
        for i in range(len(item_list)):
            item = QListWidgetItem(f"{item_list[i]}")
            menu_widget.addItem(item)

        label_1 = QLabel("Db connect", self)
        label_1.setGeometry(250, 60, 150, 100)
        if db_connection.check_db_connect() == True:
            label_1.setText("Połączono\nz bazą danych")
            label_1.setStyleSheet("color: blue")
        else:
            label_1.setText("Brak połączenia\nz bazą danych")
            label_1.setStyleSheet("color: red")

        label_2 = QLabel("DB IP ADRESS:", self)
        label_2.setGeometry(10, 2, 160, 20)

        edit_label_1 = QLineEdit(f"{self.db_ip_adress}", self)
        edit_label_1.setGeometry(10, 22, 160, 20)

        input_time_1 = QDateTimeEdit(self)
        input_time_1.setCalendarPopup(True)
        input_time_1.setGeometry(10, 200, 300, 40)

        input_time_2 = QDateTimeEdit(self)
        input_time_2.setCalendarPopup(True)
        input_time_2.setGeometry(10, 260, 300, 40)

        button_1 = QPushButton("Odśwież połaczenie\n z bazą danych", self)
        button_1.clicked.connect(
            lambda: print(
                datetime.now(),
                "Refresh Db conn",
                edit_label_1.text(),
                "\n",
            )
        )

        str_input_time_1 = input_time_1.text()
        str_input_time_2 = input_time_2.text()

        button_1.setGeometry(10, 60, 230, 100)

        combox_1 = QComboBox(self)
        combox_1.setGeometry(440, 300, 230, 60)
        combox_1.addItems(
            ["PM1", "PM2.5", "PM10", "Temperatura", "Ciśnienie", "Wilgotność"]
        )

        # user_choice_plot_var = int(list_widget_1.currentIndex())
        plot = DataView(combox_1.currentIndex())
        button_2 = QPushButton("Wyświetl przykładowe\ndane pomiarowe dla:", self)
        button_2.clicked.connect(
            lambda: print(combox_1.currentIndex())
            or (plot.plot_data_from_csv(combox_1.currentIndex() + 2)),
        )
        button_2.setGeometry(440, 200, 230, 100)


try:
    if __name__ == "__main__":
        app = QApplication()
        m = MainWindow()
        m.show()

        with open("main.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)

        sys.exit(app.exec())

except ValueError:
    pass
