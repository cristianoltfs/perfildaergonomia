from Template.perfildaergonomia import Ui_PerfilErgonomia
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor
from cliente_sem_janela import cliente
from carta import Carta
from time import sleep
HOST = 'localhost'
PORT = 8000

class Tabu(QDialog):
    def __init__(self, nick):
        super(Tabu, self).__init__()
        self.ui = Ui_PerfilErgonomia()
        self.ui.setupUi(self)
        self.ui.btnCarta_2.clicked.connect(self.tiraCarta)
        #self.ui.btnPontos.clicked.connect(self.enviaPontos)
        self.player = cliente(HOST, PORT, nick)
        #self.ui.leJogador1.setDisabled(1)
        #self.ui.leJogador2.setDisabled(1)
        #self.ui.leJogador3.setDisabled(1)
        #self.ui.leJogador4.setDisabled(1)
        #self.ui.leJogador5.setDisabled(1)
        #self.ui.leJogador6.setDisabled(1)
        #self.ui.leJogador7.setDisabled(1)
        #self.ui.leJogador8.setDisabled(1)


    def enviaPontos(self):
        self.ui.leJogador1.setText('LUCAS')
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
        sleep(1)
        self.atualiza()

    def atualiza(self):
        arquivo = open('ptsServer.csv', 'r')
        vet = arquivo.readline()
        arquivo.close()
        atual = vet.replace("[", "")
        atual = atual.replace("]", "")
        atual = atual.replace("'", "")
        vetPontos = atual.split(',')

        valor1 = int(vetPontos[0]) + int(self.ui.lePontJog1.text())
        print(valor1)
        self.ui.leJogador1.setText(vetPontos[0])
        self.ui.leJogador2.setText(vetPontos[1])
        self.ui.leJogador3.setText(vetPontos[2])
        self.ui.leJogador4.setText(vetPontos[3])
        self.ui.leJogador5.setText(vetPontos[4])
        self.ui.leJogador6.setText(vetPontos[5])
        self.ui.leJogador7.setText(vetPontos[6])
        self.ui.leJogador8.setText(vetPontos[7])
        return

    def tiraCarta(self):
        dfCarta = self.player.carta()
        # Chamando o form da carta
        frmCarta = Carta(dfCarta)
        frmCarta.exec_()

