from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtGui as qg
import sys
import urllib
import urllib.request as url
from gtts import gTTS
import uuid

# fungsi message box ketika tidak ada koneksi internet
def fail_connect_msg():
    msg = qtw.QMessageBox()
    msg.setIcon(qtw.QMessageBox.Warning)
    msg.setText("Tidak terkoneksi ke internet")
    msg.setWindowTitle("Kendala")
    msg.exec()

# fungsi mengecek koneksi
def check_connection():
    try:
        url.urlopen("http://google.com")
    except:
        fail_connect_msg()
        raise Exception("Tidak ada koneksi internet ")

# fungsi message box ketika Audio berhasil disimpan
def saved_success(text):
    msg = qtw.QMessageBox()
    msg.setIcon(qtw.QMessageBox.Information)
    msg.setText("Berhasil disimpan dengan nama "+text+".mp3")
    msg.setWindowTitle("Informasi")
    msg.exec()

# Sub window dari main window
class Another(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,150)

        layout = qtw.QVBoxLayout()
        layout2 = qtw.QHBoxLayout()
        otherLayout = qtw.QFormLayout()

        self.setLayout(layout)

        self.label = qtw.QTextEdit()
        button = qtw.QPushButton("Proses")
        button2 = qtw.QPushButton("Bersihkan")
        button.clicked.connect(self.proceed)
        button2.clicked.connect(self.clear)

        otherLayout.addRow("Buat kalimat = ", self.label)
        layout2.addWidget(button)
        layout2.addWidget(button2)

        layout.addLayout(otherLayout)
        layout.addLayout(layout2)

    def clear(self):
        self.label.setText("")

    def proceed(self):
        # pemanggilan cek koneksi
        check_connection()
        # dapatkan teks dari line edit
        text = self.label.toPlainText()
        # proses text ke audio dengan gtts
        Audio = gTTS(text, lang='id')
        # proses id unik setiap Audio
        fileAudio = str(uuid.uuid4())[:8]
        # simpan audio dengan id unik
        Audio.save(fileAudio+".mp3")
        # keluarkan pesan sukses tersimpan
        saved_success(fileAudio)

class About(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,150)

        layout = qtw.QVBoxLayout()

        self.setLayout(layout)

        label = qtw.QLabel("Fajri Kusuma")
        label2 = qtw.QLabel("alfajriaskus@gmail.com")
        label3 = qtw.QLabel("https://github.com/Askus99")

        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)


class Menu(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,150)

        vlayout = qtw.QVBoxLayout()

        l1 = qtw.QLabel("Ketik dan suarakan !")
        l1.setAlignment(Qt.AlignCenter)
        l1.setStyleSheet("QLabel{font-size: 20pt}")
        b1 = qtw.QPushButton("Mulai")
        b2 = qtw.QPushButton("Tentang")

        vlayout.addWidget(l1)
        vlayout.addWidget(b1)
        vlayout.addWidget(b2)

        w = qtw.QWidget()
        w.setLayout(vlayout)
        self.setCentralWidget(w)

        self.sub = Another()
        self.abt = About()
        b1.clicked.connect(self.sub.show)
        b2.clicked.connect(self.abt.show)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    i = Menu()
    i.show()
    sys.exit(app.exec_())
