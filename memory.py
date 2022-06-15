from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel

class MemoryGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(MemoryGame, self).__init__()

        self.memory = uic.loadUi("pyqt/memory.ui")

        self.memory.show()
