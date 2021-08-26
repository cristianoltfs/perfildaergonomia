from Template.perfildaergonomia import Ui_PerfilErgonomia
from PyQt5.QtWidgets import *


class Tabuleiro(QDialog):
    def __init__(self, *args, **kwargs):
        super(Tabuleiro, self).__init__(*args, **kwargs)
        self.ui = Ui_PerfilErgonomia()
        self.ui.setupUi(self)


