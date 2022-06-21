from PyQt5.QtWidgets import *
from gui.mainWindowLogic import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
