import sys, random, sqlite3

from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gitnd_yellow_bolls.UI import Ui_MainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Hазвание сорта", "Cтепень обжарки", "Mолотый/в зернах", "Oписание вкуса", "цена".capitalize(), "Oбъем упаковки(мл)"])
        self.update()

    def update(self):
        res = self.con.cursor().execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(res))
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
