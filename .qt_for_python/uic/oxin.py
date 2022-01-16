# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oxin.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 705)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-col"
                        "or: rgb(212,212,212);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: Transparent;\n"
"	background-image: url(:/images/images/images/whiteview.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left:15px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, "
                        "147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"\n"
"	text-align: left;\n"
"	padding-left:44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title"
                        " Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(230,230,230)\n"
"}\n"
"#extraLeftBox:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(20,20,20); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extr"
                        "aContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44"
                        ", 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, "
                        "249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	padding: 1px;\n"
"	border-radius:1px;\n"
"	gridline-color: rgb(40,70,160);\n"
"	border-bottom: 1px solid rgb(180,180,180);\n"
"\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(180,180,108);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(180,180,108);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"	padding: 3px;\n"
"    background-color: rgb(30,30,30);\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"background-color: rgb(30,30,30);\n"
"color:rgb(255,255,255);\n"
"\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(70,135,230);\n"
"	color : White;\n"
"}"
                        "\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(210,210,150);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border"
                        ": 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(30,30,30);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(40,70,160);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(30,30,30);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: "
                        "left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(40,70,160);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(30,30,30);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(30,30,30);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
" "
                        "    subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
""
                        "    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
""
                        "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    backg"
                        "round-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
""
                        "}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_94 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.toggleButton = QPushButton(self.topLogo)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setGeometry(QRect(-10, 0, 60, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/t1.png);")
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Data_auquzation_btn = QPushButton(self.topMenu)
        self.Data_auquzation_btn.setObjectName(u"Data_auquzation_btn")
        sizePolicy.setHeightForWidth(self.Data_auquzation_btn.sizePolicy().hasHeightForWidth())
        self.Data_auquzation_btn.setSizePolicy(sizePolicy)
        self.Data_auquzation_btn.setMinimumSize(QSize(0, 45))
        self.Data_auquzation_btn.setFont(font)
        self.Data_auquzation_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Data_auquzation_btn.setLayoutDirection(Qt.LeftToRight)
        self.Data_auquzation_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/graber.png);")

        self.verticalLayout_8.addWidget(self.Data_auquzation_btn)

        self.label_btn = QPushButton(self.topMenu)
        self.label_btn.setObjectName(u"label_btn")
        sizePolicy.setHeightForWidth(self.label_btn.sizePolicy().hasHeightForWidth())
        self.label_btn.setSizePolicy(sizePolicy)
        self.label_btn.setMinimumSize(QSize(0, 45))
        self.label_btn.setFont(font)
        self.label_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_btn.setLayoutDirection(Qt.LeftToRight)
        self.label_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/label.png);")

        self.verticalLayout_8.addWidget(self.label_btn)

        self.tuning_btn = QPushButton(self.topMenu)
        self.tuning_btn.setObjectName(u"tuning_btn")
        sizePolicy.setHeightForWidth(self.tuning_btn.sizePolicy().hasHeightForWidth())
        self.tuning_btn.setSizePolicy(sizePolicy)
        self.tuning_btn.setMinimumSize(QSize(0, 45))
        self.tuning_btn.setFont(font)
        self.tuning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuning_btn.setLayoutDirection(Qt.LeftToRight)
        self.tuning_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/tuning.png);\n"
"")
        self.tuning_btn.setIconSize(QSize(20, 44))

        self.verticalLayout_8.addWidget(self.tuning_btn)

        self.pbt_btn = QPushButton(self.topMenu)
        self.pbt_btn.setObjectName(u"pbt_btn")
        sizePolicy.setHeightForWidth(self.pbt_btn.sizePolicy().hasHeightForWidth())
        self.pbt_btn.setSizePolicy(sizePolicy)
        self.pbt_btn.setMinimumSize(QSize(0, 45))
        self.pbt_btn.setFont(font)
        self.pbt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbt_btn.setLayoutDirection(Qt.LeftToRight)
        self.pbt_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/pbt.png)")

        self.verticalLayout_8.addWidget(self.pbt_btn)

        self.btn_about_us = QPushButton(self.topMenu)
        self.btn_about_us.setObjectName(u"btn_about_us")
        sizePolicy.setHeightForWidth(self.btn_about_us.sizePolicy().hasHeightForWidth())
        self.btn_about_us.setSizePolicy(sizePolicy)
        self.btn_about_us.setMinimumSize(QSize(0, 45))
        self.btn_about_us.setFont(font)
        self.btn_about_us.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_about_us.setLayoutDirection(Qt.LeftToRight)
        self.btn_about_us.setStyleSheet(u"background-image: url(:/icons/images/icons/Artboard1.png);\n"
"color : rgb(220,220,220);")

        self.verticalLayout_8.addWidget(self.btn_about_us)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 1, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setTextFormat(Qt.PlainText)

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Binary_btn = QPushButton(self.extraCenter)
        self.Binary_btn.setObjectName(u"Binary_btn")
        self.Binary_btn.setMinimumSize(QSize(0, 45))
        self.Binary_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Binary_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;")

        self.verticalLayout_10.addWidget(self.Binary_btn)

        self.Localization_btn = QPushButton(self.extraCenter)
        self.Localization_btn.setObjectName(u"Localization_btn")
        self.Localization_btn.setMinimumSize(QSize(0, 45))
        self.Localization_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Localization_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;")

        self.verticalLayout_10.addWidget(self.Localization_btn, 0, Qt.AlignLeft)

        self.Classification_btn = QPushButton(self.extraCenter)
        self.Classification_btn.setObjectName(u"Classification_btn")
        self.Classification_btn.setMinimumSize(QSize(0, 45))
        self.Classification_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Classification_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;")

        self.verticalLayout_10.addWidget(self.Classification_btn, 0, Qt.AlignLeft)

        self.extraBottom = QFrame(self.extraCenter)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.extraBottom)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent, 0, Qt.AlignLeft)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.leftBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.label_2.setPixmap(QPixmap(u"images/images/whitew.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(-11)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMinimumSize(QSize(200, 0))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.frame_login = QFrame(self.leftBox)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMinimumSize(QSize(0, 0))
        self.frame_login.setMaximumSize(QSize(0, 40))
        self.frame_login.setStyleSheet(u"QFrame {\n"
"background-color: rgb(50,50,70);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"	border-radius:6px;\n"
"	text-align:center;\n"
"}")
        self.frame_login.setFrameShape(QFrame.Box)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_login)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_43 = QLabel(self.frame_login)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(100, 0))
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setStyleSheet(u"color : rgb(255,255,255);")
        self.label_43.setIndent(6)

        self.horizontalLayout_34.addWidget(self.label_43)

        self.lineEdit_6 = QLineEdit(self.frame_login)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(150, 25))
        self.lineEdit_6.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_34.addWidget(self.lineEdit_6)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_44 = QLabel(self.frame_login)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(100, 16777215))
        self.label_44.setStyleSheet(u"color : rgb(255,255,255);")
        self.label_44.setMargin(0)
        self.label_44.setIndent(17)

        self.horizontalLayout_35.addWidget(self.label_44)

        self.lineEdit_7 = QLineEdit(self.frame_login)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(100, 25))
        self.lineEdit_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_35.addWidget(self.lineEdit_7)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_35)

        self.pushButton_7 = QPushButton(self.frame_login)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(23, 22))
        self.pushButton_7.setMaximumSize(QSize(21, 21))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setToolTipDuration(-1)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"background-color: Transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_36.addWidget(self.pushButton_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_51 = QLabel(self.frame_login)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color : rgb(255,255,255);")

        self.horizontalLayout_36.addWidget(self.label_51)


        self.horizontalLayout_3.addWidget(self.frame_login)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(15, 18, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.login_btn = QPushButton(self.rightButtons)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(32, 28))
        self.login_btn.setMaximumSize(QSize(28, 28))
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/icons/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.login_btn)

        self.setting_btn = QPushButton(self.rightButtons)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setMinimumSize(QSize(28, 28))
        self.setting_btn.setMaximumSize(QSize(28, 28))
        self.setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon2)
        self.setting_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.setting_btn)

        self.miniButton = QPushButton(self.rightButtons)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon3)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.rightButtons)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font3)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon4)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.rightButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon5)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_settin2 = QFrame(self.contentBottom)
        self.frame_settin2.setObjectName(u"frame_settin2")
        self.frame_settin2.setMinimumSize(QSize(0, 0))
        self.frame_settin2.setMaximumSize(QSize(16777215, 0))
        self.frame_settin2.setStyleSheet(u"background-color: rgb(33, 37, 50);")
        self.frame_settin2.setFrameShape(QFrame.StyledPanel)
        self.frame_settin2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_settin2)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_8)

        self.btn_software_setting = QPushButton(self.frame_settin2)
        self.btn_software_setting.setObjectName(u"btn_software_setting")
        self.btn_software_setting.setMinimumSize(QSize(150, 0))
        self.btn_software_setting.setMaximumSize(QSize(150, 16777215))
        self.btn_software_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_software_setting.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.btn_software_setting)

        self.pushButton_9 = QPushButton(self.frame_settin2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(150, 0))
        self.pushButton_9.setMaximumSize(QSize(150, 16777215))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_9)

        self.pushButton_15 = QPushButton(self.frame_settin2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(150, 0))
        self.pushButton_15.setMaximumSize(QSize(150, 16777215))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_settin2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(150, 0))
        self.pushButton_16.setMaximumSize(QSize(150, 16777215))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_settin2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(150, 0))
        self.pushButton_17.setMaximumSize(QSize(150, 16777215))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_17)


        self.verticalLayout_6.addWidget(self.frame_settin2)

        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setToolTipDuration(-1)
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.pagesContainer.setLineWidth(1)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"color : rgb(20,20,20);")
        self.page_data_auquzation = QWidget()
        self.page_data_auquzation.setObjectName(u"page_data_auquzation")
        self.page_data_auquzation.setStyleSheet(u"color : rgb(20,20,20);")
        self.horizontalLayout_7 = QHBoxLayout(self.page_data_auquzation)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.main = QFrame(self.page_data_auquzation)
        self.main.setObjectName(u"main")
        palette = QPalette()
        brush = QBrush(QColor(20, 20, 20, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(20, 20, 20, 128))
        brush1.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(20, 20, 20, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(20, 20, 20, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.main.setPalette(palette)
        self.main.setToolTipDuration(-1)
        self.main.setFrameShape(QFrame.Panel)
        self.main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.main)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(2, 5, 2, 2)
        self.tabWidget_2 = QTabWidget(self.main)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: Transparent;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    bord"
                        "er-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_84 = QVBoxLayout(self.tab_6)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(1, 1, 1, 1)
        self.frame_44 = QFrame(self.tab_6)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_44)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(7, 8, 7, 1)
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_133 = QLabel(self.frame_44)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_91.addWidget(self.label_133)

        self.label_3 = QLabel(self.frame_44)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_91.addWidget(self.label_3)


        self.verticalLayout_85.addLayout(self.horizontalLayout_91)

        self.crop_image_up = QLabel(self.frame_44)
        self.crop_image_up.setObjectName(u"crop_image_up")
        self.crop_image_up.setMinimumSize(QSize(125, 100))
        self.crop_image_up.setMaximumSize(QSize(1920, 463))
        self.crop_image_up.setBaseSize(QSize(240, 130))
        self.crop_image_up.setFrameShape(QFrame.Box)
        self.crop_image_up.setFrameShadow(QFrame.Plain)
        self.crop_image_up.setPixmap(QPixmap(u"2.jpg"))
        self.crop_image_up.setScaledContents(True)
        self.crop_image_up.setWordWrap(False)
        self.crop_image_up.setMargin(2)

        self.verticalLayout_85.addWidget(self.crop_image_up)

        self.line_30 = QFrame(self.frame_44)
        self.line_30.setObjectName(u"line_30")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(57)
        sizePolicy3.setVerticalStretch(25)
        sizePolicy3.setHeightForWidth(self.line_30.sizePolicy().hasHeightForWidth())
        self.line_30.setSizePolicy(sizePolicy3)
        self.line_30.setMinimumSize(QSize(600, 0))
        self.line_30.setFrameShadow(QFrame.Raised)
        self.line_30.setFrameShape(QFrame.HLine)

        self.verticalLayout_85.addWidget(self.line_30, 0, Qt.AlignHCenter)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(3)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_8 = QSpacerItem(5, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_8)

        self.pushButton_26 = QPushButton(self.frame_44)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(100, 25))
        self.pushButton_26.setMaximumSize(QSize(130, 30))
        self.pushButton_26.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.verticalLayout_21.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame_44)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(100, 25))
        self.pushButton_27.setMaximumSize(QSize(130, 30))
        self.pushButton_27.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.verticalLayout_21.addWidget(self.pushButton_27)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)

        self.pushButton_22 = QPushButton(self.frame_44)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(100, 25))
        self.pushButton_22.setMaximumSize(QSize(120, 30))
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.verticalLayout_21.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.frame_44)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(100, 25))
        self.pushButton_23.setMaximumSize(QSize(130, 30))
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.verticalLayout_21.addWidget(self.pushButton_23)

        self.verticalSpacer_9 = QSpacerItem(5, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_9)


        self.horizontalLayout_93.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_10)

        self.listWidget = QListWidget(self.frame_44)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_93.addWidget(self.listWidget)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_9)


        self.verticalLayout_85.addLayout(self.horizontalLayout_93)


        self.verticalLayout_84.addWidget(self.frame_44)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.horizontalLayout_86.addWidget(self.tabWidget_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(212, 0))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_76 = QVBoxLayout(self.frame_3)
        self.verticalLayout_76.setSpacing(4)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(1, 0, 1, 0)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_76.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.scrollArea_4 = QScrollArea(self.frame_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 204, 17))
        self.verticalLayout_77 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_77.setSpacing(5)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 1, 0)
        self.down_side_technical = QLabel(self.scrollAreaWidgetContents_4)
        self.down_side_technical.setObjectName(u"down_side_technical")
        self.down_side_technical.setCursor(QCursor(Qt.ArrowCursor))
        self.down_side_technical.setPixmap(QPixmap(u"../train/oxin/09-10-2021 16-47-14-412661__0.jpg"))
        self.down_side_technical.setScaledContents(True)
        self.down_side_technical.setWordWrap(False)

        self.verticalLayout_77.addWidget(self.down_side_technical)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_76.addWidget(self.scrollArea_4)


        self.horizontalLayout_86.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(212, 0))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 0, 1, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.scrollArea_up_side = QScrollArea(self.frame_2)
        self.scrollArea_up_side.setObjectName(u"scrollArea_up_side")
        self.scrollArea_up_side.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_up_side.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 204, 17))
        self.horizontalLayout_90 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.up_side_technical = QLabel(self.scrollAreaWidgetContents_2)
        self.up_side_technical.setObjectName(u"up_side_technical")
        self.up_side_technical.setPixmap(QPixmap(u"../train/oxin/03-11-2021 09-43-52-296900__0.jpg"))
        self.up_side_technical.setScaledContents(True)

        self.horizontalLayout_90.addWidget(self.up_side_technical)

        self.scrollArea_up_side.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_up_side)


        self.horizontalLayout_86.addWidget(self.frame_2)

        self.frame_41 = QFrame(self.main)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(1920, 1200))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_86.addWidget(self.frame_41)


        self.horizontalLayout_7.addWidget(self.main)

        self.stackedWidget.addWidget(self.page_data_auquzation)
        self.page_label = QWidget()
        self.page_label.setObjectName(u"page_label")
        self.horizontalLayout_6 = QHBoxLayout(self.page_label)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.page_label)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_38 = QVBoxLayout(self.frame)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_28 = QPushButton(self.frame_7)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(37, 0))
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_28.setToolTip(u"Open image")
#endif // QT_CONFIG(tooltip)
        self.pushButton_28.setToolTipDuration(-1)
        self.pushButton_28.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon6)
        self.pushButton_28.setIconSize(QSize(20, 28))

        self.verticalLayout_28.addWidget(self.pushButton_28)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(37, 0))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(u"Open Folder")
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setToolTipDuration(-1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"images/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(24, 31))

        self.verticalLayout_28.addWidget(self.pushButton_2)

        self.line_34 = QFrame(self.frame_7)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_34)

        self.pushButton_10 = QPushButton(self.frame_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(37, 0))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(u"Next")
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"images/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon8)
        self.pushButton_10.setIconSize(QSize(24, 31))

        self.verticalLayout_28.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(37, 0))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(u"Previous")
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"images/arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QSize(24, 31))

        self.verticalLayout_28.addWidget(self.pushButton_11)

        self.line_35 = QFrame(self.frame_7)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_35)

        self.pushButton_12 = QPushButton(self.frame_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setMinimumSize(QSize(37, 0))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(u"Zoom in")
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"images/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon10)
        self.pushButton_12.setIconSize(QSize(24, 31))

        self.verticalLayout_28.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setMinimumSize(QSize(37, 0))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_13.setToolTip(u"Zoom back")
#endif // QT_CONFIG(tooltip)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"images/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon11)
        self.pushButton_13.setIconSize(QSize(36, 31))

        self.verticalLayout_28.addWidget(self.pushButton_13)

        self.line_36 = QFrame(self.frame_7)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_36)

        self.polygon_btn = QPushButton(self.frame_7)
        self.polygon_btn.setObjectName(u"polygon_btn")
        self.polygon_btn.setMinimumSize(QSize(37, 0))
        self.polygon_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.polygon_btn.setToolTip(u"Polygon")
#endif // QT_CONFIG(tooltip)
        self.polygon_btn.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"images/clipart1919813.png", QSize(), QIcon.Normal, QIcon.Off)
        self.polygon_btn.setIcon(icon12)
        self.polygon_btn.setIconSize(QSize(28, 27))

        self.verticalLayout_28.addWidget(self.polygon_btn)

        self.bounding_btn = QPushButton(self.frame_7)
        self.bounding_btn.setObjectName(u"bounding_btn")
        self.bounding_btn.setMinimumSize(QSize(37, 0))
        self.bounding_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.bounding_btn.setToolTip(u"Bounding Box")
#endif // QT_CONFIG(tooltip)
        self.bounding_btn.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"images/noun-rectangle-667504.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bounding_btn.setIcon(icon13)
        self.bounding_btn.setIconSize(QSize(31, 29))

        self.verticalLayout_28.addWidget(self.bounding_btn)

        self.line_37 = QFrame(self.frame_7)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_37)

        self.pushButton_14 = QPushButton(self.frame_7)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(37, 0))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_14.setToolTip(u"Delete Rec")
#endif // QT_CONFIG(tooltip)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border:0px\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(180,180,180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"images/x-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon14)
        self.pushButton_14.setIconSize(QSize(22, 27))

        self.verticalLayout_28.addWidget(self.pushButton_14)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addWidget(self.frame_7)

        self.line_5 = QFrame(self.frame_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_5)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.n_image = QLabel(self.frame_8)
        self.n_image.setObjectName(u"n_image")
        self.n_image.setMaximumSize(QSize(200, 200))
        self.n_image.setFrameShape(QFrame.Box)
        self.n_image.setScaledContents(True)
        self.n_image.setMargin(2)

        self.horizontalLayout_15.addWidget(self.n_image, 0, Qt.AlignVCenter)

        self.frame_58 = QFrame(self.frame_8)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.Box)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.frame_58.setLineWidth(2)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_87.setSpacing(2)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(2, 2, 2, 2)
        self.image = QLabel(self.frame_58)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(16777215, 16777215))
        self.image.setFrameShape(QFrame.NoFrame)
        self.image.setFrameShadow(QFrame.Plain)
        self.image.setLineWidth(2)
        self.image.setScaledContents(True)
        self.image.setMargin(0)
        self.image.setIndent(0)

        self.horizontalLayout_87.addWidget(self.image)


        self.horizontalLayout_15.addWidget(self.frame_58)

        self.p_image = QLabel(self.frame_8)
        self.p_image.setObjectName(u"p_image")
        self.p_image.setMaximumSize(QSize(200, 200))
        self.p_image.setFrameShape(QFrame.Box)
        self.p_image.setScaledContents(True)
        self.p_image.setMargin(2)

        self.horizontalLayout_15.addWidget(self.p_image, 0, Qt.AlignVCenter)


        self.horizontalLayout_14.addWidget(self.frame_8)


        self.verticalLayout_38.addWidget(self.frame_6)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_38.addWidget(self.line_2)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 80))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 80))
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 13)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_24.addWidget(self.label_4)

        self.label_10 = QLabel(self.frame_19)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_24.addWidget(self.label_10)

        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_24.addWidget(self.label_5)


        self.horizontalLayout_10.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_25.addWidget(self.label_13)

        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_25.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_19)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_25.addWidget(self.label_12)


        self.horizontalLayout_10.addLayout(self.verticalLayout_25)


        self.horizontalLayout_24.addWidget(self.frame_19)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_6)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 80))
        self.frame_20.setFrameShape(QFrame.Box)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 13)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_26.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_26.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_26.addWidget(self.label_16)


        self.horizontalLayout_13.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_27.addWidget(self.label_17)

        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_27.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_27.addWidget(self.label_25)


        self.horizontalLayout_13.addLayout(self.verticalLayout_27)


        self.horizontalLayout_24.addWidget(self.frame_20)


        self.verticalLayout_38.addWidget(self.frame_18)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_11 = QFrame(self.page_label)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(115, 0))
        self.frame_11.setMaximumSize(QSize(350, 16777215))
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.frame_11.setLineWidth(1)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 60))
        self.frame_12.setFrameShape(QFrame.Panel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(2)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_27 = QLabel(self.frame_12)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_20.addWidget(self.label_27)

        self.yes_defect = QRadioButton(self.frame_12)
        self.yes_defect.setObjectName(u"yes_defect")
        self.yes_defect.setMaximumSize(QSize(70, 16777215))
        self.yes_defect.setCursor(QCursor(Qt.PointingHandCursor))
        self.yes_defect.setStyleSheet(u"QRadioButton {\n"
"    background-color:       Transparent;\n"
"    color:                  Black;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 2px solid green;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")

        self.horizontalLayout_20.addWidget(self.yes_defect, 0, Qt.AlignVCenter)

        self.no_defect = QRadioButton(self.frame_12)
        self.no_defect.setObjectName(u"no_defect")
        self.no_defect.setMaximumSize(QSize(70, 16777215))
        self.no_defect.setCursor(QCursor(Qt.PointingHandCursor))
        self.no_defect.setStyleSheet(u"QRadioButton {\n"
"    background-color:       Transparent;\n"
"    color:                  Black;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid red;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")

        self.horizontalLayout_20.addWidget(self.no_defect)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)


        self.verticalLayout_34.addWidget(self.frame_12)

        self.stackedWidget_defect = QStackedWidget(self.frame_11)
        self.stackedWidget_defect.setObjectName(u"stackedWidget_defect")
        self.stackedWidget_defect.setFrameShape(QFrame.Box)
        self.page_yes = QWidget()
        self.page_yes.setObjectName(u"page_yes")
        self.verticalLayout_35 = QVBoxLayout(self.page_yes)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_13 = QFrame(self.page_yes)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.tabWidget_defect = QTabWidget(self.frame_13)
        self.tabWidget_defect.setObjectName(u"tabWidget_defect")
        self.tabWidget_defect.setMinimumSize(QSize(0, 185))
        self.tabWidget_defect.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top"
                        "-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_defect.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_defect.addTab(self.tab_2, "")

        self.verticalLayout_36.addWidget(self.tabWidget_defect)


        self.verticalLayout_35.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.page_yes)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 54))
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_22.addWidget(self.label_21)

        self.comboBox_3 = QComboBox(self.frame_15)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_22.addWidget(self.comboBox_3)


        self.verticalLayout_35.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_yes)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.frame_16)

        self.stackedWidget_defect.addWidget(self.page_yes)
        self.page_no = QWidget()
        self.page_no.setObjectName(u"page_no")
        self.page_no.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_37 = QVBoxLayout(self.page_no)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_22 = QLabel(self.page_no)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_37.addWidget(self.label_22)

        self.stackedWidget_defect.addWidget(self.page_no)

        self.verticalLayout_34.addWidget(self.stackedWidget_defect)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_17)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.pushButton_3 = QPushButton(self.frame_17)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(200, 59))
        self.pushButton_3.setMaximumSize(QSize(150, 16777215))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_39.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.tableWidget_3 = QTableWidget(self.frame_17)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(3, 3))

        self.verticalLayout_39.addWidget(self.tableWidget_3)


        self.verticalLayout_34.addWidget(self.frame_17)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_label)
        self.page_tuning = QWidget()
        self.page_tuning.setObjectName(u"page_tuning")
        self.stackedWidget.addWidget(self.page_tuning)
        self.page_pbt = QWidget()
        self.page_pbt.setObjectName(u"page_pbt")
        self.verticalLayout_78 = QVBoxLayout(self.page_pbt)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.frame_51 = QFrame(self.page_pbt)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(200, 50))
        self.frame_51.setMaximumSize(QSize(16777215, 50))
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.load_dataset_pbt = QPushButton(self.frame_51)
        self.load_dataset_pbt.setObjectName(u"load_dataset_pbt")
        self.load_dataset_pbt.setMinimumSize(QSize(150, 40))
        self.load_dataset_pbt.setMaximumSize(QSize(150, 16777215))
        self.load_dataset_pbt.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_dataset_pbt.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_95.addWidget(self.load_dataset_pbt)

        self.pipeline_pbt = QPushButton(self.frame_51)
        self.pipeline_pbt.setObjectName(u"pipeline_pbt")
        self.pipeline_pbt.setMinimumSize(QSize(150, 40))
        self.pipeline_pbt.setMaximumSize(QSize(150, 16777215))
        self.pipeline_pbt.setCursor(QCursor(Qt.PointingHandCursor))
        self.pipeline_pbt.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_95.addWidget(self.pipeline_pbt)

        self.history_pbt = QPushButton(self.frame_51)
        self.history_pbt.setObjectName(u"history_pbt")
        self.history_pbt.setMinimumSize(QSize(150, 40))
        self.history_pbt.setMaximumSize(QSize(150, 16777215))
        self.history_pbt.setCursor(QCursor(Qt.PointingHandCursor))
        self.history_pbt.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_95.addWidget(self.history_pbt)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_13)


        self.verticalLayout_78.addWidget(self.frame_51)

        self.line_38 = QFrame(self.page_pbt)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_78.addWidget(self.line_38)

        self.stackedWidget_pbt = QStackedWidget(self.page_pbt)
        self.stackedWidget_pbt.setObjectName(u"stackedWidget_pbt")
        self.stackedWidget_pbt.setMinimumSize(QSize(0, 84))
        self.page_pipeline = QWidget()
        self.page_pipeline.setObjectName(u"page_pipeline")
        self.verticalLayout_80 = QVBoxLayout(self.page_pipeline)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.label_120 = QLabel(self.page_pipeline)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 30))
        self.label_120.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_80.addWidget(self.label_120)

        self.frame_52 = QFrame(self.page_pipeline)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(16777215, 80))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_121 = QLabel(self.frame_52)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(80, 25))
        self.label_121.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_96.addWidget(self.label_121)

        self.comboBox_4 = QComboBox(self.frame_52)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(200, 25))
        self.comboBox_4.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_96.addWidget(self.comboBox_4)

        self.toolButton = QToolButton(self.frame_52)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_96.addWidget(self.toolButton)


        self.horizontalLayout_112.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_122 = QLabel(self.frame_52)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(110, 25))
        self.label_122.setMaximumSize(QSize(110, 25))

        self.horizontalLayout_97.addWidget(self.label_122)

        self.comboBox_5 = QComboBox(self.frame_52)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(200, 25))
        self.comboBox_5.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_97.addWidget(self.comboBox_5)

        self.toolButton_2 = QToolButton(self.frame_52)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_97.addWidget(self.toolButton_2)


        self.horizontalLayout_112.addLayout(self.horizontalLayout_97)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_123 = QLabel(self.frame_52)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(120, 25))
        self.label_123.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_98.addWidget(self.label_123)

        self.comboBox_8 = QComboBox(self.frame_52)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(200, 25))
        self.comboBox_8.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_98.addWidget(self.comboBox_8)

        self.toolButton_3 = QToolButton(self.frame_52)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_98.addWidget(self.toolButton_3)


        self.horizontalLayout_112.addLayout(self.horizontalLayout_98)


        self.verticalLayout_80.addWidget(self.frame_52)

        self.line_39 = QFrame(self.page_pipeline)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setMinimumSize(QSize(510, 0))
        self.line_39.setMaximumSize(QSize(510, 16777215))
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_80.addWidget(self.line_39, 0, Qt.AlignHCenter)

        self.frame_53 = QFrame(self.page_pipeline)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setGeometry(QRect(180, 50, 120, 80))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setGeometry(QRect(450, 50, 120, 80))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)

        self.verticalLayout_80.addWidget(self.frame_53)

        self.frame_46 = QFrame(self.page_pipeline)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.verticalLayout_80.addWidget(self.frame_46)

        self.stackedWidget_pbt.addWidget(self.page_pipeline)
        self.page_load_dataset = QWidget()
        self.page_load_dataset.setObjectName(u"page_load_dataset")
        self.stackedWidget_pbt.addWidget(self.page_load_dataset)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.stackedWidget_pbt.addWidget(self.page_history)

        self.verticalLayout_78.addWidget(self.stackedWidget_pbt)

        self.frame_50 = QFrame(self.page_pbt)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 130))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_50)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(2, 0, 0, 0)

        self.verticalLayout_78.addWidget(self.frame_50)

        self.stackedWidget.addWidget(self.page_pbt)
        self.page_Binary = QWidget()
        self.page_Binary.setObjectName(u"page_Binary")
        self.verticalLayout_22 = QVBoxLayout(self.page_Binary)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_4 = QFrame(self.page_Binary)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.binary_list = QPushButton(self.frame_4)
        self.binary_list.setObjectName(u"binary_list")
        self.binary_list.setMinimumSize(QSize(150, 40))
        self.binary_list.setMaximumSize(QSize(150, 16777215))
        self.binary_list.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_8.addWidget(self.binary_list)

        self.binary_training = QPushButton(self.frame_4)
        self.binary_training.setObjectName(u"binary_training")
        self.binary_training.setMinimumSize(QSize(150, 40))
        self.binary_training.setMaximumSize(QSize(150, 16777215))
        self.binary_training.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_8.addWidget(self.binary_training)

        self.binary_history = QPushButton(self.frame_4)
        self.binary_history.setObjectName(u"binary_history")
        self.binary_history.setMinimumSize(QSize(150, 40))
        self.binary_history.setMaximumSize(QSize(150, 16777215))
        self.binary_history.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_8.addWidget(self.binary_history)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_22.addWidget(self.frame_4)

        self.line = QFrame(self.page_Binary)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line)

        self.stackedWidget_binary = QStackedWidget(self.page_Binary)
        self.stackedWidget_binary.setObjectName(u"stackedWidget_binary")
        self.page_binary_list = QWidget()
        self.page_binary_list.setObjectName(u"page_binary_list")
        self.label_20 = QLabel(self.page_binary_list)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(150, 150, 55, 16))
        self.stackedWidget_binary.addWidget(self.page_binary_list)
        self.page_binary_training = QWidget()
        self.page_binary_training.setObjectName(u"page_binary_training")
        self.horizontalLayout_85 = QHBoxLayout(self.page_binary_training)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_47 = QFrame(self.page_binary_training)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(250, 16777215))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_47)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 50))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_48)
        self.verticalLayout_82.setSpacing(4)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_137 = QLabel(self.frame_48)
        self.label_137.setObjectName(u"label_137")

        self.horizontalLayout_99.addWidget(self.label_137, 0, Qt.AlignLeft)

        self.comboBox_9 = QComboBox(self.frame_48)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_99.addWidget(self.comboBox_9)


        self.verticalLayout_82.addLayout(self.horizontalLayout_99)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_138 = QLabel(self.frame_48)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_100.addWidget(self.label_138, 0, Qt.AlignLeft)

        self.lineEdit_52 = QLineEdit(self.frame_48)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_100.addWidget(self.lineEdit_52)


        self.verticalLayout_82.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.label_139 = QLabel(self.frame_48)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_101.addWidget(self.label_139, 0, Qt.AlignLeft)

        self.lineEdit_53 = QLineEdit(self.frame_48)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_101.addWidget(self.lineEdit_53)


        self.verticalLayout_82.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_140 = QLabel(self.frame_48)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_102.addWidget(self.label_140)

        self.lineEdit_54 = QLineEdit(self.frame_48)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_102.addWidget(self.lineEdit_54)


        self.verticalLayout_82.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_141 = QLabel(self.frame_48)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_103.addWidget(self.label_141)

        self.lineEdit_55 = QLineEdit(self.frame_48)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_103.addWidget(self.lineEdit_55)


        self.verticalLayout_82.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_142 = QLabel(self.frame_48)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_104.addWidget(self.label_142)

        self.lineEdit_56 = QLineEdit(self.frame_48)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_104.addWidget(self.lineEdit_56)


        self.verticalLayout_82.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.label_143 = QLabel(self.frame_48)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_105.addWidget(self.label_143)

        self.lineEdit_57 = QLineEdit(self.frame_48)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_105.addWidget(self.lineEdit_57)


        self.verticalLayout_82.addLayout(self.horizontalLayout_105)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.label_144 = QLabel(self.frame_48)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_106.addWidget(self.label_144)

        self.lineEdit_58 = QLineEdit(self.frame_48)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_106.addWidget(self.lineEdit_58)


        self.verticalLayout_82.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.label_145 = QLabel(self.frame_48)
        self.label_145.setObjectName(u"label_145")

        self.horizontalLayout_107.addWidget(self.label_145)

        self.lineEdit_59 = QLineEdit(self.frame_48)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_107.addWidget(self.lineEdit_59)


        self.verticalLayout_82.addLayout(self.horizontalLayout_107)


        self.verticalLayout_81.addWidget(self.frame_48, 0, Qt.AlignLeft)

        self.frame_49 = QFrame(self.frame_47)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_49.setFrameShape(QFrame.Box)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_49)
        self.verticalLayout_83.setSpacing(3)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_146 = QLabel(self.frame_49)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(100, 0))
        self.label_146.setStyleSheet(u"text-align: center;")
        self.label_146.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.label_146)

        self.table_classification_select_class_4 = QTableWidget(self.frame_49)
        if (self.table_classification_select_class_4.columnCount() < 3):
            self.table_classification_select_class_4.setColumnCount(3)
        if (self.table_classification_select_class_4.rowCount() < 20):
            self.table_classification_select_class_4.setRowCount(20)
        self.table_classification_select_class_4.setObjectName(u"table_classification_select_class_4")
        self.table_classification_select_class_4.setRowCount(20)
        self.table_classification_select_class_4.setColumnCount(3)

        self.verticalLayout_83.addWidget(self.table_classification_select_class_4)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.label_147 = QLabel(self.frame_49)
        self.label_147.setObjectName(u"label_147")

        self.horizontalLayout_108.addWidget(self.label_147)

        self.label_148 = QLabel(self.frame_49)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_108.addWidget(self.label_148)


        self.verticalLayout_83.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_149 = QLabel(self.frame_49)
        self.label_149.setObjectName(u"label_149")

        self.horizontalLayout_109.addWidget(self.label_149)

        self.label_150 = QLabel(self.frame_49)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_109.addWidget(self.label_150)


        self.verticalLayout_83.addLayout(self.horizontalLayout_109)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.label_151 = QLabel(self.frame_49)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_110.addWidget(self.label_151)

        self.label_152 = QLabel(self.frame_49)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_110.addWidget(self.label_152)


        self.verticalLayout_83.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.label_153 = QLabel(self.frame_49)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_111.addWidget(self.label_153)

        self.label_154 = QLabel(self.frame_49)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_111.addWidget(self.label_154)


        self.verticalLayout_83.addLayout(self.horizontalLayout_111)

        self.pushButton_24 = QPushButton(self.frame_49)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(110, 25))
        self.pushButton_24.setMaximumSize(QSize(110, 30))
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_83.addWidget(self.pushButton_24, 0, Qt.AlignHCenter)


        self.verticalLayout_81.addWidget(self.frame_49)

        self.pushButton_25 = QPushButton(self.frame_47)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(180, 30))
        self.pushButton_25.setMaximumSize(QSize(180, 16777215))
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_81.addWidget(self.pushButton_25, 0, Qt.AlignHCenter)


        self.horizontalLayout_85.addWidget(self.frame_47)

        self.line_29 = QFrame(self.page_binary_training)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.VLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_85.addWidget(self.line_29)

        self.frame_42 = QFrame(self.page_binary_training)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_85.addWidget(self.frame_42)

        self.stackedWidget_binary.addWidget(self.page_binary_training)
        self.page_binary_history = QWidget()
        self.page_binary_history.setObjectName(u"page_binary_history")
        self.horizontalLayout_44 = QHBoxLayout(self.page_binary_history)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_33 = QFrame(self.page_binary_history)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(400, 0))
        self.frame_33.setMaximumSize(QSize(300, 16777215))
        self.frame_33.setFrameShape(QFrame.Panel)
        self.frame_33.setFrameShadow(QFrame.Plain)
        self.frame_33.setLineWidth(1)
        self.verticalLayout_52 = QVBoxLayout(self.frame_33)
        self.verticalLayout_52.setSpacing(7)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(5, 5, 5, 5)
        self.label_78 = QLabel(self.frame_33)
        self.label_78.setObjectName(u"label_78")

        self.verticalLayout_52.addWidget(self.label_78)

        self.line_25 = QFrame(self.frame_33)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_25)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.spinBox_tedad_2 = QSpinBox(self.frame_33)
        self.spinBox_tedad_2.setObjectName(u"spinBox_tedad_2")
        self.spinBox_tedad_2.setMaximumSize(QSize(50, 16777212))
        self.spinBox_tedad_2.setFont(font)
        self.spinBox_tedad_2.setMaximum(999)
        self.spinBox_tedad_2.setValue(10)

        self.horizontalLayout_45.addWidget(self.spinBox_tedad_2)

        self.label_79 = QLabel(self.frame_33)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_79)

        self.request_btn_2 = QPushButton(self.frame_33)
        self.request_btn_2.setObjectName(u"request_btn_2")
        self.request_btn_2.setFont(font)
        self.request_btn_2.setStyleSheet(u"	color:rgb(255,255,255);")

        self.horizontalLayout_45.addWidget(self.request_btn_2)


        self.verticalLayout_52.addLayout(self.horizontalLayout_45)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.line_15 = QFrame(self.frame_33)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_15)

        self.label_80 = QLabel(self.frame_33)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(16777215, 20))
        self.label_80.setFont(font)

        self.verticalLayout_53.addWidget(self.label_80)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.lineEdit_id_8 = QLineEdit(self.frame_33)
        self.lineEdit_id_8.setObjectName(u"lineEdit_id_8")
        self.lineEdit_id_8.setFont(font)

        self.horizontalLayout_46.addWidget(self.lineEdit_id_8)

        self.search_id_btn_3 = QPushButton(self.frame_33)
        self.search_id_btn_3.setObjectName(u"search_id_btn_3")
        self.search_id_btn_3.setFont(font)

        self.horizontalLayout_46.addWidget(self.search_id_btn_3)


        self.verticalLayout_53.addLayout(self.horizontalLayout_46)


        self.verticalLayout_52.addLayout(self.verticalLayout_53)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.line_16 = QFrame(self.frame_33)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_54.addWidget(self.line_16)

        self.label_81 = QLabel(self.frame_33)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font)

        self.verticalLayout_54.addWidget(self.label_81)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_82 = QLabel(self.frame_33)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(16777215, 20))
        self.label_82.setFont(font)

        self.verticalLayout_55.addWidget(self.label_82)

        self.lineEdit_id_9 = QLineEdit(self.frame_33)
        self.lineEdit_id_9.setObjectName(u"lineEdit_id_9")
        self.lineEdit_id_9.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_9.setFont(font)

        self.verticalLayout_55.addWidget(self.lineEdit_id_9)


        self.horizontalLayout_47.addLayout(self.verticalLayout_55)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_83 = QLabel(self.frame_33)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMaximumSize(QSize(16777215, 20))
        self.label_83.setFont(font)

        self.verticalLayout_56.addWidget(self.label_83)

        self.lineEdit_id_10 = QLineEdit(self.frame_33)
        self.lineEdit_id_10.setObjectName(u"lineEdit_id_10")
        self.lineEdit_id_10.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_10.setFont(font)

        self.verticalLayout_56.addWidget(self.lineEdit_id_10)


        self.horizontalLayout_47.addLayout(self.verticalLayout_56)


        self.verticalLayout_54.addLayout(self.horizontalLayout_47)

        self.search_id_btn_5 = QPushButton(self.frame_33)
        self.search_id_btn_5.setObjectName(u"search_id_btn_5")
        self.search_id_btn_5.setMaximumSize(QSize(16777215, 30))
        self.search_id_btn_5.setFont(font)

        self.verticalLayout_54.addWidget(self.search_id_btn_5)


        self.verticalLayout_52.addLayout(self.verticalLayout_54)

        self.line_17 = QFrame(self.frame_33)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_17)

        self.label_84 = QLabel(self.frame_33)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMaximumSize(QSize(16777215, 20))
        self.label_84.setFont(font)

        self.verticalLayout_52.addWidget(self.label_84)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_85 = QLabel(self.frame_33)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(16777215, 20))
        self.label_85.setFont(font)

        self.verticalLayout_57.addWidget(self.label_85)

        self.lineEdit_id_11 = QLineEdit(self.frame_33)
        self.lineEdit_id_11.setObjectName(u"lineEdit_id_11")
        self.lineEdit_id_11.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_11.setFont(font)

        self.verticalLayout_57.addWidget(self.lineEdit_id_11)


        self.horizontalLayout_48.addLayout(self.verticalLayout_57)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_86 = QLabel(self.frame_33)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMaximumSize(QSize(16777215, 20))
        self.label_86.setFont(font)

        self.verticalLayout_58.addWidget(self.label_86)

        self.lineEdit_id_12 = QLineEdit(self.frame_33)
        self.lineEdit_id_12.setObjectName(u"lineEdit_id_12")
        self.lineEdit_id_12.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_12.setFont(font)

        self.verticalLayout_58.addWidget(self.lineEdit_id_12)


        self.horizontalLayout_48.addLayout(self.verticalLayout_58)


        self.verticalLayout_52.addLayout(self.horizontalLayout_48)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.line_18 = QFrame(self.frame_33)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_59.addWidget(self.line_18)

        self.label_87 = QLabel(self.frame_33)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMaximumSize(QSize(16777215, 20))
        self.label_87.setFont(font)

        self.verticalLayout_59.addWidget(self.label_87)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_88 = QLabel(self.frame_33)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(16777215, 20))
        self.label_88.setFont(font)

        self.verticalLayout_60.addWidget(self.label_88)

        self.lineEdit_id_13 = QLineEdit(self.frame_33)
        self.lineEdit_id_13.setObjectName(u"lineEdit_id_13")
        self.lineEdit_id_13.setMinimumSize(QSize(0, 15))
        self.lineEdit_id_13.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_13.setFont(font)

        self.verticalLayout_60.addWidget(self.lineEdit_id_13)


        self.horizontalLayout_49.addLayout(self.verticalLayout_60)

        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_89 = QLabel(self.frame_33)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(16777215, 20))
        self.label_89.setFont(font)

        self.verticalLayout_61.addWidget(self.label_89)

        self.lineEdit_id_14 = QLineEdit(self.frame_33)
        self.lineEdit_id_14.setObjectName(u"lineEdit_id_14")
        self.lineEdit_id_14.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_14.setFont(font)

        self.verticalLayout_61.addWidget(self.lineEdit_id_14)


        self.horizontalLayout_49.addLayout(self.verticalLayout_61)


        self.verticalLayout_59.addLayout(self.horizontalLayout_49)

        self.search_id_btn_6 = QPushButton(self.frame_33)
        self.search_id_btn_6.setObjectName(u"search_id_btn_6")
        self.search_id_btn_6.setFont(font)

        self.verticalLayout_59.addWidget(self.search_id_btn_6)


        self.verticalLayout_52.addLayout(self.verticalLayout_59)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_5)


        self.horizontalLayout_44.addWidget(self.frame_33)

        self.line_14 = QFrame(self.page_binary_history)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_44.addWidget(self.line_14)

        self.frame_31 = QFrame(self.page_binary_history)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_31)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(100, -20, 332, 430))

        self.horizontalLayout_44.addWidget(self.frame_31)

        self.stackedWidget_binary.addWidget(self.page_binary_history)

        self.verticalLayout_22.addWidget(self.stackedWidget_binary)

        self.label_9 = QLabel(self.page_Binary)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_22.addWidget(self.label_9)

        self.stackedWidget.addWidget(self.page_Binary)
        self.page_Localization = QWidget()
        self.page_Localization.setObjectName(u"page_Localization")
        self.verticalLayout_23 = QVBoxLayout(self.page_Localization)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_5 = QFrame(self.page_Localization)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.localization_Statistic = QPushButton(self.frame_5)
        self.localization_Statistic.setObjectName(u"localization_Statistic")
        self.localization_Statistic.setMinimumSize(QSize(150, 40))
        self.localization_Statistic.setMaximumSize(QSize(150, 16777215))
        self.localization_Statistic.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_18.addWidget(self.localization_Statistic, 0, Qt.AlignTop)

        self.localization_training = QPushButton(self.frame_5)
        self.localization_training.setObjectName(u"localization_training")
        self.localization_training.setMinimumSize(QSize(150, 40))
        self.localization_training.setMaximumSize(QSize(150, 16777215))
        self.localization_training.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_18.addWidget(self.localization_training)

        self.localization_history = QPushButton(self.frame_5)
        self.localization_history.setObjectName(u"localization_history")
        self.localization_history.setMinimumSize(QSize(150, 40))
        self.localization_history.setMaximumSize(QSize(150, 16777215))
        self.localization_history.setFont(font)
        self.localization_history.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_18.addWidget(self.localization_history)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)


        self.verticalLayout_23.addWidget(self.frame_5)

        self.line_3 = QFrame(self.page_Localization)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_3)

        self.stackedWidget_localization = QStackedWidget(self.page_Localization)
        self.stackedWidget_localization.setObjectName(u"stackedWidget_localization")
        self.page_localization_statics = QWidget()
        self.page_localization_statics.setObjectName(u"page_localization_statics")
        self.horizontalLayout_60 = QHBoxLayout(self.page_localization_statics)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.frame_30 = QFrame(self.page_localization_statics)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(250, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")

        self.horizontalLayout_60.addWidget(self.frame_30)

        self.line_27 = QFrame(self.page_localization_statics)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.VLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_60.addWidget(self.line_27)

        self.frame_35 = QFrame(self.page_localization_statics)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_60.addWidget(self.frame_35)

        self.stackedWidget_localization.addWidget(self.page_localization_statics)
        self.page_localization_training = QWidget()
        self.page_localization_training.setObjectName(u"page_localization_training")
        self.horizontalLayout_84 = QHBoxLayout(self.page_localization_training)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.frame_36 = QFrame(self.page_localization_training)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(250, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_36)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(250, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_37)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 50))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_38)
        self.verticalLayout_73.setSpacing(4)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_101 = QLabel(self.frame_38)
        self.label_101.setObjectName(u"label_101")

        self.horizontalLayout_73.addWidget(self.label_101, 0, Qt.AlignLeft)

        self.comboBox_7 = QComboBox(self.frame_38)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_73.addWidget(self.comboBox_7)


        self.verticalLayout_73.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_102 = QLabel(self.frame_38)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_74.addWidget(self.label_102, 0, Qt.AlignLeft)

        self.lineEdit_36 = QLineEdit(self.frame_38)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_74.addWidget(self.lineEdit_36)


        self.verticalLayout_73.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_103 = QLabel(self.frame_38)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_75.addWidget(self.label_103, 0, Qt.AlignLeft)

        self.lineEdit_37 = QLineEdit(self.frame_38)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_75.addWidget(self.lineEdit_37)


        self.verticalLayout_73.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_104 = QLabel(self.frame_38)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_76.addWidget(self.label_104)

        self.lineEdit_38 = QLineEdit(self.frame_38)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_76.addWidget(self.lineEdit_38)


        self.verticalLayout_73.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_105 = QLabel(self.frame_38)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_77.addWidget(self.label_105)

        self.lineEdit_39 = QLineEdit(self.frame_38)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_77.addWidget(self.lineEdit_39)


        self.verticalLayout_73.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_106 = QLabel(self.frame_38)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_78.addWidget(self.label_106)

        self.lineEdit_40 = QLineEdit(self.frame_38)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_78.addWidget(self.lineEdit_40)


        self.verticalLayout_73.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_107 = QLabel(self.frame_38)
        self.label_107.setObjectName(u"label_107")

        self.horizontalLayout_79.addWidget(self.label_107)

        self.lineEdit_41 = QLineEdit(self.frame_38)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_79.addWidget(self.lineEdit_41)


        self.verticalLayout_73.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_108 = QLabel(self.frame_38)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_80.addWidget(self.label_108)

        self.lineEdit_42 = QLineEdit(self.frame_38)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_80.addWidget(self.lineEdit_42)


        self.verticalLayout_73.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_109 = QLabel(self.frame_38)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_81.addWidget(self.label_109)

        self.lineEdit_43 = QLineEdit(self.frame_38)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_81.addWidget(self.lineEdit_43)


        self.verticalLayout_73.addLayout(self.horizontalLayout_81)


        self.verticalLayout_72.addWidget(self.frame_38, 0, Qt.AlignLeft)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_39.setFrameShape(QFrame.Box)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_39)
        self.verticalLayout_74.setSpacing(3)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_110 = QLabel(self.frame_39)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(100, 0))
        self.label_110.setStyleSheet(u"text-align: center;")
        self.label_110.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.label_110)

        self.table_classification_select_class_2 = QTableWidget(self.frame_39)
        if (self.table_classification_select_class_2.columnCount() < 3):
            self.table_classification_select_class_2.setColumnCount(3)
        if (self.table_classification_select_class_2.rowCount() < 20):
            self.table_classification_select_class_2.setRowCount(20)
        self.table_classification_select_class_2.setObjectName(u"table_classification_select_class_2")
        self.table_classification_select_class_2.setRowCount(20)
        self.table_classification_select_class_2.setColumnCount(3)

        self.verticalLayout_74.addWidget(self.table_classification_select_class_2)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_111 = QLabel(self.frame_39)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_61.addWidget(self.label_111)

        self.label_112 = QLabel(self.frame_39)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_61.addWidget(self.label_112)


        self.verticalLayout_74.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_113 = QLabel(self.frame_39)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_62.addWidget(self.label_113)

        self.label_114 = QLabel(self.frame_39)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.label_114)


        self.verticalLayout_74.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_115 = QLabel(self.frame_39)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_63.addWidget(self.label_115)

        self.label_116 = QLabel(self.frame_39)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_63.addWidget(self.label_116)


        self.verticalLayout_74.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_117 = QLabel(self.frame_39)
        self.label_117.setObjectName(u"label_117")

        self.horizontalLayout_82.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_39)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_82.addWidget(self.label_118)


        self.verticalLayout_74.addLayout(self.horizontalLayout_82)

        self.pushButton_21 = QPushButton(self.frame_39)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(110, 25))
        self.pushButton_21.setMaximumSize(QSize(110, 30))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_74.addWidget(self.pushButton_21, 0, Qt.AlignHCenter)


        self.verticalLayout_72.addWidget(self.frame_39)

        self.pushButton_19 = QPushButton(self.frame_37)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(180, 30))
        self.pushButton_19.setMaximumSize(QSize(180, 16777215))
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_72.addWidget(self.pushButton_19, 0, Qt.AlignHCenter)


        self.verticalLayout_75.addWidget(self.frame_37)


        self.horizontalLayout_84.addWidget(self.frame_36)

        self.line_28 = QFrame(self.page_localization_training)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.VLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_84.addWidget(self.line_28)

        self.frame_40 = QFrame(self.page_localization_training)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_84.addWidget(self.frame_40)

        self.stackedWidget_localization.addWidget(self.page_localization_training)
        self.page_localization_history = QWidget()
        self.page_localization_history.setObjectName(u"page_localization_history")
        self.horizontalLayout_54 = QHBoxLayout(self.page_localization_history)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.frame_34 = QFrame(self.page_localization_history)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(400, 0))
        self.frame_34.setMaximumSize(QSize(300, 16777215))
        self.frame_34.setFrameShape(QFrame.Panel)
        self.frame_34.setFrameShadow(QFrame.Plain)
        self.frame_34.setLineWidth(1)
        self.verticalLayout_62 = QVBoxLayout(self.frame_34)
        self.verticalLayout_62.setSpacing(7)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(5, 5, 5, 5)
        self.label_90 = QLabel(self.frame_34)
        self.label_90.setObjectName(u"label_90")

        self.verticalLayout_62.addWidget(self.label_90)

        self.line_24 = QFrame(self.frame_34)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_24)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.spinBox_tedad_3 = QSpinBox(self.frame_34)
        self.spinBox_tedad_3.setObjectName(u"spinBox_tedad_3")
        self.spinBox_tedad_3.setMaximumSize(QSize(50, 16777212))
        self.spinBox_tedad_3.setFont(font)
        self.spinBox_tedad_3.setMaximum(999)
        self.spinBox_tedad_3.setValue(10)

        self.horizontalLayout_55.addWidget(self.spinBox_tedad_3)

        self.label_61 = QLabel(self.frame_34)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font)

        self.horizontalLayout_55.addWidget(self.label_61)

        self.request_btn_3 = QPushButton(self.frame_34)
        self.request_btn_3.setObjectName(u"request_btn_3")
        self.request_btn_3.setFont(font)
        self.request_btn_3.setStyleSheet(u"	color:rgb(255,255,255);")

        self.horizontalLayout_55.addWidget(self.request_btn_3)


        self.verticalLayout_62.addLayout(self.horizontalLayout_55)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.line_20 = QFrame(self.frame_34)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_63.addWidget(self.line_20)

        self.label_91 = QLabel(self.frame_34)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMaximumSize(QSize(16777215, 20))
        self.label_91.setFont(font)

        self.verticalLayout_63.addWidget(self.label_91)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.lineEdit_id_15 = QLineEdit(self.frame_34)
        self.lineEdit_id_15.setObjectName(u"lineEdit_id_15")
        self.lineEdit_id_15.setFont(font)

        self.horizontalLayout_56.addWidget(self.lineEdit_id_15)

        self.search_id_btn_7 = QPushButton(self.frame_34)
        self.search_id_btn_7.setObjectName(u"search_id_btn_7")
        self.search_id_btn_7.setFont(font)

        self.horizontalLayout_56.addWidget(self.search_id_btn_7)


        self.verticalLayout_63.addLayout(self.horizontalLayout_56)


        self.verticalLayout_62.addLayout(self.verticalLayout_63)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.line_21 = QFrame(self.frame_34)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_21)

        self.label_92 = QLabel(self.frame_34)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font)

        self.verticalLayout_64.addWidget(self.label_92)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_93 = QLabel(self.frame_34)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMaximumSize(QSize(16777215, 20))
        self.label_93.setFont(font)

        self.verticalLayout_65.addWidget(self.label_93)

        self.lineEdit_id_16 = QLineEdit(self.frame_34)
        self.lineEdit_id_16.setObjectName(u"lineEdit_id_16")
        self.lineEdit_id_16.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_16.setFont(font)

        self.verticalLayout_65.addWidget(self.lineEdit_id_16)


        self.horizontalLayout_57.addLayout(self.verticalLayout_65)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_94 = QLabel(self.frame_34)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMaximumSize(QSize(16777215, 20))
        self.label_94.setFont(font)

        self.verticalLayout_66.addWidget(self.label_94)

        self.lineEdit_id_17 = QLineEdit(self.frame_34)
        self.lineEdit_id_17.setObjectName(u"lineEdit_id_17")
        self.lineEdit_id_17.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_17.setFont(font)

        self.verticalLayout_66.addWidget(self.lineEdit_id_17)


        self.horizontalLayout_57.addLayout(self.verticalLayout_66)


        self.verticalLayout_64.addLayout(self.horizontalLayout_57)

        self.search_id_btn_8 = QPushButton(self.frame_34)
        self.search_id_btn_8.setObjectName(u"search_id_btn_8")
        self.search_id_btn_8.setMaximumSize(QSize(16777215, 30))
        self.search_id_btn_8.setFont(font)

        self.verticalLayout_64.addWidget(self.search_id_btn_8)


        self.verticalLayout_62.addLayout(self.verticalLayout_64)

        self.line_22 = QFrame(self.frame_34)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_22)

        self.label_95 = QLabel(self.frame_34)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMaximumSize(QSize(16777215, 20))
        self.label_95.setFont(font)

        self.verticalLayout_62.addWidget(self.label_95)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_96 = QLabel(self.frame_34)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMaximumSize(QSize(16777215, 20))
        self.label_96.setFont(font)

        self.verticalLayout_67.addWidget(self.label_96)

        self.lineEdit_id_18 = QLineEdit(self.frame_34)
        self.lineEdit_id_18.setObjectName(u"lineEdit_id_18")
        self.lineEdit_id_18.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_18.setFont(font)

        self.verticalLayout_67.addWidget(self.lineEdit_id_18)


        self.horizontalLayout_58.addLayout(self.verticalLayout_67)

        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_97 = QLabel(self.frame_34)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMaximumSize(QSize(16777215, 20))
        self.label_97.setFont(font)

        self.verticalLayout_68.addWidget(self.label_97)

        self.lineEdit_id_19 = QLineEdit(self.frame_34)
        self.lineEdit_id_19.setObjectName(u"lineEdit_id_19")
        self.lineEdit_id_19.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_19.setFont(font)

        self.verticalLayout_68.addWidget(self.lineEdit_id_19)


        self.horizontalLayout_58.addLayout(self.verticalLayout_68)


        self.verticalLayout_62.addLayout(self.horizontalLayout_58)

        self.verticalLayout_69 = QVBoxLayout()
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.line_23 = QFrame(self.frame_34)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_69.addWidget(self.line_23)

        self.label_98 = QLabel(self.frame_34)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(16777215, 20))
        self.label_98.setFont(font)

        self.verticalLayout_69.addWidget(self.label_98)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.verticalLayout_70 = QVBoxLayout()
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_99 = QLabel(self.frame_34)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(16777215, 20))
        self.label_99.setFont(font)

        self.verticalLayout_70.addWidget(self.label_99)

        self.lineEdit_id_20 = QLineEdit(self.frame_34)
        self.lineEdit_id_20.setObjectName(u"lineEdit_id_20")
        self.lineEdit_id_20.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_20.setFont(font)

        self.verticalLayout_70.addWidget(self.lineEdit_id_20)


        self.horizontalLayout_59.addLayout(self.verticalLayout_70)

        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_100 = QLabel(self.frame_34)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(16777215, 20))
        self.label_100.setFont(font)

        self.verticalLayout_71.addWidget(self.label_100)

        self.lineEdit_id_21 = QLineEdit(self.frame_34)
        self.lineEdit_id_21.setObjectName(u"lineEdit_id_21")
        self.lineEdit_id_21.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_21.setFont(font)

        self.verticalLayout_71.addWidget(self.lineEdit_id_21)


        self.horizontalLayout_59.addLayout(self.verticalLayout_71)


        self.verticalLayout_69.addLayout(self.horizontalLayout_59)

        self.search_id_btn_9 = QPushButton(self.frame_34)
        self.search_id_btn_9.setObjectName(u"search_id_btn_9")
        self.search_id_btn_9.setFont(font)

        self.verticalLayout_69.addWidget(self.search_id_btn_9)


        self.verticalLayout_62.addLayout(self.verticalLayout_69)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_6)


        self.horizontalLayout_54.addWidget(self.frame_34)

        self.line_19 = QFrame(self.page_localization_history)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_54.addWidget(self.line_19)

        self.label_28 = QLabel(self.page_localization_history)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_54.addWidget(self.label_28)

        self.frame_32 = QFrame(self.page_localization_history)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_54.addWidget(self.frame_32)

        self.stackedWidget_localization.addWidget(self.page_localization_history)

        self.verticalLayout_23.addWidget(self.stackedWidget_localization)

        self.label_18 = QLabel(self.page_Localization)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_23.addWidget(self.label_18)

        self.stackedWidget.addWidget(self.page_Localization)
        self.page_Classification = QWidget()
        self.page_Classification.setObjectName(u"page_Classification")
        self.verticalLayout_33 = QVBoxLayout(self.page_Classification)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_10 = QFrame(self.page_Classification)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(200, 50))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setSizeIncrement(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.classification_class_list = QPushButton(self.frame_10)
        self.classification_class_list.setObjectName(u"classification_class_list")
        self.classification_class_list.setMinimumSize(QSize(150, 40))
        self.classification_class_list.setMaximumSize(QSize(150, 16777215))
        self.classification_class_list.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_19.addWidget(self.classification_class_list)

        self.classification_training = QPushButton(self.frame_10)
        self.classification_training.setObjectName(u"classification_training")
        self.classification_training.setMinimumSize(QSize(150, 40))
        self.classification_training.setMaximumSize(QSize(150, 16777215))
        self.classification_training.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_19.addWidget(self.classification_training)

        self.classification_history = QPushButton(self.frame_10)
        self.classification_history.setObjectName(u"classification_history")
        self.classification_history.setMinimumSize(QSize(150, 40))
        self.classification_history.setMaximumSize(QSize(150, 16777215))
        self.classification_history.setFont(font)
        self.classification_history.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_19.addWidget(self.classification_history)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)


        self.verticalLayout_33.addWidget(self.frame_10)

        self.line_4 = QFrame(self.page_Classification)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_33.addWidget(self.line_4)

        self.stackedWidget_classification = QStackedWidget(self.page_Classification)
        self.stackedWidget_classification.setObjectName(u"stackedWidget_classification")
        self.page_classification_class_list = QWidget()
        self.page_classification_class_list.setObjectName(u"page_classification_class_list")
        self.verticalLayout_29 = QVBoxLayout(self.page_classification_class_list)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.class_list = QTableWidget(self.page_classification_class_list)
        if (self.class_list.columnCount() < 11):
            self.class_list.setColumnCount(11)
        if (self.class_list.rowCount() < 20):
            self.class_list.setRowCount(20)
        self.class_list.setObjectName(u"class_list")
        self.class_list.setMaximumSize(QSize(16777215, 500))
        self.class_list.setStyleSheet(u"	background-color: Transparent;")
        self.class_list.setLineWidth(1)
        self.class_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.class_list.setRowCount(20)
        self.class_list.setColumnCount(11)

        self.horizontalLayout_21.addWidget(self.class_list)

        self.frame_22 = QFrame(self.page_classification_class_list)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(30, 23))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")

        self.horizontalLayout_21.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.page_classification_class_list)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(300, 48))
        self.frame_21.setMaximumSize(QSize(300, 16777215))
        self.frame_21.setFrameShape(QFrame.Box)
        self.frame_21.setFrameShadow(QFrame.Plain)
        self.frame_21.setLineWidth(2)
        self.verticalLayout_30 = QVBoxLayout(self.frame_21)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_41 = QLabel(self.frame_21)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 10))
        self.label_41.setFont(font)

        self.verticalLayout_30.addWidget(self.label_41)

        self.line_7 = QFrame(self.frame_21)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_7)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_35 = QLabel(self.frame_21)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(100, 26))
        self.label_35.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_23.addWidget(self.label_35)

        self.lineEdit_2 = QLineEdit(self.frame_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_23.addWidget(self.lineEdit_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_36 = QLabel(self.frame_21)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 26))
        self.label_36.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.label_36)

        self.lineEdit_3 = QLineEdit(self.frame_21)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_25.addWidget(self.lineEdit_3)


        self.verticalLayout_30.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_42 = QLabel(self.frame_21)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(100, 26))
        self.label_42.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_31.addWidget(self.label_42)

        self.lineEdit_4 = QLineEdit(self.frame_21)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_31.addWidget(self.lineEdit_4)


        self.verticalLayout_30.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_37 = QLabel(self.frame_21)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(100, 26))
        self.label_37.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_26.addWidget(self.label_37)

        self.radioButton_3 = QRadioButton(self.frame_21)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_26.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.frame_21)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_26.addWidget(self.radioButton_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_38 = QLabel(self.frame_21)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(100, 26))
        self.label_38.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_27.addWidget(self.label_38)

        self.lineEdit_5 = QLineEdit(self.frame_21)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_27.addWidget(self.lineEdit_5)


        self.verticalLayout_30.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_39 = QLabel(self.frame_21)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(100, 26))
        self.label_39.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_28.addWidget(self.label_39)

        self.comboBox_2 = QComboBox(self.frame_21)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_28.addWidget(self.comboBox_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_40 = QLabel(self.frame_21)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(100, 0))
        self.label_40.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_29.addWidget(self.label_40)

        self.pushButton_6 = QPushButton(self.frame_21)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 0))
        self.pushButton_6.setMaximumSize(QSize(30, 16777215))
        self.pushButton_6.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_29.addWidget(self.pushButton_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_7)


        self.verticalLayout_30.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_3 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_30.addItem(self.verticalSpacer_3)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.classification_add_new_class = QPushButton(self.frame_21)
        self.classification_add_new_class.setObjectName(u"classification_add_new_class")
        self.classification_add_new_class.setMinimumSize(QSize(70, 40))
        self.classification_add_new_class.setMaximumSize(QSize(70, 16777215))
        self.classification_add_new_class.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_30.addWidget(self.classification_add_new_class)

        self.classification_add_new_class_2 = QPushButton(self.frame_21)
        self.classification_add_new_class_2.setObjectName(u"classification_add_new_class_2")
        self.classification_add_new_class_2.setMinimumSize(QSize(70, 40))
        self.classification_add_new_class_2.setMaximumSize(QSize(70, 16777215))
        self.classification_add_new_class_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_30.addWidget(self.classification_add_new_class_2)

        self.classification_add_new_class_3 = QPushButton(self.frame_21)
        self.classification_add_new_class_3.setObjectName(u"classification_add_new_class_3")
        self.classification_add_new_class_3.setMinimumSize(QSize(70, 40))
        self.classification_add_new_class_3.setMaximumSize(QSize(70, 16777215))
        self.classification_add_new_class_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(100,100,100);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")

        self.horizontalLayout_30.addWidget(self.classification_add_new_class_3)


        self.verticalLayout_30.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_21.addWidget(self.frame_21)


        self.verticalLayout_29.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_31 = QLabel(self.page_classification_class_list)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 20))
        self.label_31.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_17.addWidget(self.label_31)

        self.label_34 = QLabel(self.page_classification_class_list)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setMargin(0)

        self.horizontalLayout_17.addWidget(self.label_34)


        self.verticalLayout_29.addLayout(self.horizontalLayout_17)

        self.frame_9 = QFrame(self.page_classification_class_list)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(80, 100))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.frame_9.setLineWidth(5)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(40, 16777215))
        self.pushButton_4.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(40, 39))

        self.horizontalLayout_16.addWidget(self.pushButton_4)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_14)

        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(40, 16777215))
        self.pushButton_5.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.horizontalLayout_16.addWidget(self.pushButton_5)


        self.verticalLayout_29.addWidget(self.frame_9)

        self.line_6 = QFrame(self.page_classification_class_list)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_29.addWidget(self.line_6)

        self.stackedWidget_classification.addWidget(self.page_classification_class_list)
        self.page_classification_add_new_class = QWidget()
        self.page_classification_add_new_class.setObjectName(u"page_classification_add_new_class")
        self.label_33 = QLabel(self.page_classification_add_new_class)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(440, 120, 55, 16))
        self.stackedWidget_classification.addWidget(self.page_classification_add_new_class)
        self.page_classification_training = QWidget()
        self.page_classification_training.setObjectName(u"page_classification_training")
        self.horizontalLayout_33 = QHBoxLayout(self.page_classification_training)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_23 = QFrame(self.page_classification_training)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(250, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_23)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 50))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_25)
        self.verticalLayout_32.setSpacing(4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_67 = QLabel(self.frame_25)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_64.addWidget(self.label_67, 0, Qt.AlignLeft)

        self.comboBox_6 = QComboBox(self.frame_25)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_64.addWidget(self.comboBox_6)


        self.verticalLayout_32.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_72 = QLabel(self.frame_25)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_69.addWidget(self.label_72, 0, Qt.AlignLeft)

        self.lineEdit_32 = QLineEdit(self.frame_25)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_69.addWidget(self.lineEdit_32)


        self.verticalLayout_32.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_74 = QLabel(self.frame_25)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_71.addWidget(self.label_74, 0, Qt.AlignLeft)

        self.lineEdit_34 = QLineEdit(self.frame_25)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_71.addWidget(self.lineEdit_34)


        self.verticalLayout_32.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_69 = QLabel(self.frame_25)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_66.addWidget(self.label_69)

        self.lineEdit_29 = QLineEdit(self.frame_25)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_66.addWidget(self.lineEdit_29)


        self.verticalLayout_32.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_71 = QLabel(self.frame_25)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_68.addWidget(self.label_71)

        self.lineEdit_31 = QLineEdit(self.frame_25)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_68.addWidget(self.lineEdit_31)


        self.verticalLayout_32.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_68 = QLabel(self.frame_25)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_65.addWidget(self.label_68)

        self.lineEdit_28 = QLineEdit(self.frame_25)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_65.addWidget(self.lineEdit_28)


        self.verticalLayout_32.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_73 = QLabel(self.frame_25)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_70.addWidget(self.label_73)

        self.lineEdit_33 = QLineEdit(self.frame_25)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_70.addWidget(self.lineEdit_33)


        self.verticalLayout_32.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_70 = QLabel(self.frame_25)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_67.addWidget(self.label_70)

        self.lineEdit_30 = QLineEdit(self.frame_25)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_67.addWidget(self.lineEdit_30)


        self.verticalLayout_32.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_75 = QLabel(self.frame_25)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_72.addWidget(self.label_75)

        self.lineEdit_35 = QLineEdit(self.frame_25)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_72.addWidget(self.lineEdit_35)


        self.verticalLayout_32.addLayout(self.horizontalLayout_72)


        self.verticalLayout_31.addWidget(self.frame_25, 0, Qt.AlignLeft)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_26.setFrameShape(QFrame.Box)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_26)
        self.verticalLayout_40.setSpacing(3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_26)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(100, 0))
        self.label_52.setStyleSheet(u"text-align: center;")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_52)

        self.table_classification_select_class = QTableWidget(self.frame_26)
        if (self.table_classification_select_class.columnCount() < 3):
            self.table_classification_select_class.setColumnCount(3)
        if (self.table_classification_select_class.rowCount() < 20):
            self.table_classification_select_class.setRowCount(20)
        self.table_classification_select_class.setObjectName(u"table_classification_select_class")
        self.table_classification_select_class.setRowCount(20)
        self.table_classification_select_class.setColumnCount(3)

        self.verticalLayout_40.addWidget(self.table_classification_select_class)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_53 = QLabel(self.frame_26)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_50.addWidget(self.label_53)

        self.label_57 = QLabel(self.frame_26)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_57)


        self.verticalLayout_40.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_54 = QLabel(self.frame_26)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_51.addWidget(self.label_54)

        self.label_64 = QLabel(self.frame_26)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.label_64)


        self.verticalLayout_40.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_55 = QLabel(self.frame_26)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_52.addWidget(self.label_55)

        self.label_65 = QLabel(self.frame_26)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_52.addWidget(self.label_65)


        self.verticalLayout_40.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_56 = QLabel(self.frame_26)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_53.addWidget(self.label_56)

        self.label_66 = QLabel(self.frame_26)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_66)


        self.verticalLayout_40.addLayout(self.horizontalLayout_53)

        self.pushButton_20 = QPushButton(self.frame_26)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(110, 25))
        self.pushButton_20.setMaximumSize(QSize(110, 30))
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_40.addWidget(self.pushButton_20, 0, Qt.AlignHCenter)


        self.verticalLayout_31.addWidget(self.frame_26)

        self.pushButton_18 = QPushButton(self.frame_23)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(180, 30))
        self.pushButton_18.setMaximumSize(QSize(180, 16777215))
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.pushButton_18, 0, Qt.AlignHCenter)


        self.horizontalLayout_33.addWidget(self.frame_23)

        self.line_8 = QFrame(self.page_classification_training)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_33.addWidget(self.line_8)

        self.frame_24 = QFrame(self.page_classification_training)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.frame_24)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(120, 0, 354, 463))

        self.horizontalLayout_33.addWidget(self.frame_24)

        self.stackedWidget_classification.addWidget(self.page_classification_training)
        self.page_classification_history = QWidget()
        self.page_classification_history.setObjectName(u"page_classification_history")
        self.horizontalLayout_38 = QHBoxLayout(self.page_classification_history)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_27 = QFrame(self.page_classification_history)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(400, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_27)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(400, 0))
        self.frame_29.setMaximumSize(QSize(300, 16777215))
        self.frame_29.setFrameShape(QFrame.Panel)
        self.frame_29.setFrameShadow(QFrame.Plain)
        self.frame_29.setLineWidth(1)
        self.verticalLayout_48 = QVBoxLayout(self.frame_29)
        self.verticalLayout_48.setSpacing(7)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(5, 5, 5, 5)
        self.label_77 = QLabel(self.frame_29)
        self.label_77.setObjectName(u"label_77")

        self.verticalLayout_48.addWidget(self.label_77)

        self.line_26 = QFrame(self.frame_29)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_26)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.spinBox_tedad = QSpinBox(self.frame_29)
        self.spinBox_tedad.setObjectName(u"spinBox_tedad")
        self.spinBox_tedad.setMaximumSize(QSize(50, 16777212))
        self.spinBox_tedad.setFont(font)
        self.spinBox_tedad.setMaximum(999)
        self.spinBox_tedad.setValue(10)

        self.horizontalLayout_40.addWidget(self.spinBox_tedad)

        self.label_46 = QLabel(self.frame_29)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.horizontalLayout_40.addWidget(self.label_46)

        self.request_btn = QPushButton(self.frame_29)
        self.request_btn.setObjectName(u"request_btn")
        self.request_btn.setFont(font)
        self.request_btn.setStyleSheet(u"	color:rgb(255,255,255);")

        self.horizontalLayout_40.addWidget(self.request_btn)


        self.verticalLayout_48.addLayout(self.horizontalLayout_40)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.line_10 = QFrame(self.frame_29)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_10)

        self.label_47 = QLabel(self.frame_29)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 20))
        self.label_47.setFont(font)

        self.verticalLayout_44.addWidget(self.label_47)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lineEdit_id = QLineEdit(self.frame_29)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setFont(font)

        self.horizontalLayout_41.addWidget(self.lineEdit_id)

        self.search_id_btn = QPushButton(self.frame_29)
        self.search_id_btn.setObjectName(u"search_id_btn")
        self.search_id_btn.setFont(font)

        self.horizontalLayout_41.addWidget(self.search_id_btn)


        self.verticalLayout_44.addLayout(self.horizontalLayout_41)


        self.verticalLayout_48.addLayout(self.verticalLayout_44)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.line_11 = QFrame(self.frame_29)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_11)

        self.label_48 = QLabel(self.frame_29)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.verticalLayout_45.addWidget(self.label_48)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_49 = QLabel(self.frame_29)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 20))
        self.label_49.setFont(font)

        self.verticalLayout_46.addWidget(self.label_49)

        self.lineEdit_id_2 = QLineEdit(self.frame_29)
        self.lineEdit_id_2.setObjectName(u"lineEdit_id_2")
        self.lineEdit_id_2.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_2.setFont(font)

        self.verticalLayout_46.addWidget(self.lineEdit_id_2)


        self.horizontalLayout_42.addLayout(self.verticalLayout_46)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_50 = QLabel(self.frame_29)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 20))
        self.label_50.setFont(font)

        self.verticalLayout_47.addWidget(self.label_50)

        self.lineEdit_id_3 = QLineEdit(self.frame_29)
        self.lineEdit_id_3.setObjectName(u"lineEdit_id_3")
        self.lineEdit_id_3.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_3.setFont(font)

        self.verticalLayout_47.addWidget(self.lineEdit_id_3)


        self.horizontalLayout_42.addLayout(self.verticalLayout_47)


        self.verticalLayout_45.addLayout(self.horizontalLayout_42)

        self.search_id_btn_2 = QPushButton(self.frame_29)
        self.search_id_btn_2.setObjectName(u"search_id_btn_2")
        self.search_id_btn_2.setMaximumSize(QSize(16777215, 30))
        self.search_id_btn_2.setFont(font)

        self.verticalLayout_45.addWidget(self.search_id_btn_2)


        self.verticalLayout_48.addLayout(self.verticalLayout_45)

        self.line_12 = QFrame(self.frame_29)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_12)

        self.label_76 = QLabel(self.frame_29)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 20))
        self.label_76.setFont(font)

        self.verticalLayout_48.addWidget(self.label_76)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_62 = QLabel(self.frame_29)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 20))
        self.label_62.setFont(font)

        self.verticalLayout_50.addWidget(self.label_62)

        self.lineEdit_id_4 = QLineEdit(self.frame_29)
        self.lineEdit_id_4.setObjectName(u"lineEdit_id_4")
        self.lineEdit_id_4.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_4.setFont(font)

        self.verticalLayout_50.addWidget(self.lineEdit_id_4)


        self.horizontalLayout_43.addLayout(self.verticalLayout_50)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_63 = QLabel(self.frame_29)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 20))
        self.label_63.setFont(font)

        self.verticalLayout_51.addWidget(self.label_63)

        self.lineEdit_id_5 = QLineEdit(self.frame_29)
        self.lineEdit_id_5.setObjectName(u"lineEdit_id_5")
        self.lineEdit_id_5.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_5.setFont(font)

        self.verticalLayout_51.addWidget(self.lineEdit_id_5)


        self.horizontalLayout_43.addLayout(self.verticalLayout_51)


        self.verticalLayout_48.addLayout(self.horizontalLayout_43)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.line_13 = QFrame(self.frame_29)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_41.addWidget(self.line_13)

        self.label_58 = QLabel(self.frame_29)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(16777215, 20))
        self.label_58.setFont(font)

        self.verticalLayout_41.addWidget(self.label_58)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_59 = QLabel(self.frame_29)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(16777215, 20))
        self.label_59.setFont(font)

        self.verticalLayout_42.addWidget(self.label_59)

        self.lineEdit_id_6 = QLineEdit(self.frame_29)
        self.lineEdit_id_6.setObjectName(u"lineEdit_id_6")
        self.lineEdit_id_6.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_6.setFont(font)

        self.verticalLayout_42.addWidget(self.lineEdit_id_6)


        self.horizontalLayout_39.addLayout(self.verticalLayout_42)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_60 = QLabel(self.frame_29)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(16777215, 20))
        self.label_60.setFont(font)

        self.verticalLayout_43.addWidget(self.label_60)

        self.lineEdit_id_7 = QLineEdit(self.frame_29)
        self.lineEdit_id_7.setObjectName(u"lineEdit_id_7")
        self.lineEdit_id_7.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id_7.setFont(font)

        self.verticalLayout_43.addWidget(self.lineEdit_id_7)


        self.horizontalLayout_39.addLayout(self.verticalLayout_43)


        self.verticalLayout_41.addLayout(self.horizontalLayout_39)

        self.search_id_btn_4 = QPushButton(self.frame_29)
        self.search_id_btn_4.setObjectName(u"search_id_btn_4")
        self.search_id_btn_4.setFont(font)

        self.verticalLayout_41.addWidget(self.search_id_btn_4)


        self.verticalLayout_48.addLayout(self.verticalLayout_41)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_4)


        self.verticalLayout_49.addWidget(self.frame_29)


        self.horizontalLayout_38.addWidget(self.frame_27)

        self.line_9 = QFrame(self.page_classification_history)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_38.addWidget(self.line_9)

        self.frame_28 = QFrame(self.page_classification_history)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_28)

        self.label_45 = QLabel(self.page_classification_history)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_38.addWidget(self.label_45)

        self.stackedWidget_classification.addWidget(self.page_classification_history)

        self.verticalLayout_33.addWidget(self.stackedWidget_classification)

        self.label_19 = QLabel(self.page_Classification)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_33.addWidget(self.label_19)

        self.stackedWidget.addWidget(self.page_Classification)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon15)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 222, 222))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon16)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 0))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush6 = QBrush(QColor(221, 221, 221, 255))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.page_software_setting = QWidget()
        self.page_software_setting.setObjectName(u"page_software_setting")
        self.verticalLayout_20 = QVBoxLayout(self.page_software_setting)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_43 = QFrame(self.page_software_setting)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_43)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.frame_57 = QFrame(self.frame_45)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setGeometry(QRect(30, 20, 261, 81))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_57)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 81, 16))
        self.comboBox_10 = QComboBox(self.frame_57)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(100, 30, 151, 22))
        self.fontComboBox = QFontComboBox(self.frame_45)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setGeometry(QRect(100, 190, 187, 22))

        self.verticalLayout_86.addWidget(self.frame_45)

        self.frame_56 = QFrame(self.frame_43)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)

        self.verticalLayout_86.addWidget(self.frame_56)


        self.verticalLayout_20.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.page_software_setting)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_94.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget_defect.setCurrentIndex(1)
        self.tabWidget_defect.setCurrentIndex(1)
        self.stackedWidget_pbt.setCurrentIndex(0)
        self.stackedWidget_binary.setCurrentIndex(1)
        self.stackedWidget_localization.setCurrentIndex(1)
        self.stackedWidget_classification.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"SABA", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"    Trainer", None))
        self.Data_auquzation_btn.setText(QCoreApplication.translate("MainWindow", u"Data Auquzation", None))
        self.label_btn.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.tuning_btn.setText(QCoreApplication.translate("MainWindow", u"Tuning", None))
        self.pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Offline Test", None))
        self.btn_about_us.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Tuning", None))
        self.Binary_btn.setText(QCoreApplication.translate("MainWindow", u"Binary            ", None))
        self.Localization_btn.setText(QCoreApplication.translate("MainWindow", u"Localization", None))
        self.Classification_btn.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.label_2.setText("")
        self.titleRightInfo.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Please Login", None))
#if QT_CONFIG(tooltip)
        self.login_btn.setToolTip(QCoreApplication.translate("MainWindow", u"User", None))
#endif // QT_CONFIG(tooltip)
        self.login_btn.setText("")
#if QT_CONFIG(tooltip)
        self.setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.setting_btn.setText("")
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
        self.btn_software_setting.setText(QCoreApplication.translate("MainWindow", u"Software setting", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Tuning Setting", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"User Settings", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Database Setting", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Storage Setting", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"LIVE", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Cursor :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start Draging", None))
        self.crop_image_up.setText("")
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Technical View", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"DOWN Side Technical View", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DSTV", None))
        self.down_side_technical.setText("")
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"UP Side Technical View", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"USTV", None))
        self.up_side_technical.setText("")
#if QT_CONFIG(statustip)
        self.pushButton_28.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_28.setText("")
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.polygon_btn.setText("")
        self.bounding_btn.setText("")
        self.pushButton_14.setText("")
        self.n_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.p_image.setText(QCoreApplication.translate("MainWindow", u"prev ima", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Coil number :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cam num :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total Images Labeled:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Problem images labaled :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"User labaled :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Defect :", None))
        self.yes_defect.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.no_defect.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.tabWidget_defect.setTabText(self.tabWidget_defect.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Mask", None))
        self.tabWidget_defect.setTabText(self.tabWidget_defect.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Labels :", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Image has no Defect", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.load_dataset_pbt.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.pipeline_pbt.setText(QCoreApplication.translate("MainWindow", u"Pipeline", None))
        self.history_pbt.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Select Algorithm :", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Binary : ", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Localization : ", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Classification :", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.binary_list.setText(QCoreApplication.translate("MainWindow", u"Binary list", None))
        self.binary_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.binary_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"list", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name :", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Epochs :", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Learning Rate :", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Tuning Epochs :", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Validation Split % :", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Image Path :", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Label Path :", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Select Class", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Total Classes:", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Selected Classes:", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Total Images :", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Selected Images :", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Search Tab", None))
        self.spinBox_tedad_2.setPrefix("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u" last row", None))
        self.request_btn_2.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"by Name :", None))
        self.search_id_btn_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"by Accuracy :", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.search_id_btn_5.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"by Recall :", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"by Epooch :", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.search_id_btn_6.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"hist", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"hist", None))
        self.localization_Statistic.setText(QCoreApplication.translate("MainWindow", u"Statistic", None))
        self.localization_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.localization_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name :", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Epochs :", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Learning Rate :", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Tuning Epochs :", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Validation Split % :", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Image Path :", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Label Path :", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Select Class", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Total Classes:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Selected Classes:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Total Images :", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Selected Images :", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Search Tab", None))
        self.spinBox_tedad_3.setPrefix("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u" last row", None))
        self.request_btn_3.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"by Name :", None))
        self.search_id_btn_7.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"by Accuracy :", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.search_id_btn_8.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"by Recall :", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"by Epooch :", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.search_id_btn_9.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"his", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.classification_class_list.setText(QCoreApplication.translate("MainWindow", u"Class list", None))
        self.classification_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.classification_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Add & Edit Class", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Name ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Short-Name", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Is Defect", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Color :", None))
        self.pushButton_6.setText("")
        self.classification_add_new_class.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.classification_add_new_class_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.classification_add_new_class_3.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Images Class :", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Oil", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name :", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Epochs :", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Learning Rate :", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Tuning Epochs :", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Validation Split % :", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Image Path :", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Label Path :", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Select Class", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Total Classes:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Selected Classes:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Total Images :", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Selected Images :", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"train", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Search Tab", None))
        self.spinBox_tedad.setPrefix("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u" last row", None))
        self.request_btn.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"by Name :", None))
        self.search_id_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"by Accuracy :", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.search_id_btn_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"by Recall :", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"by Epooch :", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.search_id_btn_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"hist", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Dorsa-co", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi
