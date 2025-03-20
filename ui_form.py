# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1293, 834)
        self.connection_settings = QAction(MainWindow)
        self.connection_settings.setObjectName(u"connection_settings")
        self.graph = QAction(MainWindow)
        self.graph.setObjectName(u"graph")
        self.force_graph = QAction(MainWindow)
        self.force_graph.setObjectName(u"force_graph")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_layout = QGridLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.log_layout = QVBoxLayout()
        self.log_layout.setObjectName(u"log_layout")
        self.log_frame = QFrame(self.centralwidget)
        self.log_frame.setObjectName(u"log_frame")
        self.log_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.log_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.log_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tedit_global_log = QTextEdit(self.log_frame)
        self.tedit_global_log.setObjectName(u"tedit_global_log")
        self.tedit_global_log.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tedit_global_log.sizePolicy().hasHeightForWidth())
        self.tedit_global_log.setSizePolicy(sizePolicy)
        self.tedit_global_log.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setKerning(False)
        self.tedit_global_log.setFont(font)
        self.tedit_global_log.setFrameShadow(QFrame.Shadow.Raised)
        self.tedit_global_log.setLineWidth(0)
        self.tedit_global_log.setReadOnly(True)

        self.gridLayout_6.addWidget(self.tedit_global_log, 1, 0, 1, 1)

        self.label_module_rec_data = QLabel(self.log_frame)
        self.label_module_rec_data.setObjectName(u"label_module_rec_data")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_module_rec_data.setFont(font1)
        self.label_module_rec_data.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_6.addWidget(self.label_module_rec_data, 0, 0, 1, 1)


        self.log_layout.addWidget(self.log_frame)


        self.main_layout.addLayout(self.log_layout, 1, 2, 3, 1)

        self.experiment_layout = QGridLayout()
        self.experiment_layout.setObjectName(u"experiment_layout")
        self.experiment_frame = QFrame(self.centralwidget)
        self.experiment_frame.setObjectName(u"experiment_frame")
        font2 = QFont()
        font2.setPointSize(12)
        self.experiment_frame.setFont(font2)
        self.experiment_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.experiment_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.experiment_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_dist_to_trans_deform = QLabel(self.experiment_frame)
        self.label_dist_to_trans_deform.setObjectName(u"label_dist_to_trans_deform")

        self.gridLayout_7.addWidget(self.label_dist_to_trans_deform, 5, 0, 1, 2)

        self.label_type_deform = QLabel(self.experiment_frame)
        self.label_type_deform.setObjectName(u"label_type_deform")
        self.label_type_deform.setFont(font2)

        self.gridLayout_7.addWidget(self.label_type_deform, 2, 0, 1, 1)

        self.dsbox_trans_deform = QDoubleSpinBox(self.experiment_frame)
        self.dsbox_trans_deform.setObjectName(u"dsbox_trans_deform")
        self.dsbox_trans_deform.setEnabled(False)
        self.dsbox_trans_deform.setDecimals(3)
        self.dsbox_trans_deform.setMaximum(9999.000000000000000)

        self.gridLayout_7.addWidget(self.dsbox_trans_deform, 4, 1, 1, 1)

        self.cbox_units_long_deform = QComboBox(self.experiment_frame)
        self.cbox_units_long_deform.addItem("")
        self.cbox_units_long_deform.addItem("")
        self.cbox_units_long_deform.addItem("")
        self.cbox_units_long_deform.setObjectName(u"cbox_units_long_deform")
        self.cbox_units_long_deform.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(11)
        self.cbox_units_long_deform.setFont(font3)

        self.gridLayout_7.addWidget(self.cbox_units_long_deform, 3, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 9, 0, 1, 1)

        self.label_trans_deform = QLabel(self.experiment_frame)
        self.label_trans_deform.setObjectName(u"label_trans_deform")
        self.label_trans_deform.setFont(font2)

        self.gridLayout_7.addWidget(self.label_trans_deform, 4, 0, 1, 1)

        self.label_deform_area = QLabel(self.experiment_frame)
        self.label_deform_area.setObjectName(u"label_deform_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_deform_area.sizePolicy().hasHeightForWidth())
        self.label_deform_area.setSizePolicy(sizePolicy1)
        self.label_deform_area.setFont(font2)

        self.gridLayout_7.addWidget(self.label_deform_area, 1, 0, 1, 1)

        self.dsbox_dist_to_trans_deform = QDoubleSpinBox(self.experiment_frame)
        self.dsbox_dist_to_trans_deform.setObjectName(u"dsbox_dist_to_trans_deform")
        self.dsbox_dist_to_trans_deform.setEnabled(False)
        self.dsbox_dist_to_trans_deform.setDecimals(3)
        self.dsbox_dist_to_trans_deform.setMaximum(9999.000000000000000)

        self.gridLayout_7.addWidget(self.dsbox_dist_to_trans_deform, 5, 2, 1, 1)

        self.label_utins_dist_to_trans_deform = QLabel(self.experiment_frame)
        self.label_utins_dist_to_trans_deform.setObjectName(u"label_utins_dist_to_trans_deform")
        self.label_utins_dist_to_trans_deform.setFont(font3)

        self.gridLayout_7.addWidget(self.label_utins_dist_to_trans_deform, 5, 3, 1, 1)

        self.cmob_type_deform = QComboBox(self.experiment_frame)
        self.cmob_type_deform.addItem("")
        self.cmob_type_deform.addItem("")
        self.cmob_type_deform.addItem("")
        self.cmob_type_deform.setObjectName(u"cmob_type_deform")
        self.cmob_type_deform.setEnabled(False)
        self.cmob_type_deform.setFont(font2)

        self.gridLayout_7.addWidget(self.cmob_type_deform, 2, 1, 1, 2)

        self.label_total_deform = QLabel(self.experiment_frame)
        self.label_total_deform.setObjectName(u"label_total_deform")

        self.gridLayout_7.addWidget(self.label_total_deform, 7, 0, 1, 1)

        self.cbox_units_trans_deform = QComboBox(self.experiment_frame)
        self.cbox_units_trans_deform.addItem("")
        self.cbox_units_trans_deform.addItem("")
        self.cbox_units_trans_deform.setObjectName(u"cbox_units_trans_deform")
        self.cbox_units_trans_deform.setEnabled(False)
        self.cbox_units_trans_deform.setFont(font3)

        self.gridLayout_7.addWidget(self.cbox_units_trans_deform, 4, 2, 1, 1)

        self.dsbox_long_deform = QDoubleSpinBox(self.experiment_frame)
        self.dsbox_long_deform.setObjectName(u"dsbox_long_deform")
        self.dsbox_long_deform.setEnabled(False)
        self.dsbox_long_deform.setFont(font2)
        self.dsbox_long_deform.setDecimals(3)
        self.dsbox_long_deform.setMaximum(9999.000000000000000)

        self.gridLayout_7.addWidget(self.dsbox_long_deform, 3, 1, 1, 1)

        self.label_leng_trans = QLabel(self.experiment_frame)
        self.label_leng_trans.setObjectName(u"label_leng_trans")

        self.gridLayout_7.addWidget(self.label_leng_trans, 6, 0, 1, 1)

        self.dsbox_deform_area = QDoubleSpinBox(self.experiment_frame)
        self.dsbox_deform_area.setObjectName(u"dsbox_deform_area")
        self.dsbox_deform_area.setEnabled(False)
        self.dsbox_deform_area.setMaximumSize(QSize(16777215, 16777215))
        self.dsbox_deform_area.setFont(font2)
        self.dsbox_deform_area.setDecimals(3)
        self.dsbox_deform_area.setMaximum(9999.000000000000000)

        self.gridLayout_7.addWidget(self.dsbox_deform_area, 1, 1, 1, 1)

        self.pbutton_set_zero = QPushButton(self.experiment_frame)
        self.pbutton_set_zero.setObjectName(u"pbutton_set_zero")
        self.pbutton_set_zero.setEnabled(False)
        self.pbutton_set_zero.setFont(font2)

        self.gridLayout_7.addWidget(self.pbutton_set_zero, 1, 5, 1, 1)

        self.label_units_deform_area = QLabel(self.experiment_frame)
        self.label_units_deform_area.setObjectName(u"label_units_deform_area")

        self.gridLayout_7.addWidget(self.label_units_deform_area, 1, 2, 1, 1)

        self.label_long_deform = QLabel(self.experiment_frame)
        self.label_long_deform.setObjectName(u"label_long_deform")
        self.label_long_deform.setFont(font2)

        self.gridLayout_7.addWidget(self.label_long_deform, 3, 0, 1, 1)

        self.pbutton_start_deform = QPushButton(self.experiment_frame)
        self.pbutton_start_deform.setObjectName(u"pbutton_start_deform")
        self.pbutton_start_deform.setEnabled(False)
        self.pbutton_start_deform.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.pbutton_start_deform, 8, 0, 1, 1)

        self.chbox_write_file = QCheckBox(self.experiment_frame)
        self.chbox_write_file.setObjectName(u"chbox_write_file")
        self.chbox_write_file.setEnabled(False)

        self.gridLayout_7.addWidget(self.chbox_write_file, 8, 1, 1, 1)

        self.label_module_deform = QLabel(self.experiment_frame)
        self.label_module_deform.setObjectName(u"label_module_deform")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_module_deform.setFont(font4)
        self.label_module_deform.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_7.addWidget(self.label_module_deform, 0, 0, 1, 6)

        self.label_units_leng_trans = QLabel(self.experiment_frame)
        self.label_units_leng_trans.setObjectName(u"label_units_leng_trans")
        self.label_units_leng_trans.setFont(font3)

        self.gridLayout_7.addWidget(self.label_units_leng_trans, 6, 3, 1, 1)

        self.label_leng_trans_out = QLabel(self.experiment_frame)
        self.label_leng_trans_out.setObjectName(u"label_leng_trans_out")
        self.label_leng_trans_out.setEnabled(False)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setUnderline(True)
        self.label_leng_trans_out.setFont(font5)

        self.gridLayout_7.addWidget(self.label_leng_trans_out, 6, 1, 1, 2)

        self.label_total_deform_out = QLabel(self.experiment_frame)
        self.label_total_deform_out.setObjectName(u"label_total_deform_out")
        self.label_total_deform_out.setEnabled(False)
        self.label_total_deform_out.setFont(font5)

        self.gridLayout_7.addWidget(self.label_total_deform_out, 7, 1, 1, 2)

        self.label_units_total_deform = QLabel(self.experiment_frame)
        self.label_units_total_deform.setObjectName(u"label_units_total_deform")

        self.gridLayout_7.addWidget(self.label_units_total_deform, 7, 3, 1, 1)

        self.pbutton_save_file = QPushButton(self.experiment_frame)
        self.pbutton_save_file.setObjectName(u"pbutton_save_file")
        self.pbutton_save_file.setEnabled(False)

        self.gridLayout_7.addWidget(self.pbutton_save_file, 8, 2, 1, 1)


        self.experiment_layout.addWidget(self.experiment_frame, 0, 0, 1, 1)


        self.main_layout.addLayout(self.experiment_layout, 3, 0, 1, 2)

        self.module_surv_dev_layout = QVBoxLayout()
        self.module_surv_dev_layout.setObjectName(u"module_surv_dev_layout")
        self.module_surv_dev_frame = QFrame(self.centralwidget)
        self.module_surv_dev_frame.setObjectName(u"module_surv_dev_frame")
        self.module_surv_dev_frame.setFont(font2)
        self.module_surv_dev_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_surv_dev_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.module_surv_dev_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_name_uo = QLabel(self.module_surv_dev_frame)
        self.label_name_uo.setObjectName(u"label_name_uo")
        sizePolicy1.setHeightForWidth(self.label_name_uo.sizePolicy().hasHeightForWidth())
        self.label_name_uo.setSizePolicy(sizePolicy1)
        self.label_name_uo.setFont(font2)

        self.gridLayout_5.addWidget(self.label_name_uo, 2, 0, 1, 1)

        self.dsbox_meas_dist = QDoubleSpinBox(self.module_surv_dev_frame)
        self.dsbox_meas_dist.setObjectName(u"dsbox_meas_dist")
        self.dsbox_meas_dist.setEnabled(False)
        self.dsbox_meas_dist.setMaximum(9999.989999999999782)
        self.dsbox_meas_dist.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.dsbox_meas_dist, 5, 2, 1, 1)

        self.label_fac_no = QLabel(self.module_surv_dev_frame)
        self.label_fac_no.setObjectName(u"label_fac_no")
        sizePolicy1.setHeightForWidth(self.label_fac_no.sizePolicy().hasHeightForWidth())
        self.label_fac_no.setSizePolicy(sizePolicy1)
        self.label_fac_no.setFont(font2)

        self.gridLayout_5.addWidget(self.label_fac_no, 3, 0, 1, 1)

        self.dsbox_spat_res = QDoubleSpinBox(self.module_surv_dev_frame)
        self.dsbox_spat_res.setObjectName(u"dsbox_spat_res")
        self.dsbox_spat_res.setEnabled(False)
        self.dsbox_spat_res.setMaximum(9999.989999999999782)
        self.dsbox_spat_res.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.dsbox_spat_res, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 10, 0, 1, 1)

        self.dsbox_opt_dist = QDoubleSpinBox(self.module_surv_dev_frame)
        self.dsbox_opt_dist.setObjectName(u"dsbox_opt_dist")
        self.dsbox_opt_dist.setEnabled(False)
        self.dsbox_opt_dist.setDecimals(1)
        self.dsbox_opt_dist.setMaximum(99999.000000000000000)
        self.dsbox_opt_dist.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.dsbox_opt_dist, 9, 2, 1, 1)

        self.label_chan_no = QLabel(self.module_surv_dev_frame)
        self.label_chan_no.setObjectName(u"label_chan_no")
        sizePolicy1.setHeightForWidth(self.label_chan_no.sizePolicy().hasHeightForWidth())
        self.label_chan_no.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_chan_no, 7, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 5, 1, 1, 1)

        self.label_meas_dist = QLabel(self.module_surv_dev_frame)
        self.label_meas_dist.setObjectName(u"label_meas_dist")
        sizePolicy1.setHeightForWidth(self.label_meas_dist.sizePolicy().hasHeightForWidth())
        self.label_meas_dist.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_meas_dist, 5, 0, 1, 1)

        self.label_units_spat_res = QLabel(self.module_surv_dev_frame)
        self.label_units_spat_res.setObjectName(u"label_units_spat_res")
        self.label_units_spat_res.setFont(font3)

        self.gridLayout_5.addWidget(self.label_units_spat_res, 6, 3, 1, 1)

        self.label_type_uo = QLabel(self.module_surv_dev_frame)
        self.label_type_uo.setObjectName(u"label_type_uo")
        sizePolicy1.setHeightForWidth(self.label_type_uo.sizePolicy().hasHeightForWidth())
        self.label_type_uo.setSizePolicy(sizePolicy1)
        self.label_type_uo.setFont(font2)

        self.gridLayout_5.addWidget(self.label_type_uo, 1, 0, 1, 1)

        self.ledit_diap_meas_def = QLineEdit(self.module_surv_dev_frame)
        self.ledit_diap_meas_def.setObjectName(u"ledit_diap_meas_def")
        self.ledit_diap_meas_def.setEnabled(False)
        font6 = QFont()
        font6.setPointSize(9)
        self.ledit_diap_meas_def.setFont(font6)

        self.gridLayout_5.addWidget(self.ledit_diap_meas_def, 8, 1, 1, 3)

        self.sbox_chan_no = QSpinBox(self.module_surv_dev_frame)
        self.sbox_chan_no.setObjectName(u"sbox_chan_no")
        self.sbox_chan_no.setEnabled(False)

        self.gridLayout_5.addWidget(self.sbox_chan_no, 7, 2, 1, 1)

        self.ledit_fac_no = QLineEdit(self.module_surv_dev_frame)
        self.ledit_fac_no.setObjectName(u"ledit_fac_no")
        self.ledit_fac_no.setEnabled(False)
        self.ledit_fac_no.setFont(font6)

        self.gridLayout_5.addWidget(self.ledit_fac_no, 3, 1, 1, 3)

        self.label_diap_meas_def = QLabel(self.module_surv_dev_frame)
        self.label_diap_meas_def.setObjectName(u"label_diap_meas_def")
        sizePolicy1.setHeightForWidth(self.label_diap_meas_def.sizePolicy().hasHeightForWidth())
        self.label_diap_meas_def.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_diap_meas_def, 8, 0, 1, 1)

        self.label_units_meas_dist = QLabel(self.module_surv_dev_frame)
        self.label_units_meas_dist.setObjectName(u"label_units_meas_dist")
        self.label_units_meas_dist.setFont(font3)

        self.gridLayout_5.addWidget(self.label_units_meas_dist, 5, 3, 1, 1)

        self.label_units_opt_dist = QLabel(self.module_surv_dev_frame)
        self.label_units_opt_dist.setObjectName(u"label_units_opt_dist")
        self.label_units_opt_dist.setFont(font3)

        self.gridLayout_5.addWidget(self.label_units_opt_dist, 9, 3, 1, 1)

        self.ledit_type_uo = QLineEdit(self.module_surv_dev_frame)
        self.ledit_type_uo.setObjectName(u"ledit_type_uo")
        self.ledit_type_uo.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ledit_type_uo.sizePolicy().hasHeightForWidth())
        self.ledit_type_uo.setSizePolicy(sizePolicy2)
        self.ledit_type_uo.setFont(font6)

        self.gridLayout_5.addWidget(self.ledit_type_uo, 1, 1, 1, 3)

        self.label_opt_dist = QLabel(self.module_surv_dev_frame)
        self.label_opt_dist.setObjectName(u"label_opt_dist")
        sizePolicy1.setHeightForWidth(self.label_opt_dist.sizePolicy().hasHeightForWidth())
        self.label_opt_dist.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_opt_dist, 9, 0, 1, 2)

        self.label_spat_res = QLabel(self.module_surv_dev_frame)
        self.label_spat_res.setObjectName(u"label_spat_res")
        sizePolicy1.setHeightForWidth(self.label_spat_res.sizePolicy().hasHeightForWidth())
        self.label_spat_res.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_spat_res, 6, 0, 1, 1)

        self.ledit_name_uo = QLineEdit(self.module_surv_dev_frame)
        self.ledit_name_uo.setObjectName(u"ledit_name_uo")
        self.ledit_name_uo.setEnabled(False)
        self.ledit_name_uo.setFont(font6)

        self.gridLayout_5.addWidget(self.ledit_name_uo, 2, 1, 1, 3)

        self.label_module_surv_dev = QLabel(self.module_surv_dev_frame)
        self.label_module_surv_dev.setObjectName(u"label_module_surv_dev")
        self.label_module_surv_dev.setFont(font4)
        self.label_module_surv_dev.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_5.addWidget(self.label_module_surv_dev, 0, 0, 1, 4)

        self.label_type_of = QLabel(self.module_surv_dev_frame)
        self.label_type_of.setObjectName(u"label_type_of")
        sizePolicy1.setHeightForWidth(self.label_type_of.sizePolicy().hasHeightForWidth())
        self.label_type_of.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_type_of, 4, 0, 1, 1)

        self.ledit_type_of = QLineEdit(self.module_surv_dev_frame)
        self.ledit_type_of.setObjectName(u"ledit_type_of")
        self.ledit_type_of.setEnabled(False)
        self.ledit_type_of.setFont(font6)

        self.gridLayout_5.addWidget(self.ledit_type_of, 4, 1, 1, 3)


        self.module_surv_dev_layout.addWidget(self.module_surv_dev_frame)


        self.main_layout.addLayout(self.module_surv_dev_layout, 1, 1, 1, 1)

        self.module_move_layout = QGridLayout()
        self.module_move_layout.setObjectName(u"module_move_layout")
        self.module_move_frame = QFrame(self.centralwidget)
        self.module_move_frame.setObjectName(u"module_move_frame")
        self.module_move_frame.setFont(font2)
        self.module_move_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_move_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.module_move_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.toggle_direct = QCheckBox(self.module_move_frame)
        self.toggle_direct.setObjectName(u"toggle_direct")
        self.toggle_direct.setEnabled(False)

        self.gridLayout_3.addWidget(self.toggle_direct, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.label_units_distance = QLabel(self.module_move_frame)
        self.label_units_distance.setObjectName(u"label_units_distance")
        self.label_units_distance.setFont(font3)

        self.gridLayout_3.addWidget(self.label_units_distance, 3, 3, 1, 1)

        self.distance_mm = QLabel(self.module_move_frame)
        self.distance_mm.setObjectName(u"distance_mm")
        self.distance_mm.setFont(font2)

        self.gridLayout_3.addWidget(self.distance_mm, 3, 0, 1, 1)

        self.dsbox_distance = QDoubleSpinBox(self.module_move_frame)
        self.dsbox_distance.setObjectName(u"dsbox_distance")
        self.dsbox_distance.setEnabled(False)
        self.dsbox_distance.setFont(font2)
        self.dsbox_distance.setDecimals(3)

        self.gridLayout_3.addWidget(self.dsbox_distance, 3, 2, 1, 1)

        self.label_units_speed = QLabel(self.module_move_frame)
        self.label_units_speed.setObjectName(u"label_units_speed")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_units_speed.sizePolicy().hasHeightForWidth())
        self.label_units_speed.setSizePolicy(sizePolicy3)
        self.label_units_speed.setFont(font3)

        self.gridLayout_3.addWidget(self.label_units_speed, 1, 3, 1, 2)

        self.label_speed = QLabel(self.module_move_frame)
        self.label_speed.setObjectName(u"label_speed")
        sizePolicy3.setHeightForWidth(self.label_speed.sizePolicy().hasHeightForWidth())
        self.label_speed.setSizePolicy(sizePolicy3)
        self.label_speed.setFont(font2)

        self.gridLayout_3.addWidget(self.label_speed, 1, 0, 1, 1)

        self.sbox_speed = QSpinBox(self.module_move_frame)
        self.sbox_speed.setObjectName(u"sbox_speed")
        self.sbox_speed.setEnabled(False)
        self.sbox_speed.setFont(font2)

        self.gridLayout_3.addWidget(self.sbox_speed, 1, 2, 1, 1)

        self.label_module_move = QLabel(self.module_move_frame)
        self.label_module_move.setObjectName(u"label_module_move")
        self.label_module_move.setFont(font4)
        self.label_module_move.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_3.addWidget(self.label_module_move, 0, 0, 1, 5)

        self.direct_mm = QLabel(self.module_move_frame)
        self.direct_mm.setObjectName(u"direct_mm")
        self.direct_mm.setFont(font2)

        self.gridLayout_3.addWidget(self.direct_mm, 2, 0, 1, 1)

        self.pbutton_start = QPushButton(self.module_move_frame)
        self.pbutton_start.setObjectName(u"pbutton_start")
        self.pbutton_start.setEnabled(False)

        self.gridLayout_3.addWidget(self.pbutton_start, 4, 0, 1, 1)

        self.pbutton_stop = QPushButton(self.module_move_frame)
        self.pbutton_stop.setObjectName(u"pbutton_stop")
        self.pbutton_stop.setEnabled(False)

        self.gridLayout_3.addWidget(self.pbutton_stop, 4, 2, 1, 1)


        self.module_move_layout.addWidget(self.module_move_frame, 0, 0, 1, 1)


        self.main_layout.addLayout(self.module_move_layout, 2, 0, 1, 1)

        self.sens_el_layout = QGridLayout()
        self.sens_el_layout.setObjectName(u"sens_el_layout")
        self.sens_el_frame = QFrame(self.centralwidget)
        self.sens_el_frame.setObjectName(u"sens_el_frame")
        self.sens_el_frame.setFont(font2)
        self.sens_el_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sens_el_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.sens_el_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_type_se = QLabel(self.sens_el_frame)
        self.label_type_se.setObjectName(u"label_type_se")
        sizePolicy1.setHeightForWidth(self.label_type_se.sizePolicy().hasHeightForWidth())
        self.label_type_se.setSizePolicy(sizePolicy1)
        self.label_type_se.setFont(font2)

        self.gridLayout_4.addWidget(self.label_type_se, 1, 0, 1, 1)

        self.label_units_deform_lim = QLabel(self.sens_el_frame)
        self.label_units_deform_lim.setObjectName(u"label_units_deform_lim")
        self.label_units_deform_lim.setFont(font3)

        self.gridLayout_4.addWidget(self.label_units_deform_lim, 7, 4, 1, 1)

        self.label_max_force = QLabel(self.sens_el_frame)
        self.label_max_force.setObjectName(u"label_max_force")
        self.label_max_force.setFont(font2)

        self.gridLayout_4.addWidget(self.label_max_force, 6, 0, 1, 2)

        self.dsbox_deform_lim = QDoubleSpinBox(self.sens_el_frame)
        self.dsbox_deform_lim.setObjectName(u"dsbox_deform_lim")
        self.dsbox_deform_lim.setEnabled(False)
        self.dsbox_deform_lim.setFont(font2)
        self.dsbox_deform_lim.setMaximum(9999.989999999999782)
        self.dsbox_deform_lim.setSingleStep(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsbox_deform_lim, 7, 3, 1, 1)

        self.label_units_max_force = QLabel(self.sens_el_frame)
        self.label_units_max_force.setObjectName(u"label_units_max_force")
        self.label_units_max_force.setFont(font3)

        self.gridLayout_4.addWidget(self.label_units_max_force, 6, 4, 1, 1)

        self.dsbox_max_deform = QDoubleSpinBox(self.sens_el_frame)
        self.dsbox_max_deform.setObjectName(u"dsbox_max_deform")
        self.dsbox_max_deform.setEnabled(False)
        self.dsbox_max_deform.setFont(font2)
        self.dsbox_max_deform.setMaximum(9999.989999999999782)
        self.dsbox_max_deform.setSingleStep(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsbox_max_deform, 5, 3, 1, 1)

        self.lable_deform_lim = QLabel(self.sens_el_frame)
        self.lable_deform_lim.setObjectName(u"lable_deform_lim")
        self.lable_deform_lim.setFont(font2)

        self.gridLayout_4.addWidget(self.lable_deform_lim, 7, 0, 1, 2)

        self.label_diam_start = QLabel(self.sens_el_frame)
        self.label_diam_start.setObjectName(u"label_diam_start")
        self.label_diam_start.setFont(font2)

        self.gridLayout_4.addWidget(self.label_diam_start, 3, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.label_mod_young = QLabel(self.sens_el_frame)
        self.label_mod_young.setObjectName(u"label_mod_young")
        self.label_mod_young.setFont(font2)

        self.gridLayout_4.addWidget(self.label_mod_young, 4, 0, 1, 2)

        self.ledit_notes = QLineEdit(self.sens_el_frame)
        self.ledit_notes.setObjectName(u"ledit_notes")
        self.ledit_notes.setEnabled(False)
        self.ledit_notes.setFont(font6)

        self.gridLayout_4.addWidget(self.ledit_notes, 9, 1, 1, 4)

        self.label_sagging = QLabel(self.sens_el_frame)
        self.label_sagging.setObjectName(u"label_sagging")
        self.label_sagging.setFont(font2)

        self.gridLayout_4.addWidget(self.label_sagging, 8, 0, 1, 2)

        self.label_max_deform = QLabel(self.sens_el_frame)
        self.label_max_deform.setObjectName(u"label_max_deform")
        self.label_max_deform.setFont(font2)

        self.gridLayout_4.addWidget(self.label_max_deform, 5, 0, 1, 2)

        self.label_scheme_con = QLabel(self.sens_el_frame)
        self.label_scheme_con.setObjectName(u"label_scheme_con")
        self.label_scheme_con.setFont(font2)

        self.gridLayout_4.addWidget(self.label_scheme_con, 2, 0, 1, 1)

        self.label_units_diam_start = QLabel(self.sens_el_frame)
        self.label_units_diam_start.setObjectName(u"label_units_diam_start")
        self.label_units_diam_start.setFont(font3)

        self.gridLayout_4.addWidget(self.label_units_diam_start, 3, 4, 1, 1)

        self.label_sens_el = QLabel(self.sens_el_frame)
        self.label_sens_el.setObjectName(u"label_sens_el")
        self.label_sens_el.setFont(font4)
        self.label_sens_el.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_4.addWidget(self.label_sens_el, 0, 0, 1, 5)

        self.ledit_type_se = QLineEdit(self.sens_el_frame)
        self.ledit_type_se.setObjectName(u"ledit_type_se")
        self.ledit_type_se.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ledit_type_se.sizePolicy().hasHeightForWidth())
        self.ledit_type_se.setSizePolicy(sizePolicy4)
        self.ledit_type_se.setFont(font6)

        self.gridLayout_4.addWidget(self.ledit_type_se, 1, 1, 1, 4)

        self.label_units_max_deform = QLabel(self.sens_el_frame)
        self.label_units_max_deform.setObjectName(u"label_units_max_deform")
        self.label_units_max_deform.setFont(font3)

        self.gridLayout_4.addWidget(self.label_units_max_deform, 5, 4, 1, 1)

        self.dsbox_sagging = QDoubleSpinBox(self.sens_el_frame)
        self.dsbox_sagging.setObjectName(u"dsbox_sagging")
        self.dsbox_sagging.setEnabled(False)
        self.dsbox_sagging.setFont(font2)
        self.dsbox_sagging.setMaximum(9999.989999999999782)
        self.dsbox_sagging.setSingleStep(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsbox_sagging, 8, 3, 1, 1)

        self.ledit_sens_el = QLineEdit(self.sens_el_frame)
        self.ledit_sens_el.setObjectName(u"ledit_sens_el")
        self.ledit_sens_el.setEnabled(False)
        self.ledit_sens_el.setFont(font6)

        self.gridLayout_4.addWidget(self.ledit_sens_el, 2, 1, 1, 4)

        self.dsbox_max_force = QDoubleSpinBox(self.sens_el_frame)
        self.dsbox_max_force.setObjectName(u"dsbox_max_force")
        self.dsbox_max_force.setEnabled(False)
        self.dsbox_max_force.setFont(font2)
        self.dsbox_max_force.setMaximum(9999.989999999999782)
        self.dsbox_max_force.setSingleStep(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsbox_max_force, 6, 3, 1, 1)

        self.label_units_mod_young = QLabel(self.sens_el_frame)
        self.label_units_mod_young.setObjectName(u"label_units_mod_young")
        self.label_units_mod_young.setFont(font2)

        self.gridLayout_4.addWidget(self.label_units_mod_young, 4, 4, 1, 1)

        self.label_notes = QLabel(self.sens_el_frame)
        self.label_notes.setObjectName(u"label_notes")
        self.label_notes.setFont(font2)

        self.gridLayout_4.addWidget(self.label_notes, 9, 0, 1, 1)

        self.label_units_sagging = QLabel(self.sens_el_frame)
        self.label_units_sagging.setObjectName(u"label_units_sagging")
        self.label_units_sagging.setFont(font3)

        self.gridLayout_4.addWidget(self.label_units_sagging, 8, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.dsbox_diam_start = QDoubleSpinBox(self.sens_el_frame)
        self.dsbox_diam_start.setObjectName(u"dsbox_diam_start")
        self.dsbox_diam_start.setEnabled(False)
        self.dsbox_diam_start.setFont(font2)
        self.dsbox_diam_start.setDecimals(3)
        self.dsbox_diam_start.setMaximum(9999.989999999999782)
        self.dsbox_diam_start.setSingleStep(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsbox_diam_start, 3, 3, 1, 1)

        self.dsbox_mod_young = QDoubleSpinBox(self.sens_el_frame)
        self.dsbox_mod_young.setObjectName(u"dsbox_mod_young")
        self.dsbox_mod_young.setEnabled(False)
        self.dsbox_mod_young.setFont(font2)
        self.dsbox_mod_young.setMaximum(9999.989999999999782)
        self.dsbox_mod_young.setSingleStep(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsbox_mod_young, 4, 3, 1, 1)


        self.sens_el_layout.addWidget(self.sens_el_frame, 0, 0, 1, 1)


        self.main_layout.addLayout(self.sens_el_layout, 1, 0, 1, 1)

        self.calculation_data_layout = QGridLayout()
        self.calculation_data_layout.setObjectName(u"calculation_data_layout")
        self.calculation_data_frame = QFrame(self.centralwidget)
        self.calculation_data_frame.setObjectName(u"calculation_data_frame")
        self.calculation_data_frame.setFont(font2)
        self.calculation_data_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.calculation_data_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.calculation_data_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_units_rel_elong = QLabel(self.calculation_data_frame)
        self.label_units_rel_elong.setObjectName(u"label_units_rel_elong")
        self.label_units_rel_elong.setFont(font3)

        self.gridLayout_8.addWidget(self.label_units_rel_elong, 3, 2, 1, 1)

        self.label_rel_elong = QLabel(self.calculation_data_frame)
        self.label_rel_elong.setObjectName(u"label_rel_elong")

        self.gridLayout_8.addWidget(self.label_rel_elong, 3, 0, 1, 1)

        self.label_units_final_diam = QLabel(self.calculation_data_frame)
        self.label_units_final_diam.setObjectName(u"label_units_final_diam")
        sizePolicy1.setHeightForWidth(self.label_units_final_diam.sizePolicy().hasHeightForWidth())
        self.label_units_final_diam.setSizePolicy(sizePolicy1)
        self.label_units_final_diam.setFont(font3)

        self.gridLayout_8.addWidget(self.label_units_final_diam, 1, 2, 1, 1)

        self.label_output_rel_narrow = QLabel(self.calculation_data_frame)
        self.label_output_rel_narrow.setObjectName(u"label_output_rel_narrow")
        self.label_output_rel_narrow.setEnabled(False)
        self.label_output_rel_narrow.setFont(font5)

        self.gridLayout_8.addWidget(self.label_output_rel_narrow, 4, 1, 1, 1)

        self.dsbox_final_length = QDoubleSpinBox(self.calculation_data_frame)
        self.dsbox_final_length.setObjectName(u"dsbox_final_length")
        self.dsbox_final_length.setEnabled(False)
        self.dsbox_final_length.setMaximum(9999.989999999999782)
        self.dsbox_final_length.setSingleStep(0.100000000000000)

        self.gridLayout_8.addWidget(self.dsbox_final_length, 2, 1, 1, 1)

        self.label_final_length = QLabel(self.calculation_data_frame)
        self.label_final_length.setObjectName(u"label_final_length")

        self.gridLayout_8.addWidget(self.label_final_length, 2, 0, 1, 1)

        self.dsbox_final_diam = QDoubleSpinBox(self.calculation_data_frame)
        self.dsbox_final_diam.setObjectName(u"dsbox_final_diam")
        self.dsbox_final_diam.setEnabled(False)
        self.dsbox_final_diam.setDecimals(3)
        self.dsbox_final_diam.setMaximum(9999.989999999999782)
        self.dsbox_final_diam.setSingleStep(0.100000000000000)

        self.gridLayout_8.addWidget(self.dsbox_final_diam, 1, 1, 1, 1)

        self.label_calculation_data = QLabel(self.calculation_data_frame)
        self.label_calculation_data.setObjectName(u"label_calculation_data")
        self.label_calculation_data.setFont(font1)
        self.label_calculation_data.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_8.addWidget(self.label_calculation_data, 0, 0, 1, 3)

        self.label_units_rel_narrow = QLabel(self.calculation_data_frame)
        self.label_units_rel_narrow.setObjectName(u"label_units_rel_narrow")
        self.label_units_rel_narrow.setFont(font3)

        self.gridLayout_8.addWidget(self.label_units_rel_narrow, 4, 2, 1, 1)

        self.label_units_final_length = QLabel(self.calculation_data_frame)
        self.label_units_final_length.setObjectName(u"label_units_final_length")
        self.label_units_final_length.setFont(font3)

        self.gridLayout_8.addWidget(self.label_units_final_length, 2, 2, 1, 1)

        self.label_final_diam = QLabel(self.calculation_data_frame)
        self.label_final_diam.setObjectName(u"label_final_diam")

        self.gridLayout_8.addWidget(self.label_final_diam, 1, 0, 1, 1)

        self.label_rel_narrow = QLabel(self.calculation_data_frame)
        self.label_rel_narrow.setObjectName(u"label_rel_narrow")

        self.gridLayout_8.addWidget(self.label_rel_narrow, 4, 0, 1, 1)

        self.label_output_rel_elong = QLabel(self.calculation_data_frame)
        self.label_output_rel_elong.setObjectName(u"label_output_rel_elong")
        self.label_output_rel_elong.setEnabled(False)
        self.label_output_rel_elong.setFont(font5)

        self.gridLayout_8.addWidget(self.label_output_rel_elong, 3, 1, 1, 1)

        self.label_module_elast = QLabel(self.calculation_data_frame)
        self.label_module_elast.setObjectName(u"label_module_elast")

        self.gridLayout_8.addWidget(self.label_module_elast, 5, 0, 1, 1)

        self.label_output_module_elast = QLabel(self.calculation_data_frame)
        self.label_output_module_elast.setObjectName(u"label_output_module_elast")
        self.label_output_module_elast.setEnabled(False)
        self.label_output_module_elast.setFont(font5)

        self.gridLayout_8.addWidget(self.label_output_module_elast, 5, 1, 1, 1)

        self.label_units__module_elast = QLabel(self.calculation_data_frame)
        self.label_units__module_elast.setObjectName(u"label_units__module_elast")

        self.gridLayout_8.addWidget(self.label_units__module_elast, 5, 2, 1, 1)


        self.calculation_data_layout.addWidget(self.calculation_data_frame, 0, 0, 1, 1)


        self.main_layout.addLayout(self.calculation_data_layout, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.main_layout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1293, 20))
        self.menu_conn = QMenu(self.menubar)
        self.menu_conn.setObjectName(u"menu_conn")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_conn.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu_conn.addAction(self.connection_settings)
        self.menu.addAction(self.graph)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connection_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f", None))
        self.graph.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.force_graph.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430", None))
        self.label_module_rec_data.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u043c\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_dist_to_trans_deform.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0434\u043e \u0442\u043e\u0447\u043a\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e\u043f\u0435\u0440\u0435\u0447\u043d\u043e\u0439 \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438, \u0394L\u043f", None))
        self.label_type_deform.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.cbox_units_long_deform.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043c\u043a\u03b5", None))
        self.cbox_units_long_deform.setItemText(1, QCoreApplication.translate("MainWindow", u"%", None))
        self.cbox_units_long_deform.setItemText(2, QCoreApplication.translate("MainWindow", u"\u043c\u043a\u043c", None))

        self.label_trans_deform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0435\u043c\u0430\u044f \u043f\u043e\u043f\u0435\u0440\u0435\u0447\u043d\u0430\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f, \u03b5\u043f", None))
        self.label_deform_area.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0443\u0447\u0430\u0441\u0442\u043e\u043a, \u0394L", None))
        self.label_utins_dist_to_trans_deform.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.cmob_type_deform.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u044c\u043d\u0430\u044f", None))
        self.cmob_type_deform.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u0435\u0440\u0435\u0447\u043d\u0430\u044f", None))
        self.cmob_type_deform.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u044c\u043d\u0430\u044f \u0438 \u043f\u043e\u043f\u0435\u0440\u0435\u0447\u043d\u0430\u044f", None))

        self.label_total_deform.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f, \u03b5\u043e\u0431", None))
        self.cbox_units_trans_deform.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043c\u043a\u03b5", None))
        self.cbox_units_trans_deform.setItemText(1, QCoreApplication.translate("MainWindow", u"%", None))

        self.label_leng_trans.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u043e\u043f\u0435\u0440\u0435\u0447\u043d\u043e\u0433\u043e \u0443\u0434\u043b\u0438\u043d\u0435\u043d\u0438\u044f, \u03b4L\u043f", None))
        self.pbutton_set_zero.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u043d\u043e\u0432\u0438\u0442\u044c \u00ab0\u00bb", None))
        self.label_units_deform_area.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.label_long_deform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0435\u043c\u0430\u044f \u043f\u0440\u043e\u0434\u043e\u043b\u044c\u043d\u0430\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f, \u03b5", None))
        self.pbutton_start_deform.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043f\u0443\u0441\u043a", None))
        self.chbox_write_file.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c \u0432 \u0444\u0430\u0439\u043b", None))
        self.label_module_deform.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.label_units_leng_trans.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043c", None))
        self.label_leng_trans_out.setText("")
        self.label_total_deform_out.setText("")
        self.label_units_total_deform.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043a\u03b5", None))
        self.pbutton_save_file.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_name_uo.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0423\u041e", None))
        self.label_fac_no.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u043e\u0434\u0441\u043a\u043e\u0439 \u2116", None))
        self.label_chan_no.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u043a\u0430\u043d\u0430\u043b\u0430 \u0438\u0437\u043c.", None))
        self.label_meas_dist.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u0440\u044f\u0435\u043c\u0430\u044f \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u044f", None))
        self.label_units_spat_res.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.label_type_uo.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0423\u041e", None))
        self.label_diap_meas_def.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0438\u0437\u043c\u0435\u0440\u044f\u0435\u043c\u043e\u0439 \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.label_units_meas_dist.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043c", None))
        self.label_units_opt_dist.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.label_opt_dist.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u0432\u0445\u043e\u0434\u0430 \u0423\u041e \u0434\u043e \u0443\u0447\u0430\u0441\u0442\u043a\u0430 \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.label_spat_res.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.label_module_surv_dev.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0438\u0441\u043f\u044b\u0442\u0443\u0435\u043c\u043e\u0433\u043e \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label_type_of.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u041e\u0412", None))
        self.toggle_direct.setText("")
        self.label_units_distance.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043c", None))
        self.distance_mm.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.label_units_speed.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043a\u043c/c", None))
        self.label_speed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.label_module_move.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0434\u0432\u0438\u0436\u043a\u0438", None))
        self.direct_mm.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pbutton_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pbutton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_type_se.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0427\u042d", None))
        self.label_units_deform_lim.setText(QCoreApplication.translate("MainWindow", u"\u041d", None))
        self.label_max_force.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0443\u0441\u0438\u043b\u0438\u0435", None))
        self.label_units_max_force.setText(QCoreApplication.translate("MainWindow", u"\u041d", None))
        self.lable_deform_lim.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0434\u0435\u043b \u0443\u043f\u0440\u0443\u0433\u043e\u0439 \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.label_diam_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440 \u0441\u0435\u0447\u0435\u043d\u0438\u044f \u0427\u042d, d\u041d", None))
        self.label_mod_young.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u042e\u043d\u0433\u0430", None))
        self.label_sagging.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0438\u043b\u0438\u0435 \u0438\u0441\u043a\u043b\u044e\u0447\u0430\u044e\u0449\u0435\u0435 \u043f\u0440\u043e\u0432\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_max_deform.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_scheme_con.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0445\u0435\u043c\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.label_units_diam_start.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043c", None))
        self.label_sens_el.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 ", None))
        self.label_units_max_deform.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_units_mod_young.setText(QCoreApplication.translate("MainWindow", u"\u0415", None))
        self.label_notes.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_units_sagging.setText(QCoreApplication.translate("MainWindow", u"\u041d", None))
        self.label_units_rel_elong.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_rel_elong.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u0434\u043b\u0438\u043d\u0435\u043d\u0438\u0435 \u0427\u042d, \u03b4", None))
        self.label_units_final_diam.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043c", None))
        self.label_output_rel_narrow.setText("")
        self.label_final_length.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0434\u043b\u0438\u043d\u0430 \u0427\u042d, \u0394Lk", None))
        self.label_calculation_data.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0440\u0430\u0441\u0447\u0451\u0442\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_units_rel_narrow.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_units_final_length.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.label_final_diam.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440 \u0427\u042d", None))
        self.label_rel_narrow.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0441\u0443\u0436\u0435\u043d\u0438\u0435 \u0427\u042d, \u03c8", None))
        self.label_output_rel_elong.setText("")
        self.label_module_elast.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0443\u043f\u0440\u0443\u0433\u043e\u0441\u0442\u0438 (\u042e\u043d\u0433\u0430)", None))
        self.label_output_module_elast.setText("")
        self.label_units__module_elast.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.menu_conn.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 ", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

