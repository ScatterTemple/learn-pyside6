# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizardDKaNvw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget, QWizard,
    QWizardPage)

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        if not Wizard.objectName():
            Wizard.setObjectName(u"Wizard")
        Wizard.resize(670, 460)
        Wizard.setWizardStyle(QWizard.WizardStyle.ModernStyle)
        Wizard.setOptions(QWizard.WizardOption.ExtendedWatermarkPixmap)
        self.wizardPage1_launch = QWizardPage()
        self.wizardPage1_launch.setObjectName(u"wizardPage1_launch")
        self.pushButton = QPushButton(self.wizardPage1_launch)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 130, 131, 61))
        Wizard.addPage(self.wizardPage1_launch)
        self.wizardPage2_verify = QWizardPage()
        self.wizardPage2_verify.setObjectName(u"wizardPage2_verify")
        self.refresh_button = QPushButton(self.wizardPage2_verify)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(90, 150, 81, 81))
        self.label_1 = QLabel(self.wizardPage2_verify)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(280, 140, 49, 16))
        self.label_2 = QLabel(self.wizardPage2_verify)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 200, 49, 16))
        self.label_femprj_path = QLabel(self.wizardPage2_verify)
        self.label_femprj_path.setObjectName(u"label_femprj_path")
        self.label_femprj_path.setGeometry(QRect(320, 140, 221, 16))
        self.label_model_name = QLabel(self.wizardPage2_verify)
        self.label_model_name.setObjectName(u"label_model_name")
        self.label_model_name.setGeometry(QRect(320, 200, 211, 16))
        Wizard.addPage(self.wizardPage2_verify)
        self.wizardPage3_param = QWizardPage()
        self.wizardPage3_param.setObjectName(u"wizardPage3_param")
        self.tableView = QTableView(self.wizardPage3_param)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(170, 120, 361, 192))
        self.pushButton_3 = QPushButton(self.wizardPage3_param)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 200, 75, 24))
        Wizard.addPage(self.wizardPage3_param)
        self.wizardPage4_obj = QWizardPage()
        self.wizardPage4_obj.setObjectName(u"wizardPage4_obj")
        self.tableView_2 = QTableView(self.wizardPage4_obj)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(230, 130, 256, 192))
        self.pushButton_4 = QPushButton(self.wizardPage4_obj)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 210, 75, 24))
        Wizard.addPage(self.wizardPage4_obj)

        self.retranslateUi(Wizard)

        QMetaObject.connectSlotsByName(Wizard)
    # setupUi

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QCoreApplication.translate("Wizard", u"Wizard", None))
        self.pushButton.setText(QCoreApplication.translate("Wizard", u"Launch Femtet", None))
        self.refresh_button.setText(QCoreApplication.translate("Wizard", u"refresh", None))
        self.label_1.setText(QCoreApplication.translate("Wizard", u"femprj", None))
        self.label_2.setText(QCoreApplication.translate("Wizard", u"model", None))
        self.label_femprj_path.setText(QCoreApplication.translate("Wizard", u"some\\model.femprj", None))
        self.label_model_name.setText(QCoreApplication.translate("Wizard", u"somemodel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Wizard", u"refresh", None))
        self.pushButton_4.setText(QCoreApplication.translate("Wizard", u"refresh", None))
    # retranslateUi

