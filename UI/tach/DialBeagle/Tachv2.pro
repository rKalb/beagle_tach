# Add more folders to ship with the application, here
folder_01.source = qml/dialcontrol
folder_01.target = qml
DEPLOYMENTFOLDERS = folder_01

# Additional import path used to resolve QML modules in Creator's code model
QML_IMPORT_PATH =

# The .cpp file which was generated for your project. Feel free to hack it.
HEADERS = receiver.h
SOURCES += main.cpp \
    receiver.cpp

QT += network

# Installation path
# target.path =

# Please do not modify the following two lines. Required for deployment.
include(qtquick1applicationviewer/qtquick1applicationviewer.pri)
qtcAddDeployment()


OTHER_FILES += \
    qml/Tachv2/dial.qml \
    dialcontrol.qmlproject \
    dialcontrol.png \
    dialcontrol.svg \
    Tachv2.pro.user \
    qml/dialcontrol/dialcontrol.qml \
    qml/dialcontrol/content/Dial.qml \
    qml/dialcontrol/content/QuitButton.qml \
    qml/dialcontrol/content/background.png \
    qml/dialcontrol/content/needle_shadow.png \
    qml/dialcontrol/content/needle.png \
    qml/dialcontrol/content/overlay.png \
    qml/dialcontrol/content/quit.png
#HEADERS += \
#    receiver.h


