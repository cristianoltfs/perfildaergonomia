import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from Template.room import Ui_room
#from cliente import Cliente
from classeTabuleiro import Tabu

#HOST = '200.239.165.217'
HOST = 'localhost'
PORT = 8000

class Login(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.ui = Ui_room()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.logar)
        self.ui.btnClose.clicked.connect(self.end)
        csv = open('ptsServer.csv', 'w')
        csv.write('')
        csv.close()

    def logar(self):
        nick = self.ui.leNickName.text()
        x = 0
        if nick == "":
            QMessageBox.critical(QMessageBox(), "ERROR", "Entre com um nickname válido.")
        else:
            if x == 0:
                self.close()
                frmTabuleiro = Tabu(nick)
                frmTabuleiro.exec_()
            x = 1

    def end(self):
        self.close()


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    janela = Login()
    janela.show()
sys.exit(app.exec_())
