import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties.
        self.resize(200, 200)

        self.chkEnabled = QCheckBox("Enabled", self)
        self.chkEnabled.move(30,40)
        self.chkEnabled.setChecked(True)
        self.chkEnabled.toggled.connect(self.evt_chkEnabled_toggled)

        self.chkTree = QCheckBox("Three State",self)
        self.chkTree.move(30,70)
        self.chkTree.setTristate(True)
        self.chkTree.stateChanged.connect(self.evt_chkThree_changed)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(40, 100)
        self.lbl.resize(100, 100)
        font = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(font)

    def evt_chkThree_changed(self,state):
        if state == 0:
            QMessageBox.information(self, "State", "Unchecked")
        elif state == 2:
            QMessageBox.information(self, "State", "Checkd")
        else:
            QMessageBox.information(self, "State", "Partially checked")


    def evt_chkEnabled_toggled(self, chkd):
        if chkd:
            self.lbl.setDisabled(False)
        else:
            self.lbl.setDisabled(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
