import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties.
        self.resize(200, 200)

        self.btn = QPushButton("Change label", self)
        self.btn.move(40, 40)
        self.btn.resize(120,50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(40, 100)
        self.lbl.resize(100,100)
        font = QFont("Times New Roman", 20,75,True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        str = """
        <h5>Header</h5>
            <ul>
                <li>Red</li>
                <li>Blue</li>
            </ul>
        """
        self.lbl.setText(str)
        pxm = QPixmap("photos/bear.jpg").scaled(100,100)
        self.lbl.setPixmap(pxm)
        self.lbl.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
