# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'labeling.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(317, 187)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #b7baab;\n"
"color: black;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_defects = QComboBox(self.frame)
        self.comboBox_defects.setObjectName(u"comboBox_defects")

        self.verticalLayout_2.addWidget(self.comboBox_defects)

        self.tableWidget_defects = QTableWidget(self.frame)
        if (self.tableWidget_defects.columnCount() < 5):
            self.tableWidget_defects.setColumnCount(5)
        self.tableWidget_defects.setObjectName(u"tableWidget_defects")
        self.tableWidget_defects.setColumnCount(5)

        self.verticalLayout_2.addWidget(self.tableWidget_defects)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_btn = QPushButton(self.frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

