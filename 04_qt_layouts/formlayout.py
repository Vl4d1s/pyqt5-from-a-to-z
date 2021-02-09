import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties

#         Create widgets
        self.ledFname = QLineEdit("Vladis")
        self.ledLname = QLineEdit("Markin")
        self.dteStarted = QDateTimeEdit()
        self.spbAge = QSpinBox()
        self.btnSubmit = QPushButton("Submit")

#         Setup Layouts
        self.mainLayout = QFormLayout()
        self.mainLayout.setLabelAlignment(Qt.AlignLeft)
        self.mainLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.mainLayout.addRow("First Name:", self.ledFname)
        self.mainLayout.addRow("First Name:", self.ledLname)
        self.mainLayout.addRow("Date started:", self.dteStarted)
        self.mainLayout.addRow("Age:", self.spbAge)
        self.mainLayout.addRow("", self.btnSubmit)

        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
