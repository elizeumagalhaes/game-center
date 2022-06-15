from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel


class TicTacToe(QtWidgets.QMainWindow):
    def __init__(self):
        super(TicTacToe, self).__init__()

        # CONTADOR DE JOGADAS
        self.count = 0

        # INICIANDO A JANELA
        self.tic_tac_toe = uic.loadUi("pyqt/tictactoe.ui")

        # DEFININDO OBJETOS
        self.button1 = self.tic_tac_toe.findChild(QPushButton, "btn1")
        self.button2 = self.tic_tac_toe.findChild(QPushButton, "btn2")
        self.button3 = self.tic_tac_toe.findChild(QPushButton, "btn3")
        self.button4 = self.tic_tac_toe.findChild(QPushButton, "btn4")
        self.button5 = self.tic_tac_toe.findChild(QPushButton, "btn5")
        self.button6 = self.tic_tac_toe.findChild(QPushButton, "btn6")
        self.button7 = self.tic_tac_toe.findChild(QPushButton, "btn7")
        self.button8 = self.tic_tac_toe.findChild(QPushButton, "btn8")
        self.button9 = self.tic_tac_toe.findChild(QPushButton, "btn9")
        self.btn_reset = self.tic_tac_toe.findChild(QPushButton, "btn_playagain")
        self.lbl_msg = self.tic_tac_toe.findChild(QLabel, "lbl_turn")

        # RELACIONANDO CLIQUE COM FUNÇÃO CLICAR
        self.button1.clicked.connect(self.click)
        self.button2.clicked.connect(self.click)
        self.button3.clicked.connect(self.click)
        self.button4.clicked.connect(self.click)
        self.button5.clicked.connect(self.click)
        self.button6.clicked.connect(self.click)
        self.button7.clicked.connect(self.click)
        self.button8.clicked.connect(self.click)
        self.button9.clicked.connect(self.click)
        self.btn_reset.clicked.connect(self.reset)

        # MENSAGEM DE INICIO
        self.lbl_msg.setText("X Goes First!")

        # EXIBINDO JANELA
        self.tic_tac_toe.show()

    # CHECAR VITÓRIA
    def check_Win(self):
        # HORIZONTAL
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1, self.button4, self.button7)

        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2, self.button5, self.button8)

        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3, self.button6, self.button9)

        # VERTICAL
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1, self.button2, self.button3)

        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4, self.button5, self.button6)

        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7, self.button8, self.button9)

        # DIAGONAL
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1, self.button5, self.button9)

        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3, self.button5, self.button7)

    def win(self, a, b, c):
        # MUDANDO COR DOS BOTÕES
        a.setStyleSheet('QPushButton {color: yellow; background-color: transparent;}')
        b.setStyleSheet('QPushButton {color: yellow; background-color: transparent;}')
        c.setStyleSheet('QPushButton {color: yellow; background-color: transparent;}')

        # EXIBIR A MENSAGEM DE VENCEDOR
        self.lbl_msg.setText(f"{a.text()} Wins!")

        # DESABILITANDO OS BOTÕES
        self.disable()

    def disable(self):
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9, ]

        for b in button_list:
            b.setEnabled(False)

    # FUNÇÕES DO CÓDIGO
    def click(self):
        b = self.sender()
        if self.count % 2 == 0:
            b.setText('X')
            self.lbl_msg.setText("O's Turn")
        else:
            b.setText('O')
            self.lbl_msg.setText("X's Turn")

        b.setEnabled(False)
        self.count += 1
        self.check_Win()

    def reset(self):
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9, ]

        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet('QPushButton {color: white; background-color: transparent;}')

        self.lbl_msg.setText("X Goes First!")

        self.count = 0
