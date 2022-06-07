from PyQt5 import uic, QtWidgets
import sys
from tictactoe import TicTacToe
from jokenpo import JokenPo
from hangman import HangMan


class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuPrincipal, self).__init__()

        self.menu = uic.loadUi("pyqt/tela.ui")

        self.menu.btn_hangman.clicked.connect(self.show_hangman)
        self.menu.btn_tictactoe.clicked.connect(self.show_tictactoe)
        self.menu.btn_jokenpo.clicked.connect(self.show_jokenpo)

        self.menu.show()

    def show_hangman(self):
        self.game = HangMan()

    def show_tictactoe(self):
        self.game = TicTacToe()

    def show_jokenpo(self):
        self.game = JokenPo()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu = MenuPrincipal()
    app.exec()
