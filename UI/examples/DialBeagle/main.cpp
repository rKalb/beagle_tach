#include "qtquick1applicationviewer.h"
#include <QApplication>
#include <QWSServer>
#include <QDeclarativeEngine>
#include <QDeclarativeComponent>
#include <QDeclarativeContext>
#include <QDebug>
#include <QDeclarativeProperty>

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
    viewer.addImportPath(QLatin1String("modules"));
    viewer.setOrientation(QtQuick1ApplicationViewer::ScreenOrientationAuto);
    viewer.setMainQmlFile(QLatin1String("qml/dialcontrol/dialcontrol.qml"));
    viewer.showExpanded();



    return app.exec();
}

void set_rpm(QtQuick1ApplicationViewer &viewer, int rpm){
    /*
     * Write RPM to Slot
     */

}
