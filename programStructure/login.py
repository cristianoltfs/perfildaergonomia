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
        if nick == "":
            QMessageBox.critical(QMessageBox(), "ERROR", "Entre com um nickname válido.")
        else:
            pass


    def end(self):
        self.close()


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    janela = login()
    janela.show()
sys.exit(app.exec_())









