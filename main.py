import sys
from UI_py import Ui_MainWindow as new_version
from random import randint, randrange
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow, new_version):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.status = None
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.picture_coords = [(390, 580, 51, 321)]
            for i in range(randint(3, 12)):
                self.i = QPainter()
                self.i.begin(self)
                self.draw(self.i)
                self.i.end()

    def draw(self, picture):
        while True:
            a = randint(20, 100)
            h = randint(1, 700)
            w = randint(1, 1300)
            you_can_draw = True
            for j in self.picture_coords:
                other_h = j[0]
                other_w = j[1]
                if (h > other_h and h < other_h + j[2])\
                   or (w > other_w and w < other_w + j[3])\
                   or (h + a > other_h and h + a < other_h + j[2])\
                   or (w + a > other_w and w + a < other_w + j[3]):
                    you_can_draw = False
            if you_can_draw:
                picture.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
                picture.drawEllipse(w, h, a, a)
                self.picture_coords.append((h, w, a, a))
                break


if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=MyWidget()
    form.show()
    sys.exit(app.exec_())
