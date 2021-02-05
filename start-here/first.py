import sys
from PyQt5.QtWidgets import *  # imports section

app = QApplication(sys.argv)  # create application
dlgMain = QDialog()  # create main GUI canvas
dlgMain.setWindowTitle("My GUI")
dlgMain.show()  # show the GUI

sys.exit(app.exec_())  # execute the application
