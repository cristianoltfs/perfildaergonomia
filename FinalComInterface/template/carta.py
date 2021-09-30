from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_carta(object):
    def setupUi(self, carta):
        carta.setObjectName("carta")
        carta.resize(1003, 768)
        carta.setMinimumSize(QtCore.QSize(1003, 768))
        carta.setMaximumSize(QtCore.QSize(1003, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/ergonomia_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        carta.setWindowIcon(icon)
        self.label_4 = QtWidgets.QLabel(carta)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 81, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(carta)
        self.groupBox_3.setGeometry(QtCore.QRect(12, 10, 981, 721))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(5, -6, 971, 41))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(15)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(290, 22, 401, 16))
        self.label_2.setStyleSheet("color: rgb(142, 211, 105);")
        self.label_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(4)
        self.label_2.setMidLineWidth(15)
        self.label_2.setObjectName("label_2")
        self.lblTipoCarta = QtWidgets.QLabel(self.groupBox_3)
        self.lblTipoCarta.setEnabled(True)
        self.lblTipoCarta.setGeometry(QtCore.QRect(3, 25, 971, 41))
        self.lblTipoCarta.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTipoCarta.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTipoCarta.setLineWidth(1)
        self.lblTipoCarta.setMidLineWidth(15)
        self.lblTipoCarta.setObjectName("lblTipoCarta")
        self.lblResposta = QtWidgets.QLabel(self.groupBox_3)
        self.lblResposta.setEnabled(True)
        self.lblResposta.setGeometry(QtCore.QRect(5, 50, 971, 41))
        self.lblResposta.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblResposta.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblResposta.setLineWidth(1)
        self.lblResposta.setMidLineWidth(15)
        self.lblResposta.setObjectName("lblResposta")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 87, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 85, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pteDica2 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica2.setGeometry(QtCore.QRect(60, 136, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica2.sizePolicy().hasHeightForWidth())
        self.pteDica2.setSizePolicy(sizePolicy)
        self.pteDica2.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica2.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica2.setFont(font)
        self.pteDica2.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica2.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica2.setLineWidth(1)
        self.pteDica2.setPlainText("")
        self.pteDica2.setObjectName("pteDica2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(30, 137, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 139, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(30, 191, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pteDica3 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica3.setGeometry(QtCore.QRect(60, 190, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica3.sizePolicy().hasHeightForWidth())
        self.pteDica3.setSizePolicy(sizePolicy)
        self.pteDica3.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica3.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica3.setFont(font)
        self.pteDica3.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica3.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica3.setLineWidth(1)
        self.pteDica3.setPlainText("")
        self.pteDica3.setObjectName("pteDica3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 193, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 247, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.pteDica4 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica4.setGeometry(QtCore.QRect(60, 244, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica4.sizePolicy().hasHeightForWidth())
        self.pteDica4.setSizePolicy(sizePolicy)
        self.pteDica4.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica4.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica4.setFont(font)
        self.pteDica4.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica4.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica4.setLineWidth(1)
        self.pteDica4.setPlainText("")
        self.pteDica4.setObjectName("pteDica4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(30, 245, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(30, 298, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pteDica5 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica5.setGeometry(QtCore.QRect(60, 297, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica5.sizePolicy().hasHeightForWidth())
        self.pteDica5.setSizePolicy(sizePolicy)
        self.pteDica5.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica5.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica5.setFont(font)
        self.pteDica5.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica5.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica5.setLineWidth(1)
        self.pteDica5.setPlainText("")
        self.pteDica5.setObjectName("pteDica5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 300, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(30, 351, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 353, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.pteDica6 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica6.setGeometry(QtCore.QRect(60, 350, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica6.sizePolicy().hasHeightForWidth())
        self.pteDica6.setSizePolicy(sizePolicy)
        self.pteDica6.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica6.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica6.setFont(font)
        self.pteDica6.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica6.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica6.setLineWidth(1)
        self.pteDica6.setPlainText("")
        self.pteDica6.setObjectName("pteDica6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 404, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(30, 402, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pteDica7 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica7.setGeometry(QtCore.QRect(60, 401, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica7.sizePolicy().hasHeightForWidth())
        self.pteDica7.setSizePolicy(sizePolicy)
        self.pteDica7.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica7.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica7.setFont(font)
        self.pteDica7.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica7.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica7.setLineWidth(1)
        self.pteDica7.setPlainText("")
        self.pteDica7.setObjectName("pteDica7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 456, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 454, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pteDica8 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica8.setGeometry(QtCore.QRect(60, 453, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica8.sizePolicy().hasHeightForWidth())
        self.pteDica8.setSizePolicy(sizePolicy)
        self.pteDica8.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica8.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica8.setFont(font)
        self.pteDica8.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica8.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica8.setLineWidth(1)
        self.pteDica8.setPlainText("")
        self.pteDica8.setObjectName("pteDica8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 509, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(30, 507, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pteDica9 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica9.setGeometry(QtCore.QRect(60, 506, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(46)
        sizePolicy.setHeightForWidth(self.pteDica9.sizePolicy().hasHeightForWidth())
        self.pteDica9.setSizePolicy(sizePolicy)
        self.pteDica9.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica9.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica9.setFont(font)
        self.pteDica9.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica9.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica9.setLineWidth(1)
        self.pteDica9.setPlainText("")
        self.pteDica9.setObjectName("pteDica9")
        self.pteDica10 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica10.setGeometry(QtCore.QRect(60, 559, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(46)
        sizePolicy.setHeightForWidth(self.pteDica10.sizePolicy().hasHeightForWidth())
        self.pteDica10.setSizePolicy(sizePolicy)
        self.pteDica10.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica10.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica10.setFont(font)
        self.pteDica10.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica10.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica10.setLineWidth(1)
        self.pteDica10.setPlainText("")
        self.pteDica10.setObjectName("pteDica10")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(30, 560, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 562, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.pteDica11 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica11.setGeometry(QtCore.QRect(60, 612, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(46)
        sizePolicy.setHeightForWidth(self.pteDica11.sizePolicy().hasHeightForWidth())
        self.pteDica11.setSizePolicy(sizePolicy)
        self.pteDica11.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica11.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica11.setFont(font)
        self.pteDica11.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica11.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica11.setLineWidth(1)
        self.pteDica11.setPlainText("")
        self.pteDica11.setObjectName("pteDica11")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(30, 613, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 615, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_12.setGeometry(QtCore.QRect(10, 667, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setStyleSheet("QCheckBox{\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(120,120,120);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    color: rgb(220, 220, 220);\n"
"    border: 2px solid rgb(34,63,102);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox::pressed {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(148,28,52);\n"
"    border: 3px solid rgb(239,184,16);\n"
"}\n"
"")
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(30, 665, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.pteDica12 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica12.setGeometry(QtCore.QRect(60, 664, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(46)
        sizePolicy.setHeightForWidth(self.pteDica12.sizePolicy().hasHeightForWidth())
        self.pteDica12.setSizePolicy(sizePolicy)
        self.pteDica12.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica12.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica12.setFont(font)
        self.pteDica12.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica12.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica12.setLineWidth(1)
        self.pteDica12.setPlainText("")
        self.pteDica12.setObjectName("pteDica12")
        self.pteDica1 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pteDica1.setGeometry(QtCore.QRect(60, 83, 911, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteDica1.sizePolicy().hasHeightForWidth())
        self.pteDica1.setSizePolicy(sizePolicy)
        self.pteDica1.setMinimumSize(QtCore.QSize(0, 47))
        self.pteDica1.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pteDica1.setFont(font)
        self.pteDica1.setStyleSheet("QLPlainTextEdit{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(148,28,52);\n"
"}\n"
"")
        self.pteDica1.setFrameShape(QtWidgets.QFrame.Panel)
        self.pteDica1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pteDica1.setLineWidth(1)
        self.pteDica1.setPlainText("")
        self.pteDica1.setObjectName("pteDica1")
        self.lblTipoCarta.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lblResposta.raise_()
        self.checkBox.raise_()
        self.label_5.raise_()
        self.pteDica2.raise_()
        self.label_6.raise_()
        self.checkBox_2.raise_()
        self.label_7.raise_()
        self.pteDica3.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.pteDica4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.pteDica5.raise_()
        self.checkBox_5.raise_()
        self.label_10.raise_()
        self.checkBox_6.raise_()
        self.pteDica6.raise_()
        self.checkBox_7.raise_()
        self.label_11.raise_()
        self.pteDica7.raise_()
        self.checkBox_8.raise_()
        self.label_12.raise_()
        self.pteDica8.raise_()
        self.checkBox_9.raise_()
        self.label_13.raise_()
        self.pteDica9.raise_()
        self.pteDica10.raise_()
        self.label_14.raise_()
        self.checkBox_10.raise_()
        self.pteDica11.raise_()
        self.label_15.raise_()
        self.checkBox_11.raise_()
        self.checkBox_12.raise_()
        self.label_16.raise_()
        self.pteDica12.raise_()
        self.pteDica1.raise_()
        self.btnCarta_2 = QtWidgets.QPushButton(carta)
        self.btnCarta_2.setGeometry(QtCore.QRect(866, 735, 131, 31))
        self.btnCarta_2.setMinimumSize(QtCore.QSize(0, 0))
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

        self.retranslateUi(carta)
        QtCore.QMetaObject.connectSlotsByName(carta)

    def retranslateUi(self, carta):
        _translate = QtCore.QCoreApplication.translate
        carta.setWindowTitle(_translate("carta", "Carta"))
        self.label.setText(_translate("carta", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Diga aos jogadores que sou</span></p></body></html>"))
        self.label_2.setText(_translate("carta", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lblTipoCarta.setText(_translate("carta", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">CONCEITO</span></p></body></html>"))
        self.lblResposta.setText(_translate("carta", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">AET</span></p></body></html>"))
        self.label_5.setText(_translate("carta", "1 - "))
        self.label_6.setText(_translate("carta", "2 - "))
        self.label_7.setText(_translate("carta", "3 - "))
        self.label_8.setText(_translate("carta", "4 - "))
        self.label_9.setText(_translate("carta", "5 - "))
        self.label_10.setText(_translate("carta", "6 - "))
        self.label_11.setText(_translate("carta", "7 - "))
        self.label_12.setText(_translate("carta", "8 - "))
        self.label_13.setText(_translate("carta", "9 - "))
        self.label_14.setText(_translate("carta", "10 - "))
        self.label_15.setText(_translate("carta", "11 - "))
        self.label_16.setText(_translate("carta", "12 - "))
        self.btnCarta_2.setText(_translate("carta", "SAIR"))
from template import img