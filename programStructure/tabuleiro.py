from Template.perfildaergonomia import Ui_PerfilErgonomia
from PyQt5.QtWidgets import *
from cliente_sem_janela import cliente
from carta import Carta


HOST = 'localhost'
PORT = 8000

class Tabuleiro(QDialog):
    def __init__(self, nick):
        super(Tabuleiro, self).__init__()
        self.ui = Ui_PerfilErgonomia()
        self.ui.setupUi(self)
        self.ui.btnCarta_2.clicked.connect(self.tiraCarta)
        self.player = cliente(HOST, PORT, nick)

    def tiraCarta(self):
        carta_df = self.player.carta()
        print('!!!!!!!!!!!!!!!!!!!!!')
        print(self.player.carta())
        print("*********************")

        #Chamando o form da carta
        frmCarta = Carta()
        frmCarta.exec_()



        #Ler a carta
        #Imprimir a carta na tela carta

