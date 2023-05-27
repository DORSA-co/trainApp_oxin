# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextEdit, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1303, 709)
        MainWindow.setMinimumSize(QSize(1303, 709))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font-size: 8pt;\n"
"background-color: rgb(220, 220,220);\n"
"\n"
"border-color: rgb(188, 188, 188);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setStyleSheet(u"background-color: #b7baab;\n"
"color: black;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(34, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox_font = QSpinBox(self.frame_4)
        self.spinBox_font.setObjectName(u"spinBox_font")
        self.spinBox_font.setStyleSheet(u"")
        self.spinBox_font.setMinimum(8)
        self.spinBox_font.setMaximum(20)

        self.horizontalLayout.addWidget(self.spinBox_font)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.miniButton = QPushButton(self.frame_4)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(20, 20))
        self.miniButton.setMaximumSize(QSize(20, 20))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniButton.setStyleSheet(u"QPushButton {\n"
" 	background-color:rgb(120, 120, 120);\n"
" 	border: none;  \n"
"	border-radius: 5px;\n"
" }\n"
"QPushButton:hover { \n"
"	background-color: rgb(44, 49, 57); \n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
" }\n"
"QPushButton:pressed { \n"
"	background-color: rgb(23, 26, 30); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}")
        icon = QIcon()
        icon.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.frame_4)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(20, 20))
        self.maxiButton.setMaximumSize(QSize(20, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font1)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxiButton.setStyleSheet(u"QPushButton {\n"
" 	background-color:rgb(120, 120, 120);\n"
" 	border: none;  \n"
"	border-radius: 5px;\n"
" }\n"
"QPushButton:hover { \n"
"	background-color: rgb(44, 49, 57); \n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
" }\n"
"QPushButton:pressed { \n"
"	background-color: rgb(23, 26, 30); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon1)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.frame_4)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(20, 20))
        self.closeButton.setMaximumSize(QSize(20, 20))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"QPushButton {\n"
" 	background-color:rgb(120, 120, 120);\n"
" 	border: none;  \n"
"	border-radius: 5px;\n"
" }\n"
"QPushButton:hover { \n"
"	background-color: rgb(44, 49, 57); \n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
" }\n"
"QPushButton:pressed { \n"
"	background-color: rgb(23, 26, 30); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.closeButton)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 35))
        self.frame.setStyleSheet(u"background-color: #b7baab;\n"
"color: black;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(250, 0))
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.frame_3)
        self.treeView.setObjectName(u"treeView")
        font2 = QFont()
        font2.setPointSize(8)
        self.treeView.setFont(font2)
        self.treeView.setStyleSheet(u"QTreeView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"     border: 1px solid #d9d9d9;\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
"}")

        self.verticalLayout_3.addWidget(self.treeView)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 90))
        self.textEdit.setFrameShape(QFrame.Box)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1046, 573))
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setScaledContents(True)
        self.label.setMargin(2)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Help - Sens", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Font :", None))
#if QT_CONFIG(tooltip)
        self.miniButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniButton.setText("")
#if QT_CONFIG(tooltip)
        self.maxiButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxiButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.label.setText("")
    # retranslateUi

