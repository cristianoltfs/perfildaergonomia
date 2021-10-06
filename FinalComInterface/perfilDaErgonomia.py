from template.perfildaergonomia import Ui_PerfilErgonomia
from PyQt5.QtWidgets import *
import sys
from carta import Carta
from cliente import cliente
from PyQt5.QtWidgets import QDialog
import pandas as pd
PORT = 8000
HOST = '200.239.165.217'

class Tabuleiro(QDialog):
    def __init__(self):
        super(Tabuleiro, self).__init__()
        self.ui = Ui_PerfilErgonomia()
        self.ui.setupUi(self)
        self.ui.btnCarta.clicked.connect(self.carta)
        self.player = cliente(HOST, PORT)
        self.ui.btnPontos.clicked.connect(self.verPontos)
        self.ui.btnAtualizaPontos.clicked.connect(self.enviarPontos)
        self.ui.lePontJog1.setText("0")
        self.ui.lePontJog2.setText("0")
        self.ui.lePontJog3.setText("0")
        self.ui.lePontJog4.setText("0")
        self.ui.lePontJog5.setText("0")
        self.ui.lePontJog6.setText("0")
        self.ui.lePontJog7.setText("0")
        self.ui.lePontJog8.setText("0")
        self.ui.leJogador1.setDisabled(1)
        self.ui.leJogador2.setDisabled(1)
        self.ui.leJogador3.setDisabled(1)
        self.ui.leJogador4.setDisabled(1)
        self.ui.leJogador5.setDisabled(1)
        self.ui.leJogador6.setDisabled(1)
        self.ui.leJogador7.setDisabled(1)
        self.ui.leJogador8.setDisabled(1)




    def carta(self):
        dfCarta = self.player.carta()
        # Chamando o form da carta
        frmCarta = Carta(dfCarta)
        frmCarta.exec_()

    def enviarPontos(self):
        listaPontos = self.player.visualizar_ranking()
        print("PRINT", listaPontos.iloc[1, 1])
        self.ui.leJogador1.setText(str(listaPontos.iloc[0, 1]))
        self.ui.leJogador2.setText(str(listaPontos.iloc[1, 1]))
        self.ui.leJogador3.setText(str(listaPontos.iloc[2, 1]))
        self.ui.leJogador4.setText(str(listaPontos.iloc[3, 1]))
        self.ui.leJogador5.setText(str(listaPontos.iloc[4, 1]))
        self.ui.leJogador6.setText(str(listaPontos.iloc[5, 1]))
        self.ui.leJogador7.setText(str(listaPontos.iloc[6, 1]))
        self.ui.leJogador8.setText(str(listaPontos.iloc[7, 1]))


    def verPontos(self):
        vetPont = []
        # Pega as pontuações do line edit
        vetPont.append(int(self.ui.lePontJog1.text()))
        vetPont.append(int(self.ui.lePontJog2.text()))
        vetPont.append(int(self.ui.lePontJog3.text()))
        vetPont.append(int(self.ui.lePontJog4.text()))
        vetPont.append(int(self.ui.lePontJog5.text()))
        vetPont.append(int(self.ui.lePontJog6.text()))
        vetPont.append(int(self.ui.lePontJog7.text()))
        vetPont.append(int(self.ui.lePontJog8.text()))
        self.player.enviar_pontos(vetPont)

        self.ui.lePontJog1.setText("0")
        self.ui.lePontJog2.setText("0")
        self.ui.lePontJog3.setText("0")
        self.ui.lePontJog4.setText("0")
        self.ui.lePontJog5.setText("0")
        self.ui.lePontJog6.setText("0")
        self.ui.lePontJog7.setText("0")
        self.ui.lePontJog8.setText("0")


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    janela = Tabuleiro()
    janela.show()
sys.exit(app.exec_())
