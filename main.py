import io
import sys
from random import randint

from templateFile import template
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QMainWindow, QApplication


class YellowEllipce(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.draw)
        self.drawingFlag = False

    def paintEvent(self, event):
        if self.drawingFlag:
            painter = QPainter(self)

            painter.setBrush(QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255))))

            center_x = self.width() // 2
            center_y = self.height() // 2
            radius = randint(10, 500)
            painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)
            self.drawingFlag = False

    def draw(self):
        self.drawingFlag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowEllipce()
    ex.show()
    sys.exit(app.exec())
