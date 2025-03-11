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
    QLabel, QSizePolicy, QSpacerItem, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(448, 178)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_setting_connection = QLabel(Frame)
        self.label_setting_connection.setObjectName(u"label_setting_connection")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_setting_connection.sizePolicy().hasHeightForWidth())
        self.label_setting_connection.setSizePolicy(sizePolicy)
        self.label_setting_connection.setMinimumSize(QSize(158, 55))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_setting_connection.setFont(font)
        self.label_setting_connection.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_setting_connection, 0, 0, 1, 2)

        self.label_dinamomert = QLabel(Frame)
        self.label_dinamomert.setObjectName(u"label_dinamomert")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_dinamomert.setFont(font1)

        self.gridLayout.addWidget(self.label_dinamomert, 2, 0, 1, 1)

        self.cbox_stepper_motor = QComboBox(Frame)
        self.cbox_stepper_motor.setObjectName(u"cbox_stepper_motor")
        font2 = QFont()
        font2.setPointSize(12)
        self.cbox_stepper_motor.setFont(font2)

        self.gridLayout.addWidget(self.cbox_stepper_motor, 1, 1, 1, 1)

        self.label_stepper_motor = QLabel(Frame)
        self.label_stepper_motor.setObjectName(u"label_stepper_motor")
        self.label_stepper_motor.setFont(font1)

        self.gridLayout.addWidget(self.label_stepper_motor, 1, 0, 1, 1)

        self.cbox_dinamomert = QComboBox(Frame)
        self.cbox_dinamomert.setObjectName(u"cbox_dinamomert")
        self.cbox_dinamomert.setFont(font2)

        self.gridLayout.addWidget(self.cbox_dinamomert, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_setting_connection.setText(QCoreApplication.translate("Frame", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f", None))
        self.label_dinamomert.setText(QCoreApplication.translate("Frame", u"\u0414\u0438\u043d\u0430\u043c\u043e\u043c\u0435\u0442\u0440", None))
        self.label_stepper_motor.setText(QCoreApplication.translate("Frame", u"\u0428\u0430\u0433\u043e\u0432\u044b\u0439 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c", None))
    # retranslateUi

