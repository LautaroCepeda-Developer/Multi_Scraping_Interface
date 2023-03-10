/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.2
import QtQuick.Controls 6.2
import MSI_QT

Rectangle {
    id: mainContainer
    width: Constants.width
    height: Constants.height
    color: "#0f0f0f"
    border.color: "#ff88b2"
    border.width: 3

    Rectangle {
        id: urlMenuContainer
        x: 25
        y: 25
        width: 550
        height: 718
        color: "#1f1f1f"
        border.color: "#ff88b2"
        border.width: 2

        Text {
            id: urlMenuLabel
            x: 161
            y: 8
            color: "#ffffff"
            text: qsTr("URL Menu")
            font.pixelSize: 50
        }
    }

    Rectangle {
        id: fileSettingsContainer
        x: 791
        y: 25
        width: 550
        height: 718
        color: "#1f1f1f"
        border.color: "#ff88b2"
        border.width: 3

        Text {
            id: fileSettingsLabel
            x: 143
            y: 8
            color: "#ffffff"
            text: qsTr("File Settings")
            font.pixelSize: 50
        }

        Button {
            id: scrapButton
            x: 415
            y: 653
            width: 120
            height: 50
            text: qsTr("¡Scrap!")
            scale: 1
            focus: false
            antialiasing: false
            smooth: true
            hoverEnabled: true
            icon.color: "#ffffff"
            checkable: false
            display: AbstractButton.TextBesideIcon
            icon.source: ""
            highlighted: true
            flat: true
        }

        ComboBox {
            id: dialectCBX
            x: 20
            y: 658
            hoverEnabled: true
            font.bold: false
            currentIndex: 0
            editable: false
            displayText: "Dialect"
            textRole: ""
            flat: true
        }
    }

    states: [
        State {
            name: "clicked"
            when: scrapButton.checked
        }
    ]
}
