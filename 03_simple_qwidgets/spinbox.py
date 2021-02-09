import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties

        self.spbInt = QSpinBox(self)
        self.spbInt.move(50, 50)
        self.spbInt.setWrapping(True)
        self.spbInt.setRange(0, 10000)
        self.spbInt.setSingleStep(200)
        self.spbInt.setValue(1000)
        self.spbInt.valueChanged.connect(self.evt_spbInt_valueChanged)
        self.spbInt.editingFinished.connect(self.evt_spbInt_editingFinished)

        self.spbDbl = QDoubleSpinBox(self)
        self.spbDbl.move(50, 80)
        self.spbDbl.setDecimals(5)
        self.spbDbl.setSingleStep(0.1)
        self.spbDbl.setPrefix("Latitde: ")
        self.spbDbl.setSuffix(chr(176))
        self.spbDbl.setRange(-90, 90)
        self.spbDbl.valueChanged.connect(self.evt_spbInt_valueChanged)

    def evt_spbInt_valueChanged(self, val):
        print(val, val % 200)
        if (val % 200):
            self.spbInt.setStyleSheet('color: red')
        else:
            self.spbInt.setStyleSheet('color: black')

    def evt_spbDbl_valueChanged(self, val):
        print(self.spbDbl.text())
        print(self.spbDbl.value())

    def evt_spbInt_editingFinished(self):
        if self.spbInt.value() % 200:
            QMessageBox.critical(self,"Invaled Number","Invalid value entered \n\n Must be devesible by 200")
            self.spbInt.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
