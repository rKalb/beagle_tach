/*
 * Author: Ryan Kalb
 * Date: 12/19/14
 *
 * NOTE: UDP Message handler.
 */
#include <QtNetwork/QAbstractSocket>
#include <QDebug>

void initSocket()
{
    udpSocket = new QUdpSocket(this);
}
