# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'full_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 609)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.rightButtons = QFrame(self.centralwidget)
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

        self.miniButton = QPushButton(self.rightButtons)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniButton.setStyleSheet(u"#rightButtons .QPushButton { background-color:rgb(120, 120, 120); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon = QIcon()
        icon.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.verticalLayout.addWidget(self.rightButtons)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_single = QWidget()
        self.page_single.setObjectName(u"page_single")
        self.verticalLayout_2 = QVBoxLayout(self.page_single)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.live = QLabel(self.page_single)
        self.live.setObjectName(u"live")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live.sizePolicy().hasHeightForWidth())
        self.live.setSizePolicy(sizePolicy)
        self.live.setMinimumSize(QSize(800, 500))
        self.live.setFrameShape(QFrame.Box)
        self.live.setFrameShadow(QFrame.Plain)
        self.live.setScaledContents(True)
        self.live.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.live.setMargin(0)
        self.live.setIndent(0)

        self.verticalLayout_2.addWidget(self.live)

        self.stackedWidget.addWidget(self.page_single)
        self.page_top = QWidget()
        self.page_top.setObjectName(u"page_top")
        self.verticalLayout_3 = QVBoxLayout(self.page_top)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_64 = QFrame(self.page_top)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.Box)
        self.frame_64.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_225 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_225.setSpacing(0)
        self.horizontalLayout_225.setObjectName(u"horizontalLayout_225")
        self.horizontalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.tlive1 = QLabel(self.frame_64)
        self.tlive1.setObjectName(u"tlive1")
        self.tlive1.setMinimumSize(QSize(200, 125))
        self.tlive1.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive1)

        self.tlive2 = QLabel(self.frame_64)
        self.tlive2.setObjectName(u"tlive2")
        self.tlive2.setMinimumSize(QSize(200, 125))
        self.tlive2.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive2)

        self.tlive3 = QLabel(self.frame_64)
        self.tlive3.setObjectName(u"tlive3")
        self.tlive3.setMinimumSize(QSize(200, 125))
        self.tlive3.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive3)

        self.tlive4 = QLabel(self.frame_64)
        self.tlive4.setObjectName(u"tlive4")
        self.tlive4.setMinimumSize(QSize(200, 125))
        self.tlive4.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive4)


        self.verticalLayout_3.addWidget(self.frame_64)

        self.horizontalLayout_205 = QHBoxLayout()
        self.horizontalLayout_205.setSpacing(10)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(10, -1, 10, -1)
        self.label_46 = QLabel(self.page_top)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 20))
        self.label_46.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_46)

        self.label_47 = QLabel(self.page_top)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 20))
        self.label_47.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_47)

        self.label_48 = QLabel(self.page_top)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 20))
        self.label_48.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_48)

        self.label_49 = QLabel(self.page_top)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 20))
        self.label_49.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_49)


        self.verticalLayout_3.addLayout(self.horizontalLayout_205)

        self.frame_67 = QFrame(self.page_top)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.Box)
        self.frame_67.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_226 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_226.setSpacing(0)
        self.horizontalLayout_226.setObjectName(u"horizontalLayout_226")
        self.horizontalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.tlive5 = QLabel(self.frame_67)
        self.tlive5.setObjectName(u"tlive5")
        self.tlive5.setMinimumSize(QSize(200, 125))
        self.tlive5.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive5)

        self.tlive6 = QLabel(self.frame_67)
        self.tlive6.setObjectName(u"tlive6")
        self.tlive6.setMinimumSize(QSize(200, 125))
        self.tlive6.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive6)

        self.tlive7 = QLabel(self.frame_67)
        self.tlive7.setObjectName(u"tlive7")
        self.tlive7.setMinimumSize(QSize(200, 125))
        self.tlive7.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive7)

        self.tlive8 = QLabel(self.frame_67)
        self.tlive8.setObjectName(u"tlive8")
        self.tlive8.setMinimumSize(QSize(200, 125))
        self.tlive8.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive8)


        self.verticalLayout_3.addWidget(self.frame_67)

        self.horizontalLayout_206 = QHBoxLayout()
        self.horizontalLayout_206.setSpacing(10)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(10, -1, 10, -1)
        self.label_50 = QLabel(self.page_top)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 20))
        self.label_50.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.label_50)

        self.label_51 = QLabel(self.page_top)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 20))
        self.label_51.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.label_51)

        self.label_53 = QLabel(self.page_top)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(16777215, 20))
        self.label_53.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.label_53)

        self.label_54 = QLabel(self.page_top)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 20))
        self.label_54.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.label_54)


        self.verticalLayout_3.addLayout(self.horizontalLayout_206)

        self.frame_69 = QFrame(self.page_top)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.Box)
        self.frame_69.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_193 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_193.setSpacing(0)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.tlive9 = QLabel(self.frame_69)
        self.tlive9.setObjectName(u"tlive9")
        self.tlive9.setMinimumSize(QSize(200, 125))
        self.tlive9.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive9)

        self.tlive10 = QLabel(self.frame_69)
        self.tlive10.setObjectName(u"tlive10")
        self.tlive10.setMinimumSize(QSize(200, 125))
        self.tlive10.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive10)

        self.tlive11 = QLabel(self.frame_69)
        self.tlive11.setObjectName(u"tlive11")
        self.tlive11.setMinimumSize(QSize(200, 125))
        self.tlive11.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive11)

        self.tlive12 = QLabel(self.frame_69)
        self.tlive12.setObjectName(u"tlive12")
        self.tlive12.setMinimumSize(QSize(200, 125))
        self.tlive12.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive12)


        self.verticalLayout_3.addWidget(self.frame_69)

        self.horizontalLayout_207 = QHBoxLayout()
        self.horizontalLayout_207.setSpacing(10)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_207.setContentsMargins(10, -1, 10, -1)
        self.label_55 = QLabel(self.page_top)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(16777215, 20))
        self.label_55.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_207.addWidget(self.label_55)

        self.label_56 = QLabel(self.page_top)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(16777215, 20))
        self.label_56.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_207.addWidget(self.label_56)

        self.label_57 = QLabel(self.page_top)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(16777215, 20))
        self.label_57.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_207.addWidget(self.label_57)

        self.label_58 = QLabel(self.page_top)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(16777215, 20))
        self.label_58.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_207.addWidget(self.label_58)


        self.verticalLayout_3.addLayout(self.horizontalLayout_207)

        self.stackedWidget.addWidget(self.page_top)
        self.page_bottom = QWidget()
        self.page_bottom.setObjectName(u"page_bottom")
        self.verticalLayout_4 = QVBoxLayout(self.page_bottom)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.frame_78 = QFrame(self.page_bottom)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.Box)
        self.frame_78.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_200 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_200.setSpacing(0)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.blive13 = QLabel(self.frame_78)
        self.blive13.setObjectName(u"blive13")
        self.blive13.setMinimumSize(QSize(200, 125))
        self.blive13.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive13)

        self.blive14 = QLabel(self.frame_78)
        self.blive14.setObjectName(u"blive14")
        self.blive14.setMinimumSize(QSize(200, 125))
        self.blive14.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive14)

        self.blive15 = QLabel(self.frame_78)
        self.blive15.setObjectName(u"blive15")
        self.blive15.setMinimumSize(QSize(200, 125))
        self.blive15.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive15)

        self.blive16 = QLabel(self.frame_78)
        self.blive16.setObjectName(u"blive16")
        self.blive16.setMinimumSize(QSize(200, 125))
        self.blive16.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive16)


        self.verticalLayout_4.addWidget(self.frame_78)

        self.horizontalLayout_209 = QHBoxLayout()
        self.horizontalLayout_209.setSpacing(10)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(10, -1, 10, -1)
        self.label_64 = QLabel(self.page_bottom)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 20))
        self.label_64.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_209.addWidget(self.label_64)

        self.label_65 = QLabel(self.page_bottom)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 20))
        self.label_65.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_209.addWidget(self.label_65)

        self.label_66 = QLabel(self.page_bottom)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 20))
        self.label_66.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_209.addWidget(self.label_66)

        self.label_70 = QLabel(self.page_bottom)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 20))
        self.label_70.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_209.addWidget(self.label_70)


        self.verticalLayout_4.addLayout(self.horizontalLayout_209)

        self.frame_101 = QFrame(self.page_bottom)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.Box)
        self.frame_101.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_202 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_202.setSpacing(0)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.blive17 = QLabel(self.frame_101)
        self.blive17.setObjectName(u"blive17")
        self.blive17.setMinimumSize(QSize(200, 125))
        self.blive17.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive17)

        self.blive18 = QLabel(self.frame_101)
        self.blive18.setObjectName(u"blive18")
        self.blive18.setMinimumSize(QSize(200, 125))
        self.blive18.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive18)

        self.blive19 = QLabel(self.frame_101)
        self.blive19.setObjectName(u"blive19")
        self.blive19.setMinimumSize(QSize(200, 125))
        self.blive19.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive19)

        self.blive20 = QLabel(self.frame_101)
        self.blive20.setObjectName(u"blive20")
        self.blive20.setMinimumSize(QSize(200, 125))
        self.blive20.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive20)


        self.verticalLayout_4.addWidget(self.frame_101)

        self.horizontalLayout_211 = QHBoxLayout()
        self.horizontalLayout_211.setSpacing(10)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(10, -1, 10, -1)
        self.label_85 = QLabel(self.page_bottom)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(16777215, 20))
        self.label_85.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.label_85)

        self.label_128 = QLabel(self.page_bottom)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(16777215, 20))
        self.label_128.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.label_128)

        self.label_129 = QLabel(self.page_bottom)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMaximumSize(QSize(16777215, 20))
        self.label_129.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.label_129)

        self.label_130 = QLabel(self.page_bottom)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMaximumSize(QSize(16777215, 20))
        self.label_130.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.label_130)


        self.verticalLayout_4.addLayout(self.horizontalLayout_211)

        self.frame_102 = QFrame(self.page_bottom)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.Box)
        self.frame_102.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_201 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_201.setSpacing(0)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.blive21 = QLabel(self.frame_102)
        self.blive21.setObjectName(u"blive21")
        self.blive21.setMinimumSize(QSize(200, 125))
        self.blive21.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive21)

        self.blive22 = QLabel(self.frame_102)
        self.blive22.setObjectName(u"blive22")
        self.blive22.setMinimumSize(QSize(200, 125))
        self.blive22.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive22)

        self.blive23 = QLabel(self.frame_102)
        self.blive23.setObjectName(u"blive23")
        self.blive23.setMinimumSize(QSize(200, 125))
        self.blive23.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive23)

        self.blive24 = QLabel(self.frame_102)
        self.blive24.setObjectName(u"blive24")
        self.blive24.setMinimumSize(QSize(200, 125))
        self.blive24.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive24)


        self.verticalLayout_4.addWidget(self.frame_102)

        self.horizontalLayout_210 = QHBoxLayout()
        self.horizontalLayout_210.setSpacing(10)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(10, -1, 10, -1)
        self.label_75 = QLabel(self.page_bottom)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(16777215, 20))
        self.label_75.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_210.addWidget(self.label_75)

        self.label_76 = QLabel(self.page_bottom)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 20))
        self.label_76.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_210.addWidget(self.label_76)

        self.label_77 = QLabel(self.page_bottom)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(16777215, 20))
        self.label_77.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_210.addWidget(self.label_77)

        self.label_84 = QLabel(self.page_bottom)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMaximumSize(QSize(16777215, 20))
        self.label_84.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_84.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_210.addWidget(self.label_84)


        self.verticalLayout_4.addLayout(self.horizontalLayout_210)

        self.stackedWidget.addWidget(self.page_bottom)
        self.page_all = QWidget()
        self.page_all.setObjectName(u"page_all")
        self.verticalLayout_5 = QVBoxLayout(self.page_all)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.page_all)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 280))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.label, 0, Qt.AlignHCenter)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.frame_103 = QFrame(self.frame_3)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 1))
        self.frame_103.setMaximumSize(QSize(16777215, 250))
        self.frame_103.setFrameShape(QFrame.Box)
        self.frame_103.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.live1 = QLabel(self.frame_103)
        self.live1.setObjectName(u"live1")
        self.live1.setMinimumSize(QSize(1, 1))
        self.live1.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live1)

        self.live2 = QLabel(self.frame_103)
        self.live2.setObjectName(u"live2")
        self.live2.setMinimumSize(QSize(1, 1))
        self.live2.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live2)

        self.live3 = QLabel(self.frame_103)
        self.live3.setObjectName(u"live3")
        self.live3.setMinimumSize(QSize(1, 1))
        self.live3.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live3)

        self.live4 = QLabel(self.frame_103)
        self.live4.setObjectName(u"live4")
        self.live4.setMinimumSize(QSize(1, 1))
        self.live4.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live4)

        self.live5 = QLabel(self.frame_103)
        self.live5.setObjectName(u"live5")
        self.live5.setMinimumSize(QSize(1, 1))
        self.live5.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live5)

        self.live6 = QLabel(self.frame_103)
        self.live6.setObjectName(u"live6")
        self.live6.setMinimumSize(QSize(1, 1))
        self.live6.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live6)

        self.live7 = QLabel(self.frame_103)
        self.live7.setObjectName(u"live7")
        self.live7.setMinimumSize(QSize(1, 1))
        self.live7.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live7)

        self.live8 = QLabel(self.frame_103)
        self.live8.setObjectName(u"live8")
        self.live8.setMinimumSize(QSize(1, 1))
        self.live8.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live8)

        self.live9 = QLabel(self.frame_103)
        self.live9.setObjectName(u"live9")
        self.live9.setMinimumSize(QSize(1, 1))
        self.live9.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live9)

        self.live10 = QLabel(self.frame_103)
        self.live10.setObjectName(u"live10")
        self.live10.setMinimumSize(QSize(1, 1))
        self.live10.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live10)

        self.live11 = QLabel(self.frame_103)
        self.live11.setObjectName(u"live11")
        self.live11.setMinimumSize(QSize(1, 1))
        self.live11.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live11)

        self.live12 = QLabel(self.frame_103)
        self.live12.setObjectName(u"live12")
        self.live12.setMinimumSize(QSize(1, 1))
        self.live12.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live12)


        self.verticalLayout_8.addWidget(self.frame_103)

        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setSpacing(10)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(5, -1, 5, -1)
        self.label_59 = QLabel(self.frame_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(16777215, 20))
        self.label_59.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_59)

        self.label_60 = QLabel(self.frame_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(16777215, 20))
        self.label_60.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_60)

        self.label_62 = QLabel(self.frame_3)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 20))
        self.label_62.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_62)

        self.label_63 = QLabel(self.frame_3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 20))
        self.label_63.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_63)

        self.label_184 = QLabel(self.frame_3)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setMaximumSize(QSize(16777215, 20))
        self.label_184.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_184.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_184)

        self.label_198 = QLabel(self.frame_3)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMaximumSize(QSize(16777215, 20))
        self.label_198.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_198.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_198)

        self.label_199 = QLabel(self.frame_3)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMaximumSize(QSize(16777215, 20))
        self.label_199.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_199.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_199)

        self.label_200 = QLabel(self.frame_3)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMaximumSize(QSize(16777215, 20))
        self.label_200.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_200.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_200)

        self.label_201 = QLabel(self.frame_3)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMaximumSize(QSize(16777215, 20))
        self.label_201.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_201.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_201)

        self.label_202 = QLabel(self.frame_3)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setMaximumSize(QSize(16777215, 20))
        self.label_202.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_202.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_202)

        self.label_203 = QLabel(self.frame_3)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMaximumSize(QSize(16777215, 20))
        self.label_203.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_203.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_203)

        self.label_204 = QLabel(self.frame_3)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setMaximumSize(QSize(16777215, 20))
        self.label_204.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_204.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_208.addWidget(self.label_204)


        self.verticalLayout_8.addLayout(self.horizontalLayout_208)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame = QFrame(self.page_all)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 280))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.frame_105 = QFrame(self.frame)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 1))
        self.frame_105.setMaximumSize(QSize(16777215, 250))
        self.frame_105.setFrameShape(QFrame.Box)
        self.frame_105.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_150 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_150.setSpacing(0)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.live13 = QLabel(self.frame_105)
        self.live13.setObjectName(u"live13")
        self.live13.setMinimumSize(QSize(1, 1))
        self.live13.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live13)

        self.live14 = QLabel(self.frame_105)
        self.live14.setObjectName(u"live14")
        self.live14.setMinimumSize(QSize(1, 1))
        self.live14.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live14)

        self.live15 = QLabel(self.frame_105)
        self.live15.setObjectName(u"live15")
        self.live15.setMinimumSize(QSize(1, 1))
        self.live15.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live15)

        self.live16 = QLabel(self.frame_105)
        self.live16.setObjectName(u"live16")
        self.live16.setMinimumSize(QSize(1, 1))
        self.live16.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live16)

        self.live17 = QLabel(self.frame_105)
        self.live17.setObjectName(u"live17")
        self.live17.setMinimumSize(QSize(1, 1))
        self.live17.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live17)

        self.live18 = QLabel(self.frame_105)
        self.live18.setObjectName(u"live18")
        self.live18.setMinimumSize(QSize(1, 1))
        self.live18.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live18)

        self.live19 = QLabel(self.frame_105)
        self.live19.setObjectName(u"live19")
        self.live19.setMinimumSize(QSize(1, 1))
        self.live19.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live19)

        self.live20 = QLabel(self.frame_105)
        self.live20.setObjectName(u"live20")
        self.live20.setMinimumSize(QSize(1, 1))
        self.live20.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live20)

        self.live21 = QLabel(self.frame_105)
        self.live21.setObjectName(u"live21")
        self.live21.setMinimumSize(QSize(1, 1))
        self.live21.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live21)

        self.live22 = QLabel(self.frame_105)
        self.live22.setObjectName(u"live22")
        self.live22.setMinimumSize(QSize(1, 1))
        self.live22.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live22)

        self.live23 = QLabel(self.frame_105)
        self.live23.setObjectName(u"live23")
        self.live23.setMinimumSize(QSize(1, 1))
        self.live23.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live23)

        self.live24 = QLabel(self.frame_105)
        self.live24.setObjectName(u"live24")
        self.live24.setMinimumSize(QSize(1, 1))
        self.live24.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live24)


        self.verticalLayout_6.addWidget(self.frame_105)

        self.horizontalLayout_215 = QHBoxLayout()
        self.horizontalLayout_215.setSpacing(10)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(5, -1, 5, -1)
        self.label_205 = QLabel(self.frame)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setMaximumSize(QSize(16777215, 20))
        self.label_205.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_205.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_205)

        self.label_206 = QLabel(self.frame)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setMaximumSize(QSize(16777215, 20))
        self.label_206.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_206.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_206)

        self.label_207 = QLabel(self.frame)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setMaximumSize(QSize(16777215, 20))
        self.label_207.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_207.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_207)

        self.label_208 = QLabel(self.frame)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setMaximumSize(QSize(16777215, 20))
        self.label_208.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_208.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_208)

        self.label_209 = QLabel(self.frame)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setMaximumSize(QSize(16777215, 20))
        self.label_209.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_209.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_209)

        self.label_210 = QLabel(self.frame)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setMaximumSize(QSize(16777215, 20))
        self.label_210.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_210.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_210)

        self.label_212 = QLabel(self.frame)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setMaximumSize(QSize(16777215, 20))
        self.label_212.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_212.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_212)

        self.label_213 = QLabel(self.frame)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setMaximumSize(QSize(16777215, 20))
        self.label_213.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_213.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_213)

        self.label_214 = QLabel(self.frame)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setMaximumSize(QSize(16777215, 20))
        self.label_214.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_214.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_214)

        self.label_215 = QLabel(self.frame)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setMaximumSize(QSize(16777215, 20))
        self.label_215.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_215.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_215)

        self.label_216 = QLabel(self.frame)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setMaximumSize(QSize(16777215, 20))
        self.label_216.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_216.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_216)

        self.label_217 = QLabel(self.frame)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setMaximumSize(QSize(16777215, 20))
        self.label_217.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_217.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.label_217)


        self.verticalLayout_6.addLayout(self.horizontalLayout_215)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_all)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.live.setText("")
        self.tlive1.setText("")
        self.tlive2.setText("")
        self.tlive3.setText("")
        self.tlive4.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.tlive5.setText("")
        self.tlive6.setText("")
        self.tlive7.setText("")
        self.tlive8.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.tlive9.setText("")
        self.tlive10.setText("")
        self.tlive11.setText("")
        self.tlive12.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.blive13.setText("")
        self.blive14.setText("")
        self.blive15.setText("")
        self.blive16.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.blive17.setText("")
        self.blive18.setText("")
        self.blive19.setText("")
        self.blive20.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.blive21.setText("")
        self.blive22.setText("")
        self.blive23.setText("")
        self.blive24.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Top side", None))
        self.live1.setText("")
        self.live2.setText("")
        self.live3.setText("")
        self.live4.setText("")
        self.live5.setText("")
        self.live6.setText("")
        self.live7.setText("")
        self.live8.setText("")
        self.live9.setText("")
        self.live10.setText("")
        self.live11.setText("")
        self.live12.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bottom side", None))
        self.live13.setText("")
        self.live14.setText("")
        self.live15.setText("")
        self.live16.setText("")
        self.live17.setText("")
        self.live18.setText("")
        self.live19.setText("")
        self.live20.setText("")
        self.live21.setText("")
        self.live22.setText("")
        self.live23.setText("")
        self.live24.setText("")
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"24", None))
    # retranslateUi

