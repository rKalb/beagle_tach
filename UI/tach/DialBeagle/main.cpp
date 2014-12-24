#include "qtquick1applicationviewer.h"
#include <QApplication>
#include <QWSServer>
#include <QDeclarativeEngine>
#include <QDeclarativeComponent>
#include <QDeclarativeContext>
#include <QDebug>
#include <QDeclarativeProperty>
#include <QString>

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
    int varRPM = udp_rpm.pullRPM();

    viewer.addImportPath(QLatin1String("modules"));
    viewer.setOrientation(QtQuick1ApplicationViewer::ScreenOrientationAuto);
    viewer.rootContext()->setContextProperty("currentRPM", (varRPM = udp_rpm.pullRPM()));
    qDebug() << varRPM;
    viewer.setMainQmlFile(QLatin1String("qml/dialcontrol/dialcontrol.qml"));
    viewer.showExpanded();

    udp_rpm.show();



    //Receiver reciever;
    //reciever.show();
    //reciever.pullRPM();


    return app.exec();
}

void set_rpm(QtQuick1ApplicationViewer &viewer, int rpm){
    /*
     * Write RPM to Slot
     */


}
