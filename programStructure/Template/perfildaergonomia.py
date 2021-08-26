from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PerfilErgonomia(object):
    def setupUi(self, PerfilErgonomia):
        PerfilErgonomia.setObjectName("PerfilErgonomia")
        PerfilErgonomia.resize(1366, 768)
        PerfilErgonomia.setMinimumSize(QtCore.QSize(1366, 768))
        PerfilErgonomia.setMaximumSize(QtCore.QSize(1366, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/ergonomia_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PerfilErgonomia.setWindowIcon(icon)
        PerfilErgonomia.setStyleSheet("")
        self.btnPontos = QtWidgets.QPushButton(PerfilErgonomia)
        self.btnPontos.setGeometry(QtCore.QRect(760, 537, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnPontos.setFont(font)
        self.btnPontos.setStyleSheet("QPushButton {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"    border-radius: 5px\n"
"}")
        self.btnPontos.setObjectName("btnPontos")
        self.btnCarta_2 = QtWidgets.QPushButton(PerfilErgonomia)
        self.btnCarta_2.setGeometry(QtCore.QRect(585, 704, 181, 51))
        self.btnCarta_2.setMinimumSize(QtCore.QSize(20, 50))
        self.btnCarta_2.setMaximumSize(QtCore.QSize(16666, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnCarta_2.setFont(font)
        self.btnCarta_2.setStyleSheet("QPushButton {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"    border-radius: 5px\n"
"}")
        self.btnCarta_2.setObjectName("btnCarta_2")
        self.groupBox_3 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_3.setGeometry(QtCore.QRect(414, 56, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lblJogador1 = QtWidgets.QLabel(self.groupBox_3)
        self.lblJogador1.setGeometry(QtCore.QRect(1, -1, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador1.setFont(font)
        self.lblJogador1.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador1.setObjectName("lblJogador1")
        self.leJogador1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.leJogador1.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador1.setFont(font)
        self.leJogador1.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador1.setObjectName("leJogador1")
        self.lePontJog1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lePontJog1.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog1.setFont(font)
        self.lePontJog1.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog1.setObjectName("lePontJog1")
        self.groupBox_4 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_4.setGeometry(QtCore.QRect(569, 27, 171, 503))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.leJogador2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.leJogador2.setGeometry(QtCore.QRect(17, 102, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador2.setFont(font)
        self.leJogador2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador2.setObjectName("leJogador2")
        self.groupBox_5 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_5.setGeometry(QtCore.QRect(738, 27, 171, 503))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.lePontJog2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lePontJog2.setGeometry(QtCore.QRect(18, 102, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog2.setFont(font)
        self.lePontJog2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog2.setObjectName("lePontJog2")
        self.groupBox_6 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_6.setGeometry(QtCore.QRect(414, 27, 157, 503))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.lblJogador2 = QtWidgets.QLabel(self.groupBox_6)
        self.lblJogador2.setGeometry(QtCore.QRect(1, 87, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador2.setFont(font)
        self.lblJogador2.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador2.setObjectName("lblJogador2")
        self.groupBox_7 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_7.setGeometry(QtCore.QRect(414, 115, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_8 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_8.setGeometry(QtCore.QRect(414, 174, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.lblJogador3 = QtWidgets.QLabel(self.groupBox_8)
        self.lblJogador3.setGeometry(QtCore.QRect(1, 1, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador3.setFont(font)
        self.lblJogador3.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador3.setObjectName("lblJogador3")
        self.leJogador3 = QtWidgets.QLineEdit(self.groupBox_8)
        self.leJogador3.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador3.setFont(font)
        self.leJogador3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador3.setObjectName("leJogador3")
        self.lePontJog3 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lePontJog3.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog3.setFont(font)
        self.lePontJog3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog3.setObjectName("lePontJog3")
        self.groupBox_9 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_9.setGeometry(QtCore.QRect(414, 233, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.lblJogador4 = QtWidgets.QLabel(self.groupBox_9)
        self.lblJogador4.setGeometry(QtCore.QRect(1, 0, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador4.setFont(font)
        self.lblJogador4.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador4.setObjectName("lblJogador4")
        self.leJogador4 = QtWidgets.QLineEdit(self.groupBox_9)
        self.leJogador4.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador4.setFont(font)
        self.leJogador4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador4.setObjectName("leJogador4")
        self.lePontJog4 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lePontJog4.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog4.setFont(font)
        self.lePontJog4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog4.setObjectName("lePontJog4")
        self.groupBox_10 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_10.setGeometry(QtCore.QRect(414, 292, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.lblJogador5 = QtWidgets.QLabel(self.groupBox_10)
        self.lblJogador5.setGeometry(QtCore.QRect(1, 0, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador5.setFont(font)
        self.lblJogador5.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador5.setObjectName("lblJogador5")
        self.leJogador5 = QtWidgets.QLineEdit(self.groupBox_10)
        self.leJogador5.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador5.setFont(font)
        self.leJogador5.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador5.setObjectName("leJogador5")
        self.lePontJog5 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lePontJog5.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog5.setFont(font)
        self.lePontJog5.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog5.setObjectName("lePontJog5")
        self.groupBox_11 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_11.setGeometry(QtCore.QRect(414, 351, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.lblJogador6 = QtWidgets.QLabel(self.groupBox_11)
        self.lblJogador6.setGeometry(QtCore.QRect(1, 0, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador6.setFont(font)
        self.lblJogador6.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador6.setObjectName("lblJogador6")
        self.leJogador6 = QtWidgets.QLineEdit(self.groupBox_11)
        self.leJogador6.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador6.setFont(font)
        self.leJogador6.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador6.setObjectName("leJogador6")
        self.lePontJog6 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lePontJog6.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog6.setFont(font)
        self.lePontJog6.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog6.setObjectName("lePontJog6")
        self.groupBox_12 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_12.setGeometry(QtCore.QRect(414, 410, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.lblJogador7 = QtWidgets.QLabel(self.groupBox_12)
        self.lblJogador7.setGeometry(QtCore.QRect(1, 0, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador7.setFont(font)
        self.lblJogador7.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador7.setObjectName("lblJogador7")
        self.leJogador7 = QtWidgets.QLineEdit(self.groupBox_12)
        self.leJogador7.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador7.setFont(font)
        self.leJogador7.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador7.setObjectName("leJogador7")
        self.lePontJog7 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lePontJog7.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog7.setFont(font)
        self.lePontJog7.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog7.setObjectName("lePontJog7")
        self.groupBox_13 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_13.setGeometry(QtCore.QRect(414, 469, 495, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_13.setTitle("")
        self.groupBox_13.setObjectName("groupBox_13")
        self.lblJogador8 = QtWidgets.QLabel(self.groupBox_13)
        self.lblJogador8.setGeometry(QtCore.QRect(2, 1, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblJogador8.setFont(font)
        self.lblJogador8.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador8.setObjectName("lblJogador8")
        self.leJogador8 = QtWidgets.QLineEdit(self.groupBox_13)
        self.leJogador8.setGeometry(QtCore.QRect(171, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leJogador8.setFont(font)
        self.leJogador8.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leJogador8.setObjectName("leJogador8")
        self.lePontJog8 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lePontJog8.setGeometry(QtCore.QRect(341, 14, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lePontJog8.setFont(font)
        self.lePontJog8.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148,28,52);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lePontJog8.setObjectName("lePontJog8")
        self.groupBox_17 = QtWidgets.QGroupBox(PerfilErgonomia)
        self.groupBox_17.setGeometry(QtCore.QRect(414, 27, 495, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.lblJogador8_2 = QtWidgets.QLabel(self.groupBox_17)
        self.lblJogador8_2.setGeometry(QtCore.QRect(2, 1, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblJogador8_2.setFont(font)
        self.lblJogador8_2.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador8_2.setObjectName("lblJogador8_2")
        self.lblJogador8_3 = QtWidgets.QLabel(self.groupBox_17)
        self.lblJogador8_3.setGeometry(QtCore.QRect(160, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblJogador8_3.setFont(font)
        self.lblJogador8_3.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador8_3.setObjectName("lblJogador8_3")
        self.lblJogador8_4 = QtWidgets.QLabel(self.groupBox_17)
        self.lblJogador8_4.setGeometry(QtCore.QRect(329, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblJogador8_4.setFont(font)
        self.lblJogador8_4.setStyleSheet("QLabel {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.lblJogador8_4.setObjectName("lblJogador8_4")
        self.frame = QtWidgets.QFrame(PerfilErgonomia)
        self.frame.setGeometry(QtCore.QRect(-87, -2, 1541, 771))
        self.frame.setStyleSheet("image: url(:/img/img/TabuleiroTabelaClaroLogo.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.groupBox_7.raise_()
        self.groupBox_6.raise_()
        self.groupBox_5.raise_()
        self.groupBox_4.raise_()
        self.btnPontos.raise_()
        self.btnCarta_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_8.raise_()
        self.groupBox_9.raise_()
        self.groupBox_10.raise_()
        self.groupBox_11.raise_()
        self.groupBox_12.raise_()
        self.groupBox_13.raise_()
        self.groupBox_17.raise_()

        self.retranslateUi(PerfilErgonomia)
        QtCore.QMetaObject.connectSlotsByName(PerfilErgonomia)

    def retranslateUi(self, PerfilErgonomia):
        _translate = QtCore.QCoreApplication.translate
        PerfilErgonomia.setWindowTitle(_translate("PerfilErgonomia", "Perfil Da Ergonomia"))
        self.btnPontos.setText(_translate("PerfilErgonomia", "Enviar Pontuação"))
        self.btnCarta_2.setText(_translate("PerfilErgonomia", "Tirar Carta"))
        self.lblJogador1.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 1</p></body></html>"))
        self.leJogador1.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog1.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.leJogador2.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog2.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador2.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 2</p></body></html>"))
        self.lblJogador3.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 3</p></body></html>"))
        self.leJogador3.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog3.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador4.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 4</p></body></html>"))
        self.leJogador4.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog4.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador5.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 5</p></body></html>"))
        self.leJogador5.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog5.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador6.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 6</p></body></html>"))
        self.leJogador6.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog6.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador7.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 7</p></body></html>"))
        self.leJogador7.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog7.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador8.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogador 8</p></body></html>"))
        self.leJogador8.setPlaceholderText(_translate("PerfilErgonomia", "Pontos"))
        self.lePontJog8.setPlaceholderText(_translate("PerfilErgonomia", "Inserir pontuação"))
        self.lblJogador8_2.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Jogadores</p></body></html>"))
        self.lblJogador8_3.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Pontuação</p></body></html>"))
        self.lblJogador8_4.setText(_translate("PerfilErgonomia", "<html><head/><body><p align=\"center\">Inserir Pontos</p></body></html>"))
from Template import img