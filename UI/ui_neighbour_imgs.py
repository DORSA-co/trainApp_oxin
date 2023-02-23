# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'neighbour_imgs.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 732)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rightButtons = QFrame(self.frame)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 50))
        self.rightButtons.setMaximumSize(QSize(16777215, 50))
        self.rightButtons.setStyleSheet(u"background-color: #b7baab;")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.helpButton = QPushButton(self.rightButtons)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(28, 28))
        self.helpButton.setMaximumSize(QSize(28, 28))
        self.helpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpButton.setStyleSheet(u"#rightButtons .QPushButton { background-color:rgb(120, 120, 120); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon = QIcon()
        icon.addFile(u"images/icons/icon_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QSize(17, 17))

        self.horizontalLayout_2.addWidget(self.helpButton)

        self.miniButton = QPushButton(self.rightButtons)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniButton.setStyleSheet(u"#rightButtons .QPushButton { background-color:rgb(120, 120, 120); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon1)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.rightButtons)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxiButton.setStyleSheet(u"#rightButtons .QPushButton { background-color:rgb(120, 120, 120); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon2)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.rightButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"#rightButtons .QPushButton { background-color:rgb(120, 120, 120); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.verticalLayout_3.addWidget(self.rightButtons)

        self.n_image = QLabel(self.frame)
        self.n_image.setObjectName(u"n_image")
        self.n_image.setMinimumSize(QSize(940, 600))
        self.n_image.setMaximumSize(QSize(16777215, 16777215))
        self.n_image.setStyleSheet(u"border: 3px solid rgb(255, 255, 255);")
        self.n_image.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.n_image)

        self.rightButtons_2 = QFrame(self.frame)
        self.rightButtons_2.setObjectName(u"rightButtons_2")
        self.rightButtons_2.setMinimumSize(QSize(0, 50))
        self.rightButtons_2.setMaximumSize(QSize(16777215, 50))
        self.rightButtons_2.setStyleSheet(u"background-color: #b7baab;")
        self.rightButtons_2.setFrameShape(QFrame.NoFrame)
        self.rightButtons_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.rightButtons_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.annot_checkbox = QCheckBox(self.rightButtons_2)
        self.annot_checkbox.setObjectName(u"annot_checkbox")
        self.annot_checkbox.setEnabled(False)
        self.annot_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.annot_checkbox.setStyleSheet(u"color: black;")

        self.horizontalLayout.addWidget(self.annot_checkbox)

        self.msg_label = QLabel(self.rightButtons_2)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setStyleSheet(u"color:red;")

        self.horizontalLayout.addWidget(self.msg_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.rightButtons_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText("")
#if QT_CONFIG(tooltip)
        self.miniButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniButton.setText("")
#if QT_CONFIG(tooltip)
        self.maxiButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.maxiButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.n_image.setText("")
        self.annot_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show Labels", None))
        self.msg_label.setText("")
    # retranslateUi
