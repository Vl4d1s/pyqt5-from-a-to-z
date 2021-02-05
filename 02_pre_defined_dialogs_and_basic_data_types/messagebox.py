import sys
from PyQt5.QtWidgets import *  # imports section


def evt_btn_clicked():
    # we cant also replace question with: information, critical, warning
    # res = QMessageBox.question(self, "Disk Full", "Your disk drive is almost full")
    # if res == QMessageBox.Yes:
    #     QMessageBox.information(self,"","You clicked Yes")
    # else:
    #     QMessageBox.information(self,"","You clicked No")

    msg_disk_full = QMessageBox()
    msg_disk_full.setText("Your hard disk is almost full")
    msg_disk_full.setDetailedText("Please make room on your disk")
    msg_disk_full.setIcon(QMessageBox.Information)
    msg_disk_full.setWindowTitle("Full Disk")
    msg_disk_full.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_disk_full.exec_()


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties
        self.resize(200, 200)

        self.btn = QPushButton("ShowMessage", self)
        self.btn.move(40, 40);
        self.btn.clicked.connect(evt_btn_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
