from cProfile import label
from msilib.schema import LaunchCondition
import sys
from turtle import right
from PySide6.QtCore import QRect,Qt
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
    QLineEdit

    
    
)

from datetime import datetime

from database.db_connect import DbConnection

class MainWindow(QLabel):
    def __init__(self, parent=None):
        
        self.db_ip_adress = '192.168.55.115' 
        
        super(MainWindow, self).__init__()
        
        db_connection = DbConnection()

        MainWindow.setGeometry(self,300,300,700,520)

        item_list = ['PM1','PM2.5','PM10','Temperatura','Ciśnienie', 'Wilgotność']
        menu_widget = QListWidget()
        for i in range(len(item_list)):
            item = QListWidgetItem(f"{item_list[i]}")
            menu_widget.addItem(item)      
             
        label_1 = QLabel("Db connect", self)
        label_1.setGeometry(250,60, 150 ,100)
        if db_connection.check_db_connect() == True:
            label_1.setText("Połączono\nz bazą danych")
            label_1.setStyleSheet('color: blue')
        else:
            label_1.setText("Brak połączenia\nz bazą danych")
            label_1.setStyleSheet('color: red')
            
        edit_label_1 = QLineEdit(f'Adres IP bazy danych {self.db_ip_adress}', self)
        edit_label_1.setGeometry(10, 2, 160,20)
        
        menu_widget.setGeometry(QRect(30,30,200,21))
        
        button_1 = QPushButton('Odśwież połaczenie\n z bazą danych', self)
        button_1.clicked.connect(lambda: print(datetime.now(),"Refresh Db conn", edit_label_1.text()))
        button_1.setGeometry(10,60,230,100)    
        


if __name__ == "__main__":
    app = QApplication()
    m = MainWindow()
    m.show()

    with open("main.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
