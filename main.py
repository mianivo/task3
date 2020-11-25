from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen

import sys
import random


class Intarface:
    def __init__(self, window):
        self.window = window
        self.push_button = QPushButton(window)
        window.__setattr__('push_button', self.push_button)
        window.resize(800, 800)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        Intarface(self)
        self.flag = False
        self.circles = []

        self.push_button.clicked.connect(self.click)

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
        return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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
