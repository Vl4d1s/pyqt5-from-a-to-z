import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties.
        self.resize(200, 200)

        self.btn = QPushButton("Dates", self)
        self.btn.move(40, 40);
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        qt = QTime(14,30,15)
        qt2 = QTime(20,30)
        qdt = QDateTime.currentDateTime()
        print(dt.dayOfWeek())
        print(dt.daysInMonth())
        print(dt.toJulianDay())
        print(dt.addDays(23).toString())
        print(qt.toString())
        print(qt2.addSecs(12).toString())
        print(qdt.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
