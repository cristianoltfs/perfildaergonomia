from template.carta import Ui_carta
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

class Carta(QDialog):
    def __init__(self, df):
        super(Carta, self).__init__()
        self.ui = Ui_carta()
        self.ui.setupUi(self)
        self.ui.btnCarta_2.clicked.connect(self.sair)
        self.ui.lblResposta.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.lblResposta.setFont(QFont('Times', 16))
        self.ui.lblTipoCarta.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.lblTipoCarta.setFont(QFont('Times', 16))

        self.ui.lblTipoCarta.setText(df[0])
        self.ui.lblResposta.setText(df[1])

        self.ui.pteDica1.setPlainText(df[2])
        self.ui.pteDica2.setPlainText(df[3])
        self.ui.pteDica3.setPlainText(df[4])
        self.ui.pteDica4.setPlainText(df[5])
        self.ui.pteDica5.setPlainText(df[6])
        self.ui.pteDica6.setPlainText(df[7])
        self.ui.pteDica7.setPlainText(df[8])
        self.ui.pteDica8.setPlainText(df[9])
        self.ui.pteDica9.setPlainText(df[10])
        self.ui.pteDica10.setPlainText(df[11])
        self.ui.pteDica11.setPlainText(df[12])
        self.ui.pteDica12.setPlainText(df[13])

        """self.ui.pteDica1.setDisabled(1)
                                self.ui.pteDica2.setDisabled(1)
                                self.ui.pteDica3.setDisabled(1)
                                self.ui.pteDica4.setDisabled(1)
                                self.ui.pteDica5.setDisabled(1)
                                self.ui.pteDica6.setDisabled(1)
                                self.ui.pteDica7.setDisabled(1)
                                self.ui.pteDica8.setDisabled(1)
                                self.ui.pteDica9.setDisabled(1)
                                self.ui.pteDica10.setDisabled(1)
                                self.ui.pteDica11.setDisabled(1)
                                self.ui.pteDica12.setDisabled(1)"""



    def sair(self):
        self.close()