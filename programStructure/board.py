from Template.perfildaergonomia import Ui_PerfilErgonomia
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor
from cliente_sem_janela import cliente
from carta import Carta

HOST = 'localhost'
PORT = 8000




p2 = int(self.ui.leJogador2.text())
        p3 = int(self.ui.leJogador3.text())
        p4 = int(self.ui.leJogador4.text())
        if self.ui.leJogador5.text() != "":
            p5 = int(self.ui.leJogador5.text())
        if self.ui.leJogador6.text() != "":
            p6 = int(self.ui.leJogador6.text())
        if self.ui.leJogador7.text() != "":
            p7 = int(self.ui.leJogador7.text())
        if self.ui.leJogador8.text() != "":
            p8 = int(self.ui.leJogador8.text())
        else:




class Tabu(QDialog):
    def __init__(self, nick):
        super(Tabu, self).__init__()
        self.ui = Ui_PerfilErgonomia()
        self.ui.setupUi(self)
        self.ui.btnCarta_2.clicked.connect(self.tiraCarta)
        self.ui.btnPontos.clicked.connect(self.enviaPontos)
        self.player = cliente(HOST, PORT, nick)
        self.ui.leJogador1.setDisabled(1)
        self.ui.leJogador2.setDisabled(1)
        self.ui.leJogador3.setDisabled(1)
        self.ui.leJogador4.setDisabled(1)
        self.ui.leJogador5.setDisabled(1)
        self.ui.leJogador6.setDisabled(1)
        self.ui.leJogador7.setDisabled(1)
        self.ui.leJogador8.setDisabled(1)


    def enviaPontos(self):
        vetPont = []
        # Pega as pontuações do line edit
        vetPont.append(self.ui.lePontJog1.text())
        vetPont.append(self.ui.lePontJog2.text())
        vetPont.append(self.ui.lePontJog3.text())
        vetPont.append(self.ui.lePontJog4.text())
        vetPont.append(self.ui.lePontJog5.text())
        vetPont.append(self.ui.lePontJog6.text())
        vetPont.append(self.ui.lePontJog7.text())
        vetPont.append(self.ui.lePontJog8.text())

        self.player.enviar_pontos(vetPont)
        print("AQUI")
        #self.player.visualizar_ranking()

    def tiraCarta(self):
        dfCarta = self.player.carta()
        print('!!!!!!!!!!!!!!!!!!!!!')
        print("*********************")

        #Chamando o form da carta
        frmCarta = Carta(dfCarta)
        frmCarta.exec_()

