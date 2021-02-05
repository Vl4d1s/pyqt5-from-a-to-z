import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties.
        self.resize(200, 200)

        self.btn = QPushButton("Choose Font", self)
        self.btn.move(40, 40);
        font = QFont("Time New Roman", 16,75,True)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # We can pass other type of colors like: rgb, rgba, name strings and more
        font, bOk = QFontDialog.getFont()
        print(font,bOk)
        if bOk:
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.pointSize())
            print(font.family())
            self.btn.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
