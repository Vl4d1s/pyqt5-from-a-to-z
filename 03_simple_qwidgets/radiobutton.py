import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties

        self.lbl = QLabel("My label", self)
        self.lbl.setStyleSheet("color:red; font-size:15px")
        self.lbl.move(50, 30)

        # Color Button Group
        self.btgColor = QButtonGroup()

        self.rbtRed = QRadioButton("red", self)
        self.rbtRed.move(50, 60)
        self.rbtRed.setChecked(True)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtRed)

        self.rbtBlue = QRadioButton("blue", self)
        self.rbtBlue.move(50, 90)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtBlue)

        self.rbtGreen = QRadioButton("green", self)
        self.rbtGreen.move(50, 120)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtGreen)

        # Text size button
        self.btgSize = QButtonGroup()
        self.rbtSmall = QRadioButton("Small text", self)
        self.rbtSmall.move(50,150)
        self.btgSize.addButton(self.rbtSmall,10)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)

        self.rbtMedium = QRadioButton("Medium text", self)
        self.rbtMedium.setChecked(True)
        self.rbtMedium.move(50,180)
        self.btgSize.addButton(self.rbtMedium,15)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)

        self.rbtLarge = QRadioButton("Large text", self)
        self.rbtLarge.move(50,210)
        self.btgSize.addButton(self.rbtLarge,20)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)

    def evt_rbt_clicked(self):
        clr = self.btgColor.checkedButton()
        size = self.btgSize.checkedId()
        ss = "color:" + clr.text() + "; font-size:" + str(size) + "px"
        self.lbl.setStyleSheet(ss)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
