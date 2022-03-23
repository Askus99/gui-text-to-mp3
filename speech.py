from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtGui as qg
import sys

class Another(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,150)
        layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class Menu(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,150)

        vlayout = qtw.QVBoxLayout()


        l1 = qtw.QLabel("Ketik dan suarakan !")
        b1 = qtw.QPushButton("Mulai")
        b2 = qtw.QPushButton("Tentang")

        vlayout.addWidget(l1)
        vlayout.addWidget(b1)
        vlayout.addWidget(b2)

        w = qtw.QWidget()
        w.setLayout(vlayout)
        self.setCentralWidget(w)

        self.sub = Another()
        b1.clicked.connect(self.sub.show)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    i = Menu()
    i.show()
    sys.exit(app.exec_())
