from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
import random
from face import Ui_MainWindow


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circle)
        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        w = random.randint(10, 100)
        x = random.randint(10, 500 - w)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor(*[random.randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, x, x + w, x + w)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())