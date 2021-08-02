import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from Template.room import Ui_room


class login(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(login, self).__init__(*args, **kwargs)
        self.ui = Ui_room()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.logar)
        self.ui.btnClose.clicked.connect(self.end)


    def logar(self):
        nick = self.ui.leNickName.text()
        room = self.ui.leRoom.text()

        if not room.isnumeric() or room == "" or int(room) > 100:
            QMessageBox.critical(QMessageBox(), "ERROR", "Entre com um valor inteiro entre 1 e 100 para a sala.")
        elif nick == "":
            QMessageBox.critical(QMessageBox(), "ERROR", "Entre com um nickname válido.")
        else:
            from cw2 import cw
            cw(nick, room)


    def end(self):
        self.close()


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    janela = login()
    janela.show()
sys.exit(app.exec_())









