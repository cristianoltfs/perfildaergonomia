/********************************************************************************
** Form generated from reading UI file 'room.ui'
**
** Created by: Qt User Interface Compiler version 5.12.10
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ROOM_H
#define UI_ROOM_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_room
{
public:
    QWidget *centralwidget;
    QLabel *label_2;
    QLineEdit *leNickName;
    QLabel *label_3;
    QPushButton *btnLogin;
    QPushButton *btnClose;
    QFrame *frame;
    QGroupBox *groupBox;

    void setupUi(QMainWindow *room)
    {
        if (room->objectName().isEmpty())
            room->setObjectName(QString::fromUtf8("room"));
        room->resize(403, 198);
        room->setMinimumSize(QSize(403, 198));
        room->setMaximumSize(QSize(403, 198));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/img/img/ergonomia_logo.png"), QSize(), QIcon::Normal, QIcon::Off);
        room->setWindowIcon(icon);
        centralwidget = new QWidget(room);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(130, 25, 141, 41));
        label_2->setMinimumSize(QSize(141, 41));
        label_2->setMaximumSize(QSize(141, 41));
        QFont font;
        font.setFamily(QString::fromUtf8("Forte"));
        font.setPointSize(22);
        font.setBold(false);
        font.setWeight(50);
        label_2->setFont(font);
        label_2->setStyleSheet(QString::fromUtf8("QLabel {\n"
"	color: rgb(102,102, 102);\n"
"}\n"
""));
        leNickName = new QLineEdit(centralwidget);
        leNickName->setObjectName(QString::fromUtf8("leNickName"));
        leNickName->setGeometry(QRect(118, 80, 254, 36));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Segoe UI"));
        font1.setPointSize(11);
        font1.setBold(true);
        font1.setWeight(75);
        leNickName->setFont(font1);
        leNickName->setStyleSheet(QString::fromUtf8("QLineEdit {\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	backgroud-color: rgb(30,30,30);\n"
"	color: rgb(57,57, 253);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(34,63,102);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(14,93,213);\n"
"	color: rgb(50, 50, 50);\n"
"}"));
        leNickName->setMaxLength(14);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(23, 80, 89, 36));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Segoe UI"));
        font2.setPointSize(14);
        font2.setBold(true);
        font2.setWeight(75);
        label_3->setFont(font2);
        label_3->setStyleSheet(QString::fromUtf8("QLabel {\n"
"	color: rgb(102,102,102);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	color: 2px solid rgb(20,20,253);\n"
"}\n"
"\n"
""));
        btnLogin = new QPushButton(centralwidget);
        btnLogin->setObjectName(QString::fromUtf8("btnLogin"));
        btnLogin->setGeometry(QRect(192, 154, 91, 31));
        QFont font3;
        font3.setFamily(QString::fromUtf8("Segoe UI"));
        font3.setPointSize(11);
        btnLogin->setFont(font3);
        btnLogin->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(50, 50, 50);\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(0, 0, 163);\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border-radius: 5px\n"
"}"));
        btnClose = new QPushButton(centralwidget);
        btnClose->setObjectName(QString::fromUtf8("btnClose"));
        btnClose->setGeometry(QRect(292, 154, 91, 31));
        btnClose->setFont(font3);
        btnClose->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(50, 50, 50);\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(0, 0, 163);\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border-radius: 5px\n"
"}"));
        frame = new QFrame(centralwidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(-710, -180, 1931, 951));
        frame->setStyleSheet(QString::fromUtf8("background-image: url(:/img/img/fundo_jogo_1.png);"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(10, 19, 381, 121));
        groupBox->setStyleSheet(QString::fromUtf8("QGroupBox {\n"
"	border: 2px solid rgb(34,63,102);\n"
"	border-radius: 5px;\n"
"}"));
        room->setCentralWidget(centralwidget);
        frame->raise();
        groupBox->raise();
        label_2->raise();
        leNickName->raise();
        label_3->raise();
        btnLogin->raise();
        btnClose->raise();

        retranslateUi(room);

        QMetaObject::connectSlotsByName(room);
    } // setupUi

    void retranslateUi(QMainWindow *room)
    {
        room->setWindowTitle(QApplication::translate("room", "room", nullptr));
        label_2->setText(QApplication::translate("room", "<html><head/><body><p align=\"center\">Login</p></body></html>", nullptr));
        label_3->setText(QApplication::translate("room", "Nickname", nullptr));
        btnLogin->setText(QApplication::translate("room", "Login", nullptr));
        btnClose->setText(QApplication::translate("room", "Close", nullptr));
        groupBox->setTitle(QString());
    } // retranslateUi

};

namespace Ui {
    class room: public Ui_room {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ROOM_H
