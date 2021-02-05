import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties
        self.resize(200, 200)

        self.btn = QPushButton("Choose Color", self)
        self.btn.move(40, 40);
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # We can pass other type of colors like: rgb, rgba, name strings and more
        color = QColorDialog.getColor(QColor("FF0000"),self,"Choose Color")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
