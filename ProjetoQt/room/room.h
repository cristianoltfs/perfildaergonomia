#ifndef ROOM_H
#define ROOM_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class room; }
QT_END_NAMESPACE

class room : public QMainWindow
{
    Q_OBJECT

public:
    room(QWidget *parent = nullptr);
    ~room();

private:
    Ui::room *ui;
};
#endif // ROOM_H
