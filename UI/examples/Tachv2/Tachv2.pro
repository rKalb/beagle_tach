# Add more folders to ship with the application, here
folder_01.source = qml/Tachv2
folder_01.target = qml
DEPLOYMENTFOLDERS = folder_01

# Additional import path used to resolve QML modules in Creator's code model
QML_IMPORT_PATH =

# The .cpp file which was generated for your project. Feel free to hack it.
SOURCES += main.cpp

# Installation path
# target.path =

# Please do not modify the following two lines. Required for deployment.
include(qtquick1applicationviewer/qtquick1applicationviewer.pri)
qtcAddDeployment()

OTHER_FILES += \
    qml/Tachv2/dial.qml \
    qml/dialcontrol/content/Dial.qml \
    qml/dialcontrol/content/QuitButton.qml \
    qml/dialcontrol/content/background.png \
    qml/dialcontrol/content/needle_shadow.png \
    qml/dialcontrol/content/needle.png \
    qml/dialcontrol/content/overlay.png \
    qml/dialcontrol/content/quit.png \
    ../DialBeagle/dialcontrol.svg
