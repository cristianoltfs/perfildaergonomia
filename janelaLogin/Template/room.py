from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_room(object):
    def setupUi(self, room):
        room.setObjectName("room")
        room.resize(403, 198)
        room.setMinimumSize(QtCore.QSize(403, 198))
        room.setMaximumSize(QtCore.QSize(403, 198))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/ergonomia_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        room.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(room)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 25, 141, 41))
        self.label_2.setMinimumSize(QtCore.QSize(141, 41))
        self.label_2.setMaximumSize(QtCore.QSize(141, 41))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(102,102, 102);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.leNickName = QtWidgets.QLineEdit(self.centralwidget)
        self.leNickName.setGeometry(QtCore.QRect(118, 80, 254, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leNickName.setFont(font)
        self.leNickName.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    backgroud-color: rgb(30,30,30);\n"
"    color: rgb(57,57, 253);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(34,63,102);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(14,93,213);\n"
"    color: rgb(50, 50, 50);\n"
"}")
        self.leNickName.setMaxLength(14)
        self.leNickName.setObjectName("leNickName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(23, 80, 89, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(102,102,102);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(192, 154, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(0, 0, 163);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border-radius: 5px\n"
"}")
        self.btnLogin.setObjectName("btnLogin")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(292, 154, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnClose.setFont(font)
        self.btnClose.setStyleSheet("QPushButton {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(0, 0, 163);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border-radius: 5px\n"
"}")
        self.btnClose.setObjectName("btnClose")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-710, -180, 1931, 951))
        self.frame.setStyleSheet("background-image: url(:/img/img/fundo_jogo_1.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 19, 381, 121))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.frame.raise_()
        self.groupBox.raise_()
        self.label_2.raise_()
        self.leNickName.raise_()
        self.label_3.raise_()
        self.btnLogin.raise_()
        self.btnClose.raise_()
        room.setCentralWidget(self.centralwidget)

        self.retranslateUi(room)
        QtCore.QMetaObject.connectSlotsByName(room)

    def retranslateUi(self, room):
        _translate = QtCore.QCoreApplication.translate
        room.setWindowTitle(_translate("room", "room"))
        self.label_2.setText(_translate("room", "<html><head/><body><p align=\"center\">Login</p></body></html>"))
        self.label_3.setText(_translate("room", "Nickname"))
        self.btnLogin.setText(_translate("room", "Login"))
        self.btnClose.setText(_translate("room", "Close"))
from Template import img
