# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(636, 427)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbox_stepper_motor = QComboBox(Frame)
        self.cbox_stepper_motor.setObjectName(u"cbox_stepper_motor")
        font = QFont()
        font.setPointSize(12)
        self.cbox_stepper_motor.setFont(font)

        self.gridLayout.addWidget(self.cbox_stepper_motor, 1, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.pbutton_disconnect = QPushButton(Frame)
        self.pbutton_disconnect.setObjectName(u"pbutton_disconnect")

        self.gridLayout.addWidget(self.pbutton_disconnect, 3, 2, 1, 1)

        self.cbox_dinamomert = QComboBox(Frame)
        self.cbox_dinamomert.setObjectName(u"cbox_dinamomert")
        self.cbox_dinamomert.setFont(font)

        self.gridLayout.addWidget(self.cbox_dinamomert, 2, 1, 1, 2)

        self.label_stepper_motor = QLabel(Frame)
        self.label_stepper_motor.setObjectName(u"label_stepper_motor")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_stepper_motor.setFont(font1)

        self.gridLayout.addWidget(self.label_stepper_motor, 1, 0, 1, 1)

        self.pbutton_connect = QPushButton(Frame)
        self.pbutton_connect.setObjectName(u"pbutton_connect")

        self.gridLayout.addWidget(self.pbutton_connect, 3, 1, 1, 1)

        self.label_setting_connection = QLabel(Frame)
        self.label_setting_connection.setObjectName(u"label_setting_connection")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_setting_connection.sizePolicy().hasHeightForWidth())
        self.label_setting_connection.setSizePolicy(sizePolicy)
        self.label_setting_connection.setMinimumSize(QSize(158, 55))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_setting_connection.setFont(font2)
        self.label_setting_connection.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_setting_connection, 0, 0, 1, 3)

        self.label_dinamomert = QLabel(Frame)
        self.label_dinamomert.setObjectName(u"label_dinamomert")
        self.label_dinamomert.setFont(font1)

        self.gridLayout.addWidget(self.label_dinamomert, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.pbutton_disconnect.setText(QCoreApplication.translate("Frame", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.label_stepper_motor.setText(QCoreApplication.translate("Frame", u"\u0428\u0430\u0433\u043e\u0432\u044b\u0439 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c", None))
        self.pbutton_connect.setText(QCoreApplication.translate("Frame", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.label_setting_connection.setText(QCoreApplication.translate("Frame", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f", None))
        self.label_dinamomert.setText(QCoreApplication.translate("Frame", u"\u0414\u0438\u043d\u0430\u043c\u043e\u043c\u0435\u0442\u0440", None))
    # retranslateUi

