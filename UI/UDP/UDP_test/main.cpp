#include <QCoreApplication>
#include <QUdpSocket>
#include <stdio.h>
#include <QDebug>
#include <QString>
#include <QRegExp>
#include <QStringList>

using namespace std;

/*
 * Prototypes
 */

void pullRPM(QByteArray* datagram, int* rpm);

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QUdpSocket udpSocket;

    int rpm = 0;

    udpSocket.bind(5050, QUdpSocket::ShareAddress);

    while(1 == 1)
    {
        QByteArray datagram;
        QHostAddress sender;
        quint16 senderPort;

        if(udpSocket.hasPendingDatagrams())
        {
            qDebug() << "Recieved Datagram" << endl;
            qDebug() << "Datagram Size " << udpSocket.pendingDatagramSize() << endl;
            datagram.resize(udpSocket.pendingDatagramSize());

            udpSocket.readDatagram(datagram.data(), datagram.size(),
                                    &sender, &senderPort);
            qDebug() << "Datagram: " << datagram << endl;

            pullRPM(&datagram, &rpm);

            qDebug() << "RPM is " << rpm << endl;

        }

    }
    return a.exec();
}

void pullRPM(QByteArray* datagram, int* rpm)
{
    QString str = datagram->data();
    QRegExp rx("[: ]");
    QStringList rpm_split = str.split(rx, QString::SkipEmptyParts);

    //qDebug() << rpm_split;

    //statusLabel->setText(str);

    QString rpm_str = rpm_split.at(1);
    *rpm = rpm_str.toInt();

    //qDebug() << rpm;

}


/*
void readPendingDatagrams()
 {
     while (udpSocket->hasPendingDatagrams()) {
         QByteArray datagram;
         datagram.resize(udpSocket->pendingDatagramSize());
         QHostAddress sender;
         quint16 senderPort;

         udpSocket->readDatagram(datagram.data(), datagram.size(),
                                 &sender, &senderPort);

         processTheDatagram(datagram);
     }
 }
*/
