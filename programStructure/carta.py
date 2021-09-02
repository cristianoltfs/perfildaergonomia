from Template.carta import Ui_carta
from PyQt5.QtWidgets import QDialog


class Carta(QDialog):
    def __init__(self, *args, **kwargs):
        super(Carta, self).__init__(*args, **kwargs)
        self.ui = Ui_carta()
        self.ui.setupUi(self)
        self.ui.btnCarta_2.clicked.connect(self.sair)

    def sair(self):
        self.close()