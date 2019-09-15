# -- coding: utf-8 --

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow

from Design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.indexmass)
        self.listWidget.clicked.connect(self.getgender)

    def getgender(self):
        global gender
        gender = str(self.listWidget.currentItem().text())

    def indexmass(self):
        try:
            weight = int(self.lineEdit.text())
            height = int(self.lineEdit_2.text())
            if (weight or height) < 0:
                self.textEdit.setText('Do not enter negative values!')
            else:
                result = round(weight/((height/100)**2), 1)
                global Names
                Names = ['Weight deficit', 'Standard', 'Slight overweight', 'Obesity',
                         'Obesity dangerous for health']
                if gender == 'Male':
                    bins_males = [(0, 20), (20, 25), (25, 30), (30, 40), (40, 1000)]
                    List_bins_males = []
                    for i in bins_males:
                        List_bins_males.append(pd.Interval(i[0], i[1], closed='left'))
                    List_bins_males = list(zip(List_bins_males, Names))
                    for x, i in List_bins_males:
                        if result in x:
                            global comment
                            comment = i
                if gender == 'Female':
                    bins_females = [(0, 19), (19, 24), (24, 30), (30, 40), (40, 1000)]
                    List_bins_females = []
                    for i in bins_females:
                        List_bins_females.append(pd.Interval(i[0], i[1], closed='left'))
                    List_bins_females = list(zip(List_bins_females, Names))
                    for x, i in List_bins_females:
                        if result in x:
                            comment = i
                self.textEdit.setText(str(result) + ' ' + comment)
        except ValueError:
            self.textEdit.setText('')


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

main()

