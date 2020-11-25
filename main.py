from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen

import sys

import random


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.circles = []

        self.pushButton.clicked.connect(self.click)

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        self.flag = False


    def draw_circle(self, qp):
        for x, y, radius, color in self.circles:
            qp.setBrush(QBrush(color))
            qp.setPen(QPen(color))
            qp.drawEllipse(x, y, radius, radius)
        self.update()


    def get_color(self):
        return QColor(255, 255, 0)


    def click(self):
        self.circles.append((random.randint(0, self.height()),
                             random.randint(0, self.width()),
                             random.randint(1, 300),
                             self.get_color()))
        self.flag = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
