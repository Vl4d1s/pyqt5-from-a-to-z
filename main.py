import sys
from PyQt5.QtWidgets import *  # imports section


# app = QApplication(sys.argv)  # create application
# dlgMain = QDialog()  # create main GUI canvas
# dlgMain.setWindowTitle("My GUI")
# dlgMain.show()  # show the GUI
#
# sys.exit(app.exec_())  # execute the application

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties
        self.resize(200, 200)
        self.ledText = QLineEdit("My GUI", self)
        self.ledText.move(35, 50)
        self.btnUpdate = QPushButton("Update Window Title", self)
        self.btnUpdate.move(45, 80)
        self.btnUpdate.clicked.connect(self.evt_btnUpdate_clicked)

    def evt_btnUpdate_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
