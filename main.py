from threading import Timer
import time
from PyQt5 import QtCore, QtGui, QtWidgets

from ui import Ui_MainWindow


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec_()