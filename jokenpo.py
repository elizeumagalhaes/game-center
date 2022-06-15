import random
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel


class JokenPo(QtWidgets.QMainWindow):

    choices = ["stone", "paper", "scissors"]
    choice = ""
    user_choice = ""

    def __init__(self):
        super(JokenPo, self).__init__()

        # INICIANDO A JANELA
        self.jokenpo = uic.loadUi("pyqt/jokenpo.ui")

        # DEFININDO BOTÕES
        self.btn_stone = self.jokenpo.findChild(QPushButton, "btn_stone")
        self.btn_paper = self.jokenpo.findChild(QPushButton, "btn_paper")
        self.btn_scissors = self.jokenpo.findChild(QPushButton, "btn_scissors")
        self.btn_reset = self.jokenpo.findChild(QPushButton, "btn_reset")
        self.lbl_msg = self.jokenpo.findChild(QLabel, "lbl_msg")
        self.lbl_computer = self.jokenpo.findChild(QLabel, "jogada")

        # RELACIONANDO FUNÇÃO DO BOTÃO COM BOTÃO
        self.btn_stone.clicked.connect(self.stone)
        self.btn_paper.clicked.connect(self.paper)
        self.btn_scissors.clicked.connect(self.scissors)
        self.btn_reset.clicked.connect(self.reset)

        # SORTEIA ALGO
        self.draw()

        # EXIBINDO JANELA
        self.jokenpo.show()

    def verify_win(self):
        if self.user_choice == "paper" and self.choice == "stone":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("You win!")
        elif self.user_choice == "stone" and self.choice == "paper":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("You lose!")
        elif self.user_choice == "scissors" and self.choice == "paper":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("You win!")
        elif self.user_choice == "paper" and self.choice == "scissors":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("You lose!")
        elif self.user_choice == "stone" and self.choice == "scissors":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("You win!")
        elif self.user_choice == "scissors" and self.choice == "stone":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("You lose!")
        elif self.user_choice == "paper" and self.choice == "paper":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("A tie!")
        elif self.user_choice == "stone" and self.choice == "stone":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("A tie!")
        elif self.user_choice == "scissors" and self.choice == "scissors":
            self.lbl_computer.setText(f"💻 {JokenPo.choice}")
            self.lbl_msg.setText("A tie!")

        self.btn_stone.setEnabled(False)
        self.btn_paper.setEnabled(False)
        self.btn_scissors.setEnabled(False)

    def stone(self):
        self.user_choice = "stone"
        self.verify_win()

    def paper(self):
        self.user_choice = "paper"
        self.verify_win()

    def scissors(self):
        self.user_choice = "scissors"
        self.verify_win()

    def draw(self):
        JokenPo.choice = random.choice(JokenPo.choices)

    def reset(self):
        self.draw()
        self.btn_stone.setEnabled(True)
        self.btn_paper.setEnabled(True)
        self.btn_scissors.setEnabled(True)
