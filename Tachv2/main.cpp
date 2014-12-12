#include "qtquick1applicationviewer.h"
#include <QApplication>
#include <QWSServer>

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
    viewer.setMainQmlFile(QLatin1String("qml/Tachv2/main.qml"));
    viewer.showExpanded();

    return app.exec();
}
