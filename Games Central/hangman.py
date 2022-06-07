import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit


class HangMan(QtWidgets.QMainWindow):

    palavras = ["Abóbora", "Lápis", "Baleia"]
    dicas = ["Vegetal", "Objeto", "Animal"]
    chutes = []
    palavra_sorteada = ''
    palavra_oculta = ''
    chute_errado = 1

    def __init__(self):
        super(HangMan, self).__init__()

        # INICIANDO TELA DO JOGO
        self.hangman = uic.loadUi("pyqt/jogodaforca.ui")

        # INICIANDO BOTOES E LABELS
        self.btn_chute = self.hangman.findChild(QPushButton, "btn_chute")
        self.lbl_dica = self.hangman.findChild(QLabel, "lbl_dica")
        self.lbl_palavra = self.hangman.findChild(QLabel, "lbl_palavra")
        self.cabeca = self.hangman.findChild(QLabel, "lbl_cabeca")

        # SORTEANDO DICA E PALAVRA
        self.sortear()

        # EXIBINDO TELA DO JOGO
        self.hangman.show()

    def sortear(self):
        x = random.randint(0, 2)
        self.palavra_sorteada = self.palavras[x]
        dica = self.dicas[x]
        self.lbl_dica.setText(f"Dica: {dica}")
        print(self.palavra_sorteada)
        self.imprimir_palavra()

    def imprimir_palavra(self):
        self.palavra_oculta = ' _ ' * len(self.palavra_sorteada)
        self.lbl_palavra.setText(self.palavra_oculta)

    def verificar_erro(self):
        if self.chute_errado == 1:
            print("erro 1")
        if self.chute_errado == 2:
            print("erro 2")
        if self.chute_errado == 3:
            print("erro 3")
        if self.chute_errado == 4:
            print("erro 4")
        if self.chute_errado == 5:
            print("erro 5")
        if self.chute_errado == 6:
            print("erro 6")
