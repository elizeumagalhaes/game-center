import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit


class HangMan(QtWidgets.QMainWindow):

    palavras = ["Laranja", "Cadeira", "Baleia", "Oculos", "Curitiba"]
    dicas = ["Fruta", "Objeto", "Animal", "Acessório", "Cidade"]
    letras_certas = []
    letras_chutadas = []
    palavra_sorteada = ''
    palavra_oculta = ''
    chute = ''
    erros = 0

    listaa = []

    def __init__(self):
        super(HangMan, self).__init__()

        # INICIANDO TELA DO JOGO
        self.hangman = uic.loadUi("pyqt/hangman.ui")

        # INICIANDO BOTOES E LABELS
        self.btn_chute = self.hangman.findChild(QPushButton, "btn_chute")
        self.lbl_dica = self.hangman.findChild(QLabel, "lbl_dica")
        self.lbl_palavra = self.hangman.findChild(QLabel, "lbl_palavra")
        self.box_chute = self.hangman.findChild(QLineEdit, "box_chute")
        self.lbl_chutes_errados = self.hangman.findChild(QLabel, "lbl_chutes")
        self.head = self.hangman.findChild(QLabel, "head")
        self.camisa = self.hangman.findChild(QLabel, "tshirt")
        self.left_arm = self.hangman.findChild(QLabel, "left_arm")
        self.right_arm = self.hangman.findChild(QLabel, "right_arm")
        self.left_leg = self.hangman.findChild(QLabel, "left_leg")
        self.right_leg = self.hangman.findChild(QLabel, "right_leg")
        self.msg_vitoria = self.hangman.findChild(QLabel, "msg_vitoria")
        self.forca = self.hangman.findChild(QLabel, "forca")
        self.anjo = self.hangman.findChild(QLabel, "anjo")
        self.trofeu = self.hangman.findChild(QLabel, "trofeu")

        self.hangman.btn_chute.clicked.connect(self.verificar_erro)

        # SORTEANDO DICA E PALAVRA
        self.sortear()

        self.head.setHidden(True)
        self.camisa.setHidden(True)
        self.left_arm.setHidden(True)
        self.right_arm.setHidden(True)
        self.left_leg.setHidden(True)
        self.right_leg.setHidden(True)
        self.msg_vitoria.setHidden(True)
        self.anjo.setHidden(True)
        self.trofeu.setHidden(True)

        # EXIBINDO TELA DO JOGO
        self.hangman.show()

    def sortear(self):
        x = random.randint(0, 4)
        self.palavra_sorteada = self.palavras[x].upper()
        dica = self.dicas[x]
        self.lbl_dica.setText(f"Dica: {dica}")
        self.exibir_palavra()

    def exibir_palavra(self):
        for letra in self.palavra_sorteada:
            if letra in self.letras_certas:
                self.palavra_oculta += " " + letra
            else:
                self.palavra_oculta += " _"
        self.lbl_palavra.setText(self.palavra_oculta)
        self.palavra_oculta = ""

    def verificar_erro(self):
        self.chute = self.box_chute.text().upper()
        if self.chute in self.palavra_sorteada:
            quantas_tem = self.palavra_sorteada.count(self.chute)
            for i in range(quantas_tem):
                self.letras_certas.append(self.chute)
            self.box_chute.setText("")
            self.exibir_palavra()
            if len(self.letras_certas) == len(self.palavra_sorteada):
                self.vitoria()
        else:
            if self.chute in self.letras_chutadas:
                pass
            else:
                self.letras_chutadas.append(self.chute)
                self.lbl_chutes_errados.setText(str(self.letras_chutadas))
                self.box_chute.setText("")
                self.erros += 1
                self.desenho()

    def desenho(self):
        if self.erros == 1:
            self.head.setHidden(False)
        if self.erros == 2:
            self.camisa.setHidden(False)
        if self.erros == 3:
            self.left_arm.setHidden(False)
        if self.erros == 4:
            self.right_arm.setHidden(False)
        if self.erros == 5:
            self.left_leg.setHidden(False)
        if self.erros == 6:
            self.head.setHidden(True)
            self.camisa.setHidden(True)
            self.left_arm.setHidden(True)
            self.right_arm.setHidden(True)
            self.left_leg.setHidden(True)
            self.right_leg.setHidden(True)
            self.box_chute.setHidden(True)
            self.btn_chute.setHidden(True)
            self.lbl_dica.setHidden(True)
            self.lbl_chutes_errados.setHidden(True)
            self.forca.setHidden(True)
            self.msg_vitoria.setHidden(False)
            self.anjo.setHidden(False)
            self.lbl_palavra.setText(self.palavra_sorteada)
            self.msg_vitoria.setText("Você perdeu!")

    def vitoria(self):
        self.box_chute.setHidden(True)
        self.btn_chute.setHidden(True)
        self.lbl_dica.setHidden(True)
        self.forca.setHidden(True)
        self.head.setHidden(True)
        self.camisa.setHidden(True)
        self.left_arm.setHidden(True)
        self.right_arm.setHidden(True)
        self.left_leg.setHidden(True)
        self.right_leg.setHidden(True)
        self.msg_vitoria.setHidden(False)
        self.trofeu.setHidden(False)
        self.msg_vitoria.setText("Você venceu!")
        self.lbl_palavra.setText(self.palavra_sorteada)
