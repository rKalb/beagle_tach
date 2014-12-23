#include "qtquick1applicationviewer.h"
#include <QApplication>
#include <QWSServer>
#include <QDeclarativeEngine>
#include <QDeclarativeComponent>
#include <QDeclarativeContext>
#include <QDebug>
#include <QDeclarativeProperty>

#include "receiver.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    #ifdef Q_WS_QWS
    /*
     * Remove the Cursor There is no need for it
     */
        QWSServer::setCursorVisible( false );
    #endif

    QtQuick1ApplicationViewer viewer;
    Receiver udp_rpm;
    udp_rpm.show();
    viewer.addImportPath(QLatin1String("modules"));
    viewer.setOrientation(QtQuick1ApplicationViewer::ScreenOrientationAuto);
    viewer.rootContext()->setContextProperty("currentRPM", udp_rpm.pullRPM());
    qDebug() << udp_rpm.pullRPM();
    viewer.setMainQmlFile(QLatin1String("qml/dialcontrol/dialcontrol.qml"));
    viewer.showExpanded();

    //Receiver reciever;
    //reciever.show();
    //reciever.pullRPM();


    return app.exec();
}

void set_rpm(QtQuick1ApplicationViewer &viewer, int rpm){
    /*
     * Write RPM to Slot
     */
    Receiver udp_rpm;
    rpm = udp_rpm.pullRPM();

}
