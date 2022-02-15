from msilib.schema import LaunchCondition
import sys
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
    
    
)

class MainWindow(QLabel):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        MainWindow.setGeometry(self,300,300,700,520)

        item_list = ['PM1','PM2.5','PM10','Temperatura','Ciśnienie', 'Wilgotność']
        menu_widget = QListWidget()
        for i in range(len(item_list)):
            item = QListWidgetItem(f"{item_list[i]}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)           

        menu_widget.setGeometry(QRect(30,30,20,21))

        text_widget = QLabel("_placeholder")
        button = QPushButton("Pobierz Dane z bazy danych")
        button.show()
        button.setGeometry(QRect(0,30,40,20))

        
        


if __name__ == "__main__":
    app = QApplication()
    m = MainWindow()
    m.show()

    with open("main.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
