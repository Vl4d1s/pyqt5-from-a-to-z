import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties

        self.lbl = QLabel("My label", self)
        self.lbl.setStyleSheet("color:red")
        self.lbl.move(50, 30)

        self.rbtRed = QRadioButton("red", self)
        self.rbtRed.move(50, 60)
        self.rbtRed.setChecked(True)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)

        self.rbtBlue = QRadioButton("blue", self)
        self.rbtBlue.move(50, 90)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)

        self.rbtGreen = QRadioButton("green", self)
        self.rbtGreen.move(50, 120)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)

    def evt_rbt_clicked(self):
        rbt = self.sender()
        ss = "color: " + rbt.text()
        self.lbl.setStyleSheet(ss)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
