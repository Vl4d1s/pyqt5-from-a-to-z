import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties
        self.resize(200, 200)

        self.btn = QPushButton("Show Input", self)
        self.btn.move(40, 40);
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # also have: getText, getDouble, getItem and more...
        iAge, bOk = QInputDialog.getInt(self, "Text", "Enter your Age:", 18, 18, 65, 1)
        if bOk:
            QMessageBox.information(self, "Name", "Your age is " + str(iAge))
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
