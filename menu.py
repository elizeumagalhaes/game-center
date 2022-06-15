from PyQt5 import uic, QtWidgets
import sys
from memory import MemoryGame
from tictactoe import TicTacToe
from jokenpo import JokenPo
from hangman import HangMan


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()

        self.menu = uic.loadUi("pyqt/tela.ui")

        self.menu.btn_hangman.clicked.connect(self.show_hangman)
        self.menu.btn_tictactoe.clicked.connect(self.show_tictactoe)
        self.menu.btn_jokenpo.clicked.connect(self.show_jokenpo)
        self.menu.btn_memory.clicked.connect(self.show_memory)

        self.menu.show()

    def show_hangman(self):
        self.game = HangMan()

    def show_tictactoe(self):
        self.game = TicTacToe()

    def show_jokenpo(self):
        self.game = JokenPo()

    def show_memory(self):
        self.game = MemoryGame()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu = MainMenu()
    app.exec()
