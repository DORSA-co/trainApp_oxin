# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oxin.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFontComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

from checkablecombobox import CheckableComboBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1527, 970)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1527, 970))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
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
"	background-color: rgb(212,212,212);\n"
"	bor"
                        "der: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(20, 22, 92);\n"
"}\n"
"#topLogo {\n"
"	background-color: Transparent;\n"
"	\n"
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
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	back"
                        "ground-position: left center;\n"
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
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(20, 22, 92);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(20, 22, 92);\n"
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
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
""
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
"	background-color: rgb(20, 22, 92);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: "
                        "4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(20, 22, 92); }\n"
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
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWi"
                        "dget */\n"
"QTableWidget {	\n"
"	padding: 1px;\n"
"	border-radius:1px;\n"
"	gridline-color: rgb(40,70,160);\n"
"	border-bottom: 1px solid rgb(180,180,180);\n"
"\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: transparent;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(180,180,108);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"	padding: 3px;\n"
"    background-color: rgb(50,50,100);\n"
"\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"background-color: rgb(30,30,30);\n"
"color:rgb(255,255,255);\n"
"\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(70,135,230);\n"
"	color : White;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(210,210,150);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	s"
                        "election-color: rgb(255, 255, 255);\n"
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
"TextEdit */\n"
"QTextEdit {\n"
"	background-color: rgb(210,210,150);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
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
""
                        "	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
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
"    subcontrol-origin: m"
                        "argin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
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
""
                        "     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(30,30,30);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"/*\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, "
                        "66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"/*\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
"	padding: 2px;\n"
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
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121"
                        ", 198);	\n"
"	background-color: rgb(200,200,200);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"\n"
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
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	color:white;\n"
"	border: 1px solid rgb(52, 59, 72);\n"
"	border-radius: 2px;	\n"
"	background-color: rgb(100"
                        ",100,100);\n"
"	\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 5px solid rgb(43, 50, 61);\n"
"}\n"
"#warning_label_page{\n"
"	background-color: transparent;\n"
"	border: None\n"
"}\n"
"\n"
"#warning_train_page{\n"
"	background-color: transparent;\n"
"	border: None\n"
"}\n"
"\n"
"#l_warning_train_page{\n"
"	background-color: transparent;\n"
"	border: None\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"QProgressBar {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 1px;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #fff,\n"
"stop: 0.4999 #eee,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
""
                        "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #78d,\n"
"stop: 0.4999 #46a,\n"
"stop: 0.5 #45a,\n"
"stop: 1 #238 );\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_94 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 5, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"font: 11pt \"ubuntu\";")
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
        self.topLogoInfo.setStyleSheet(u"")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font1 = QFont()
        font1.setFamilies([u"ubuntu"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/t1.png);\n"
"")
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setStyleSheet(u"border-color: rgb(20, 22, 92);")
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
        sizePolicy1.setHeightForWidth(self.Data_auquzation_btn.sizePolicy().hasHeightForWidth())
        self.Data_auquzation_btn.setSizePolicy(sizePolicy1)
        self.Data_auquzation_btn.setMinimumSize(QSize(0, 45))
        self.Data_auquzation_btn.setFont(font1)
        self.Data_auquzation_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Data_auquzation_btn.setLayoutDirection(Qt.LeftToRight)
        self.Data_auquzation_btn.setStyleSheet(u"background-image: url(./images/icons/graber.png);\n"
"background-color: rgb(170, 170, 212);")

        self.verticalLayout_8.addWidget(self.Data_auquzation_btn)

        self.label_btn = QPushButton(self.topMenu)
        self.label_btn.setObjectName(u"label_btn")
        sizePolicy1.setHeightForWidth(self.label_btn.sizePolicy().hasHeightForWidth())
        self.label_btn.setSizePolicy(sizePolicy1)
        self.label_btn.setMinimumSize(QSize(0, 45))
        self.label_btn.setFont(font1)
        self.label_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_btn.setLayoutDirection(Qt.LeftToRight)
        self.label_btn.setStyleSheet(u"background-image: url(./images/icons/label.png);\n"
"")

        self.verticalLayout_8.addWidget(self.label_btn)

        self.tuning_btn = QPushButton(self.topMenu)
        self.tuning_btn.setObjectName(u"tuning_btn")
        sizePolicy1.setHeightForWidth(self.tuning_btn.sizePolicy().hasHeightForWidth())
        self.tuning_btn.setSizePolicy(sizePolicy1)
        self.tuning_btn.setMinimumSize(QSize(0, 45))
        self.tuning_btn.setFont(font1)
        self.tuning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuning_btn.setLayoutDirection(Qt.LeftToRight)
        self.tuning_btn.setStyleSheet(u"background-image: url(./images/icons/tuning.png);\n"
"")
        self.tuning_btn.setIconSize(QSize(20, 44))

        self.verticalLayout_8.addWidget(self.tuning_btn)

        self.pbt_btn = QPushButton(self.topMenu)
        self.pbt_btn.setObjectName(u"pbt_btn")
        self.pbt_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pbt_btn.sizePolicy().hasHeightForWidth())
        self.pbt_btn.setSizePolicy(sizePolicy1)
        self.pbt_btn.setMinimumSize(QSize(0, 45))
        self.pbt_btn.setFont(font1)
        self.pbt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbt_btn.setLayoutDirection(Qt.LeftToRight)
        self.pbt_btn.setStyleSheet(u"background-image: url(./images/icons/PBT.png)")

        self.verticalLayout_8.addWidget(self.pbt_btn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.log_btn = QPushButton(self.topMenu)
        self.log_btn.setObjectName(u"log_btn")
        self.log_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.log_btn.sizePolicy().hasHeightForWidth())
        self.log_btn.setSizePolicy(sizePolicy1)
        self.log_btn.setMinimumSize(QSize(0, 45))
        self.log_btn.setFont(font1)
        self.log_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.log_btn.setLayoutDirection(Qt.LeftToRight)
        self.log_btn.setStyleSheet(u"background-image: url(./images/icons/log.png)")

        self.verticalLayout_8.addWidget(self.log_btn)

        self.label_12 = QLabel(self.topMenu)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(0, 72))
        self.label_12.setStyleSheet(u" font-size: 13px;\n"
"color: rgb(113, 126, 149); \n"
"padding-left: 10px; \n"
"padding-right: 10px; \n"
"padding-bottom: 2px; \n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_12)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setStyleSheet(u"bacground-color: (20, 68, 117)")
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
        self.extraLabel.setStyleSheet(u"color: white;")
        self.extraLabel.setTextFormat(Qt.PlainText)

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setStyleSheet(u"border-color: rgb(20, 68, 117);")
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Binary_btn.sizePolicy().hasHeightForWidth())
        self.Binary_btn.setSizePolicy(sizePolicy2)
        self.Binary_btn.setMinimumSize(QSize(100, 45))
        self.Binary_btn.setMaximumSize(QSize(100, 16777215))
        self.Binary_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Binary_btn.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"color: black;\n"
"text-align:center;")

        self.verticalLayout_10.addWidget(self.Binary_btn)

        self.Localization_btn = QPushButton(self.extraCenter)
        self.Localization_btn.setObjectName(u"Localization_btn")
        self.Localization_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.Localization_btn.sizePolicy().hasHeightForWidth())
        self.Localization_btn.setSizePolicy(sizePolicy2)
        self.Localization_btn.setMinimumSize(QSize(100, 45))
        self.Localization_btn.setMaximumSize(QSize(100, 16777215))
        self.Localization_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Localization_btn.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"color: black;\n"
"text-align:center;")

        self.verticalLayout_10.addWidget(self.Localization_btn, 0, Qt.AlignLeft)

        self.Classification_btn = QPushButton(self.extraCenter)
        self.Classification_btn.setObjectName(u"Classification_btn")
        self.Classification_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.Classification_btn.sizePolicy().hasHeightForWidth())
        self.Classification_btn.setSizePolicy(sizePolicy2)
        self.Classification_btn.setMinimumSize(QSize(100, 45))
        self.Classification_btn.setMaximumSize(QSize(100, 16777215))
        self.Classification_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Classification_btn.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"color: black;\n"
"text-align:center;")

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setMinimumSize(QSize(0, 0))
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_dorsa = QLabel(self.leftBox)
        self.label_dorsa.setObjectName(u"label_dorsa")
        self.label_dorsa.setMaximumSize(QSize(0, 62))
        self.label_dorsa.setPixmap(QPixmap(u"images/images/dorsa_oxin_white.png"))
        self.label_dorsa.setScaledContents(True)
        self.label_dorsa.setMargin(0)

        self.horizontalLayout_3.addWidget(self.label_dorsa, 0, Qt.AlignLeft)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMinimumSize(QSize(0, 0))
        self.titleRightInfo.setMaximumSize(QSize(20, 45))
        self.titleRightInfo.setFont(font1)
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
        self.label_51.setMinimumSize(QSize(0, 0))
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
        self.user_name = QLabel(self.rightButtons)
        self.user_name.setObjectName(u"user_name")
        sizePolicy3.setHeightForWidth(self.user_name.sizePolicy().hasHeightForWidth())
        self.user_name.setSizePolicy(sizePolicy3)
        self.user_name.setMinimumSize(QSize(0, 0))
        self.user_name.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.user_name, 0, Qt.AlignRight)

        self.label_app_erors = QLabel(self.rightButtons)
        self.label_app_erors.setObjectName(u"label_app_erors")
        self.label_app_erors.setMaximumSize(QSize(16777215, 30))
        self.label_app_erors.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_app_erors)

        self.horizontalSpacer_2 = QSpacerItem(15, 18, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.login_btn = QPushButton(self.rightButtons)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setEnabled(True)
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

        self.helpButton = QPushButton(self.rightButtons)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(28, 28))
        self.helpButton.setMaximumSize(QSize(28, 28))
        self.helpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/icon_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon3)
        self.helpButton.setIconSize(QSize(17, 17))

        self.horizontalLayout_2.addWidget(self.helpButton)

        self.miniButton = QPushButton(self.rightButtons)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon4)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.rightButtons)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"ubuntu"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font2)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon5)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.rightButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon6)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setStyleSheet(u"border-color: rgb(20, 68, 117);")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_settin2 = QFrame(self.contentBottom)
        self.frame_settin2.setObjectName(u"frame_settin2")
        self.frame_settin2.setMinimumSize(QSize(188, 0))
        self.frame_settin2.setMaximumSize(QSize(16777215, 0))
        self.frame_settin2.setStyleSheet(u"background-color: rgb(20, 22, 92);")
        self.frame_settin2.setFrameShape(QFrame.StyledPanel)
        self.frame_settin2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_settin2)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.setting_eror = QLabel(self.frame_settin2)
        self.setting_eror.setObjectName(u"setting_eror")

        self.horizontalLayout_37.addWidget(self.setting_eror)

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

        self.btn_user_profile = QPushButton(self.frame_settin2)
        self.btn_user_profile.setObjectName(u"btn_user_profile")
        self.btn_user_profile.setMinimumSize(QSize(150, 0))
        self.btn_user_profile.setMaximumSize(QSize(150, 16777215))
        self.btn_user_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_user_profile.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_37.addWidget(self.btn_user_profile)


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
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setToolTipDuration(-1)
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
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.main.setPalette(palette)
        self.main.setToolTipDuration(-1)
        self.main.setFrameShape(QFrame.Panel)
        self.main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.main)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_89 = QVBoxLayout(self.tab_5)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(-1, 2, -1, 2)
        self.camera_connection_msg = QLabel(self.tab_5)
        self.camera_connection_msg.setObjectName(u"camera_connection_msg")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.camera_connection_msg.sizePolicy().hasHeightForWidth())
        self.camera_connection_msg.setSizePolicy(sizePolicy5)
        self.camera_connection_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_89.addWidget(self.camera_connection_msg)

        self.frame_73 = QFrame(self.tab_5)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 0))
        self.frame_73.setMaximumSize(QSize(16777215, 16666666))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_44.setSpacing(4)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(2, 2, 2, 2)
        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 0))
        self.frame_75.setMaximumSize(QSize(16666666, 16777215))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_75)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.connect_camera_btn = QPushButton(self.frame_75)
        self.connect_camera_btn.setObjectName(u"connect_camera_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.connect_camera_btn.sizePolicy().hasHeightForWidth())
        self.connect_camera_btn.setSizePolicy(sizePolicy6)
        self.connect_camera_btn.setMaximumSize(QSize(16777215, 16777215))
        self.connect_camera_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_camera_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(180, 200, 180);\n"
"color:rgb(0,0,0);\n"
"border: 1px solid rgb(52, 59, 72);\n"
"border-radius: 1px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(50,200,50);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(10,210,10);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled-hover{\n"
"    background-color:rgb(255,255,255);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"images/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_camera_btn.setIcon(icon7)

        self.verticalLayout_52.addWidget(self.connect_camera_btn)

        self.disconnect_camera_btn = QPushButton(self.frame_75)
        self.disconnect_camera_btn.setObjectName(u"disconnect_camera_btn")
        self.disconnect_camera_btn.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.disconnect_camera_btn.sizePolicy().hasHeightForWidth())
        self.disconnect_camera_btn.setSizePolicy(sizePolicy6)
        self.disconnect_camera_btn.setMaximumSize(QSize(16777215, 16777215))
        self.disconnect_camera_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnect_camera_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(200,160,160);\n"
"color:rgb(0,0,0);\n"
"border: 1px solid rgb(52, 59, 72);\n"
"border-radius: 1px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,50,50);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(210,10,10);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled-hover {\n"
"    background-color:rgb(255,255,255);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"images/disconnected-chains.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnect_camera_btn.setIcon(icon8)
        self.disconnect_camera_btn.setIconSize(QSize(20, 18))

        self.verticalLayout_52.addWidget(self.disconnect_camera_btn)


        self.horizontalLayout_44.addWidget(self.frame_75)

        self.frame_42 = QFrame(self.frame_73)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(87, 0))
        self.frame_42.setStyleSheet(u"border: None;")
        self.frame_42.setFrameShape(QFrame.Box)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setSpacing(1)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_46 = QFrame(self.frame_42)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(16777215, 95))
        self.frame_46.setStyleSheet(u"border: None")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_46)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(18)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_80 = QLabel(self.frame_46)
        self.label_80.setObjectName(u"label_80")
        sizePolicy2.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"ubuntu"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_80.setFont(font3)
        self.label_80.setStyleSheet(u"font: 10pt ;")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_80)

        self.label_81 = QLabel(self.frame_46)
        self.label_81.setObjectName(u"label_81")
        sizePolicy2.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy2)
        self.label_81.setFont(font3)
        self.label_81.setStyleSheet(u"font: 10pt ;")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_81)

        self.label_82 = QLabel(self.frame_46)
        self.label_82.setObjectName(u"label_82")
        sizePolicy2.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy2)
        self.label_82.setFont(font3)
        self.label_82.setStyleSheet(u"font: 10pt ;")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_82)

        self.label_83 = QLabel(self.frame_46)
        self.label_83.setObjectName(u"label_83")
        sizePolicy2.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy2)
        self.label_83.setFont(font3)
        self.label_83.setStyleSheet(u"font: 10pt ;")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_83)

        self.label_86 = QLabel(self.frame_46)
        self.label_86.setObjectName(u"label_86")
        sizePolicy2.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy2)
        self.label_86.setFont(font3)
        self.label_86.setStyleSheet(u"font: 10pt ;")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_46)
        self.label_87.setObjectName(u"label_87")
        sizePolicy2.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy2)
        self.label_87.setFont(font3)
        self.label_87.setStyleSheet(u"font: 10pt ;")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_87)

        self.label_88 = QLabel(self.frame_46)
        self.label_88.setObjectName(u"label_88")
        sizePolicy2.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy2)
        self.label_88.setFont(font3)
        self.label_88.setStyleSheet(u"font: 10pt ;")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_88)

        self.label_89 = QLabel(self.frame_46)
        self.label_89.setObjectName(u"label_89")
        sizePolicy2.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy2)
        self.label_89.setFont(font3)
        self.label_89.setStyleSheet(u"font: 10pt ;")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_89)

        self.label_94 = QLabel(self.frame_46)
        self.label_94.setObjectName(u"label_94")
        sizePolicy2.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy2)
        self.label_94.setFont(font3)
        self.label_94.setStyleSheet(u"font: 10pt ;")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_94)

        self.label_98 = QLabel(self.frame_46)
        self.label_98.setObjectName(u"label_98")
        sizePolicy2.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy2)
        self.label_98.setFont(font3)
        self.label_98.setStyleSheet(u"font: 10pt ;")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_98)

        self.label_99 = QLabel(self.frame_46)
        self.label_99.setObjectName(u"label_99")
        sizePolicy2.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy2)
        self.label_99.setFont(font3)
        self.label_99.setStyleSheet(u"font: 10pt ;")
        self.label_99.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_99)

        self.label_100 = QLabel(self.frame_46)
        self.label_100.setObjectName(u"label_100")
        sizePolicy2.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy2)
        self.label_100.setFont(font3)
        self.label_100.setStyleSheet(u"font: 10pt")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_100)


        self.verticalLayout_69.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setSpacing(20)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.camera01_btn = QPushButton(self.frame_46)
        self.camera01_btn.setObjectName(u"camera01_btn")
        self.camera01_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera01_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        icon9 = QIcon()
        icon9.addFile(u"images/camtop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera01_btn.setIcon(icon9)
        self.camera01_btn.setIconSize(QSize(20, 20))
        self.camera01_btn.setFlat(False)

        self.horizontalLayout_81.addWidget(self.camera01_btn)

        self.camera02_btn = QPushButton(self.frame_46)
        self.camera02_btn.setObjectName(u"camera02_btn")
        self.camera02_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera02_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera02_btn.setIcon(icon9)
        self.camera02_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera02_btn)

        self.camera03_btn = QPushButton(self.frame_46)
        self.camera03_btn.setObjectName(u"camera03_btn")
        self.camera03_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera03_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera03_btn.setIcon(icon9)
        self.camera03_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera03_btn)

        self.camera04_btn = QPushButton(self.frame_46)
        self.camera04_btn.setObjectName(u"camera04_btn")
        self.camera04_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera04_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera04_btn.setIcon(icon9)
        self.camera04_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera04_btn)

        self.camera05_btn = QPushButton(self.frame_46)
        self.camera05_btn.setObjectName(u"camera05_btn")
        self.camera05_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera05_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera05_btn.setIcon(icon9)
        self.camera05_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera05_btn)

        self.camera06_btn = QPushButton(self.frame_46)
        self.camera06_btn.setObjectName(u"camera06_btn")
        self.camera06_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera06_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera06_btn.setIcon(icon9)
        self.camera06_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera06_btn)

        self.camera07_btn = QPushButton(self.frame_46)
        self.camera07_btn.setObjectName(u"camera07_btn")
        self.camera07_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera07_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera07_btn.setIcon(icon9)
        self.camera07_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera07_btn)

        self.camera08_btn = QPushButton(self.frame_46)
        self.camera08_btn.setObjectName(u"camera08_btn")
        self.camera08_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera08_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera08_btn.setIcon(icon9)
        self.camera08_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera08_btn)

        self.camera09_btn = QPushButton(self.frame_46)
        self.camera09_btn.setObjectName(u"camera09_btn")
        self.camera09_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera09_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera09_btn.setIcon(icon9)
        self.camera09_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera09_btn)

        self.camera10_btn = QPushButton(self.frame_46)
        self.camera10_btn.setObjectName(u"camera10_btn")
        self.camera10_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera10_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera10_btn.setIcon(icon9)
        self.camera10_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera10_btn)

        self.camera11_btn = QPushButton(self.frame_46)
        self.camera11_btn.setObjectName(u"camera11_btn")
        self.camera11_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera11_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera11_btn.setIcon(icon9)
        self.camera11_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera11_btn)

        self.camera12_btn = QPushButton(self.frame_46)
        self.camera12_btn.setObjectName(u"camera12_btn")
        self.camera12_btn.setEnabled(True)
        self.camera12_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera12_btn.setStyleSheet(u"QPushButton{\n"
"background:Transparent;\n"
"border-color:Transparent;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:Transparent;\n"
"}\n"
"\n"
"")
        self.camera12_btn.setIcon(icon9)
        self.camera12_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_81.addWidget(self.camera12_btn)


        self.verticalLayout_69.addLayout(self.horizontalLayout_81)


        self.verticalLayout_68.addWidget(self.frame_46)

        self.line_11 = QFrame(self.frame_42)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShadow(QFrame.Raised)
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QFrame.HLine)

        self.verticalLayout_68.addWidget(self.line_11)

        self.frame_47 = QFrame(self.frame_42)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(16777215, 95))
        self.frame_47.setStyleSheet(u"border: None")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_47)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(20)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.camera13_btn = QPushButton(self.frame_47)
        self.camera13_btn.setObjectName(u"camera13_btn")
        self.camera13_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera13_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        icon10 = QIcon()
        icon10.addFile(u"images/cambtm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera13_btn.setIcon(icon10)
        self.camera13_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera13_btn)

        self.camera14_btn = QPushButton(self.frame_47)
        self.camera14_btn.setObjectName(u"camera14_btn")
        self.camera14_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera14_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera14_btn.setIcon(icon10)
        self.camera14_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera14_btn)

        self.camera15_btn = QPushButton(self.frame_47)
        self.camera15_btn.setObjectName(u"camera15_btn")
        self.camera15_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera15_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera15_btn.setIcon(icon10)
        self.camera15_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera15_btn)

        self.camera16_btn = QPushButton(self.frame_47)
        self.camera16_btn.setObjectName(u"camera16_btn")
        self.camera16_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera16_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera16_btn.setIcon(icon10)
        self.camera16_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera16_btn)

        self.camera17_btn = QPushButton(self.frame_47)
        self.camera17_btn.setObjectName(u"camera17_btn")
        self.camera17_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera17_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera17_btn.setIcon(icon10)
        self.camera17_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera17_btn)

        self.camera18_btn = QPushButton(self.frame_47)
        self.camera18_btn.setObjectName(u"camera18_btn")
        self.camera18_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera18_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera18_btn.setIcon(icon10)
        self.camera18_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera18_btn)

        self.camera19_btn = QPushButton(self.frame_47)
        self.camera19_btn.setObjectName(u"camera19_btn")
        self.camera19_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera19_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera19_btn.setIcon(icon10)
        self.camera19_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera19_btn)

        self.camera20_btn = QPushButton(self.frame_47)
        self.camera20_btn.setObjectName(u"camera20_btn")
        self.camera20_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera20_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera20_btn.setIcon(icon10)
        self.camera20_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera20_btn)

        self.camera21_btn = QPushButton(self.frame_47)
        self.camera21_btn.setObjectName(u"camera21_btn")
        self.camera21_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera21_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera21_btn.setIcon(icon10)
        self.camera21_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera21_btn)

        self.camera22_btn = QPushButton(self.frame_47)
        self.camera22_btn.setObjectName(u"camera22_btn")
        self.camera22_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera22_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera22_btn.setIcon(icon10)
        self.camera22_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera22_btn)

        self.camera23_btn = QPushButton(self.frame_47)
        self.camera23_btn.setObjectName(u"camera23_btn")
        self.camera23_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera23_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera23_btn.setIcon(icon10)
        self.camera23_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera23_btn)

        self.camera24_btn = QPushButton(self.frame_47)
        self.camera24_btn.setObjectName(u"camera24_btn")
        self.camera24_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera24_btn.setStyleSheet(u"background:Transparent;\n"
"border-color:Transparent")
        self.camera24_btn.setIcon(icon10)
        self.camera24_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_83.addWidget(self.camera24_btn)


        self.verticalLayout_70.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(18)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_101 = QLabel(self.frame_47)
        self.label_101.setObjectName(u"label_101")
        sizePolicy2.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy2)
        self.label_101.setFont(font3)
        self.label_101.setStyleSheet(u"font: 10pt ;")
        self.label_101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_101)

        self.label_191 = QLabel(self.frame_47)
        self.label_191.setObjectName(u"label_191")
        sizePolicy2.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy2)
        self.label_191.setFont(font3)
        self.label_191.setStyleSheet(u"font: 10pt ;")
        self.label_191.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_191)

        self.label_192 = QLabel(self.frame_47)
        self.label_192.setObjectName(u"label_192")
        sizePolicy2.setHeightForWidth(self.label_192.sizePolicy().hasHeightForWidth())
        self.label_192.setSizePolicy(sizePolicy2)
        self.label_192.setFont(font3)
        self.label_192.setStyleSheet(u"font: 10pt ;")
        self.label_192.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_192)

        self.label_193 = QLabel(self.frame_47)
        self.label_193.setObjectName(u"label_193")
        sizePolicy2.setHeightForWidth(self.label_193.sizePolicy().hasHeightForWidth())
        self.label_193.setSizePolicy(sizePolicy2)
        self.label_193.setFont(font3)
        self.label_193.setStyleSheet(u"font: 10pt ;")
        self.label_193.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_193)

        self.label_194 = QLabel(self.frame_47)
        self.label_194.setObjectName(u"label_194")
        sizePolicy2.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy2)
        self.label_194.setFont(font3)
        self.label_194.setStyleSheet(u"font: 10pt ;")
        self.label_194.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_194)

        self.label_195 = QLabel(self.frame_47)
        self.label_195.setObjectName(u"label_195")
        sizePolicy2.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy2)
        self.label_195.setFont(font3)
        self.label_195.setStyleSheet(u"font: 10pt ;")
        self.label_195.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_195)

        self.label_196 = QLabel(self.frame_47)
        self.label_196.setObjectName(u"label_196")
        sizePolicy2.setHeightForWidth(self.label_196.sizePolicy().hasHeightForWidth())
        self.label_196.setSizePolicy(sizePolicy2)
        self.label_196.setFont(font3)
        self.label_196.setStyleSheet(u"font: 10pt ;")
        self.label_196.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_196)

        self.label_279 = QLabel(self.frame_47)
        self.label_279.setObjectName(u"label_279")
        sizePolicy2.setHeightForWidth(self.label_279.sizePolicy().hasHeightForWidth())
        self.label_279.setSizePolicy(sizePolicy2)
        self.label_279.setFont(font3)
        self.label_279.setStyleSheet(u"font: 10pt ;")
        self.label_279.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_279)

        self.label_280 = QLabel(self.frame_47)
        self.label_280.setObjectName(u"label_280")
        sizePolicy2.setHeightForWidth(self.label_280.sizePolicy().hasHeightForWidth())
        self.label_280.setSizePolicy(sizePolicy2)
        self.label_280.setFont(font3)
        self.label_280.setStyleSheet(u"font: 10pt ;")
        self.label_280.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_280)

        self.label_282 = QLabel(self.frame_47)
        self.label_282.setObjectName(u"label_282")
        sizePolicy2.setHeightForWidth(self.label_282.sizePolicy().hasHeightForWidth())
        self.label_282.setSizePolicy(sizePolicy2)
        self.label_282.setFont(font3)
        self.label_282.setStyleSheet(u"font: 10pt ;")
        self.label_282.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_282)

        self.label_283 = QLabel(self.frame_47)
        self.label_283.setObjectName(u"label_283")
        sizePolicy2.setHeightForWidth(self.label_283.sizePolicy().hasHeightForWidth())
        self.label_283.setSizePolicy(sizePolicy2)
        self.label_283.setFont(font3)
        self.label_283.setStyleSheet(u"font: 10pt ;")
        self.label_283.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_283)

        self.label_284 = QLabel(self.frame_47)
        self.label_284.setObjectName(u"label_284")
        sizePolicy2.setHeightForWidth(self.label_284.sizePolicy().hasHeightForWidth())
        self.label_284.setSizePolicy(sizePolicy2)
        self.label_284.setFont(font3)
        self.label_284.setStyleSheet(u"font: 10pt ;")
        self.label_284.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_284)


        self.verticalLayout_70.addLayout(self.horizontalLayout_85)


        self.verticalLayout_68.addWidget(self.frame_47)


        self.horizontalLayout_60.addLayout(self.verticalLayout_68)

        self.frame_48 = QFrame(self.frame_42)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 0))
        self.frame_48.setMaximumSize(QSize(16777215, 16777215))
        self.frame_48.setStyleSheet(u"border: None")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_73 = QVBoxLayout()
        self.verticalLayout_73.setSpacing(4)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.checkBox_top = QCheckBox(self.frame_48)
        self.checkBox_top.setObjectName(u"checkBox_top")
        self.checkBox_top.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.checkBox_top.sizePolicy().hasHeightForWidth())
        self.checkBox_top.setSizePolicy(sizePolicy2)
        self.checkBox_top.setFont(font1)
        self.checkBox_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_top.setStyleSheet(u"")
        self.checkBox_top.setIconSize(QSize(16, 16))

        self.verticalLayout_73.addWidget(self.checkBox_top)

        self.checkBox_bottom = QCheckBox(self.frame_48)
        self.checkBox_bottom.setObjectName(u"checkBox_bottom")
        self.checkBox_bottom.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.checkBox_bottom.sizePolicy().hasHeightForWidth())
        self.checkBox_bottom.setSizePolicy(sizePolicy2)
        self.checkBox_bottom.setFont(font1)
        self.checkBox_bottom.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_73.addWidget(self.checkBox_bottom)


        self.horizontalLayout_91.addLayout(self.verticalLayout_73)

        self.checkBox_all = QCheckBox(self.frame_48)
        self.checkBox_all.setObjectName(u"checkBox_all")
        self.checkBox_all.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.checkBox_all.sizePolicy().hasHeightForWidth())
        self.checkBox_all.setSizePolicy(sizePolicy2)
        self.checkBox_all.setFont(font1)
        self.checkBox_all.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_91.addWidget(self.checkBox_all)


        self.horizontalLayout_60.addWidget(self.frame_48)


        self.horizontalLayout_44.addWidget(self.frame_42)


        self.verticalLayout_89.addWidget(self.frame_73)

        self.frame_64 = QFrame(self.tab_5)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 42))
        self.frame_64.setMaximumSize(QSize(16777215, 42))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_203 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_64)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(116, 0))
        self.frame_20.setMaximumSize(QSize(116, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_20)
        self.verticalLayout_39.setSpacing(2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.start_capture_btn = QPushButton(self.frame_20)
        self.start_capture_btn.setObjectName(u"start_capture_btn")
        self.start_capture_btn.setEnabled(True)
        self.start_capture_btn.setMinimumSize(QSize(112, 19))
        self.start_capture_btn.setMaximumSize(QSize(120, 19))
        self.start_capture_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_capture_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled {\n"
"    background-color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_39.addWidget(self.start_capture_btn)

        self.stop_capture_btn = QPushButton(self.frame_20)
        self.stop_capture_btn.setObjectName(u"stop_capture_btn")
        self.stop_capture_btn.setEnabled(False)
        self.stop_capture_btn.setMinimumSize(QSize(112, 19))
        self.stop_capture_btn.setMaximumSize(QSize(120, 19))
        self.stop_capture_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_capture_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled {\n"
"    background-color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_39.addWidget(self.stop_capture_btn)


        self.horizontalLayout_203.addWidget(self.frame_20)

        self.checkBox_save_images = QCheckBox(self.frame_64)
        self.checkBox_save_images.setObjectName(u"checkBox_save_images")
        self.checkBox_save_images.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_save_images.setStyleSheet(u"")
        self.checkBox_save_images.setChecked(True)

        self.horizontalLayout_203.addWidget(self.checkBox_save_images)

        self.line_31 = QFrame(self.frame_64)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.VLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_203.addWidget(self.line_31)

        self.scrollArea_2 = QScrollArea(self.frame_64)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(47, 0))
        self.scrollArea_2.setStyleSheet(u"background-color: Transparent;\n"
"border:None;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 488, 30))
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy7)
        self.scrollAreaWidgetContents_3.setMaximumSize(QSize(16777213, 16777215))
        self.horizontalLayout_233 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(5, 0, 6, 0)
        self.label_27 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_233.addWidget(self.label_27)

        self.detect_sensor_check_box = QCheckBox(self.scrollAreaWidgetContents_3)
        self.detect_sensor_check_box.setObjectName(u"detect_sensor_check_box")
        self.detect_sensor_check_box.setEnabled(False)
        self.detect_sensor_check_box.setMinimumSize(QSize(23, 25))
        self.detect_sensor_check_box.setMaximumSize(QSize(21, 25))
        self.detect_sensor_check_box.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 2px solid lightgreen;\n"
"	color : green;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:      red;\n"
"	color : red;\n"
"}")
        self.detect_sensor_check_box.setIconSize(QSize(57, 57))
        self.detect_sensor_check_box.setCheckable(True)

        self.horizontalLayout_233.addWidget(self.detect_sensor_check_box)

        self.line_37 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setMaximumSize(QSize(16777215, 27))
        self.line_37.setFrameShape(QFrame.VLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_233.addWidget(self.line_37)

        self.label_235 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_235.setObjectName(u"label_235")

        self.horizontalLayout_233.addWidget(self.label_235)

        self.start_wind_btn = QPushButton(self.scrollAreaWidgetContents_3)
        self.start_wind_btn.setObjectName(u"start_wind_btn")
        self.start_wind_btn.setEnabled(True)
        self.start_wind_btn.setMinimumSize(QSize(92, 30))
        self.start_wind_btn.setMaximumSize(QSize(92, 30))
        self.start_wind_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_wind_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #03296C;\n"
"    border-style: outset;\n"
"\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color : white;\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color:#cccccc;\n"
"	color:black;	\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"}")

        self.horizontalLayout_233.addWidget(self.start_wind_btn)

        self.line_46 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setMaximumSize(QSize(16777215, 27))
        self.line_46.setFrameShape(QFrame.VLine)
        self.line_46.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_233.addWidget(self.line_46)

        self.label_236 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_236.setObjectName(u"label_236")

        self.horizontalLayout_233.addWidget(self.label_236)

        self.label_up_temperature = QLabel(self.scrollAreaWidgetContents_3)
        self.label_up_temperature.setObjectName(u"label_up_temperature")

        self.horizontalLayout_233.addWidget(self.label_up_temperature)

        self.label_down_temperature = QLabel(self.scrollAreaWidgetContents_3)
        self.label_down_temperature.setObjectName(u"label_down_temperature")

        self.horizontalLayout_233.addWidget(self.label_down_temperature)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_233.addItem(self.horizontalSpacer_30)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_203.addWidget(self.scrollArea_2)

        self.line_50 = QFrame(self.frame_64)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.VLine)
        self.line_50.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_203.addWidget(self.line_50)

        self.label_237 = QLabel(self.frame_64)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_203.addWidget(self.label_237)

        self.plc_warnings = QLabel(self.frame_64)
        self.plc_warnings.setObjectName(u"plc_warnings")

        self.horizontalLayout_203.addWidget(self.plc_warnings)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_203.addItem(self.horizontalSpacer_17)


        self.verticalLayout_89.addWidget(self.frame_64)

        self.scrollArea_4 = QScrollArea(self.tab_5)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMaximumSize(QSize(16777215, 30))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 692, 18))
        self.horizontalLayout_213 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(9, 0, 0, 0)
        self.label_156 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_213.addWidget(self.label_156)

        self.label_sheet_id = QLabel(self.scrollAreaWidgetContents_5)
        self.label_sheet_id.setObjectName(u"label_sheet_id")

        self.horizontalLayout_213.addWidget(self.label_sheet_id)

        self.line_34 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.VLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_213.addWidget(self.line_34)

        self.label_heat_number_5 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_heat_number_5.setObjectName(u"label_heat_number_5")

        self.horizontalLayout_213.addWidget(self.label_heat_number_5)

        self.label_heat_number = QLabel(self.scrollAreaWidgetContents_5)
        self.label_heat_number.setObjectName(u"label_heat_number")

        self.horizontalLayout_213.addWidget(self.label_heat_number)

        self.line_51 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.VLine)
        self.line_51.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_213.addWidget(self.line_51)

        self.label_159 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_159.setObjectName(u"label_159")

        self.horizontalLayout_213.addWidget(self.label_159)

        self.label_ps_number = QLabel(self.scrollAreaWidgetContents_5)
        self.label_ps_number.setObjectName(u"label_ps_number")

        self.horizontalLayout_213.addWidget(self.label_ps_number)

        self.line_56 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.VLine)
        self.line_56.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_213.addWidget(self.line_56)

        self.label_132 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_213.addWidget(self.label_132)

        self.label_pdl_number = QLabel(self.scrollAreaWidgetContents_5)
        self.label_pdl_number.setObjectName(u"label_pdl_number")

        self.horizontalLayout_213.addWidget(self.label_pdl_number)

        self.line_57 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.VLine)
        self.line_57.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_213.addWidget(self.line_57)

        self.label_223 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_223.setObjectName(u"label_223")

        self.horizontalLayout_213.addWidget(self.label_223)

        self.label_length = QLabel(self.scrollAreaWidgetContents_5)
        self.label_length.setObjectName(u"label_length")

        self.horizontalLayout_213.addWidget(self.label_length)

        self.line_63 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.VLine)
        self.line_63.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_213.addWidget(self.line_63)

        self.label_227 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_227.setObjectName(u"label_227")

        self.horizontalLayout_213.addWidget(self.label_227)

        self.label_width = QLabel(self.scrollAreaWidgetContents_5)
        self.label_width.setObjectName(u"label_width")

        self.horizontalLayout_213.addWidget(self.label_width)

        self.line_64 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.VLine)
        self.line_64.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_213.addWidget(self.line_64)

        self.label_225 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_225.setObjectName(u"label_225")

        self.horizontalLayout_213.addWidget(self.label_225)

        self.label_thickness = QLabel(self.scrollAreaWidgetContents_5)
        self.label_thickness.setObjectName(u"label_thickness")

        self.horizontalLayout_213.addWidget(self.label_thickness)

        self.sheet_label = QLabel(self.scrollAreaWidgetContents_5)
        self.sheet_label.setObjectName(u"sheet_label")

        self.horizontalLayout_213.addWidget(self.sheet_label)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_89.addWidget(self.scrollArea_4)

        self.live_tabWidget = QTabWidget(self.tab_5)
        self.live_tabWidget.setObjectName(u"live_tabWidget")
        self.live_tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_101 = QVBoxLayout(self.tab_3)
        self.verticalLayout_101.setSpacing(2)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(4, 7, 4, 4)
        self.frame_77 = QFrame(self.tab_3)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMaximumSize(QSize(16777214, 24))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_166 = QLabel(self.frame_77)
        self.label_166.setObjectName(u"label_166")
        sizePolicy.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy)
        self.label_166.setMinimumSize(QSize(0, 0))
        self.label_166.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_124.addWidget(self.label_166)

        self.comboBox_connected_cams = QComboBox(self.frame_77)
        self.comboBox_connected_cams.setObjectName(u"comboBox_connected_cams")
        self.comboBox_connected_cams.setMaximumSize(QSize(73, 16777215))
        self.comboBox_connected_cams.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(200,200,200);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 1px solid rgb(64, 71, 188);\n"
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
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	selection-background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_124.addWidget(self.comboBox_connected_cams)


        self.verticalLayout_101.addWidget(self.frame_77, 0, Qt.AlignLeft)

        self.live = QLabel(self.tab_3)
        self.live.setObjectName(u"live")
        self.live.setFrameShape(QFrame.Box)
        self.live.setFrameShadow(QFrame.Plain)
        self.live.setScaledContents(True)
        self.live.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.live.setMargin(0)
        self.live.setIndent(0)

        self.verticalLayout_101.addWidget(self.live)

        self.live_tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_91 = QVBoxLayout(self.tab_4)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_62 = QFrame(self.tab_4)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 127))
        self.frame_62.setFrameShape(QFrame.Box)
        self.frame_62.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_225 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_225.setSpacing(0)
        self.horizontalLayout_225.setObjectName(u"horizontalLayout_225")
        self.horizontalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.tlive1 = QLabel(self.frame_62)
        self.tlive1.setObjectName(u"tlive1")
        self.tlive1.setMinimumSize(QSize(0, 0))
        self.tlive1.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive1)

        self.tlive2 = QLabel(self.frame_62)
        self.tlive2.setObjectName(u"tlive2")
        self.tlive2.setMinimumSize(QSize(0, 0))
        self.tlive2.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive2)

        self.tlive3 = QLabel(self.frame_62)
        self.tlive3.setObjectName(u"tlive3")
        self.tlive3.setMinimumSize(QSize(0, 0))
        self.tlive3.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive3)

        self.tlive4 = QLabel(self.frame_62)
        self.tlive4.setObjectName(u"tlive4")
        self.tlive4.setMinimumSize(QSize(0, 0))
        self.tlive4.setScaledContents(True)

        self.horizontalLayout_225.addWidget(self.tlive4)


        self.verticalLayout_91.addWidget(self.frame_62)

        self.horizontalLayout_205 = QHBoxLayout()
        self.horizontalLayout_205.setSpacing(10)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(10, -1, 10, -1)
        self.label_30 = QLabel(self.tab_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 20))
        self.label_30.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_30)

        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_3)

        self.label_21 = QLabel(self.tab_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_21)

        self.label_23 = QLabel(self.tab_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 20))
        self.label_23.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_205.addWidget(self.label_23)


        self.verticalLayout_91.addLayout(self.horizontalLayout_205)

        self.frame_67 = QFrame(self.tab_4)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 127))
        self.frame_67.setFrameShape(QFrame.Box)
        self.frame_67.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_226 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_226.setSpacing(0)
        self.horizontalLayout_226.setObjectName(u"horizontalLayout_226")
        self.horizontalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.tlive5 = QLabel(self.frame_67)
        self.tlive5.setObjectName(u"tlive5")
        self.tlive5.setMinimumSize(QSize(0, 0))
        self.tlive5.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive5)

        self.tlive6 = QLabel(self.frame_67)
        self.tlive6.setObjectName(u"tlive6")
        self.tlive6.setMinimumSize(QSize(0, 0))
        self.tlive6.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive6)

        self.tlive7 = QLabel(self.frame_67)
        self.tlive7.setObjectName(u"tlive7")
        self.tlive7.setMinimumSize(QSize(0, 0))
        self.tlive7.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive7)

        self.tlive8 = QLabel(self.frame_67)
        self.tlive8.setObjectName(u"tlive8")
        self.tlive8.setMinimumSize(QSize(0, 0))
        self.tlive8.setScaledContents(True)

        self.horizontalLayout_226.addWidget(self.tlive8)


        self.verticalLayout_91.addWidget(self.frame_67)

        self.horizontalLayout_206 = QHBoxLayout()
        self.horizontalLayout_206.setSpacing(10)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(10, -1, 10, -1)
        self.label_41 = QLabel(self.tab_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 20))
        self.label_41.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.label_41)

        self.label_42 = QLabel(self.tab_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_206.addWidget(self.label_42)

        self.label_53 = QLabel(self.tab_4)
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

        self.label_54 = QLabel(self.tab_4)
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


        self.verticalLayout_91.addLayout(self.horizontalLayout_206)

        self.frame_69 = QFrame(self.tab_4)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 127))
        self.frame_69.setFrameShape(QFrame.Box)
        self.frame_69.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_193 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_193.setSpacing(0)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.tlive9 = QLabel(self.frame_69)
        self.tlive9.setObjectName(u"tlive9")
        self.tlive9.setMinimumSize(QSize(0, 0))
        self.tlive9.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive9)

        self.tlive10 = QLabel(self.frame_69)
        self.tlive10.setObjectName(u"tlive10")
        self.tlive10.setMinimumSize(QSize(0, 0))
        self.tlive10.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive10)

        self.tlive11 = QLabel(self.frame_69)
        self.tlive11.setObjectName(u"tlive11")
        self.tlive11.setMinimumSize(QSize(0, 0))
        self.tlive11.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive11)

        self.tlive12 = QLabel(self.frame_69)
        self.tlive12.setObjectName(u"tlive12")
        self.tlive12.setMinimumSize(QSize(0, 0))
        self.tlive12.setScaledContents(True)

        self.horizontalLayout_193.addWidget(self.tlive12)


        self.verticalLayout_91.addWidget(self.frame_69)

        self.horizontalLayout_207 = QHBoxLayout()
        self.horizontalLayout_207.setSpacing(10)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_207.setContentsMargins(10, -1, 10, -1)
        self.label_55 = QLabel(self.tab_4)
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

        self.label_56 = QLabel(self.tab_4)
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

        self.label_57 = QLabel(self.tab_4)
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

        self.label_58 = QLabel(self.tab_4)
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


        self.verticalLayout_91.addLayout(self.horizontalLayout_207)

        self.live_tabWidget.addTab(self.tab_4, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_94 = QVBoxLayout(self.tab_8)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.frame_78 = QFrame(self.tab_8)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 126))
        self.frame_78.setFrameShape(QFrame.Box)
        self.frame_78.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_200 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_200.setSpacing(0)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.blive13 = QLabel(self.frame_78)
        self.blive13.setObjectName(u"blive13")
        self.blive13.setMinimumSize(QSize(0, 0))
        self.blive13.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive13)

        self.blive14 = QLabel(self.frame_78)
        self.blive14.setObjectName(u"blive14")
        self.blive14.setMinimumSize(QSize(0, 0))
        self.blive14.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive14)

        self.blive15 = QLabel(self.frame_78)
        self.blive15.setObjectName(u"blive15")
        self.blive15.setMinimumSize(QSize(0, 0))
        self.blive15.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive15)

        self.blive16 = QLabel(self.frame_78)
        self.blive16.setObjectName(u"blive16")
        self.blive16.setMinimumSize(QSize(0, 0))
        self.blive16.setScaledContents(True)

        self.horizontalLayout_200.addWidget(self.blive16)


        self.verticalLayout_94.addWidget(self.frame_78)

        self.horizontalLayout_209 = QHBoxLayout()
        self.horizontalLayout_209.setSpacing(10)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(10, -1, 10, -1)
        self.label_64 = QLabel(self.tab_8)
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

        self.label_65 = QLabel(self.tab_8)
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

        self.label_66 = QLabel(self.tab_8)
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

        self.label_70 = QLabel(self.tab_8)
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


        self.verticalLayout_94.addLayout(self.horizontalLayout_209)

        self.frame_101 = QFrame(self.tab_8)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(0, 126))
        self.frame_101.setFrameShape(QFrame.Box)
        self.frame_101.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_202 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_202.setSpacing(0)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.blive17 = QLabel(self.frame_101)
        self.blive17.setObjectName(u"blive17")
        self.blive17.setMinimumSize(QSize(0, 0))
        self.blive17.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive17)

        self.blive18 = QLabel(self.frame_101)
        self.blive18.setObjectName(u"blive18")
        self.blive18.setMinimumSize(QSize(0, 0))
        self.blive18.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive18)

        self.blive19 = QLabel(self.frame_101)
        self.blive19.setObjectName(u"blive19")
        self.blive19.setMinimumSize(QSize(0, 0))
        self.blive19.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive19)

        self.blive20 = QLabel(self.frame_101)
        self.blive20.setObjectName(u"blive20")
        self.blive20.setMinimumSize(QSize(0, 0))
        self.blive20.setScaledContents(True)

        self.horizontalLayout_202.addWidget(self.blive20)


        self.verticalLayout_94.addWidget(self.frame_101)

        self.horizontalLayout_211 = QHBoxLayout()
        self.horizontalLayout_211.setSpacing(10)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(10, -1, 10, -1)
        self.label_85 = QLabel(self.tab_8)
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

        self.label_126 = QLabel(self.tab_8)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMaximumSize(QSize(16777215, 20))
        self.label_126.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.label_126)

        self.label_127 = QLabel(self.tab_8)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMaximumSize(QSize(16777215, 20))
        self.label_127.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(221, 221, 221);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.label_127)

        self.label_128 = QLabel(self.tab_8)
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


        self.verticalLayout_94.addLayout(self.horizontalLayout_211)

        self.frame_102 = QFrame(self.tab_8)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 126))
        self.frame_102.setFrameShape(QFrame.Box)
        self.frame_102.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_201 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_201.setSpacing(0)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.blive21 = QLabel(self.frame_102)
        self.blive21.setObjectName(u"blive21")
        self.blive21.setMinimumSize(QSize(0, 0))
        self.blive21.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive21)

        self.blive22 = QLabel(self.frame_102)
        self.blive22.setObjectName(u"blive22")
        self.blive22.setMinimumSize(QSize(0, 0))
        self.blive22.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive22)

        self.blive23 = QLabel(self.frame_102)
        self.blive23.setObjectName(u"blive23")
        self.blive23.setMinimumSize(QSize(0, 0))
        self.blive23.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive23)

        self.blive24 = QLabel(self.frame_102)
        self.blive24.setObjectName(u"blive24")
        self.blive24.setMinimumSize(QSize(0, 0))
        self.blive24.setScaledContents(True)

        self.horizontalLayout_201.addWidget(self.blive24)


        self.verticalLayout_94.addWidget(self.frame_102)

        self.horizontalLayout_210 = QHBoxLayout()
        self.horizontalLayout_210.setSpacing(10)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(10, -1, 10, -1)
        self.label_75 = QLabel(self.tab_8)
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

        self.label_76 = QLabel(self.tab_8)
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

        self.label_77 = QLabel(self.tab_8)
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

        self.label_84 = QLabel(self.tab_8)
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


        self.verticalLayout_94.addLayout(self.horizontalLayout_210)

        self.live_tabWidget.addTab(self.tab_8, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tab_7.setStyleSheet(u"")
        self.verticalLayout_90 = QVBoxLayout(self.tab_7)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_103 = QFrame(self.tab_7)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 84))
        self.frame_103.setFrameShape(QFrame.Box)
        self.frame_103.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.live1 = QLabel(self.frame_103)
        self.live1.setObjectName(u"live1")
        self.live1.setMinimumSize(QSize(0, 0))
        self.live1.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live1)

        self.live2 = QLabel(self.frame_103)
        self.live2.setObjectName(u"live2")
        self.live2.setMinimumSize(QSize(0, 0))
        self.live2.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live2)

        self.live3 = QLabel(self.frame_103)
        self.live3.setObjectName(u"live3")
        self.live3.setMinimumSize(QSize(0, 0))
        self.live3.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live3)

        self.live4 = QLabel(self.frame_103)
        self.live4.setObjectName(u"live4")
        self.live4.setMinimumSize(QSize(0, 0))
        self.live4.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live4)

        self.live5 = QLabel(self.frame_103)
        self.live5.setObjectName(u"live5")
        self.live5.setMinimumSize(QSize(0, 0))
        self.live5.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live5)

        self.live6 = QLabel(self.frame_103)
        self.live6.setObjectName(u"live6")
        self.live6.setMinimumSize(QSize(0, 0))
        self.live6.setScaledContents(True)

        self.horizontalLayout_148.addWidget(self.live6)


        self.verticalLayout_90.addWidget(self.frame_103)

        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setSpacing(10)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(5, -1, 5, -1)
        self.label_59 = QLabel(self.tab_7)
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

        self.label_60 = QLabel(self.tab_7)
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

        self.label_62 = QLabel(self.tab_7)
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

        self.label_63 = QLabel(self.tab_7)
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

        self.label_184 = QLabel(self.tab_7)
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

        self.label_198 = QLabel(self.tab_7)
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


        self.verticalLayout_90.addLayout(self.horizontalLayout_208)

        self.frame_104 = QFrame(self.tab_7)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(0, 84))
        self.frame_104.setFrameShape(QFrame.Box)
        self.frame_104.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_149 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_149.setSpacing(0)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.live7 = QLabel(self.frame_104)
        self.live7.setObjectName(u"live7")
        self.live7.setMinimumSize(QSize(0, 0))
        self.live7.setScaledContents(True)

        self.horizontalLayout_149.addWidget(self.live7)

        self.live8 = QLabel(self.frame_104)
        self.live8.setObjectName(u"live8")
        self.live8.setMinimumSize(QSize(0, 0))
        self.live8.setScaledContents(True)

        self.horizontalLayout_149.addWidget(self.live8)

        self.live9 = QLabel(self.frame_104)
        self.live9.setObjectName(u"live9")
        self.live9.setMinimumSize(QSize(0, 0))
        self.live9.setScaledContents(True)

        self.horizontalLayout_149.addWidget(self.live9)

        self.live10 = QLabel(self.frame_104)
        self.live10.setObjectName(u"live10")
        self.live10.setMinimumSize(QSize(0, 0))
        self.live10.setScaledContents(True)

        self.horizontalLayout_149.addWidget(self.live10)

        self.live11 = QLabel(self.frame_104)
        self.live11.setObjectName(u"live11")
        self.live11.setMinimumSize(QSize(0, 0))
        self.live11.setScaledContents(True)

        self.horizontalLayout_149.addWidget(self.live11)

        self.live12 = QLabel(self.frame_104)
        self.live12.setObjectName(u"live12")
        self.live12.setMinimumSize(QSize(0, 0))
        self.live12.setScaledContents(True)

        self.horizontalLayout_149.addWidget(self.live12)


        self.verticalLayout_90.addWidget(self.frame_104)

        self.horizontalLayout_214 = QHBoxLayout()
        self.horizontalLayout_214.setSpacing(10)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(5, -1, 5, -1)
        self.label_199 = QLabel(self.tab_7)
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

        self.horizontalLayout_214.addWidget(self.label_199)

        self.label_200 = QLabel(self.tab_7)
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

        self.horizontalLayout_214.addWidget(self.label_200)

        self.label_201 = QLabel(self.tab_7)
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

        self.horizontalLayout_214.addWidget(self.label_201)

        self.label_202 = QLabel(self.tab_7)
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

        self.horizontalLayout_214.addWidget(self.label_202)

        self.label_203 = QLabel(self.tab_7)
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

        self.horizontalLayout_214.addWidget(self.label_203)

        self.label_204 = QLabel(self.tab_7)
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

        self.horizontalLayout_214.addWidget(self.label_204)


        self.verticalLayout_90.addLayout(self.horizontalLayout_214)

        self.frame_105 = QFrame(self.tab_7)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 84))
        self.frame_105.setFrameShape(QFrame.Box)
        self.frame_105.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_150 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_150.setSpacing(0)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.live13 = QLabel(self.frame_105)
        self.live13.setObjectName(u"live13")
        self.live13.setMinimumSize(QSize(0, 0))
        self.live13.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live13)

        self.live14 = QLabel(self.frame_105)
        self.live14.setObjectName(u"live14")
        self.live14.setMinimumSize(QSize(0, 0))
        self.live14.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live14)

        self.live15 = QLabel(self.frame_105)
        self.live15.setObjectName(u"live15")
        self.live15.setMinimumSize(QSize(0, 0))
        self.live15.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live15)

        self.live16 = QLabel(self.frame_105)
        self.live16.setObjectName(u"live16")
        self.live16.setMinimumSize(QSize(0, 0))
        self.live16.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live16)

        self.live17 = QLabel(self.frame_105)
        self.live17.setObjectName(u"live17")
        self.live17.setMinimumSize(QSize(0, 0))
        self.live17.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live17)

        self.live18 = QLabel(self.frame_105)
        self.live18.setObjectName(u"live18")
        self.live18.setMinimumSize(QSize(0, 0))
        self.live18.setScaledContents(True)

        self.horizontalLayout_150.addWidget(self.live18)


        self.verticalLayout_90.addWidget(self.frame_105)

        self.horizontalLayout_215 = QHBoxLayout()
        self.horizontalLayout_215.setSpacing(10)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(5, -1, 5, -1)
        self.label_205 = QLabel(self.tab_7)
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

        self.label_206 = QLabel(self.tab_7)
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

        self.label_207 = QLabel(self.tab_7)
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

        self.label_208 = QLabel(self.tab_7)
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

        self.label_209 = QLabel(self.tab_7)
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

        self.label_210 = QLabel(self.tab_7)
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


        self.verticalLayout_90.addLayout(self.horizontalLayout_215)

        self.frame_106 = QFrame(self.tab_7)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 84))
        self.frame_106.setFrameShape(QFrame.Box)
        self.frame_106.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_168.setSpacing(0)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.live19 = QLabel(self.frame_106)
        self.live19.setObjectName(u"live19")
        self.live19.setMinimumSize(QSize(0, 0))
        self.live19.setScaledContents(True)

        self.horizontalLayout_168.addWidget(self.live19)

        self.live20 = QLabel(self.frame_106)
        self.live20.setObjectName(u"live20")
        self.live20.setMinimumSize(QSize(0, 0))
        self.live20.setScaledContents(True)

        self.horizontalLayout_168.addWidget(self.live20)

        self.live21 = QLabel(self.frame_106)
        self.live21.setObjectName(u"live21")
        self.live21.setMinimumSize(QSize(0, 0))
        self.live21.setScaledContents(True)

        self.horizontalLayout_168.addWidget(self.live21)

        self.live22 = QLabel(self.frame_106)
        self.live22.setObjectName(u"live22")
        self.live22.setMinimumSize(QSize(0, 0))
        self.live22.setScaledContents(True)

        self.horizontalLayout_168.addWidget(self.live22)

        self.live23 = QLabel(self.frame_106)
        self.live23.setObjectName(u"live23")
        self.live23.setMinimumSize(QSize(0, 0))
        self.live23.setScaledContents(True)

        self.horizontalLayout_168.addWidget(self.live23)

        self.live24 = QLabel(self.frame_106)
        self.live24.setObjectName(u"live24")
        self.live24.setMinimumSize(QSize(0, 0))
        self.live24.setScaledContents(True)

        self.horizontalLayout_168.addWidget(self.live24)


        self.verticalLayout_90.addWidget(self.frame_106)

        self.horizontalLayout_227 = QHBoxLayout()
        self.horizontalLayout_227.setSpacing(10)
        self.horizontalLayout_227.setObjectName(u"horizontalLayout_227")
        self.horizontalLayout_227.setContentsMargins(5, -1, 5, -1)
        self.label_212 = QLabel(self.tab_7)
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

        self.horizontalLayout_227.addWidget(self.label_212)

        self.label_213 = QLabel(self.tab_7)
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

        self.horizontalLayout_227.addWidget(self.label_213)

        self.label_214 = QLabel(self.tab_7)
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

        self.horizontalLayout_227.addWidget(self.label_214)

        self.label_215 = QLabel(self.tab_7)
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

        self.horizontalLayout_227.addWidget(self.label_215)

        self.label_216 = QLabel(self.tab_7)
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

        self.horizontalLayout_227.addWidget(self.label_216)

        self.label_217 = QLabel(self.tab_7)
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

        self.horizontalLayout_227.addWidget(self.label_217)


        self.verticalLayout_90.addLayout(self.horizontalLayout_227)

        self.live_tabWidget.addTab(self.tab_7, "")

        self.verticalLayout_89.addWidget(self.live_tabWidget)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setMinimumSize(QSize(0, 0))
        self.verticalLayout_84 = QVBoxLayout(self.tab_6)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(1, 1, 1, 1)
        self.frame_44 = QFrame(self.tab_6)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_44)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_59 = QFrame(self.frame_44)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(400, 0))
        self.frame_59.setMaximumSize(QSize(16777215, 45))
        self.frame_59.setStyleSheet(u"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(3, 3, 3, 3)
        self.load_coil_btn = QPushButton(self.frame_59)
        self.load_coil_btn.setObjectName(u"load_coil_btn")
        self.load_coil_btn.setMinimumSize(QSize(100, 25))
        self.load_coil_btn.setMaximumSize(QSize(130, 30))
        self.load_coil_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_coil_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled {\n"
"    background-color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_89.addWidget(self.load_coil_btn)

        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.next_coil_btn = QPushButton(self.frame_59)
        self.next_coil_btn.setObjectName(u"next_coil_btn")
        self.next_coil_btn.setMinimumSize(QSize(17, 17))
        self.next_coil_btn.setMaximumSize(QSize(17, 16777215))
        self.next_coil_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_coil_btn.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"border-radius: 8px;")
        icon11 = QIcon()
        icon11.addFile(u"images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_coil_btn.setIcon(icon11)
        self.next_coil_btn.setIconSize(QSize(13, 13))

        self.verticalLayout_67.addWidget(self.next_coil_btn)

        self.prev_coil_btn = QPushButton(self.frame_59)
        self.prev_coil_btn.setObjectName(u"prev_coil_btn")
        self.prev_coil_btn.setMinimumSize(QSize(17, 17))
        self.prev_coil_btn.setMaximumSize(QSize(17, 16777215))
        self.prev_coil_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_coil_btn.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"border-radius: 8px;")
        icon12 = QIcon()
        icon12.addFile(u"images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_coil_btn.setIcon(icon12)
        self.prev_coil_btn.setIconSize(QSize(13, 13))

        self.verticalLayout_67.addWidget(self.prev_coil_btn)


        self.horizontalLayout_89.addLayout(self.verticalLayout_67)

        self.scrollArea_5 = QScrollArea(self.frame_59)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMaximumSize(QSize(16777215, 40))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 692, 20))
        self.horizontalLayout_228 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_228.setObjectName(u"horizontalLayout_228")
        self.horizontalLayout_228.setContentsMargins(9, 0, 0, 0)
        self.label_226 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_226.setObjectName(u"label_226")
        sizePolicy.setHeightForWidth(self.label_226.sizePolicy().hasHeightForWidth())
        self.label_226.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_226)

        self.label_sheet_id_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_sheet_id_2.setObjectName(u"label_sheet_id_2")

        self.horizontalLayout_228.addWidget(self.label_sheet_id_2)

        self.line_65 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.VLine)
        self.line_65.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_228.addWidget(self.line_65)

        self.label_heat_number_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_heat_number_3.setObjectName(u"label_heat_number_3")
        sizePolicy.setHeightForWidth(self.label_heat_number_3.sizePolicy().hasHeightForWidth())
        self.label_heat_number_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_heat_number_3)

        self.label_heat_number_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_heat_number_2.setObjectName(u"label_heat_number_2")

        self.horizontalLayout_228.addWidget(self.label_heat_number_2)

        self.line_66 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.VLine)
        self.line_66.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_228.addWidget(self.line_66)

        self.label_228 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_228.setObjectName(u"label_228")
        sizePolicy.setHeightForWidth(self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_228)

        self.label_ps_number_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_ps_number_2.setObjectName(u"label_ps_number_2")

        self.horizontalLayout_228.addWidget(self.label_ps_number_2)

        self.line_67 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setFrameShape(QFrame.VLine)
        self.line_67.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_228.addWidget(self.line_67)

        self.label_229 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_229.setObjectName(u"label_229")
        sizePolicy.setHeightForWidth(self.label_229.sizePolicy().hasHeightForWidth())
        self.label_229.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_229)

        self.label_pdl_number_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_pdl_number_2.setObjectName(u"label_pdl_number_2")

        self.horizontalLayout_228.addWidget(self.label_pdl_number_2)

        self.line_68 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setFrameShape(QFrame.VLine)
        self.line_68.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_228.addWidget(self.line_68)

        self.label_230 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_230.setObjectName(u"label_230")
        sizePolicy.setHeightForWidth(self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_230)

        self.label_length_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_length_2.setObjectName(u"label_length_2")

        self.horizontalLayout_228.addWidget(self.label_length_2)

        self.line_69 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setFrameShape(QFrame.VLine)
        self.line_69.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_228.addWidget(self.line_69)

        self.label_231 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_231.setObjectName(u"label_231")
        sizePolicy.setHeightForWidth(self.label_231.sizePolicy().hasHeightForWidth())
        self.label_231.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_231)

        self.label_width_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_width_2.setObjectName(u"label_width_2")

        self.horizontalLayout_228.addWidget(self.label_width_2)

        self.line_70 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.VLine)
        self.line_70.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_228.addWidget(self.line_70)

        self.label_232 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_232.setObjectName(u"label_232")
        sizePolicy.setHeightForWidth(self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy)

        self.horizontalLayout_228.addWidget(self.label_232)

        self.label_thickness_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_thickness_2.setObjectName(u"label_thickness_2")

        self.horizontalLayout_228.addWidget(self.label_thickness_2)

        self.sheet_label_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.sheet_label_2.setObjectName(u"sheet_label_2")

        self.horizontalLayout_228.addWidget(self.sheet_label_2)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_89.addWidget(self.scrollArea_5)


        self.verticalLayout_35.addWidget(self.frame_59)

        self.frame_117 = QFrame(self.frame_44)
        self.frame_117.setObjectName(u"frame_117")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_117.sizePolicy().hasHeightForWidth())
        self.frame_117.setSizePolicy(sizePolicy8)
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_344 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_344.setSpacing(15)
        self.horizontalLayout_344.setObjectName(u"horizontalLayout_344")
        self.horizontalLayout_344.setContentsMargins(-1, 3, -1, 3)
        self.checkBox_suggested_defects = QCheckBox(self.frame_117)
        self.checkBox_suggested_defects.setObjectName(u"checkBox_suggested_defects")
        self.checkBox_suggested_defects.setEnabled(False)
        self.checkBox_suggested_defects.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_suggested_defects.setStyleSheet(u"")
        self.checkBox_suggested_defects.setCheckable(True)
        self.checkBox_suggested_defects.setChecked(False)

        self.horizontalLayout_344.addWidget(self.checkBox_suggested_defects)

        self.suggested_defects_progressBar = QProgressBar(self.frame_117)
        self.suggested_defects_progressBar.setObjectName(u"suggested_defects_progressBar")
        self.suggested_defects_progressBar.setMaximum(1920)
        self.suggested_defects_progressBar.setValue(0)

        self.horizontalLayout_344.addWidget(self.suggested_defects_progressBar)


        self.verticalLayout_35.addWidget(self.frame_117)

        self.crop_image = QLabel(self.frame_44)
        self.crop_image.setObjectName(u"crop_image")
        self.crop_image.setMinimumSize(QSize(0, 0))
        self.crop_image.setMaximumSize(QSize(16777215, 16777215))
        self.crop_image.setBaseSize(QSize(240, 130))
        self.crop_image.setFrameShape(QFrame.Box)
        self.crop_image.setFrameShadow(QFrame.Plain)
        self.crop_image.setPixmap(QPixmap(u"../../UI/2.jpg"))
        self.crop_image.setScaledContents(True)
        self.crop_image.setWordWrap(False)
        self.crop_image.setMargin(2)

        self.verticalLayout_35.addWidget(self.crop_image)

        self.frame_15 = QFrame(self.frame_44)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy8.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy8)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_15)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_15)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(580, 30))
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_151 = QHBoxLayout(self.widget)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(3, 2, 3, 2)
        self.label_45 = QLabel(self.widget)
        self.label_45.setObjectName(u"label_45")
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setMinimumSize(QSize(0, 0))
        self.label_45.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"ubuntu"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_45.setFont(font4)
        self.label_45.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_45.setAcceptDrops(False)
        self.label_45.setStyleSheet(u"")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.label_45.setWordWrap(False)
        self.label_45.setOpenExternalLinks(False)

        self.horizontalLayout_151.addWidget(self.label_45)

        self.label_234 = QLabel(self.widget)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setMaximumSize(QSize(19, 30))
        self.label_234.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius:5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")
        self.label_234.setPixmap(QPixmap(u"images/pngaaa.com-4780825 - Copy.png"))
        self.label_234.setScaledContents(True)

        self.horizontalLayout_151.addWidget(self.label_234)

        self.label_221 = QLabel(self.widget)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setMaximumSize(QSize(13, 23))
        self.label_221.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_151.addWidget(self.label_221)

        self.current_pos_y = QLabel(self.widget)
        self.current_pos_y.setObjectName(u"current_pos_y")
        sizePolicy3.setHeightForWidth(self.current_pos_y.sizePolicy().hasHeightForWidth())
        self.current_pos_y.setSizePolicy(sizePolicy3)
        self.current_pos_y.setMinimumSize(QSize(0, 0))
        self.current_pos_y.setMaximumSize(QSize(16777215, 16777215))
        self.current_pos_y.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")

        self.horizontalLayout_151.addWidget(self.current_pos_y)

        self.label_222 = QLabel(self.widget)
        self.label_222.setObjectName(u"label_222")
        sizePolicy.setHeightForWidth(self.label_222.sizePolicy().hasHeightForWidth())
        self.label_222.setSizePolicy(sizePolicy)
        self.label_222.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_151.addWidget(self.label_222)

        self.label_233 = QLabel(self.widget)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setMinimumSize(QSize(29, 22))
        self.label_233.setMaximumSize(QSize(29, 22))
        self.label_233.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius:5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")
        self.label_233.setPixmap(QPixmap(u"images/pngaaa.com-4780825.png"))
        self.label_233.setScaledContents(True)

        self.horizontalLayout_151.addWidget(self.label_233)

        self.label_224 = QLabel(self.widget)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setMaximumSize(QSize(13, 23))
        self.label_224.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_151.addWidget(self.label_224)

        self.current_pos_x = QLabel(self.widget)
        self.current_pos_x.setObjectName(u"current_pos_x")
        sizePolicy3.setHeightForWidth(self.current_pos_x.sizePolicy().hasHeightForWidth())
        self.current_pos_x.setSizePolicy(sizePolicy3)
        self.current_pos_x.setMinimumSize(QSize(0, 0))
        self.current_pos_x.setMaximumSize(QSize(16777215, 16777215))
        self.current_pos_x.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")

        self.horizontalLayout_151.addWidget(self.current_pos_x)

        self.label_47 = QLabel(self.widget)
        self.label_47.setObjectName(u"label_47")
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        self.label_47.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_151.addWidget(self.label_47)

        self.line_17 = QFrame(self.widget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_151.addWidget(self.line_17)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_14)

        self.warning_data_page = QLabel(self.widget)
        self.warning_data_page.setObjectName(u"warning_data_page")
        self.warning_data_page.setMinimumSize(QSize(200, 0))
        self.warning_data_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_151.addWidget(self.warning_data_page)

        self.progressBar_SI = QProgressBar(self.widget)
        self.progressBar_SI.setObjectName(u"progressBar_SI")
        self.progressBar_SI.setMinimumSize(QSize(0, 0))
        self.progressBar_SI.setMaximumSize(QSize(0, 16777215))
        self.progressBar_SI.setValue(0)

        self.horizontalLayout_151.addWidget(self.progressBar_SI)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_15)


        self.verticalLayout_37.addWidget(self.widget)


        self.verticalLayout_35.addWidget(self.frame_15)

        self.frame_tools_technical = QFrame(self.frame_44)
        self.frame_tools_technical.setObjectName(u"frame_tools_technical")
        sizePolicy4.setHeightForWidth(self.frame_tools_technical.sizePolicy().hasHeightForWidth())
        self.frame_tools_technical.setSizePolicy(sizePolicy4)
        self.frame_tools_technical.setMinimumSize(QSize(0, 230))
        self.frame_tools_technical.setMaximumSize(QSize(16777215, 230))
        self.frame_tools_technical.setFrameShape(QFrame.Panel)
        self.frame_tools_technical.setFrameShadow(QFrame.Raised)
        self.frame_tools_technical.setLineWidth(2)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_tools_technical)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(3, 3, 3, 3)
        self.frame_25 = QFrame(self.frame_tools_technical)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_25)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 3, -1, 3)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.add_btn_SI = QPushButton(self.frame_25)
        self.add_btn_SI.setObjectName(u"add_btn_SI")
        self.add_btn_SI.setEnabled(True)
        self.add_btn_SI.setMinimumSize(QSize(30, 30))
        self.add_btn_SI.setMaximumSize(QSize(30, 30))
        self.add_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_btn_SI.setStyleSheet(u"background-color: None;\n"
"border: None")
        icon13 = QIcon()
        icon13.addFile(u"images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn_SI.setIcon(icon13)
        self.add_btn_SI.setIconSize(QSize(26, 26))

        self.horizontalLayout_22.addWidget(self.add_btn_SI)

        self.label_2 = QLabel(self.frame_25)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(72, 24))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font4)
        self.label_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet(u" background-color:rgb(70,70,70);\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)

        self.horizontalLayout_22.addWidget(self.label_2)

        self.remove_btn_SI = QPushButton(self.frame_25)
        self.remove_btn_SI.setObjectName(u"remove_btn_SI")
        self.remove_btn_SI.setMinimumSize(QSize(30, 30))
        self.remove_btn_SI.setMaximumSize(QSize(30, 30))
        self.remove_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_btn_SI.setStyleSheet(u"background-color: None;\n"
"border: None")
        icon14 = QIcon()
        icon14.addFile(u"images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_btn_SI.setIcon(icon14)
        self.remove_btn_SI.setIconSize(QSize(26, 26))

        self.horizontalLayout_22.addWidget(self.remove_btn_SI)


        self.verticalLayout_21.addLayout(self.horizontalLayout_22)

        self.checkBox_select = QCheckBox(self.frame_25)
        self.checkBox_select.setObjectName(u"checkBox_select")
        self.checkBox_select.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.checkBox_select)

        self.listWidget_append_img_list = QTableWidget(self.frame_25)
        if (self.listWidget_append_img_list.columnCount() < 1):
            self.listWidget_append_img_list.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.listWidget_append_img_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.listWidget_append_img_list.setObjectName(u"listWidget_append_img_list")
        self.listWidget_append_img_list.setStyleSheet(u"")
        self.listWidget_append_img_list.horizontalHeader().setVisible(False)
        self.listWidget_append_img_list.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_21.addWidget(self.listWidget_append_img_list)

        self.label_btn_SI = QPushButton(self.frame_25)
        self.label_btn_SI.setObjectName(u"label_btn_SI")
        self.label_btn_SI.setEnabled(True)
        self.label_btn_SI.setMinimumSize(QSize(0, 28))
        self.label_btn_SI.setMaximumSize(QSize(16777215, 16777215))
        self.label_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_btn_SI.setStyleSheet(u" background-color:rgb(70,70,70);\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:center;\n"
"color:white;")

        self.verticalLayout_21.addWidget(self.label_btn_SI)


        self.horizontalLayout_39.addWidget(self.frame_25)

        self.frame_31 = QFrame(self.frame_tools_technical)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(250, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_31)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.checkBox_all_imgs_SI = QCheckBox(self.frame_31)
        self.checkBox_all_imgs_SI.setObjectName(u"checkBox_all_imgs_SI")
        self.checkBox_all_imgs_SI.setEnabled(False)
        self.checkBox_all_imgs_SI.setStyleSheet(u"")

        self.verticalLayout_50.addWidget(self.checkBox_all_imgs_SI)

        self.horizontalLayout_212 = QHBoxLayout()
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.label_48 = QLabel(self.frame_31)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(120, 0))
        self.label_48.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_212.addWidget(self.label_48)

        self.comboBox_side_SI = QComboBox(self.frame_31)
        self.comboBox_side_SI.setObjectName(u"comboBox_side_SI")
        self.comboBox_side_SI.setEnabled(True)
        self.comboBox_side_SI.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
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
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox_side_SI.setMaxVisibleItems(20)

        self.horizontalLayout_212.addWidget(self.comboBox_side_SI)


        self.verticalLayout_50.addLayout(self.horizontalLayout_212)

        self.horizontalLayout_294 = QHBoxLayout()
        self.horizontalLayout_294.setObjectName(u"horizontalLayout_294")
        self.label_49 = QLabel(self.frame_31)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(120, 0))
        self.label_49.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_294.addWidget(self.label_49)

        self.label_ncamera_SI = QLabel(self.frame_31)
        self.label_ncamera_SI.setObjectName(u"label_ncamera_SI")
        sizePolicy9 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_ncamera_SI.sizePolicy().hasHeightForWidth())
        self.label_ncamera_SI.setSizePolicy(sizePolicy9)
        self.label_ncamera_SI.setStyleSheet(u"border: 2px solid black;\n"
"background-color: white;")

        self.horizontalLayout_294.addWidget(self.label_ncamera_SI)

        self.comboBox_ncamera_SI = CheckableComboBox(self.frame_31)
        self.comboBox_ncamera_SI.setObjectName(u"comboBox_ncamera_SI")
        self.comboBox_ncamera_SI.setEnabled(True)
        self.comboBox_ncamera_SI.setMaximumSize(QSize(85, 16777215))
        self.comboBox_ncamera_SI.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
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
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-width: 100px;\n"
"}")

        self.horizontalLayout_294.addWidget(self.comboBox_ncamera_SI)

        self.checkBox_all_camera_SI = QCheckBox(self.frame_31)
        self.checkBox_all_camera_SI.setObjectName(u"checkBox_all_camera_SI")
        self.checkBox_all_camera_SI.setEnabled(False)
        self.checkBox_all_camera_SI.setMaximumSize(QSize(50, 16777215))
        self.checkBox_all_camera_SI.setStyleSheet(u"")

        self.horizontalLayout_294.addWidget(self.checkBox_all_camera_SI)


        self.verticalLayout_50.addLayout(self.horizontalLayout_294)

        self.horizontalLayout_295 = QHBoxLayout()
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.label_50 = QLabel(self.frame_31)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(120, 0))
        self.label_50.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_295.addWidget(self.label_50)

        self.label_nframe_SI = QLabel(self.frame_31)
        self.label_nframe_SI.setObjectName(u"label_nframe_SI")
        self.label_nframe_SI.setStyleSheet(u"border: 2px solid black;\n"
"background-color: white;")

        self.horizontalLayout_295.addWidget(self.label_nframe_SI)

        self.comboBox_nframe_SI = CheckableComboBox(self.frame_31)
        self.comboBox_nframe_SI.setObjectName(u"comboBox_nframe_SI")
        self.comboBox_nframe_SI.setEnabled(True)
        self.comboBox_nframe_SI.setMaximumSize(QSize(85, 16777215))
        self.comboBox_nframe_SI.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
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
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-width: 100px;\n"
"}")

        self.horizontalLayout_295.addWidget(self.comboBox_nframe_SI)

        self.checkBox_all_frame_SI = QCheckBox(self.frame_31)
        self.checkBox_all_frame_SI.setObjectName(u"checkBox_all_frame_SI")
        self.checkBox_all_frame_SI.setEnabled(False)
        self.checkBox_all_frame_SI.setMaximumSize(QSize(50, 16777215))
        self.checkBox_all_frame_SI.setStyleSheet(u"")

        self.horizontalLayout_295.addWidget(self.checkBox_all_frame_SI)


        self.verticalLayout_50.addLayout(self.horizontalLayout_295)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.add_filter_btn_SI = QPushButton(self.frame_31)
        self.add_filter_btn_SI.setObjectName(u"add_filter_btn_SI")
        self.add_filter_btn_SI.setEnabled(True)
        self.add_filter_btn_SI.setMinimumSize(QSize(0, 28))
        self.add_filter_btn_SI.setMaximumSize(QSize(16777215, 16777215))
        self.add_filter_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_filter_btn_SI.setStyleSheet(u" background-color:rgb(70,70,70);\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:center;\n"
"color:white;")

        self.horizontalLayout_99.addWidget(self.add_filter_btn_SI)

        self.select_filter_btn_SI = QPushButton(self.frame_31)
        self.select_filter_btn_SI.setObjectName(u"select_filter_btn_SI")
        self.select_filter_btn_SI.setMinimumSize(QSize(0, 28))
        self.select_filter_btn_SI.setMaximumSize(QSize(16777215, 16777215))
        self.select_filter_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_filter_btn_SI.setStyleSheet(u" background-color:rgb(70,70,70);\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:center;\n"
"color:white;")

        self.horizontalLayout_99.addWidget(self.select_filter_btn_SI)


        self.verticalLayout_50.addLayout(self.horizontalLayout_99)


        self.horizontalLayout_39.addWidget(self.frame_31)


        self.verticalLayout_35.addWidget(self.frame_tools_technical)


        self.verticalLayout_84.addWidget(self.frame_44)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.horizontalLayout_86.addWidget(self.tabWidget_2)

        self.frame_413 = QFrame(self.main)
        self.frame_413.setObjectName(u"frame_413")
        self.frame_413.setMaximumSize(QSize(600, 1200))
        self.frame_413.setFrameShape(QFrame.StyledPanel)
        self.frame_413.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_1103 = QHBoxLayout(self.frame_413)
        self.horizontalLayout_1103.setSpacing(0)
        self.horizontalLayout_1103.setObjectName(u"horizontalLayout_1103")
        self.horizontalLayout_1103.setContentsMargins(0, 0, 0, 0)
        self.frame_2_3 = QFrame(self.frame_413)
        self.frame_2_3.setObjectName(u"frame_2_3")
        self.frame_2_3.setMinimumSize(QSize(300, 0))
        self.frame_2_3.setMaximumSize(QSize(300, 16777215))
        self.frame_2_3.setFrameShape(QFrame.Box)
        self.frame_2_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2_3)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_651 = QFrame(self.frame_2_3)
        self.frame_651.setObjectName(u"frame_651")
        self.frame_651.setMinimumSize(QSize(0, 25))
        self.frame_651.setFrameShape(QFrame.StyledPanel)
        self.frame_651.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_1191 = QHBoxLayout(self.frame_651)
        self.horizontalLayout_1191.setObjectName(u"horizontalLayout_1191")
        self.horizontalLayout_1191.setContentsMargins(0, 0, 0, 0)
        self.frame_661 = QFrame(self.frame_651)
        self.frame_661.setObjectName(u"frame_661")
        self.frame_661.setMaximumSize(QSize(108, 16777215))
        self.frame_661.setFrameShape(QFrame.StyledPanel)
        self.frame_661.setFrameShadow(QFrame.Raised)
        self.verticalLayout_931 = QVBoxLayout(self.frame_661)
        self.verticalLayout_931.setObjectName(u"verticalLayout_931")
        self.verticalLayout_931.setContentsMargins(0, 0, 0, 0)
        self.label_1291 = QLabel(self.frame_661)
        self.label_1291.setObjectName(u"label_1291")
        sizePolicy.setHeightForWidth(self.label_1291.sizePolicy().hasHeightForWidth())
        self.label_1291.setSizePolicy(sizePolicy)
        self.label_1291.setFont(font1)

        self.verticalLayout_931.addWidget(self.label_1291)

        self.label_1311 = QLabel(self.frame_661)
        self.label_1311.setObjectName(u"label_1311")
        self.label_1311.setMaximumSize(QSize(23, 8))
        self.label_1311.setPixmap(QPixmap(u"images/pngaaa.com-4780825.png"))
        self.label_1311.setScaledContents(True)

        self.verticalLayout_931.addWidget(self.label_1311)


        self.horizontalLayout_1191.addWidget(self.frame_661)

        self.label_6_1 = QLabel(self.frame_651)
        self.label_6_1.setObjectName(u"label_6_1")
        font5 = QFont()
        font5.setFamilies([u"ubuntu"])
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_6_1.setFont(font5)
        self.label_6_1.setStyleSheet(u"font-weight: bold; \n"
"font-size: 30%;")

        self.horizontalLayout_1191.addWidget(self.label_6_1, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_651)

        self.scrollArea_up_side_4 = QScrollArea(self.frame_2_3)
        self.scrollArea_up_side_4.setObjectName(u"scrollArea_up_side_4")
        self.scrollArea_up_side_4.setMinimumSize(QSize(0, 0))
        self.scrollArea_up_side_4.setMaximumSize(QSize(350, 16777215))
        self.scrollArea_up_side_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_up_side_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 288, 28))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(288, 0))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(280, 16777215))
        self.horizontalLayout_90_2 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_90_2.setObjectName(u"horizontalLayout_90_2")
        self.horizontalLayout_90_2.setContentsMargins(0, 0, 0, 0)
        self.up_side_technical = QLabel(self.scrollAreaWidgetContents_2)
        self.up_side_technical.setObjectName(u"up_side_technical")
        self.up_side_technical.setMinimumSize(QSize(288, 0))
        self.up_side_technical.setMaximumSize(QSize(280, 16777215))
        self.up_side_technical.setStyleSheet(u"")
        self.up_side_technical.setPixmap(QPixmap(u"../../.designer/train/oxin/03-11-2021 09-43-52-296900__0.jpg"))
        self.up_side_technical.setScaledContents(True)

        self.horizontalLayout_90_2.addWidget(self.up_side_technical)

        self.scrollArea_up_side_4.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_up_side_4)


        self.horizontalLayout_1103.addWidget(self.frame_2_3)

        self.frame_16_2 = QFrame(self.frame_413)
        self.frame_16_2.setObjectName(u"frame_16_2")
        self.frame_16_2.setEnabled(True)
        self.frame_16_2.setMinimumSize(QSize(300, 0))
        self.frame_16_2.setMaximumSize(QSize(300, 16777215))
        self.frame_16_2.setFrameShape(QFrame.Box)
        self.frame_16_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_87_2 = QVBoxLayout(self.frame_16_2)
        self.verticalLayout_87_2.setSpacing(1)
        self.verticalLayout_87_2.setObjectName(u"verticalLayout_87_2")
        self.verticalLayout_87_2.setContentsMargins(0, 0, 0, 0)
        self.frame_60_2 = QFrame(self.frame_16_2)
        self.frame_60_2.setObjectName(u"frame_60_2")
        self.frame_60_2.setMinimumSize(QSize(0, 25))
        self.frame_60_2.setFrameShape(QFrame.StyledPanel)
        self.frame_60_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118_2 = QHBoxLayout(self.frame_60_2)
        self.horizontalLayout_118_2.setObjectName(u"horizontalLayout_118_2")
        self.horizontalLayout_118_2.setContentsMargins(0, 0, 0, 0)
        self.frame_64_2 = QFrame(self.frame_60_2)
        self.frame_64_2.setObjectName(u"frame_64_2")
        self.frame_64_2.setMaximumSize(QSize(108, 16777215))
        self.frame_64_2.setFrameShape(QFrame.StyledPanel)
        self.frame_64_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_64_2)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_124 = QLabel(self.frame_64_2)
        self.label_124.setObjectName(u"label_124")
        sizePolicy.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy)
        self.label_124.setFont(font1)

        self.verticalLayout_92.addWidget(self.label_124)

        self.label_125 = QLabel(self.frame_64_2)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMaximumSize(QSize(23, 8))
        self.label_125.setPixmap(QPixmap(u"images/pngaaa.com-4780825.png"))
        self.label_125.setScaledContents(True)

        self.verticalLayout_92.addWidget(self.label_125)


        self.horizontalLayout_118_2.addWidget(self.frame_64_2)

        self.label_119 = QLabel(self.frame_60_2)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font5)
        self.label_119.setStyleSheet(u"font-weight: bold; \n"
"font-size: 30%;")

        self.horizontalLayout_118_2.addWidget(self.label_119, 0, Qt.AlignLeft)


        self.verticalLayout_87_2.addWidget(self.frame_60_2)

        self.scrollArea_up_side_3 = QScrollArea(self.frame_16_2)
        self.scrollArea_up_side_3.setObjectName(u"scrollArea_up_side_3")
        self.scrollArea_up_side_3.setMinimumSize(QSize(288, 0))
        self.scrollArea_up_side_3.setMaximumSize(QSize(350, 16777215))
        self.scrollArea_up_side_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_up_side_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_51 = QWidget()
        self.scrollAreaWidgetContents_51.setObjectName(u"scrollAreaWidgetContents_51")
        self.scrollAreaWidgetContents_51.setGeometry(QRect(0, 0, 288, 28))
        self.scrollAreaWidgetContents_51.setMinimumSize(QSize(288, 0))
        self.scrollAreaWidgetContents_51.setMaximumSize(QSize(280, 16777215))
        self.horizontalLayout_1141 = QHBoxLayout(self.scrollAreaWidgetContents_51)
        self.horizontalLayout_1141.setObjectName(u"horizontalLayout_1141")
        self.horizontalLayout_1141.setContentsMargins(0, 0, 0, 0)
        self.down_side_technical = QLabel(self.scrollAreaWidgetContents_51)
        self.down_side_technical.setObjectName(u"down_side_technical")
        self.down_side_technical.setEnabled(True)
        self.down_side_technical.setMinimumSize(QSize(0, 0))
        self.down_side_technical.setMaximumSize(QSize(16777215, 16777215))
        self.down_side_technical.setPixmap(QPixmap(u"../../.designer/train/oxin/03-11-2021 09-43-52-296900__0.jpg"))
        self.down_side_technical.setScaledContents(True)

        self.horizontalLayout_1141.addWidget(self.down_side_technical)

        self.scrollArea_up_side_3.setWidget(self.scrollAreaWidgetContents_51)

        self.verticalLayout_87_2.addWidget(self.scrollArea_up_side_3)


        self.horizontalLayout_1103.addWidget(self.frame_16_2)


        self.horizontalLayout_86.addWidget(self.frame_413)


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
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_27_2.setObjectName(u"verticalLayout_27_2")
        self.next_img_label_btn = QPushButton(self.frame_7)
        self.next_img_label_btn.setObjectName(u"next_img_label_btn")
        self.next_img_label_btn.setEnabled(False)
        self.next_img_label_btn.setMinimumSize(QSize(37, 0))
        self.next_img_label_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.next_img_label_btn.setToolTip(u"Next")
#endif // QT_CONFIG(tooltip)
        self.next_img_label_btn.setStyleSheet(u"QPushButton {\n"
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
        icon15 = QIcon()
        icon15.addFile(u"images/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_img_label_btn.setIcon(icon15)
        self.next_img_label_btn.setIconSize(QSize(24, 31))

        self.verticalLayout_27_2.addWidget(self.next_img_label_btn)

        self.prev_img_label_btn = QPushButton(self.frame_7)
        self.prev_img_label_btn.setObjectName(u"prev_img_label_btn")
        self.prev_img_label_btn.setEnabled(False)
        self.prev_img_label_btn.setMinimumSize(QSize(37, 0))
        self.prev_img_label_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.prev_img_label_btn.setToolTip(u"Previous")
#endif // QT_CONFIG(tooltip)
        self.prev_img_label_btn.setStyleSheet(u"QPushButton {\n"
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
        icon16 = QIcon()
        icon16.addFile(u"images/arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_img_label_btn.setIcon(icon16)
        self.prev_img_label_btn.setIconSize(QSize(24, 31))

        self.verticalLayout_27_2.addWidget(self.prev_img_label_btn)

        self.line_35 = QFrame(self.frame_7)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27_2.addWidget(self.line_35)

        self.zoomIn_btn = QPushButton(self.frame_7)
        self.zoomIn_btn.setObjectName(u"zoomIn_btn")
        self.zoomIn_btn.setEnabled(False)
        self.zoomIn_btn.setMinimumSize(QSize(37, 0))
        self.zoomIn_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.zoomIn_btn.setToolTip(u"Zoom In")
#endif // QT_CONFIG(tooltip)
        self.zoomIn_btn.setStyleSheet(u"QPushButton {\n"
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
        icon17 = QIcon()
        icon17.addFile(u"images/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomIn_btn.setIcon(icon17)
        self.zoomIn_btn.setIconSize(QSize(24, 31))

        self.verticalLayout_27_2.addWidget(self.zoomIn_btn)

        self.zoomOut_btn = QPushButton(self.frame_7)
        self.zoomOut_btn.setObjectName(u"zoomOut_btn")
        self.zoomOut_btn.setEnabled(False)
        self.zoomOut_btn.setMinimumSize(QSize(37, 0))
        self.zoomOut_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.zoomOut_btn.setToolTip(u"Zoom Out")
#endif // QT_CONFIG(tooltip)
        self.zoomOut_btn.setStyleSheet(u"QPushButton {\n"
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
        icon18 = QIcon()
        icon18.addFile(u"images/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomOut_btn.setIcon(icon18)
        self.zoomOut_btn.setIconSize(QSize(36, 31))

        self.verticalLayout_27_2.addWidget(self.zoomOut_btn)

        self.drag_btn = QPushButton(self.frame_7)
        self.drag_btn.setObjectName(u"drag_btn")
        self.drag_btn.setEnabled(False)
        self.drag_btn.setMinimumSize(QSize(37, 0))
        self.drag_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.drag_btn.setToolTip(u"Drag")
#endif // QT_CONFIG(tooltip)
        self.drag_btn.setStyleSheet(u"QPushButton {\n"
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
        icon19 = QIcon()
        icon19.addFile(u"images/drag3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.drag_btn.setIcon(icon19)
        self.drag_btn.setIconSize(QSize(30, 22))

        self.verticalLayout_27_2.addWidget(self.drag_btn)

        self.line_36 = QFrame(self.frame_7)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27_2.addWidget(self.line_36)

        self.polygon_btn = QPushButton(self.frame_7)
        self.polygon_btn.setObjectName(u"polygon_btn")
        self.polygon_btn.setEnabled(False)
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
        icon20 = QIcon()
        icon20.addFile(u"images/clipart1919813.png", QSize(), QIcon.Normal, QIcon.Off)
        self.polygon_btn.setIcon(icon20)
        self.polygon_btn.setIconSize(QSize(28, 27))

        self.verticalLayout_27_2.addWidget(self.polygon_btn)

        self.suggested_defects_btn = QPushButton(self.frame_7)
        self.suggested_defects_btn.setObjectName(u"suggested_defects_btn")
        self.suggested_defects_btn.setEnabled(False)
        self.suggested_defects_btn.setMinimumSize(QSize(37, 0))
        self.suggested_defects_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.suggested_defects_btn.setToolTip(u"Suggested Defects")
#endif // QT_CONFIG(tooltip)
        self.suggested_defects_btn.setStyleSheet(u"QPushButton {\n"
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
        icon21 = QIcon()
        icon21.addFile(u"images/suggest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.suggested_defects_btn.setIcon(icon21)
        self.suggested_defects_btn.setIconSize(QSize(45, 45))

        self.verticalLayout_27_2.addWidget(self.suggested_defects_btn)

        self.heatmap_btn = QPushButton(self.frame_7)
        self.heatmap_btn.setObjectName(u"heatmap_btn")
        self.heatmap_btn.setEnabled(False)
        self.heatmap_btn.setMinimumSize(QSize(37, 0))
        self.heatmap_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.heatmap_btn.setStyleSheet(u"QPushButton {\n"
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
        icon22 = QIcon()
        icon22.addFile(u"images/heatmap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.heatmap_btn.setIcon(icon22)
        self.heatmap_btn.setIconSize(QSize(70, 30))

        self.verticalLayout_27_2.addWidget(self.heatmap_btn)

        self.line_48 = QFrame(self.frame_7)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.HLine)
        self.line_48.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27_2.addWidget(self.line_48)

        self.delete_btn = QPushButton(self.frame_7)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setEnabled(False)
        self.delete_btn.setMinimumSize(QSize(37, 0))
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.delete_btn.setToolTip(u"Delete Polygons")
#endif // QT_CONFIG(tooltip)
        self.delete_btn.setStyleSheet(u"QPushButton {\n"
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
        icon23 = QIcon()
        icon23.addFile(u"images/x-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon23)
        self.delete_btn.setIconSize(QSize(22, 27))

        self.verticalLayout_27_2.addWidget(self.delete_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_10.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.image = QLabel(self.frame_8)
        self.image.setObjectName(u"image")
        sizePolicy4.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy4)
        self.image.setMinimumSize(QSize(0, 478))
        self.image.setStyleSheet(u"border:1px solid rgb(200, 200,200);")
        self.image.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.image)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_65)

        self.label_show_help_btn = QPushButton(self.frame_8)
        self.label_show_help_btn.setObjectName(u"label_show_help_btn")
        self.label_show_help_btn.setMinimumSize(QSize(20, 20))
        self.label_show_help_btn.setMaximumSize(QSize(20, 20))
        self.label_show_help_btn.setStyleSheet(u"background-color: white;")
        icon24 = QIcon()
        icon24.addFile(u"images/top_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.label_show_help_btn.setIcon(icon24)
        self.label_show_help_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_93.addWidget(self.label_show_help_btn)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_20)


        self.verticalLayout_26.addLayout(self.horizontalLayout_93)

        self.label_show_help_frame = QFrame(self.frame_8)
        self.label_show_help_frame.setObjectName(u"label_show_help_frame")
        sizePolicy4.setHeightForWidth(self.label_show_help_frame.sizePolicy().hasHeightForWidth())
        self.label_show_help_frame.setSizePolicy(sizePolicy4)
        self.label_show_help_frame.setMinimumSize(QSize(0, 0))
        self.label_show_help_frame.setMaximumSize(QSize(16777215, 1))
        self.label_show_help_frame.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"border: None;")
        self.label_show_help_frame.setFrameShape(QFrame.StyledPanel)
        self.label_show_help_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.label_show_help_frame)
        self.horizontalLayout_100.setSpacing(3)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(3, 3, 3, 3)
        self.labeling_help_1 = QLabel(self.label_show_help_frame)
        self.labeling_help_1.setObjectName(u"labeling_help_1")
        self.labeling_help_1.setMinimumSize(QSize(0, 100))
        self.labeling_help_1.setMaximumSize(QSize(16777215, 16777215))
        self.labeling_help_1.setStyleSheet(u"border: 2px solid black;")
        self.labeling_help_1.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.labeling_help_1)

        self.labeling_help_2 = QLabel(self.label_show_help_frame)
        self.labeling_help_2.setObjectName(u"labeling_help_2")
        self.labeling_help_2.setMinimumSize(QSize(0, 100))
        self.labeling_help_2.setMaximumSize(QSize(16777215, 16777215))
        self.labeling_help_2.setStyleSheet(u"border: 2px solid black;")
        self.labeling_help_2.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.labeling_help_2)

        self.labeling_help_3 = QLabel(self.label_show_help_frame)
        self.labeling_help_3.setObjectName(u"labeling_help_3")
        self.labeling_help_3.setMinimumSize(QSize(0, 100))
        self.labeling_help_3.setMaximumSize(QSize(16777215, 16777215))
        self.labeling_help_3.setStyleSheet(u"border: 2px solid black;")
        self.labeling_help_3.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.labeling_help_3)

        self.labeling_help_4 = QLabel(self.label_show_help_frame)
        self.labeling_help_4.setObjectName(u"labeling_help_4")
        self.labeling_help_4.setMinimumSize(QSize(0, 100))
        self.labeling_help_4.setMaximumSize(QSize(16777215, 16777215))
        self.labeling_help_4.setStyleSheet(u"border: 2px solid black;")
        self.labeling_help_4.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.labeling_help_4)

        self.labeling_help_5 = QLabel(self.label_show_help_frame)
        self.labeling_help_5.setObjectName(u"labeling_help_5")
        self.labeling_help_5.setMinimumSize(QSize(0, 100))
        self.labeling_help_5.setMaximumSize(QSize(16777215, 16777215))
        self.labeling_help_5.setStyleSheet(u"border: 2px solid black;")
        self.labeling_help_5.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.labeling_help_5)

        self.labeling_help_6 = QLabel(self.label_show_help_frame)
        self.labeling_help_6.setObjectName(u"labeling_help_6")
        self.labeling_help_6.setMinimumSize(QSize(0, 100))
        self.labeling_help_6.setMaximumSize(QSize(16777215, 16777215))
        self.labeling_help_6.setStyleSheet(u"border: 2px solid black;")
        self.labeling_help_6.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.labeling_help_6)


        self.verticalLayout_26.addWidget(self.label_show_help_frame)

        self.frame_18 = QFrame(self.frame_8)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 70))
        self.frame_18.setMaximumSize(QSize(16777215, 70))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_14.addWidget(self.label_13)

        self.plabel_date_txt = QLabel(self.frame_18)
        self.plabel_date_txt.setObjectName(u"plabel_date_txt")
        sizePolicy3.setHeightForWidth(self.plabel_date_txt.sizePolicy().hasHeightForWidth())
        self.plabel_date_txt.setSizePolicy(sizePolicy3)

        self.horizontalLayout_14.addWidget(self.plabel_date_txt)


        self.horizontalLayout_87.addLayout(self.horizontalLayout_14)

        self.line_5 = QFrame(self.frame_18)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_87.addWidget(self.line_5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(0, 0))
        self.label_22.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.label_22)

        self.plabel_coil_num_txt = QLabel(self.frame_18)
        self.plabel_coil_num_txt.setObjectName(u"plabel_coil_num_txt")
        sizePolicy3.setHeightForWidth(self.plabel_coil_num_txt.sizePolicy().hasHeightForWidth())
        self.plabel_coil_num_txt.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.plabel_coil_num_txt)


        self.horizontalLayout_87.addLayout(self.horizontalLayout_15)

        self.line_10 = QFrame(self.frame_18)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_87.addWidget(self.line_10)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_121 = QLabel(self.frame_18)
        self.label_121.setObjectName(u"label_121")
        sizePolicy.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy)
        self.label_121.setMinimumSize(QSize(0, 0))
        self.label_121.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_20.addWidget(self.label_121)

        self.plabel_cam_txt = QLabel(self.frame_18)
        self.plabel_cam_txt.setObjectName(u"plabel_cam_txt")
        sizePolicy3.setHeightForWidth(self.plabel_cam_txt.sizePolicy().hasHeightForWidth())
        self.plabel_cam_txt.setSizePolicy(sizePolicy3)

        self.horizontalLayout_20.addWidget(self.plabel_cam_txt)


        self.horizontalLayout_87.addLayout(self.horizontalLayout_20)

        self.line_27 = QFrame(self.frame_18)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.VLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_87.addWidget(self.line_27)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setSpacing(3)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_288 = QLabel(self.frame_18)
        self.label_288.setObjectName(u"label_288")
        sizePolicy.setHeightForWidth(self.label_288.sizePolicy().hasHeightForWidth())
        self.label_288.setSizePolicy(sizePolicy)
        self.label_288.setMinimumSize(QSize(0, 0))
        self.label_288.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_103.addWidget(self.label_288)

        self.plabel_frame_txt = QLabel(self.frame_18)
        self.plabel_frame_txt.setObjectName(u"plabel_frame_txt")
        sizePolicy3.setHeightForWidth(self.plabel_frame_txt.sizePolicy().hasHeightForWidth())
        self.plabel_frame_txt.setSizePolicy(sizePolicy3)

        self.horizontalLayout_103.addWidget(self.plabel_frame_txt)


        self.horizontalLayout_87.addLayout(self.horizontalLayout_103)


        self.verticalLayout_25.addLayout(self.horizontalLayout_87)

        self.line_30 = QFrame(self.frame_18)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_30)

        self.horizontalLayout_229 = QHBoxLayout()
        self.horizontalLayout_229.setObjectName(u"horizontalLayout_229")
        self.checkBox_show_neighbours = QCheckBox(self.frame_18)
        self.checkBox_show_neighbours.setObjectName(u"checkBox_show_neighbours")
        self.checkBox_show_neighbours.setEnabled(False)
        self.checkBox_show_neighbours.setStyleSheet(u"")

        self.horizontalLayout_229.addWidget(self.checkBox_show_neighbours)

        self.checkBox_show_neighbours_labels = QCheckBox(self.frame_18)
        self.checkBox_show_neighbours_labels.setObjectName(u"checkBox_show_neighbours_labels")
        self.checkBox_show_neighbours_labels.setEnabled(False)
        self.checkBox_show_neighbours_labels.setStyleSheet(u"")

        self.horizontalLayout_229.addWidget(self.checkBox_show_neighbours_labels)


        self.verticalLayout_25.addLayout(self.horizontalLayout_229)


        self.horizontalLayout_47.addLayout(self.verticalLayout_25)

        self.line_2 = QFrame(self.frame_18)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_47.addWidget(self.line_2)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_285 = QLabel(self.frame_18)
        self.label_285.setObjectName(u"label_285")
        sizePolicy.setHeightForWidth(self.label_285.sizePolicy().hasHeightForWidth())
        self.label_285.setSizePolicy(sizePolicy)

        self.horizontalLayout_45.addWidget(self.label_285)

        self.line_thickness_slider = QSlider(self.frame_18)
        self.line_thickness_slider.setObjectName(u"line_thickness_slider")
        self.line_thickness_slider.setMinimum(1)
        self.line_thickness_slider.setMaximum(30)
        self.line_thickness_slider.setValue(4)
        self.line_thickness_slider.setTracking(True)
        self.line_thickness_slider.setOrientation(Qt.Horizontal)
        self.line_thickness_slider.setInvertedAppearance(False)
        self.line_thickness_slider.setInvertedControls(False)

        self.horizontalLayout_45.addWidget(self.line_thickness_slider)


        self.verticalLayout_53.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_286 = QLabel(self.frame_18)
        self.label_286.setObjectName(u"label_286")
        sizePolicy.setHeightForWidth(self.label_286.sizePolicy().hasHeightForWidth())
        self.label_286.setSizePolicy(sizePolicy)

        self.horizontalLayout_46.addWidget(self.label_286)

        self.point_thickness_slider = QSlider(self.frame_18)
        self.point_thickness_slider.setObjectName(u"point_thickness_slider")
        self.point_thickness_slider.setMinimum(5)
        self.point_thickness_slider.setMaximum(25)
        self.point_thickness_slider.setValue(10)
        self.point_thickness_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_46.addWidget(self.point_thickness_slider)


        self.verticalLayout_53.addLayout(self.horizontalLayout_46)


        self.horizontalLayout_47.addLayout(self.verticalLayout_53)


        self.verticalLayout_26.addWidget(self.frame_18)


        self.horizontalLayout_10.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(366, 0))
        self.frame_6.setMaximumSize(QSize(366, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.label_111 = QLabel(self.frame_11)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_113.addWidget(self.label_111)

        self.no_defect = QRadioButton(self.frame_11)
        self.no_defect.setObjectName(u"no_defect")
        self.no_defect.setEnabled(False)
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
        self.no_defect.setCheckable(True)
        self.no_defect.setChecked(False)

        self.horizontalLayout_113.addWidget(self.no_defect)

        self.yes_defect = QRadioButton(self.frame_11)
        self.yes_defect.setObjectName(u"yes_defect")
        self.yes_defect.setEnabled(False)
        self.yes_defect.setStyleSheet(u"QRadioButton {\n"
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
"    background-color:       green;\n"
"    border:                 2px solid green;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")

        self.horizontalLayout_113.addWidget(self.yes_defect)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_16)


        self.verticalLayout_34.addLayout(self.horizontalLayout_113)

        self.stackedWidget_defect = QStackedWidget(self.frame_11)
        self.stackedWidget_defect.setObjectName(u"stackedWidget_defect")
        self.stackedWidget_defect.setStyleSheet(u"")
        self.stackedWidget_defect.setFrameShape(QFrame.Panel)
        self.stackedWidget_defect.setLineWidth(1)
        self.page_yes = QWidget()
        self.page_yes.setObjectName(u"page_yes")
        self.verticalLayout_38 = QVBoxLayout(self.page_yes)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_220 = QLabel(self.page_yes)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setStyleSheet(u"font: 63 14pt \"URW Bookman\";")

        self.verticalLayout_38.addWidget(self.label_220)

        self.mask_table_widget = QTableWidget(self.page_yes)
        if (self.mask_table_widget.columnCount() < 3):
            self.mask_table_widget.setColumnCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.mask_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.mask_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.mask_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        self.mask_table_widget.setObjectName(u"mask_table_widget")
        self.mask_table_widget.horizontalHeader().setVisible(False)
        self.mask_table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.mask_table_widget.verticalHeader().setVisible(False)
        self.mask_table_widget.verticalHeader().setHighlightSections(True)

        self.verticalLayout_38.addWidget(self.mask_table_widget)

        self.stackedWidget_defect.addWidget(self.page_yes)
        self.page_no = QWidget()
        self.page_no.setObjectName(u"page_no")
        self.page_no.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_97 = QVBoxLayout(self.page_no)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_211 = QLabel(self.page_no)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_97.addWidget(self.label_211)

        self.stackedWidget_defect.addWidget(self.page_no)

        self.verticalLayout_34.addWidget(self.stackedWidget_defect)

        self.warning_label_page = QTextEdit(self.frame_11)
        self.warning_label_page.setObjectName(u"warning_label_page")
        self.warning_label_page.setEnabled(False)
        self.warning_label_page.setMinimumSize(QSize(0, 40))
        self.warning_label_page.setMaximumSize(QSize(16777215, 40))
        self.warning_label_page.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.warning_label_page)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.save_dataset_btn = QPushButton(self.frame_11)
        self.save_dataset_btn.setObjectName(u"save_dataset_btn")
        self.save_dataset_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.save_dataset_btn.sizePolicy().hasHeightForWidth())
        self.save_dataset_btn.setSizePolicy(sizePolicy1)
        self.save_dataset_btn.setMinimumSize(QSize(0, 30))
        self.save_dataset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.save_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_dataset_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.save_dataset_btn)

        self.save_all_dataset_btn = QPushButton(self.frame_11)
        self.save_all_dataset_btn.setObjectName(u"save_all_dataset_btn")
        self.save_all_dataset_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.save_all_dataset_btn.sizePolicy().hasHeightForWidth())
        self.save_all_dataset_btn.setSizePolicy(sizePolicy1)
        self.save_all_dataset_btn.setMinimumSize(QSize(0, 30))
        self.save_all_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_all_dataset_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.save_all_dataset_btn)

        self.save_all_progressBar = QProgressBar(self.frame_11)
        self.save_all_progressBar.setObjectName(u"save_all_progressBar")
        self.save_all_progressBar.setValue(0)

        self.horizontalLayout_13.addWidget(self.save_all_progressBar)


        self.verticalLayout_34.addLayout(self.horizontalLayout_13)


        self.verticalLayout_24.addWidget(self.frame_11)

        self.binary_chart_frame_label = QGroupBox(self.frame_6)
        self.binary_chart_frame_label.setObjectName(u"binary_chart_frame_label")
        self.binary_chart_frame_label.setMinimumSize(QSize(0, 280))

        self.verticalLayout_24.addWidget(self.binary_chart_frame_label)


        self.horizontalLayout_10.addWidget(self.frame_6)


        self.horizontalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_label)
        self.page_user_profile = QWidget()
        self.page_user_profile.setObjectName(u"page_user_profile")
        self.horizontalLayout_119 = QHBoxLayout(self.page_user_profile)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.frame_2 = QFrame(self.page_user_profile)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(220, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_31 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_31)

        self.user_label = QLabel(self.frame_2)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setMinimumSize(QSize(230, 230))
        self.user_label.setMaximumSize(QSize(230, 230))
        self.user_label.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.user_label)

        self.horizontalSpacer_32 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_32)


        self.verticalLayout_18.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_6)

        self.user_name_2 = QLabel(self.frame_2)
        self.user_name_2.setObjectName(u"user_name_2")
        sizePolicy3.setHeightForWidth(self.user_name_2.sizePolicy().hasHeightForWidth())
        self.user_name_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_24.addWidget(self.user_name_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.horizontalLayout_88.addWidget(self.label_15)

        self.user_id = QLabel(self.frame_2)
        self.user_id.setObjectName(u"user_id")
        sizePolicy3.setHeightForWidth(self.user_id.sizePolicy().hasHeightForWidth())
        self.user_id.setSizePolicy(sizePolicy3)

        self.horizontalLayout_88.addWidget(self.user_id)


        self.verticalLayout_18.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_165.addWidget(self.label_16)

        self.role = QLabel(self.frame_2)
        self.role.setObjectName(u"role")
        sizePolicy3.setHeightForWidth(self.role.sizePolicy().hasHeightForWidth())
        self.role.setSizePolicy(sizePolicy3)

        self.horizontalLayout_165.addWidget(self.role)


        self.verticalLayout_18.addLayout(self.horizontalLayout_165)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_90.addWidget(self.label_17)

        self.date_created = QLabel(self.frame_2)
        self.date_created.setObjectName(u"date_created")
        sizePolicy3.setHeightForWidth(self.date_created.sizePolicy().hasHeightForWidth())
        self.date_created.setSizePolicy(sizePolicy3)

        self.horizontalLayout_90.addWidget(self.date_created)


        self.verticalLayout_18.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.label_79 = QLabel(self.frame_2)
        self.label_79.setObjectName(u"label_79")
        sizePolicy3.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy3)

        self.horizontalLayout_166.addWidget(self.label_79)

        self.default_dataset = QLabel(self.frame_2)
        self.default_dataset.setObjectName(u"default_dataset")
        sizePolicy3.setHeightForWidth(self.default_dataset.sizePolicy().hasHeightForWidth())
        self.default_dataset.setSizePolicy(sizePolicy3)

        self.horizontalLayout_166.addWidget(self.default_dataset)


        self.verticalLayout_18.addLayout(self.horizontalLayout_166)

        self.line_15 = QFrame(self.frame_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_15)

        self.mainHelp = QTextEdit(self.frame_2)
        self.mainHelp.setObjectName(u"mainHelp")
        self.mainHelp.setEnabled(True)

        self.verticalLayout_18.addWidget(self.mainHelp)


        self.horizontalLayout_119.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_16 = QFrame(self.page_user_profile)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.create_new_database = QPushButton(self.frame_16)
        self.create_new_database.setObjectName(u"create_new_database")
        self.create_new_database.setMinimumSize(QSize(161, 62))
        self.create_new_database.setStyleSheet(u"color:white;")

        self.verticalLayout_41.addWidget(self.create_new_database)

        self.all_databases = QPushButton(self.frame_16)
        self.all_databases.setObjectName(u"all_databases")
        self.all_databases.setMinimumSize(QSize(161, 62))
        self.all_databases.setStyleSheet(u"color:white")

        self.verticalLayout_41.addWidget(self.all_databases)

        self.my_databases_2 = QPushButton(self.frame_16)
        self.my_databases_2.setObjectName(u"my_databases_2")
        self.my_databases_2.setMinimumSize(QSize(161, 62))
        self.my_databases_2.setStyleSheet(u"color:white;\n"
"background-color: rgb(212, 212, 212);")

        self.verticalLayout_41.addWidget(self.my_databases_2)

        self.my_databases_3 = QPushButton(self.frame_16)
        self.my_databases_3.setObjectName(u"my_databases_3")
        self.my_databases_3.setEnabled(False)
        self.my_databases_3.setMinimumSize(QSize(161, 62))
        self.my_databases_3.setStyleSheet(u"color:white")

        self.verticalLayout_41.addWidget(self.my_databases_3)


        self.horizontalLayout_114.addLayout(self.verticalLayout_41)

        self.stackedWidget_2 = QStackedWidget(self.frame_16)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"border:1px solid rgb(200, 200,200);")
        self.page_create_db = QWidget()
        self.page_create_db.setObjectName(u"page_create_db")
        self.verticalLayout_55 = QVBoxLayout(self.page_create_db)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(10, -1, 10, -1)
        self.label_78 = QLabel(self.page_create_db)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(200, 0))
        self.label_78.setMaximumSize(QSize(200, 16777215))
        self.label_78.setStyleSheet(u"border:1px solid rgb(0, 0,0);")

        self.horizontalLayout_158.addWidget(self.label_78)

        self.today_date = QLineEdit(self.page_create_db)
        self.today_date.setObjectName(u"today_date")
        self.today_date.setEnabled(True)
        self.today_date.setStyleSheet(u"border:1px solid rgb(0, 0,0);")
        self.today_date.setReadOnly(True)

        self.horizontalLayout_158.addWidget(self.today_date)


        self.verticalLayout_55.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(10, -1, 10, -1)
        self.label_129 = QLabel(self.page_create_db)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(200, 0))
        self.label_129.setMaximumSize(QSize(200, 16777215))
        self.label_129.setStyleSheet(u"border:1px solid rgb(0, 0,0);")

        self.horizontalLayout_159.addWidget(self.label_129)

        self.user_name_3 = QLineEdit(self.page_create_db)
        self.user_name_3.setObjectName(u"user_name_3")
        self.user_name_3.setEnabled(True)
        self.user_name_3.setStyleSheet(u"border:1px solid rgb(0, 0,0);")
        self.user_name_3.setReadOnly(True)

        self.horizontalLayout_159.addWidget(self.user_name_3)


        self.verticalLayout_55.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(10, -1, 10, -1)
        self.label_8 = QLabel(self.page_create_db)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setMaximumSize(QSize(200, 16777215))
        self.label_8.setStyleSheet(u"border:1px solid rgb(0, 0,0);")

        self.horizontalLayout_156.addWidget(self.label_8)

        self.lineEdit_name_dataset = QLineEdit(self.page_create_db)
        self.lineEdit_name_dataset.setObjectName(u"lineEdit_name_dataset")
        self.lineEdit_name_dataset.setStyleSheet(u"border:1px solid rgb(0, 0,0);")

        self.horizontalLayout_156.addWidget(self.lineEdit_name_dataset)


        self.verticalLayout_55.addLayout(self.horizontalLayout_156)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(10, -1, 10, -1)
        self.label_157 = QLabel(self.page_create_db)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMinimumSize(QSize(200, 0))
        self.label_157.setMaximumSize(QSize(200, 16777215))
        self.label_157.setStyleSheet(u"border:1px solid rgb(0, 0,0);")

        self.horizontalLayout_160.addWidget(self.label_157)

        self.lineEdit_path_dataset = QLineEdit(self.page_create_db)
        self.lineEdit_path_dataset.setObjectName(u"lineEdit_path_dataset")
        self.lineEdit_path_dataset.setStyleSheet(u"border:1px solid rgb(0, 0,0);")
        self.lineEdit_path_dataset.setReadOnly(True)

        self.horizontalLayout_160.addWidget(self.lineEdit_path_dataset)

        self.toolButton_select_directory = QToolButton(self.page_create_db)
        self.toolButton_select_directory.setObjectName(u"toolButton_select_directory")
        self.toolButton_select_directory.setStyleSheet(u"border:1px solid rgb(0, 0,0);")

        self.horizontalLayout_160.addWidget(self.toolButton_select_directory)


        self.verticalLayout_55.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_157.addItem(self.horizontalSpacer_6)

        self.create_database_btn = QPushButton(self.page_create_db)
        self.create_database_btn.setObjectName(u"create_database_btn")
        self.create_database_btn.setMinimumSize(QSize(151, 30))
        self.create_database_btn.setMaximumSize(QSize(151, 16777215))
        self.create_database_btn.setStyleSheet(u"color:white")

        self.horizontalLayout_157.addWidget(self.create_database_btn)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_157.addItem(self.horizontalSpacer_9)


        self.verticalLayout_55.addLayout(self.horizontalLayout_157)

        self.stackedWidget_2.addWidget(self.page_create_db)
        self.page_all_db = QWidget()
        self.page_all_db.setObjectName(u"page_all_db")
        self.verticalLayout_56 = QVBoxLayout(self.page_all_db)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_24 = QLabel(self.page_all_db)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(87, 0))
        self.label_24.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_162.addWidget(self.label_24)

        self.comboBox_all_datasets = QComboBox(self.page_all_db)
        self.comboBox_all_datasets.setObjectName(u"comboBox_all_datasets")
        self.comboBox_all_datasets.setMinimumSize(QSize(140, 0))
        self.comboBox_all_datasets.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_162.addWidget(self.comboBox_all_datasets)


        self.verticalLayout_56.addLayout(self.horizontalLayout_162)

        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.label_14 = QLabel(self.page_all_db)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_163.addWidget(self.label_14)

        self.all_ds_id = QLabel(self.page_all_db)
        self.all_ds_id.setObjectName(u"all_ds_id")

        self.horizontalLayout_163.addWidget(self.all_ds_id)


        self.verticalLayout_56.addLayout(self.horizontalLayout_163)

        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_20 = QLabel(self.page_all_db)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_164.addWidget(self.label_20)

        self.all_ds_name = QLabel(self.page_all_db)
        self.all_ds_name.setObjectName(u"all_ds_name")

        self.horizontalLayout_164.addWidget(self.all_ds_name)


        self.verticalLayout_56.addLayout(self.horizontalLayout_164)

        self.horizontalLayout_216 = QHBoxLayout()
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.label_25 = QLabel(self.page_all_db)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_216.addWidget(self.label_25)

        self.all_ds_owner_user = QLabel(self.page_all_db)
        self.all_ds_owner_user.setObjectName(u"all_ds_owner_user")

        self.horizontalLayout_216.addWidget(self.all_ds_owner_user)


        self.verticalLayout_56.addLayout(self.horizontalLayout_216)

        self.horizontalLayout_217 = QHBoxLayout()
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.label_26 = QLabel(self.page_all_db)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_217.addWidget(self.label_26)

        self.all_ds_path = QLabel(self.page_all_db)
        self.all_ds_path.setObjectName(u"all_ds_path")

        self.horizontalLayout_217.addWidget(self.all_ds_path)


        self.verticalLayout_56.addLayout(self.horizontalLayout_217)

        self.stackedWidget_2.addWidget(self.page_all_db)
        self.page_my_db = QWidget()
        self.page_my_db.setObjectName(u"page_my_db")
        self.verticalLayout_57 = QVBoxLayout(self.page_my_db)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.horizontalLayout_222 = QHBoxLayout()
        self.horizontalLayout_222.setObjectName(u"horizontalLayout_222")
        self.label_219 = QLabel(self.page_my_db)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setMinimumSize(QSize(87, 0))
        self.label_219.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_222.addWidget(self.label_219)

        self.comboBox_user_datasets = QComboBox(self.page_my_db)
        self.comboBox_user_datasets.setObjectName(u"comboBox_user_datasets")
        self.comboBox_user_datasets.setMinimumSize(QSize(140, 0))
        self.comboBox_user_datasets.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_222.addWidget(self.comboBox_user_datasets)


        self.verticalLayout_57.addLayout(self.horizontalLayout_222)

        self.horizontalLayout_219 = QHBoxLayout()
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.label_154 = QLabel(self.page_my_db)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_219.addWidget(self.label_154)

        self.my_ds_id = QLabel(self.page_my_db)
        self.my_ds_id.setObjectName(u"my_ds_id")

        self.horizontalLayout_219.addWidget(self.my_ds_id)


        self.verticalLayout_57.addLayout(self.horizontalLayout_219)

        self.horizontalLayout_218 = QHBoxLayout()
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.label_131 = QLabel(self.page_my_db)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_218.addWidget(self.label_131)

        self.my_ds_name = QLabel(self.page_my_db)
        self.my_ds_name.setObjectName(u"my_ds_name")

        self.horizontalLayout_218.addWidget(self.my_ds_name)


        self.verticalLayout_57.addLayout(self.horizontalLayout_218)

        self.horizontalLayout_221 = QHBoxLayout()
        self.horizontalLayout_221.setObjectName(u"horizontalLayout_221")
        self.label_218 = QLabel(self.page_my_db)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_221.addWidget(self.label_218)

        self.my_ds_owner_user = QLabel(self.page_my_db)
        self.my_ds_owner_user.setObjectName(u"my_ds_owner_user")

        self.horizontalLayout_221.addWidget(self.my_ds_owner_user)


        self.verticalLayout_57.addLayout(self.horizontalLayout_221)

        self.horizontalLayout_220 = QHBoxLayout()
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.label_155 = QLabel(self.page_my_db)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_220.addWidget(self.label_155)

        self.my_ds_path = QLabel(self.page_my_db)
        self.my_ds_path.setObjectName(u"my_ds_path")

        self.horizontalLayout_220.addWidget(self.my_ds_path)


        self.verticalLayout_57.addLayout(self.horizontalLayout_220)

        self.horizontalLayout_223 = QHBoxLayout()
        self.horizontalLayout_223.setObjectName(u"horizontalLayout_223")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_223.addItem(self.horizontalSpacer_10)

        self.set_default_database_btn = QPushButton(self.page_my_db)
        self.set_default_database_btn.setObjectName(u"set_default_database_btn")
        self.set_default_database_btn.setMinimumSize(QSize(170, 30))
        self.set_default_database_btn.setMaximumSize(QSize(16777215, 16777215))
        self.set_default_database_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_223.addWidget(self.set_default_database_btn)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_223.addItem(self.horizontalSpacer_12)


        self.verticalLayout_57.addLayout(self.horizontalLayout_223)

        self.stackedWidget_2.addWidget(self.page_my_db)
        self.page_my_pipelines = QWidget()
        self.page_my_pipelines.setObjectName(u"page_my_pipelines")
        self.verticalLayout_17 = QVBoxLayout(self.page_my_pipelines)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_293 = QHBoxLayout()
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.label_28 = QLabel(self.page_my_pipelines)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(87, 0))
        self.label_28.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_293.addWidget(self.label_28)

        self.combo_all_pipline = QComboBox(self.page_my_pipelines)
        self.combo_all_pipline.setObjectName(u"combo_all_pipline")
        self.combo_all_pipline.setMinimumSize(QSize(140, 0))
        self.combo_all_pipline.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_293.addWidget(self.combo_all_pipline)


        self.verticalLayout_17.addLayout(self.horizontalLayout_293)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_61 = QLabel(self.page_my_pipelines)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(87, 0))
        self.label_61.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_11.addWidget(self.label_61)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.combo_my_pipline = QComboBox(self.page_my_pipelines)
        self.combo_my_pipline.setObjectName(u"combo_my_pipline")
        self.combo_my_pipline.setMinimumSize(QSize(140, 0))
        self.combo_my_pipline.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_16.addWidget(self.combo_my_pipline)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.show_details_pipline = QPushButton(self.page_my_pipelines)
        self.show_details_pipline.setObjectName(u"show_details_pipline")
        self.show_details_pipline.setMinimumSize(QSize(0, 30))
        self.show_details_pipline.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.show_details_pipline)

        self.remove_pipline = QPushButton(self.page_my_pipelines)
        self.remove_pipline.setObjectName(u"remove_pipline")
        self.remove_pipline.setMinimumSize(QSize(0, 30))
        self.remove_pipline.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.remove_pipline)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.label_pipline_details = QLabel(self.page_my_pipelines)
        self.label_pipline_details.setObjectName(u"label_pipline_details")

        self.verticalLayout_17.addWidget(self.label_pipline_details)

        self.stackedWidget_2.addWidget(self.page_my_pipelines)

        self.horizontalLayout_114.addWidget(self.stackedWidget_2)


        self.verticalLayout_19.addLayout(self.horizontalLayout_114)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.binary_chart_frame_profile = QGroupBox(self.frame_16)
        self.binary_chart_frame_profile.setObjectName(u"binary_chart_frame_profile")
        self.binary_chart_frame_profile.setMinimumSize(QSize(402, 270))

        self.horizontalLayout_118.addWidget(self.binary_chart_frame_profile)

        self.classlist_chart_frame_profile = QGroupBox(self.frame_16)
        self.classlist_chart_frame_profile.setObjectName(u"classlist_chart_frame_profile")
        self.classlist_chart_frame_profile.setMinimumSize(QSize(402, 270))

        self.horizontalLayout_118.addWidget(self.classlist_chart_frame_profile)


        self.verticalLayout_19.addLayout(self.horizontalLayout_118)

        self.frame_148 = QFrame(self.frame_16)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(0, 55))
        self.frame_148.setMaximumSize(QSize(16777215, 55))
        self.frame_148.setFrameShape(QFrame.WinPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_235 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_235.setSpacing(5)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(15, 5, 15, 5)
        self.label_278 = QLabel(self.frame_148)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setMinimumSize(QSize(70, 0))
        self.label_278.setMaximumSize(QSize(70, 16777215))
        self.label_278.setFont(font5)
        self.label_278.setStyleSheet(u" font-weight: bold;")

        self.horizontalLayout_235.addWidget(self.label_278)

        self.profile_msg_label = QLabel(self.frame_148)
        self.profile_msg_label.setObjectName(u"profile_msg_label")
        self.profile_msg_label.setMinimumSize(QSize(0, 40))
        self.profile_msg_label.setMaximumSize(QSize(16777215, 40))
        self.profile_msg_label.setFont(font1)
        self.profile_msg_label.setStyleSheet(u"QLabel{\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"")
        self.profile_msg_label.setFrameShape(QFrame.WinPanel)
        self.profile_msg_label.setFrameShadow(QFrame.Sunken)
        self.profile_msg_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_235.addWidget(self.profile_msg_label)


        self.verticalLayout_19.addWidget(self.frame_148)


        self.horizontalLayout_119.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.page_user_profile)
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
        self.pipeline_pbt_btn = QPushButton(self.frame_51)
        self.pipeline_pbt_btn.setObjectName(u"pipeline_pbt_btn")
        self.pipeline_pbt_btn.setMinimumSize(QSize(150, 40))
        self.pipeline_pbt_btn.setMaximumSize(QSize(150, 16777215))
        self.pipeline_pbt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pipeline_pbt_btn.setAutoFillBackground(False)
        self.pipeline_pbt_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_95.addWidget(self.pipeline_pbt_btn)

        self.load_dataset_pbt_btn = QPushButton(self.frame_51)
        self.load_dataset_pbt_btn.setObjectName(u"load_dataset_pbt_btn")
        self.load_dataset_pbt_btn.setMinimumSize(QSize(150, 40))
        self.load_dataset_pbt_btn.setMaximumSize(QSize(150, 16777215))
        self.load_dataset_pbt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_dataset_pbt_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_95.addWidget(self.load_dataset_pbt_btn)

        self.history_pbt_btn = QPushButton(self.frame_51)
        self.history_pbt_btn.setObjectName(u"history_pbt_btn")
        self.history_pbt_btn.setMinimumSize(QSize(150, 40))
        self.history_pbt_btn.setMaximumSize(QSize(150, 16777215))
        self.history_pbt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.history_pbt_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_95.addWidget(self.history_pbt_btn)

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
        self.page_pipeline.setMaximumSize(QSize(16777213, 16777215))
        self.verticalLayout_44 = QVBoxLayout(self.page_pipeline)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, 8, -1, -1)
        self.frame_92 = QFrame(self.page_pipeline)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(100, 0))
        self.frame_92.setMaximumSize(QSize(16777215, 50))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_199 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalLayout_199.setContentsMargins(-1, 0, -1, -1)
        self.frame_12 = QFrame(self.frame_92)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(117, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_12)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.radioButton_one = QRadioButton(self.frame_12)
        self.radioButton_one.setObjectName(u"radioButton_one")

        self.verticalLayout_76.addWidget(self.radioButton_one)

        self.radioButton_two = QRadioButton(self.frame_12)
        self.radioButton_two.setObjectName(u"radioButton_two")

        self.verticalLayout_76.addWidget(self.radioButton_two)


        self.horizontalLayout_199.addWidget(self.frame_12)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_199.addItem(self.horizontalSpacer_61)

        self.frame_54 = QFrame(self.frame_92)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(300, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_12_3 = QLabel(self.frame_54)
        self.label_12_3.setObjectName(u"label_12_3")
        self.label_12_3.setMinimumSize(QSize(58, 25))
        self.label_12_3.setMaximumSize(QSize(46, 25))

        self.horizontalLayout_32.addWidget(self.label_12_3)

        self.cbBox_of_binary_model_in_PBT_page = QComboBox(self.frame_54)
        self.cbBox_of_binary_model_in_PBT_page.setObjectName(u"cbBox_of_binary_model_in_PBT_page")
        self.cbBox_of_binary_model_in_PBT_page.setMinimumSize(QSize(105, 25))
        self.cbBox_of_binary_model_in_PBT_page.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_32.addWidget(self.cbBox_of_binary_model_in_PBT_page)

        self.toolButton_binary = QToolButton(self.frame_54)
        self.toolButton_binary.setObjectName(u"toolButton_binary")

        self.horizontalLayout_32.addWidget(self.toolButton_binary)


        self.horizontalLayout_199.addWidget(self.frame_54)

        self.line_9 = QFrame(self.frame_92)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_199.addWidget(self.line_9)

        self.stackedWidget_3 = QStackedWidget(self.frame_92)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(63, 32))
        self.page_yolo = QWidget()
        self.page_yolo.setObjectName(u"page_yolo")
        self.horizontalLayout_104 = QHBoxLayout(self.page_yolo)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.frame_63 = QFrame(self.page_yolo)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(300, 16777215))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_12_5 = QLabel(self.frame_63)
        self.label_12_5.setObjectName(u"label_12_5")
        self.label_12_5.setMinimumSize(QSize(58, 25))
        self.label_12_5.setMaximumSize(QSize(46, 25))

        self.horizontalLayout_102.addWidget(self.label_12_5)

        self.cbBox_of_yolo_model_in_PBT_page = QComboBox(self.frame_63)
        self.cbBox_of_yolo_model_in_PBT_page.setObjectName(u"cbBox_of_yolo_model_in_PBT_page")
        self.cbBox_of_yolo_model_in_PBT_page.setMinimumSize(QSize(105, 25))
        self.cbBox_of_yolo_model_in_PBT_page.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_102.addWidget(self.cbBox_of_yolo_model_in_PBT_page)

        self.toolButton_yolo = QToolButton(self.frame_63)
        self.toolButton_yolo.setObjectName(u"toolButton_yolo")

        self.horizontalLayout_102.addWidget(self.toolButton_yolo)


        self.horizontalLayout_104.addWidget(self.frame_63)

        self.stackedWidget_3.addWidget(self.page_yolo)
        self.page_localization = QWidget()
        self.page_localization.setObjectName(u"page_localization")
        self.horizontalLayout_61 = QHBoxLayout(self.page_localization)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.page_localization)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(300, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_122 = QLabel(self.frame_55)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(81, 25))
        self.label_122.setMaximumSize(QSize(86, 25))

        self.horizontalLayout_40.addWidget(self.label_122)

        self.cbBox_of_localiztion_model_in_PBT_page = QComboBox(self.frame_55)
        self.cbBox_of_localiztion_model_in_PBT_page.setObjectName(u"cbBox_of_localiztion_model_in_PBT_page")
        self.cbBox_of_localiztion_model_in_PBT_page.setMinimumSize(QSize(105, 25))
        self.cbBox_of_localiztion_model_in_PBT_page.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_40.addWidget(self.cbBox_of_localiztion_model_in_PBT_page)

        self.toolButton_localiztion = QToolButton(self.frame_55)
        self.toolButton_localiztion.setObjectName(u"toolButton_localiztion")

        self.horizontalLayout_40.addWidget(self.toolButton_localiztion)


        self.horizontalLayout_61.addWidget(self.frame_55)

        self.frame_53 = QFrame(self.page_localization)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(200, 0))
        self.frame_53.setMaximumSize(QSize(300, 16777215))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_123 = QLabel(self.frame_53)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(91, 25))
        self.label_123.setMaximumSize(QSize(105, 25))

        self.horizontalLayout_31.addWidget(self.label_123)

        self.cbBox_of_multiClassification_model_in_PBT_page = QComboBox(self.frame_53)
        self.cbBox_of_multiClassification_model_in_PBT_page.setObjectName(u"cbBox_of_multiClassification_model_in_PBT_page")
        self.cbBox_of_multiClassification_model_in_PBT_page.setMinimumSize(QSize(105, 25))
        self.cbBox_of_multiClassification_model_in_PBT_page.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_31.addWidget(self.cbBox_of_multiClassification_model_in_PBT_page)

        self.toolButton_multiClassification = QToolButton(self.frame_53)
        self.toolButton_multiClassification.setObjectName(u"toolButton_multiClassification")

        self.horizontalLayout_31.addWidget(self.toolButton_multiClassification)


        self.horizontalLayout_61.addWidget(self.frame_53)

        self.line_20 = QFrame(self.page_localization)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_61.addWidget(self.line_20)

        self.stackedWidget_3.addWidget(self.page_localization)

        self.horizontalLayout_199.addWidget(self.stackedWidget_3)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_199.addItem(self.horizontalSpacer_62)


        self.verticalLayout_44.addWidget(self.frame_92)

        self.line_22 = QFrame(self.page_pipeline)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_22)

        self.frame_88 = QFrame(self.page_pipeline)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 50))
        self.frame_88.setMaximumSize(QSize(16777215, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_88)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, -1, 4)
        self.table_of_binary_classifaction_in_PBT_page = QTableWidget(self.frame_88)
        if (self.table_of_binary_classifaction_in_PBT_page.columnCount() < 10):
            self.table_of_binary_classifaction_in_PBT_page.setColumnCount(10)
        self.table_of_binary_classifaction_in_PBT_page.setObjectName(u"table_of_binary_classifaction_in_PBT_page")
        self.table_of_binary_classifaction_in_PBT_page.setColumnCount(10)
        self.table_of_binary_classifaction_in_PBT_page.horizontalHeader().setMinimumSectionSize(70)
        self.table_of_binary_classifaction_in_PBT_page.horizontalHeader().setDefaultSectionSize(70)
        self.table_of_binary_classifaction_in_PBT_page.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_45.addWidget(self.table_of_binary_classifaction_in_PBT_page)

        self.frame_108 = QFrame(self.frame_88)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 35))
        self.frame_108.setMaximumSize(QSize(16777215, 35))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.BTN_of_goToPreviouspage_in_PBT_page = QPushButton(self.frame_108)
        self.BTN_of_goToPreviouspage_in_PBT_page.setObjectName(u"BTN_of_goToPreviouspage_in_PBT_page")
        self.BTN_of_goToPreviouspage_in_PBT_page.setEnabled(False)
        self.BTN_of_goToPreviouspage_in_PBT_page.setMaximumSize(QSize(39, 16777215))
        self.BTN_of_goToPreviouspage_in_PBT_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_of_goToPreviouspage_in_PBT_page.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.BTN_of_goToPreviouspage_in_PBT_page.setIcon(icon16)
        self.BTN_of_goToPreviouspage_in_PBT_page.setIconSize(QSize(30, 30))

        self.horizontalLayout_67.addWidget(self.BTN_of_goToPreviouspage_in_PBT_page)

        self.lineEdit_of_pageNumber_displayment_in_PBT_page = QLineEdit(self.frame_108)
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setObjectName(u"lineEdit_of_pageNumber_displayment_in_PBT_page")
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setEnabled(False)
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setMinimumSize(QSize(50, 30))
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setMaximumSize(QSize(50, 30))
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setStyleSheet(u"padding:0;")
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.lineEdit_of_pageNumber_displayment_in_PBT_page)

        self.BTN_of_goToNextpage_in_PBT_page = QPushButton(self.frame_108)
        self.BTN_of_goToNextpage_in_PBT_page.setObjectName(u"BTN_of_goToNextpage_in_PBT_page")
        self.BTN_of_goToNextpage_in_PBT_page.setEnabled(True)
        self.BTN_of_goToNextpage_in_PBT_page.setMaximumSize(QSize(39, 16777215))
        self.BTN_of_goToNextpage_in_PBT_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_of_goToNextpage_in_PBT_page.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.BTN_of_goToNextpage_in_PBT_page.setIcon(icon15)
        self.BTN_of_goToNextpage_in_PBT_page.setIconSize(QSize(30, 30))

        self.horizontalLayout_67.addWidget(self.BTN_of_goToNextpage_in_PBT_page)


        self.verticalLayout_45.addWidget(self.frame_108, 0, Qt.AlignHCenter)

        self.line_23 = QFrame(self.frame_88)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_23)

        self.scrollArea_6 = QScrollArea(self.frame_88)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_6.setFrameShape(QFrame.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1418, 200))
        self.verticalLayout_107 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1416, 84))
        self.horizontalLayout_72 = QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_12_4 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_12_4.setObjectName(u"label_12_4")
        self.label_12_4.setMinimumSize(QSize(43, 25))
        self.label_12_4.setMaximumSize(QSize(43, 25))

        self.horizontalLayout_72.addWidget(self.label_12_4)

        self.LBL_of_selected_binary_classifaction_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_8)
        self.LBL_of_selected_binary_classifaction_model_in_PBT_page.setObjectName(u"LBL_of_selected_binary_classifaction_model_in_PBT_page")

        self.horizontalLayout_72.addWidget(self.LBL_of_selected_binary_classifaction_model_in_PBT_page)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_107.addWidget(self.scrollArea_7)

        self.stackedWidget_4 = QStackedWidget(self.scrollAreaWidgetContents_7)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_localization_2 = QWidget()
        self.page_localization_2.setObjectName(u"page_localization_2")
        self.verticalLayout_77 = QVBoxLayout(self.page_localization_2)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8 = QScrollArea(self.page_localization_2)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1416, 49))
        self.horizontalLayout_41 = QHBoxLayout(self.scrollAreaWidgetContents_9)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_247 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setMinimumSize(QSize(76, 25))
        self.label_247.setMaximumSize(QSize(85, 25))

        self.horizontalLayout_41.addWidget(self.label_247)

        self.LBL_of_selected_multiClassification_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_9)
        self.LBL_of_selected_multiClassification_model_in_PBT_page.setObjectName(u"LBL_of_selected_multiClassification_model_in_PBT_page")

        self.horizontalLayout_41.addWidget(self.LBL_of_selected_multiClassification_model_in_PBT_page)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_77.addWidget(self.scrollArea_8)

        self.scrollArea_9 = QScrollArea(self.page_localization_2)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1416, 49))
        self.horizontalLayout_43 = QHBoxLayout(self.scrollAreaWidgetContents_10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_251 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setMinimumSize(QSize(75, 25))
        self.label_251.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_43.addWidget(self.label_251)

        self.LBL_of_selected_localization_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_10)
        self.LBL_of_selected_localization_model_in_PBT_page.setObjectName(u"LBL_of_selected_localization_model_in_PBT_page")

        self.horizontalLayout_43.addWidget(self.LBL_of_selected_localization_model_in_PBT_page)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_77.addWidget(self.scrollArea_9)

        self.stackedWidget_4.addWidget(self.page_localization_2)
        self.page_yolo_2 = QWidget()
        self.page_yolo_2.setObjectName(u"page_yolo_2")
        self.verticalLayout_79 = QVBoxLayout(self.page_yolo_2)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10 = QScrollArea(self.page_yolo_2)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1416, 106))
        self.horizontalLayout_105 = QHBoxLayout(self.scrollAreaWidgetContents_11)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.label_12_6 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_12_6.setObjectName(u"label_12_6")
        self.label_12_6.setMinimumSize(QSize(43, 25))
        self.label_12_6.setMaximumSize(QSize(43, 25))

        self.horizontalLayout_105.addWidget(self.label_12_6)

        self.LBL_of_selected_binary_yolo_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_11)
        self.LBL_of_selected_binary_yolo_model_in_PBT_page.setObjectName(u"LBL_of_selected_binary_yolo_model_in_PBT_page")

        self.horizontalLayout_105.addWidget(self.LBL_of_selected_binary_yolo_model_in_PBT_page)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_79.addWidget(self.scrollArea_10)

        self.stackedWidget_4.addWidget(self.page_yolo_2)

        self.verticalLayout_107.addWidget(self.stackedWidget_4)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_45.addWidget(self.scrollArea_6)


        self.verticalLayout_44.addWidget(self.frame_88)

        self.line_24 = QFrame(self.page_pipeline)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_24)

        self.frame_40 = QFrame(self.page_pipeline)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 28))
        self.frame_40.setFrameShape(QFrame.Box)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(19, 0, 0, 0)
        self.label_9 = QLabel(self.frame_40)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(122, 16777215))

        self.horizontalLayout_42.addWidget(self.label_9)

        self.pipline_name = QLineEdit(self.frame_40)
        self.pipline_name.setObjectName(u"pipline_name")
        self.pipline_name.setMinimumSize(QSize(200, 0))
        self.pipline_name.setMaximumSize(QSize(500, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(210, 210, 150, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 121, 198, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pipline_name.setPalette(palette1)

        self.horizontalLayout_42.addWidget(self.pipline_name)

        self.horizontalSpacer_63 = QSpacerItem(35, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_63)

        self.pipline_name_status = QLabel(self.frame_40)
        self.pipline_name_status.setObjectName(u"pipline_name_status")
        self.pipline_name_status.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.horizontalLayout_42.addWidget(self.pipline_name_status)


        self.verticalLayout_44.addWidget(self.frame_40)

        self.frame_107 = QFrame(self.page_pipeline)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(0, 30))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.BTN_apply_of_binary_classifaction_in_PBT_page = QPushButton(self.frame_107)
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setObjectName(u"BTN_apply_of_binary_classifaction_in_PBT_page")
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setEnabled(True)
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setMinimumSize(QSize(58, 28))
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setMaximumSize(QSize(58, 28))
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(100,100,100);\n"
"color:rgb(0,0,0);\n"
"border: 1px solid rgb(52, 59, 72);\n"
"border-radius: 1px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(10,210,10);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled-hover{\n"
"    background-color:rgb(255,255,255);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"")

        self.horizontalLayout_96.addWidget(self.BTN_apply_of_binary_classifaction_in_PBT_page)

        self.BTN_refreshing_pipline_page_in_PBT = QPushButton(self.frame_107)
        self.BTN_refreshing_pipline_page_in_PBT.setObjectName(u"BTN_refreshing_pipline_page_in_PBT")
        self.BTN_refreshing_pipline_page_in_PBT.setMinimumSize(QSize(58, 28))
        self.BTN_refreshing_pipline_page_in_PBT.setMaximumSize(QSize(58, 28))
        self.BTN_refreshing_pipline_page_in_PBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_refreshing_pipline_page_in_PBT.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(100,100,100);\n"
"color:rgb(0,0,0);\n"
"border: 1px solid rgb(52, 59, 72);\n"
"border-radius: 1px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(10,210,10);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"}\n"
"QPushButton:enabled-hover{\n"
"    background-color:rgb(255,255,255);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"")

        self.horizontalLayout_96.addWidget(self.BTN_refreshing_pipline_page_in_PBT)


        self.verticalLayout_44.addWidget(self.frame_107, 0, Qt.AlignHCenter)

        self.stackedWidget_pbt.addWidget(self.page_pipeline)
        self.page_load_dataset = QWidget()
        self.page_load_dataset.setObjectName(u"page_load_dataset")
        self.verticalLayout_48 = QVBoxLayout(self.page_load_dataset)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(-1, -1, -1, 0)
        self.frame_89 = QFrame(self.page_load_dataset)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 71))
        self.frame_89.setFrameShape(QFrame.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.frame_89)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(740, 0))
        self.groupBox_6.setMaximumSize(QSize(602, 100))
        self.horizontalLayout_97 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_35 = QLabel(self.groupBox_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_27.addWidget(self.label_35)


        self.horizontalLayout_97.addLayout(self.verticalLayout_27)

        self.cbBox_of_dataset_in_PBT_page_load_dataset = QComboBox(self.groupBox_6)
        self.cbBox_of_dataset_in_PBT_page_load_dataset.setObjectName(u"cbBox_of_dataset_in_PBT_page_load_dataset")
        self.cbBox_of_dataset_in_PBT_page_load_dataset.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_97.addWidget(self.cbBox_of_dataset_in_PBT_page_load_dataset)

        self.horizontalSpacer_18 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_18)

        self.chbox_defectdata_in_PBT_page = QCheckBox(self.groupBox_6)
        self.chbox_defectdata_in_PBT_page.setObjectName(u"chbox_defectdata_in_PBT_page")
        self.chbox_defectdata_in_PBT_page.setEnabled(True)
        self.chbox_defectdata_in_PBT_page.setChecked(True)

        self.horizontalLayout_97.addWidget(self.chbox_defectdata_in_PBT_page)

        self.chbox_prefectdata_in_PBT_page = QCheckBox(self.groupBox_6)
        self.chbox_prefectdata_in_PBT_page.setObjectName(u"chbox_prefectdata_in_PBT_page")
        self.chbox_prefectdata_in_PBT_page.setEnabled(True)
        self.chbox_prefectdata_in_PBT_page.setCheckable(True)
        self.chbox_prefectdata_in_PBT_page.setChecked(True)

        self.horizontalLayout_97.addWidget(self.chbox_prefectdata_in_PBT_page)

        self.horizontalSpacer_64 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_64)

        self.BTN_load_in_PBT_page = QPushButton(self.groupBox_6)
        self.BTN_load_in_PBT_page.setObjectName(u"BTN_load_in_PBT_page")
        self.BTN_load_in_PBT_page.setMinimumSize(QSize(56, 26))
        self.BTN_load_in_PBT_page.setMaximumSize(QSize(70, 16777215))
        self.BTN_load_in_PBT_page.setStyleSheet(u"color:white;")

        self.horizontalLayout_97.addWidget(self.BTN_load_in_PBT_page)

        self.line_7 = QFrame(self.groupBox_6)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_97.addWidget(self.line_7)

        self.lineEdit_of_path_displayment_in_PBT_page = QLineEdit(self.groupBox_6)
        self.lineEdit_of_path_displayment_in_PBT_page.setObjectName(u"lineEdit_of_path_displayment_in_PBT_page")
        self.lineEdit_of_path_displayment_in_PBT_page.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_97.addWidget(self.lineEdit_of_path_displayment_in_PBT_page)

        self.BTN_set_directory_image_in_PBT_page = QToolButton(self.groupBox_6)
        self.BTN_set_directory_image_in_PBT_page.setObjectName(u"BTN_set_directory_image_in_PBT_page")

        self.horizontalLayout_97.addWidget(self.BTN_set_directory_image_in_PBT_page)

        self.BTN_load_image_in_PBT_page = QPushButton(self.groupBox_6)
        self.BTN_load_image_in_PBT_page.setObjectName(u"BTN_load_image_in_PBT_page")
        self.BTN_load_image_in_PBT_page.setMinimumSize(QSize(93, 26))
        self.BTN_load_image_in_PBT_page.setMaximumSize(QSize(101, 16777215))
        self.BTN_load_image_in_PBT_page.setStyleSheet(u"color:white;")

        self.horizontalLayout_97.addWidget(self.BTN_load_image_in_PBT_page)

        self.LBL_of_data_is_ready_in_PBT_page_2 = QLabel(self.groupBox_6)
        self.LBL_of_data_is_ready_in_PBT_page_2.setObjectName(u"LBL_of_data_is_ready_in_PBT_page_2")
        self.LBL_of_data_is_ready_in_PBT_page_2.setMinimumSize(QSize(0, 0))
        self.LBL_of_data_is_ready_in_PBT_page_2.setMaximumSize(QSize(16777215, 28))

        self.horizontalLayout_97.addWidget(self.LBL_of_data_is_ready_in_PBT_page_2)


        self.horizontalLayout_112.addWidget(self.groupBox_6)

        self.horizontalSpacer_46 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_46)

        self.groupBox_7 = QGroupBox(self.frame_89)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(271, 0))
        self.groupBox_7.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_98 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_98.addWidget(self.label_36)

        self.cbBox_of_pipline_in_PBT_page_load_dataset = QComboBox(self.groupBox_7)
        self.cbBox_of_pipline_in_PBT_page_load_dataset.setObjectName(u"cbBox_of_pipline_in_PBT_page_load_dataset")
        self.cbBox_of_pipline_in_PBT_page_load_dataset.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_98.addWidget(self.cbBox_of_pipline_in_PBT_page_load_dataset)

        self.BTN_set_pipline_in_PBT_page = QPushButton(self.groupBox_7)
        self.BTN_set_pipline_in_PBT_page.setObjectName(u"BTN_set_pipline_in_PBT_page")
        self.BTN_set_pipline_in_PBT_page.setMinimumSize(QSize(0, 26))
        self.BTN_set_pipline_in_PBT_page.setMaximumSize(QSize(50, 16777215))
        self.BTN_set_pipline_in_PBT_page.setStyleSheet(u"color:white;")

        self.horizontalLayout_98.addWidget(self.BTN_set_pipline_in_PBT_page)


        self.horizontalLayout_112.addWidget(self.groupBox_7, 0, Qt.AlignLeft)


        self.verticalLayout_48.addWidget(self.frame_89)

        self.line_12 = QFrame(self.page_load_dataset)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_12)

        self.frame_91 = QFrame(self.page_load_dataset)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_197 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.frame_95 = QFrame(self.frame_91)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMaximumSize(QSize(270, 16777215))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_95)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_35 = QFrame(self.frame_95)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 30))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.BTN_evaluate_image_in_PBT_page_2 = QPushButton(self.frame_35)
        self.BTN_evaluate_image_in_PBT_page_2.setObjectName(u"BTN_evaluate_image_in_PBT_page_2")
        self.BTN_evaluate_image_in_PBT_page_2.setMaximumSize(QSize(101, 16777215))
        self.BTN_evaluate_image_in_PBT_page_2.setStyleSheet(u"color:white;")

        self.horizontalLayout_79.addWidget(self.BTN_evaluate_image_in_PBT_page_2)

        self.BTN_refresh_loadDataset_tab_in_PBT = QPushButton(self.frame_35)
        self.BTN_refresh_loadDataset_tab_in_PBT.setObjectName(u"BTN_refresh_loadDataset_tab_in_PBT")
        self.BTN_refresh_loadDataset_tab_in_PBT.setMaximumSize(QSize(101, 16777215))
        self.BTN_refresh_loadDataset_tab_in_PBT.setStyleSheet(u"color:white;")

        self.horizontalLayout_79.addWidget(self.BTN_refresh_loadDataset_tab_in_PBT)


        self.verticalLayout_51.addWidget(self.frame_35)

        self.GBox_model_evaluation_details = QGroupBox(self.frame_95)
        self.GBox_model_evaluation_details.setObjectName(u"GBox_model_evaluation_details")
        self.verticalLayout_59 = QVBoxLayout(self.GBox_model_evaluation_details)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.LBL_of_data_is_ready_in_PBT_page = QLabel(self.GBox_model_evaluation_details)
        self.LBL_of_data_is_ready_in_PBT_page.setObjectName(u"LBL_of_data_is_ready_in_PBT_page")
        self.LBL_of_data_is_ready_in_PBT_page.setMinimumSize(QSize(200, 0))
        self.LBL_of_data_is_ready_in_PBT_page.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_59.addWidget(self.LBL_of_data_is_ready_in_PBT_page)

        self.LBL_of_pipline_is_ready_in_PBT_page = QLabel(self.GBox_model_evaluation_details)
        self.LBL_of_pipline_is_ready_in_PBT_page.setObjectName(u"LBL_of_pipline_is_ready_in_PBT_page")
        self.LBL_of_pipline_is_ready_in_PBT_page.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_59.addWidget(self.LBL_of_pipline_is_ready_in_PBT_page)

        self.pgbar_of_pipiline_ready_in_PBT_page = QProgressBar(self.GBox_model_evaluation_details)
        self.pgbar_of_pipiline_ready_in_PBT_page.setObjectName(u"pgbar_of_pipiline_ready_in_PBT_page")
        self.pgbar_of_pipiline_ready_in_PBT_page.setValue(0)

        self.verticalLayout_59.addWidget(self.pgbar_of_pipiline_ready_in_PBT_page)

        self.LBL_of_evalution_of_binary_model_in_PBT_page = QLabel(self.GBox_model_evaluation_details)
        self.LBL_of_evalution_of_binary_model_in_PBT_page.setObjectName(u"LBL_of_evalution_of_binary_model_in_PBT_page")
        self.LBL_of_evalution_of_binary_model_in_PBT_page.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_59.addWidget(self.LBL_of_evalution_of_binary_model_in_PBT_page)

        self.LBL_of_evalution_of_classification_model_in_PBT_page = QLabel(self.GBox_model_evaluation_details)
        self.LBL_of_evalution_of_classification_model_in_PBT_page.setObjectName(u"LBL_of_evalution_of_classification_model_in_PBT_page")
        self.LBL_of_evalution_of_classification_model_in_PBT_page.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_59.addWidget(self.LBL_of_evalution_of_classification_model_in_PBT_page)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_9)


        self.verticalLayout_51.addWidget(self.GBox_model_evaluation_details)


        self.horizontalLayout_197.addWidget(self.frame_95)

        self.line_13 = QFrame(self.frame_91)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_197.addWidget(self.line_13)

        self.frame_96 = QFrame(self.frame_91)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_96)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_96)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_98)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_97 = QFrame(self.frame_98)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setEnabled(True)
        self.frame_97.setMinimumSize(QSize(0, 200))
        self.frame_97.setFrameShape(QFrame.Panel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_198 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_198.setSpacing(10)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(10, 10, 10, 10)
        self.BTN_prev_original_image_in_PBT_page = QPushButton(self.frame_97)
        self.BTN_prev_original_image_in_PBT_page.setObjectName(u"BTN_prev_original_image_in_PBT_page")
        self.BTN_prev_original_image_in_PBT_page.setEnabled(False)
        self.BTN_prev_original_image_in_PBT_page.setMinimumSize(QSize(30, 30))
        self.BTN_prev_original_image_in_PBT_page.setMaximumSize(QSize(30, 30))
        self.BTN_prev_original_image_in_PBT_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_prev_original_image_in_PBT_page.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.BTN_prev_original_image_in_PBT_page.setIcon(icon16)
        self.BTN_prev_original_image_in_PBT_page.setIconSize(QSize(30, 30))

        self.horizontalLayout_198.addWidget(self.BTN_prev_original_image_in_PBT_page)

        self.frame_39 = QFrame(self.frame_97)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_39)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_37 = QLabel(self.frame_39)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout_66.addWidget(self.label_37)

        self.original_image_list_frame = QLabel(self.frame_39)
        self.original_image_list_frame.setObjectName(u"original_image_list_frame")
        self.original_image_list_frame.setFrameShape(QFrame.Panel)
        self.original_image_list_frame.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_66.addWidget(self.original_image_list_frame)

        self.label_40 = QLabel(self.frame_39)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout_66.addWidget(self.label_40)

        self.evaluated_image_list_frame = QLabel(self.frame_39)
        self.evaluated_image_list_frame.setObjectName(u"evaluated_image_list_frame")
        self.evaluated_image_list_frame.setFrameShape(QFrame.Panel)
        self.evaluated_image_list_frame.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_66.addWidget(self.evaluated_image_list_frame)


        self.horizontalLayout_198.addWidget(self.frame_39)

        self.BTN_next_original_image_in_PBT_page = QPushButton(self.frame_97)
        self.BTN_next_original_image_in_PBT_page.setObjectName(u"BTN_next_original_image_in_PBT_page")
        self.BTN_next_original_image_in_PBT_page.setEnabled(False)
        self.BTN_next_original_image_in_PBT_page.setMinimumSize(QSize(30, 30))
        self.BTN_next_original_image_in_PBT_page.setMaximumSize(QSize(30, 30))
        self.BTN_next_original_image_in_PBT_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_next_original_image_in_PBT_page.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.BTN_next_original_image_in_PBT_page.setIcon(icon15)
        self.BTN_next_original_image_in_PBT_page.setIconSize(QSize(30, 30))

        self.horizontalLayout_198.addWidget(self.BTN_next_original_image_in_PBT_page)


        self.verticalLayout_58.addWidget(self.frame_97)


        self.verticalLayout_60.addWidget(self.frame_98)


        self.horizontalLayout_197.addWidget(self.frame_96)


        self.verticalLayout_48.addWidget(self.frame_91)

        self.stackedWidget_pbt.addWidget(self.page_load_dataset)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.horizontalLayout_73 = QHBoxLayout(self.page_history)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.frame_3 = QFrame(self.page_history)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(370, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_3)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.scrollArea_3 = QScrollArea(self.frame_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 319, 715))
        self.verticalLayout_64 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.LBL_piplines_name_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_piplines_name_in_PBT_page.setObjectName(u"LBL_piplines_name_in_PBT_page")
        self.LBL_piplines_name_in_PBT_page.setMaximumSize(QSize(16777215, 20))
        self.LBL_piplines_name_in_PBT_page.setFont(font1)

        self.horizontalLayout_74.addWidget(self.LBL_piplines_name_in_PBT_page)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.cbBox_pipline_name_in_PBT_page = QComboBox(self.scrollAreaWidgetContents_4)
        self.cbBox_pipline_name_in_PBT_page.setObjectName(u"cbBox_pipline_name_in_PBT_page")

        self.horizontalLayout_75.addWidget(self.cbBox_pipline_name_in_PBT_page)


        self.horizontalLayout_74.addLayout(self.horizontalLayout_75)


        self.verticalLayout_64.addLayout(self.horizontalLayout_74)

        self.line_119 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_119.setObjectName(u"line_119")
        self.line_119.setFrameShape(QFrame.HLine)
        self.line_119.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_119)

        self.horizontalLayout_275 = QHBoxLayout()
        self.horizontalLayout_275.setObjectName(u"horizontalLayout_275")
        self.LBL_binary_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_binary_model_in_PBT_page.setObjectName(u"LBL_binary_model_in_PBT_page")
        self.LBL_binary_model_in_PBT_page.setMaximumSize(QSize(16777215, 20))
        self.LBL_binary_model_in_PBT_page.setFont(font1)

        self.horizontalLayout_275.addWidget(self.LBL_binary_model_in_PBT_page)

        self.horizontalLayout_276 = QHBoxLayout()
        self.horizontalLayout_276.setObjectName(u"horizontalLayout_276")
        self.cbBox_binarry_model_in_PBT_page = QComboBox(self.scrollAreaWidgetContents_4)
        self.cbBox_binarry_model_in_PBT_page.setObjectName(u"cbBox_binarry_model_in_PBT_page")

        self.horizontalLayout_276.addWidget(self.cbBox_binarry_model_in_PBT_page)


        self.horizontalLayout_275.addLayout(self.horizontalLayout_276)


        self.verticalLayout_64.addLayout(self.horizontalLayout_275)

        self.line_120 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_120.setObjectName(u"line_120")
        self.line_120.setFrameShape(QFrame.HLine)
        self.line_120.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_120)

        self.horizontalLayout_271 = QHBoxLayout()
        self.horizontalLayout_271.setSpacing(0)
        self.horizontalLayout_271.setObjectName(u"horizontalLayout_271")
        self.LBL_binary_accuracy_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_binary_accuracy_in_PBT_page.setObjectName(u"LBL_binary_accuracy_in_PBT_page")
        self.LBL_binary_accuracy_in_PBT_page.setFont(font1)

        self.horizontalLayout_271.addWidget(self.LBL_binary_accuracy_in_PBT_page)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_271.addItem(self.horizontalSpacer_51)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setSpacing(10)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_111_5 = QHBoxLayout()
        self.horizontalLayout_111_5.setObjectName(u"horizontalLayout_111_5")
        self.label_103 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(16777215, 20))
        self.label_103.setFont(font1)

        self.horizontalLayout_111_5.addWidget(self.label_103)

        self.binary_acc_min_filter_lineedit_3 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_acc_min_filter_lineedit_3.setObjectName(u"binary_acc_min_filter_lineedit_3")
        self.binary_acc_min_filter_lineedit_3.setMinimumSize(QSize(50, 0))
        self.binary_acc_min_filter_lineedit_3.setMaximumSize(QSize(50, 30))
        self.binary_acc_min_filter_lineedit_3.setFont(font1)
        self.binary_acc_min_filter_lineedit_3.setMaxLength(4)

        self.horizontalLayout_111_5.addWidget(self.binary_acc_min_filter_lineedit_3)


        self.horizontalLayout_76.addLayout(self.horizontalLayout_111_5)

        self.horizontalLayout_121_5 = QHBoxLayout()
        self.horizontalLayout_121_5.setObjectName(u"horizontalLayout_121_5")
        self.label_104 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMaximumSize(QSize(16777215, 20))
        self.label_104.setFont(font1)

        self.horizontalLayout_121_5.addWidget(self.label_104)

        self.binary_acc_max_filter_lineedit_3 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_acc_max_filter_lineedit_3.setObjectName(u"binary_acc_max_filter_lineedit_3")
        self.binary_acc_max_filter_lineedit_3.setMinimumSize(QSize(50, 0))
        self.binary_acc_max_filter_lineedit_3.setMaximumSize(QSize(50, 30))
        self.binary_acc_max_filter_lineedit_3.setFont(font1)
        self.binary_acc_max_filter_lineedit_3.setMaxLength(4)

        self.horizontalLayout_121_5.addWidget(self.binary_acc_max_filter_lineedit_3)


        self.horizontalLayout_76.addLayout(self.horizontalLayout_121_5)


        self.horizontalLayout_271.addLayout(self.horizontalLayout_76)

        self.line_29 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_271.addWidget(self.line_29)


        self.verticalLayout_64.addLayout(self.horizontalLayout_271)

        self.line_121 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setFrameShape(QFrame.HLine)
        self.line_121.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_121)

        self.horizontalLayout_272 = QHBoxLayout()
        self.horizontalLayout_272.setSpacing(0)
        self.horizontalLayout_272.setObjectName(u"horizontalLayout_272")
        self.LBL_binary_precision_in_PBT_page_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_binary_precision_in_PBT_page_2.setObjectName(u"LBL_binary_precision_in_PBT_page_2")
        self.LBL_binary_precision_in_PBT_page_2.setFont(font1)

        self.horizontalLayout_272.addWidget(self.LBL_binary_precision_in_PBT_page_2)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_272.addItem(self.horizontalSpacer_52)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setSpacing(10)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_111_6 = QHBoxLayout()
        self.horizontalLayout_111_6.setObjectName(u"horizontalLayout_111_6")
        self.label_105 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(16777215, 20))
        self.label_105.setFont(font1)

        self.horizontalLayout_111_6.addWidget(self.label_105)

        self.binary_precision_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_precision_min_filter_lineedit.setObjectName(u"binary_precision_min_filter_lineedit")
        self.binary_precision_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_precision_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_precision_min_filter_lineedit.setFont(font1)
        self.binary_precision_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_6.addWidget(self.binary_precision_min_filter_lineedit)


        self.horizontalLayout_77.addLayout(self.horizontalLayout_111_6)

        self.horizontalLayout_121_6 = QHBoxLayout()
        self.horizontalLayout_121_6.setObjectName(u"horizontalLayout_121_6")
        self.label_106 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(16777215, 20))
        self.label_106.setFont(font1)

        self.horizontalLayout_121_6.addWidget(self.label_106)

        self.binary_precision_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_precision_max_filter_lineedit.setObjectName(u"binary_precision_max_filter_lineedit")
        self.binary_precision_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_precision_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_precision_max_filter_lineedit.setFont(font1)
        self.binary_precision_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_6.addWidget(self.binary_precision_max_filter_lineedit)


        self.horizontalLayout_77.addLayout(self.horizontalLayout_121_6)


        self.horizontalLayout_272.addLayout(self.horizontalLayout_77)

        self.line_33 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_272.addWidget(self.line_33)


        self.verticalLayout_64.addLayout(self.horizontalLayout_272)

        self.line_105 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_105.setObjectName(u"line_105")
        self.line_105.setFrameShape(QFrame.HLine)
        self.line_105.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_105)

        self.horizontalLayout_273 = QHBoxLayout()
        self.horizontalLayout_273.setSpacing(0)
        self.horizontalLayout_273.setObjectName(u"horizontalLayout_273")
        self.LBL_binary_recall_in_PBT_page_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_binary_recall_in_PBT_page_3.setObjectName(u"LBL_binary_recall_in_PBT_page_3")
        self.LBL_binary_recall_in_PBT_page_3.setFont(font1)

        self.horizontalLayout_273.addWidget(self.LBL_binary_recall_in_PBT_page_3)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_273.addItem(self.horizontalSpacer_53)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setSpacing(10)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_111_7 = QHBoxLayout()
        self.horizontalLayout_111_7.setObjectName(u"horizontalLayout_111_7")
        self.label_107 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMaximumSize(QSize(16777215, 20))
        self.label_107.setFont(font1)

        self.horizontalLayout_111_7.addWidget(self.label_107)

        self.binary_recall_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_recall_min_filter_lineedit.setObjectName(u"binary_recall_min_filter_lineedit")
        self.binary_recall_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_recall_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_recall_min_filter_lineedit.setFont(font1)
        self.binary_recall_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_7.addWidget(self.binary_recall_min_filter_lineedit)


        self.horizontalLayout_78.addLayout(self.horizontalLayout_111_7)

        self.horizontalLayout_121_7 = QHBoxLayout()
        self.horizontalLayout_121_7.setObjectName(u"horizontalLayout_121_7")
        self.label_108 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(16777215, 20))
        self.label_108.setFont(font1)

        self.horizontalLayout_121_7.addWidget(self.label_108)

        self.binary_recall_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_recall_max_filter_lineedit.setObjectName(u"binary_recall_max_filter_lineedit")
        self.binary_recall_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_recall_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_recall_max_filter_lineedit.setFont(font1)
        self.binary_recall_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_7.addWidget(self.binary_recall_max_filter_lineedit)


        self.horizontalLayout_78.addLayout(self.horizontalLayout_121_7)


        self.horizontalLayout_273.addLayout(self.horizontalLayout_78)

        self.line_39 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_273.addWidget(self.line_39)


        self.verticalLayout_64.addLayout(self.horizontalLayout_273)

        self.line_118 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_118.setObjectName(u"line_118")
        self.line_118.setFrameShape(QFrame.HLine)
        self.line_118.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_118)

        self.horizontalLayout_274 = QHBoxLayout()
        self.horizontalLayout_274.setSpacing(0)
        self.horizontalLayout_274.setObjectName(u"horizontalLayout_274")
        self.LBL_binary_f1_in_PBT_page_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_binary_f1_in_PBT_page_5.setObjectName(u"LBL_binary_f1_in_PBT_page_5")
        self.LBL_binary_f1_in_PBT_page_5.setFont(font1)

        self.horizontalLayout_274.addWidget(self.LBL_binary_f1_in_PBT_page_5)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_274.addItem(self.horizontalSpacer_54)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setSpacing(10)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_111_8 = QHBoxLayout()
        self.horizontalLayout_111_8.setObjectName(u"horizontalLayout_111_8")
        self.label_113 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMaximumSize(QSize(16777215, 20))
        self.label_113.setFont(font1)

        self.horizontalLayout_111_8.addWidget(self.label_113)

        self.binary_f1_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_f1_min_filter_lineedit.setObjectName(u"binary_f1_min_filter_lineedit")
        self.binary_f1_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_f1_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_f1_min_filter_lineedit.setFont(font1)
        self.binary_f1_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_8.addWidget(self.binary_f1_min_filter_lineedit)


        self.horizontalLayout_80.addLayout(self.horizontalLayout_111_8)

        self.horizontalLayout_121_8 = QHBoxLayout()
        self.horizontalLayout_121_8.setObjectName(u"horizontalLayout_121_8")
        self.label_114 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMaximumSize(QSize(16777215, 20))
        self.label_114.setFont(font1)

        self.horizontalLayout_121_8.addWidget(self.label_114)

        self.binary_f1_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.binary_f1_max_filter_lineedit.setObjectName(u"binary_f1_max_filter_lineedit")
        self.binary_f1_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_f1_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_f1_max_filter_lineedit.setFont(font1)
        self.binary_f1_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_8.addWidget(self.binary_f1_max_filter_lineedit)


        self.horizontalLayout_80.addLayout(self.horizontalLayout_121_8)


        self.horizontalLayout_274.addLayout(self.horizontalLayout_80)

        self.line_85 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setFrameShape(QFrame.HLine)
        self.line_85.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_274.addWidget(self.line_85)


        self.verticalLayout_64.addLayout(self.horizontalLayout_274)

        self.line_117 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_117.setObjectName(u"line_117")
        self.line_117.setFrameShape(QFrame.HLine)
        self.line_117.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_117)

        self.horizontalLayout_277 = QHBoxLayout()
        self.horizontalLayout_277.setObjectName(u"horizontalLayout_277")
        self.LBL_localization_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_localization_model_in_PBT_page.setObjectName(u"LBL_localization_model_in_PBT_page")
        self.LBL_localization_model_in_PBT_page.setMaximumSize(QSize(16777215, 20))
        self.LBL_localization_model_in_PBT_page.setFont(font1)

        self.horizontalLayout_277.addWidget(self.LBL_localization_model_in_PBT_page)

        self.horizontalLayout_278 = QHBoxLayout()
        self.horizontalLayout_278.setObjectName(u"horizontalLayout_278")
        self.cbBox_localization_model_in_PBT_page = QComboBox(self.scrollAreaWidgetContents_4)
        self.cbBox_localization_model_in_PBT_page.setObjectName(u"cbBox_localization_model_in_PBT_page")

        self.horizontalLayout_278.addWidget(self.cbBox_localization_model_in_PBT_page)


        self.horizontalLayout_277.addLayout(self.horizontalLayout_278)


        self.verticalLayout_64.addLayout(self.horizontalLayout_277)

        self.line_114 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_114.setObjectName(u"line_114")
        self.line_114.setFrameShape(QFrame.HLine)
        self.line_114.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_114)

        self.horizontalLayout_279 = QHBoxLayout()
        self.horizontalLayout_279.setSpacing(0)
        self.horizontalLayout_279.setObjectName(u"horizontalLayout_279")
        self.LBL_localiztion_dice_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_localiztion_dice_in_PBT_page.setObjectName(u"LBL_localiztion_dice_in_PBT_page")
        self.LBL_localiztion_dice_in_PBT_page.setFont(font1)

        self.horizontalLayout_279.addWidget(self.LBL_localiztion_dice_in_PBT_page)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_279.addItem(self.horizontalSpacer_55)

        self.horizontalLayout_280 = QHBoxLayout()
        self.horizontalLayout_280.setSpacing(10)
        self.horizontalLayout_280.setObjectName(u"horizontalLayout_280")
        self.horizontalLayout_111_9 = QHBoxLayout()
        self.horizontalLayout_111_9.setObjectName(u"horizontalLayout_111_9")
        self.label_115 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMaximumSize(QSize(16777215, 20))
        self.label_115.setFont(font1)

        self.horizontalLayout_111_9.addWidget(self.label_115)

        self.localization_dice_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.localization_dice_min_filter_lineedit.setObjectName(u"localization_dice_min_filter_lineedit")
        self.localization_dice_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_dice_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_dice_min_filter_lineedit.setFont(font1)
        self.localization_dice_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_9.addWidget(self.localization_dice_min_filter_lineedit)


        self.horizontalLayout_280.addLayout(self.horizontalLayout_111_9)

        self.horizontalLayout_121_9 = QHBoxLayout()
        self.horizontalLayout_121_9.setObjectName(u"horizontalLayout_121_9")
        self.label_116 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMaximumSize(QSize(16777215, 20))
        self.label_116.setFont(font1)

        self.horizontalLayout_121_9.addWidget(self.label_116)

        self.localization_dice_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.localization_dice_max_filter_lineedit.setObjectName(u"localization_dice_max_filter_lineedit")
        self.localization_dice_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_dice_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_dice_max_filter_lineedit.setFont(font1)
        self.localization_dice_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_9.addWidget(self.localization_dice_max_filter_lineedit)


        self.horizontalLayout_280.addLayout(self.horizontalLayout_121_9)


        self.horizontalLayout_279.addLayout(self.horizontalLayout_280)

        self.line_99 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_99.setObjectName(u"line_99")
        self.line_99.setFrameShape(QFrame.HLine)
        self.line_99.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_279.addWidget(self.line_99)


        self.verticalLayout_64.addLayout(self.horizontalLayout_279)

        self.line_113 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_113.setObjectName(u"line_113")
        self.line_113.setFrameShape(QFrame.HLine)
        self.line_113.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_113)

        self.horizontalLayout_281 = QHBoxLayout()
        self.horizontalLayout_281.setSpacing(0)
        self.horizontalLayout_281.setObjectName(u"horizontalLayout_281")
        self.LBL_localiztion_iou_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_localiztion_iou_in_PBT_page.setObjectName(u"LBL_localiztion_iou_in_PBT_page")
        self.LBL_localiztion_iou_in_PBT_page.setFont(font1)

        self.horizontalLayout_281.addWidget(self.LBL_localiztion_iou_in_PBT_page)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_281.addItem(self.horizontalSpacer_56)

        self.horizontalLayout_282 = QHBoxLayout()
        self.horizontalLayout_282.setSpacing(10)
        self.horizontalLayout_282.setObjectName(u"horizontalLayout_282")
        self.horizontalLayout_111_10 = QHBoxLayout()
        self.horizontalLayout_111_10.setObjectName(u"horizontalLayout_111_10")
        self.label_117 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMaximumSize(QSize(16777215, 20))
        self.label_117.setFont(font1)

        self.horizontalLayout_111_10.addWidget(self.label_117)

        self.localization_iou_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.localization_iou_min_filter_lineedit.setObjectName(u"localization_iou_min_filter_lineedit")
        self.localization_iou_min_filter_lineedit.setEnabled(True)
        self.localization_iou_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_iou_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_iou_min_filter_lineedit.setFont(font1)
        self.localization_iou_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_10.addWidget(self.localization_iou_min_filter_lineedit)


        self.horizontalLayout_282.addLayout(self.horizontalLayout_111_10)

        self.horizontalLayout_121_10 = QHBoxLayout()
        self.horizontalLayout_121_10.setObjectName(u"horizontalLayout_121_10")
        self.label_118 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMaximumSize(QSize(16777215, 20))
        self.label_118.setFont(font1)

        self.horizontalLayout_121_10.addWidget(self.label_118)

        self.localization_iou_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.localization_iou_max_filter_lineedit.setObjectName(u"localization_iou_max_filter_lineedit")
        self.localization_iou_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_iou_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_iou_max_filter_lineedit.setFont(font1)
        self.localization_iou_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_10.addWidget(self.localization_iou_max_filter_lineedit)


        self.horizontalLayout_282.addLayout(self.horizontalLayout_121_10)


        self.horizontalLayout_281.addLayout(self.horizontalLayout_282)

        self.line_100 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_100.setObjectName(u"line_100")
        self.line_100.setFrameShape(QFrame.HLine)
        self.line_100.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_281.addWidget(self.line_100)


        self.verticalLayout_64.addLayout(self.horizontalLayout_281)

        self.line_112 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_112.setObjectName(u"line_112")
        self.line_112.setFrameShape(QFrame.HLine)
        self.line_112.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_112)

        self.horizontalLayout_283 = QHBoxLayout()
        self.horizontalLayout_283.setObjectName(u"horizontalLayout_283")
        self.LBL_classification_model_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_classification_model_in_PBT_page.setObjectName(u"LBL_classification_model_in_PBT_page")
        self.LBL_classification_model_in_PBT_page.setMaximumSize(QSize(16777215, 20))
        self.LBL_classification_model_in_PBT_page.setFont(font1)

        self.horizontalLayout_283.addWidget(self.LBL_classification_model_in_PBT_page)

        self.horizontalLayout_284 = QHBoxLayout()
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.cbBox_classification_model_in_PBT_page = QComboBox(self.scrollAreaWidgetContents_4)
        self.cbBox_classification_model_in_PBT_page.setObjectName(u"cbBox_classification_model_in_PBT_page")

        self.horizontalLayout_284.addWidget(self.cbBox_classification_model_in_PBT_page)


        self.horizontalLayout_283.addLayout(self.horizontalLayout_284)


        self.verticalLayout_64.addLayout(self.horizontalLayout_283)

        self.line_111 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_111.setObjectName(u"line_111")
        self.line_111.setFrameShape(QFrame.HLine)
        self.line_111.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_111)

        self.horizontalLayout_285 = QHBoxLayout()
        self.horizontalLayout_285.setSpacing(0)
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.LBL_classification_accuracy_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_classification_accuracy_in_PBT_page.setObjectName(u"LBL_classification_accuracy_in_PBT_page")
        self.LBL_classification_accuracy_in_PBT_page.setFont(font1)

        self.horizontalLayout_285.addWidget(self.LBL_classification_accuracy_in_PBT_page)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_285.addItem(self.horizontalSpacer_57)

        self.horizontalLayout_286 = QHBoxLayout()
        self.horizontalLayout_286.setSpacing(10)
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.horizontalLayout_111_13 = QHBoxLayout()
        self.horizontalLayout_111_13.setObjectName(u"horizontalLayout_111_13")
        self.label_269 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setMaximumSize(QSize(16777215, 20))
        self.label_269.setFont(font1)

        self.horizontalLayout_111_13.addWidget(self.label_269)

        self.classification_acc_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_acc_min_filter_lineedit.setObjectName(u"classification_acc_min_filter_lineedit")
        self.classification_acc_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_acc_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_acc_min_filter_lineedit.setFont(font1)
        self.classification_acc_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_13.addWidget(self.classification_acc_min_filter_lineedit)


        self.horizontalLayout_286.addLayout(self.horizontalLayout_111_13)

        self.horizontalLayout_121_13 = QHBoxLayout()
        self.horizontalLayout_121_13.setObjectName(u"horizontalLayout_121_13")
        self.label_270 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setMaximumSize(QSize(16777215, 20))
        self.label_270.setFont(font1)

        self.horizontalLayout_121_13.addWidget(self.label_270)

        self.classification_acc_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_acc_max_filter_lineedit.setObjectName(u"classification_acc_max_filter_lineedit")
        self.classification_acc_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_acc_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_acc_max_filter_lineedit.setFont(font1)
        self.classification_acc_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_13.addWidget(self.classification_acc_max_filter_lineedit)


        self.horizontalLayout_286.addLayout(self.horizontalLayout_121_13)


        self.horizontalLayout_285.addLayout(self.horizontalLayout_286)

        self.line_101 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_101.setObjectName(u"line_101")
        self.line_101.setFrameShape(QFrame.HLine)
        self.line_101.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_285.addWidget(self.line_101)


        self.verticalLayout_64.addLayout(self.horizontalLayout_285)

        self.line_110 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_110.setObjectName(u"line_110")
        self.line_110.setFrameShape(QFrame.HLine)
        self.line_110.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_110)

        self.horizontalLayout_287 = QHBoxLayout()
        self.horizontalLayout_287.setSpacing(0)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.LBL_classification_precision_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_classification_precision_in_PBT_page.setObjectName(u"LBL_classification_precision_in_PBT_page")
        self.LBL_classification_precision_in_PBT_page.setFont(font1)

        self.horizontalLayout_287.addWidget(self.LBL_classification_precision_in_PBT_page)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_287.addItem(self.horizontalSpacer_58)

        self.horizontalLayout_288 = QHBoxLayout()
        self.horizontalLayout_288.setSpacing(10)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_111_14 = QHBoxLayout()
        self.horizontalLayout_111_14.setObjectName(u"horizontalLayout_111_14")
        self.label_271 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setMaximumSize(QSize(16777215, 20))
        self.label_271.setFont(font1)

        self.horizontalLayout_111_14.addWidget(self.label_271)

        self.classification_precision_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_precision_min_filter_lineedit.setObjectName(u"classification_precision_min_filter_lineedit")
        self.classification_precision_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_precision_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_precision_min_filter_lineedit.setFont(font1)
        self.classification_precision_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_14.addWidget(self.classification_precision_min_filter_lineedit)


        self.horizontalLayout_288.addLayout(self.horizontalLayout_111_14)

        self.horizontalLayout_121_14 = QHBoxLayout()
        self.horizontalLayout_121_14.setObjectName(u"horizontalLayout_121_14")
        self.label_272 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setMaximumSize(QSize(16777215, 20))
        self.label_272.setFont(font1)

        self.horizontalLayout_121_14.addWidget(self.label_272)

        self.classification_precision_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_precision_max_filter_lineedit.setObjectName(u"classification_precision_max_filter_lineedit")
        self.classification_precision_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_precision_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_precision_max_filter_lineedit.setFont(font1)
        self.classification_precision_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_14.addWidget(self.classification_precision_max_filter_lineedit)


        self.horizontalLayout_288.addLayout(self.horizontalLayout_121_14)


        self.horizontalLayout_287.addLayout(self.horizontalLayout_288)

        self.line_102 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_102.setObjectName(u"line_102")
        self.line_102.setFrameShape(QFrame.HLine)
        self.line_102.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_287.addWidget(self.line_102)


        self.verticalLayout_64.addLayout(self.horizontalLayout_287)

        self.line_109 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_109.setObjectName(u"line_109")
        self.line_109.setFrameShape(QFrame.HLine)
        self.line_109.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_109)

        self.horizontalLayout_289 = QHBoxLayout()
        self.horizontalLayout_289.setSpacing(0)
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.LBL_classification_recall_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_classification_recall_in_PBT_page.setObjectName(u"LBL_classification_recall_in_PBT_page")
        self.LBL_classification_recall_in_PBT_page.setFont(font1)

        self.horizontalLayout_289.addWidget(self.LBL_classification_recall_in_PBT_page)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_289.addItem(self.horizontalSpacer_59)

        self.horizontalLayout_290 = QHBoxLayout()
        self.horizontalLayout_290.setSpacing(10)
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.horizontalLayout_111_15 = QHBoxLayout()
        self.horizontalLayout_111_15.setObjectName(u"horizontalLayout_111_15")
        self.label_273 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setMaximumSize(QSize(16777215, 20))
        self.label_273.setFont(font1)

        self.horizontalLayout_111_15.addWidget(self.label_273)

        self.classification_recall_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_recall_min_filter_lineedit.setObjectName(u"classification_recall_min_filter_lineedit")
        self.classification_recall_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_recall_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_recall_min_filter_lineedit.setFont(font1)
        self.classification_recall_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_15.addWidget(self.classification_recall_min_filter_lineedit)


        self.horizontalLayout_290.addLayout(self.horizontalLayout_111_15)

        self.horizontalLayout_121_15 = QHBoxLayout()
        self.horizontalLayout_121_15.setObjectName(u"horizontalLayout_121_15")
        self.label_274 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setMaximumSize(QSize(16777215, 20))
        self.label_274.setFont(font1)

        self.horizontalLayout_121_15.addWidget(self.label_274)

        self.classification_recall_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_recall_max_filter_lineedit.setObjectName(u"classification_recall_max_filter_lineedit")
        self.classification_recall_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_recall_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_recall_max_filter_lineedit.setFont(font1)
        self.classification_recall_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_15.addWidget(self.classification_recall_max_filter_lineedit)


        self.horizontalLayout_290.addLayout(self.horizontalLayout_121_15)


        self.horizontalLayout_289.addLayout(self.horizontalLayout_290)

        self.line_103 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_103.setObjectName(u"line_103")
        self.line_103.setFrameShape(QFrame.HLine)
        self.line_103.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_289.addWidget(self.line_103)


        self.verticalLayout_64.addLayout(self.horizontalLayout_289)

        self.line_108 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_108.setObjectName(u"line_108")
        self.line_108.setFrameShape(QFrame.HLine)
        self.line_108.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_108)

        self.horizontalLayout_291 = QHBoxLayout()
        self.horizontalLayout_291.setSpacing(0)
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.LBL_classification_f1_in_PBT_page = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_classification_f1_in_PBT_page.setObjectName(u"LBL_classification_f1_in_PBT_page")
        self.LBL_classification_f1_in_PBT_page.setFont(font1)

        self.horizontalLayout_291.addWidget(self.LBL_classification_f1_in_PBT_page)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_291.addItem(self.horizontalSpacer_60)

        self.horizontalLayout_292 = QHBoxLayout()
        self.horizontalLayout_292.setSpacing(10)
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.horizontalLayout_111_16 = QHBoxLayout()
        self.horizontalLayout_111_16.setObjectName(u"horizontalLayout_111_16")
        self.label_275 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setMaximumSize(QSize(16777215, 20))
        self.label_275.setFont(font1)

        self.horizontalLayout_111_16.addWidget(self.label_275)

        self.classification_f1_min_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_f1_min_filter_lineedit.setObjectName(u"classification_f1_min_filter_lineedit")
        self.classification_f1_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_f1_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_f1_min_filter_lineedit.setFont(font1)
        self.classification_f1_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_16.addWidget(self.classification_f1_min_filter_lineedit)


        self.horizontalLayout_292.addLayout(self.horizontalLayout_111_16)

        self.horizontalLayout_121_16 = QHBoxLayout()
        self.horizontalLayout_121_16.setObjectName(u"horizontalLayout_121_16")
        self.label_276 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setMaximumSize(QSize(16777215, 20))
        self.label_276.setFont(font1)

        self.horizontalLayout_121_16.addWidget(self.label_276)

        self.classification_f1_max_filter_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.classification_f1_max_filter_lineedit.setObjectName(u"classification_f1_max_filter_lineedit")
        self.classification_f1_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.classification_f1_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.classification_f1_max_filter_lineedit.setFont(font1)
        self.classification_f1_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_16.addWidget(self.classification_f1_max_filter_lineedit)


        self.horizontalLayout_292.addLayout(self.horizontalLayout_121_16)


        self.horizontalLayout_291.addLayout(self.horizontalLayout_292)

        self.line_104 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_104.setObjectName(u"line_104")
        self.line_104.setFrameShape(QFrame.HLine)
        self.line_104.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_291.addWidget(self.line_104)


        self.verticalLayout_64.addLayout(self.horizontalLayout_291)

        self.line_107 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_107.setObjectName(u"line_107")
        self.line_107.setFrameShape(QFrame.HLine)
        self.line_107.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_107)

        self.horizontalLayout_197_215 = QHBoxLayout()
        self.horizontalLayout_197_215.setSpacing(5)
        self.horizontalLayout_197_215.setObjectName(u"horizontalLayout_197_215")
        self.label_291 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setMaximumSize(QSize(16777215, 20))
        self.label_291.setFont(font1)

        self.horizontalLayout_197_215.addWidget(self.label_291)

        self.pipline_year_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.pipline_year_lineedit.setObjectName(u"pipline_year_lineedit")
        self.pipline_year_lineedit.setMinimumSize(QSize(55, 0))
        self.pipline_year_lineedit.setMaximumSize(QSize(55, 30))
        self.pipline_year_lineedit.setFont(font1)
        self.pipline_year_lineedit.setMaxLength(4)

        self.horizontalLayout_197_215.addWidget(self.pipline_year_lineedit)

        self.label_292 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setMinimumSize(QSize(5, 0))
        self.label_292.setMaximumSize(QSize(5, 20))
        self.label_292.setFont(font1)

        self.horizontalLayout_197_215.addWidget(self.label_292)

        self.pipline_month_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.pipline_month_lineedit.setObjectName(u"pipline_month_lineedit")
        self.pipline_month_lineedit.setMinimumSize(QSize(30, 0))
        self.pipline_month_lineedit.setMaximumSize(QSize(30, 30))
        self.pipline_month_lineedit.setFont(font1)
        self.pipline_month_lineedit.setMaxLength(2)

        self.horizontalLayout_197_215.addWidget(self.pipline_month_lineedit)

        self.label_293 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setMinimumSize(QSize(5, 0))
        self.label_293.setMaximumSize(QSize(5, 20))
        self.label_293.setFont(font1)

        self.horizontalLayout_197_215.addWidget(self.label_293)

        self.pipline_day_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.pipline_day_lineedit.setObjectName(u"pipline_day_lineedit")
        self.pipline_day_lineedit.setMinimumSize(QSize(30, 0))
        self.pipline_day_lineedit.setMaximumSize(QSize(30, 30))
        self.pipline_day_lineedit.setFont(font1)
        self.pipline_day_lineedit.setMaxLength(2)

        self.horizontalLayout_197_215.addWidget(self.pipline_day_lineedit)


        self.verticalLayout_64.addLayout(self.horizontalLayout_197_215)

        self.line_106 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_106.setObjectName(u"line_106")
        self.line_106.setFrameShape(QFrame.HLine)
        self.line_106.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_64.addWidget(self.line_106)

        self.horizontalLayout_197_216 = QHBoxLayout()
        self.horizontalLayout_197_216.setSpacing(5)
        self.horizontalLayout_197_216.setObjectName(u"horizontalLayout_197_216")
        self.label_294 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setMaximumSize(QSize(200, 20))
        self.label_294.setFont(font1)

        self.horizontalLayout_197_216.addWidget(self.label_294)

        self.pipline_hour_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.pipline_hour_lineedit.setObjectName(u"pipline_hour_lineedit")
        self.pipline_hour_lineedit.setMinimumSize(QSize(30, 0))
        self.pipline_hour_lineedit.setMaximumSize(QSize(30, 30))
        self.pipline_hour_lineedit.setFont(font1)
        self.pipline_hour_lineedit.setMaxLength(2)

        self.horizontalLayout_197_216.addWidget(self.pipline_hour_lineedit)

        self.label_296 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setMinimumSize(QSize(5, 0))
        self.label_296.setMaximumSize(QSize(5, 20))
        self.label_296.setFont(font1)

        self.horizontalLayout_197_216.addWidget(self.label_296)

        self.pipline_minut_lineedit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.pipline_minut_lineedit.setObjectName(u"pipline_minut_lineedit")
        self.pipline_minut_lineedit.setMinimumSize(QSize(30, 0))
        self.pipline_minut_lineedit.setMaximumSize(QSize(30, 30))
        self.pipline_minut_lineedit.setFont(font1)
        self.pipline_minut_lineedit.setMaxLength(2)

        self.horizontalLayout_197_216.addWidget(self.pipline_minut_lineedit)


        self.verticalLayout_64.addLayout(self.horizontalLayout_197_216)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_65.addWidget(self.scrollArea_3)

        self.frame_37 = QFrame(self.frame_3)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.BTN_clear_filter_in_PBT = QPushButton(self.frame_37)
        self.BTN_clear_filter_in_PBT.setObjectName(u"BTN_clear_filter_in_PBT")
        self.BTN_clear_filter_in_PBT.setMinimumSize(QSize(0, 30))
        self.BTN_clear_filter_in_PBT.setMaximumSize(QSize(16777215, 30))
        self.BTN_clear_filter_in_PBT.setStyleSheet(u"color:white;")

        self.horizontalLayout_63.addWidget(self.BTN_clear_filter_in_PBT)

        self.BTN_search_and_filter_in_PBT = QPushButton(self.frame_37)
        self.BTN_search_and_filter_in_PBT.setObjectName(u"BTN_search_and_filter_in_PBT")
        self.BTN_search_and_filter_in_PBT.setMinimumSize(QSize(0, 30))
        self.BTN_search_and_filter_in_PBT.setMaximumSize(QSize(16777215, 30))
        self.BTN_search_and_filter_in_PBT.setStyleSheet(u"color:white;")

        self.horizontalLayout_63.addWidget(self.BTN_search_and_filter_in_PBT)


        self.verticalLayout_65.addWidget(self.frame_37)


        self.horizontalLayout_73.addWidget(self.frame_3)

        self.frame_38 = QFrame(self.page_history)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97_4 = QVBoxLayout(self.frame_38)
        self.verticalLayout_97_4.setObjectName(u"verticalLayout_97_4")
        self.pipline_history_tabel = QTableWidget(self.frame_38)
        if (self.pipline_history_tabel.columnCount() < 19):
            self.pipline_history_tabel.setColumnCount(19)
        self.pipline_history_tabel.setObjectName(u"pipline_history_tabel")
        self.pipline_history_tabel.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.pipline_history_tabel.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.pipline_history_tabel.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.pipline_history_tabel.setGridStyle(Qt.DotLine)
        self.pipline_history_tabel.setRowCount(0)
        self.pipline_history_tabel.setColumnCount(19)
        self.pipline_history_tabel.horizontalHeader().setMinimumSectionSize(120)
        self.pipline_history_tabel.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_97_4.addWidget(self.pipline_history_tabel)

        self.frame_68_5 = QFrame(self.frame_38)
        self.frame_68_5.setObjectName(u"frame_68_5")
        self.frame_68_5.setFrameShape(QFrame.StyledPanel)
        self.frame_68_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_68_5)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.pipline_table_refresh_btn = QPushButton(self.frame_68_5)
        self.pipline_table_refresh_btn.setObjectName(u"pipline_table_refresh_btn")
        self.pipline_table_refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pipline_table_refresh_btn.setLayoutDirection(Qt.RightToLeft)
        self.pipline_table_refresh_btn.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        icon25 = QIcon()
        icon25.addFile(u"images/free-arrows-refresh-icon-2847-thumb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pipline_table_refresh_btn.setIcon(icon25)
        self.pipline_table_refresh_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_84.addWidget(self.pipline_table_refresh_btn)

        self.line_115 = QFrame(self.frame_68_5)
        self.line_115.setObjectName(u"line_115")
        self.line_115.setFrameShape(QFrame.VLine)
        self.line_115.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_84.addWidget(self.line_115)

        self.pipline_tabel_prev_PBT = QPushButton(self.frame_68_5)
        self.pipline_tabel_prev_PBT.setObjectName(u"pipline_tabel_prev_PBT")
        self.pipline_tabel_prev_PBT.setEnabled(False)
        self.pipline_tabel_prev_PBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.pipline_tabel_prev_PBT.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.pipline_tabel_prev_PBT.setIcon(icon16)
        self.pipline_tabel_prev_PBT.setIconSize(QSize(30, 30))

        self.horizontalLayout_84.addWidget(self.pipline_tabel_prev_PBT)

        self.lineEdit_in_history_of_pipline = QLineEdit(self.frame_68_5)
        self.lineEdit_in_history_of_pipline.setObjectName(u"lineEdit_in_history_of_pipline")
        self.lineEdit_in_history_of_pipline.setEnabled(False)
        self.lineEdit_in_history_of_pipline.setMinimumSize(QSize(50, 30))
        self.lineEdit_in_history_of_pipline.setMaximumSize(QSize(50, 30))
        self.lineEdit_in_history_of_pipline.setStyleSheet(u"padding:0;")
        self.lineEdit_in_history_of_pipline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_84.addWidget(self.lineEdit_in_history_of_pipline)

        self.pipline_tabel_next_PBT = QPushButton(self.frame_68_5)
        self.pipline_tabel_next_PBT.setObjectName(u"pipline_tabel_next_PBT")
        self.pipline_tabel_next_PBT.setEnabled(False)
        self.pipline_tabel_next_PBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.pipline_tabel_next_PBT.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.pipline_tabel_next_PBT.setIcon(icon15)
        self.pipline_tabel_next_PBT.setIconSize(QSize(30, 30))

        self.horizontalLayout_84.addWidget(self.pipline_tabel_next_PBT)

        self.line_116 = QFrame(self.frame_68_5)
        self.line_116.setObjectName(u"line_116")
        self.line_116.setFrameShape(QFrame.VLine)
        self.line_116.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_84.addWidget(self.line_116)

        self.binary_tabel_label_3 = QLabel(self.frame_68_5)
        self.binary_tabel_label_3.setObjectName(u"binary_tabel_label_3")
        self.binary_tabel_label_3.setMinimumSize(QSize(600, 0))
        self.binary_tabel_label_3.setMaximumSize(QSize(600, 16777215))
        self.binary_tabel_label_3.setFrameShape(QFrame.Panel)
        self.binary_tabel_label_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_84.addWidget(self.binary_tabel_label_3)

        self.horizontalSpacer_20_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_20_5)


        self.verticalLayout_97_4.addWidget(self.frame_68_5)


        self.horizontalLayout_73.addWidget(self.frame_38)

        self.stackedWidget_pbt.addWidget(self.page_history)

        self.verticalLayout_78.addWidget(self.stackedWidget_pbt)

        self.stackedWidget.addWidget(self.page_pbt)
        self.page_Binary = QWidget()
        self.page_Binary.setObjectName(u"page_Binary")
        self.verticalLayout_22 = QVBoxLayout(self.page_Binary)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
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
        self.binary_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170 ,170, 170); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 ,195, 196);\n"
"}")

        self.horizontalLayout_8.addWidget(self.binary_list)

        self.binary_training = QPushButton(self.frame_4)
        self.binary_training.setObjectName(u"binary_training")
        self.binary_training.setMinimumSize(QSize(150, 40))
        self.binary_training.setMaximumSize(QSize(150, 16777215))
        self.binary_training.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_training.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(100, 100, 100); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"} \n"
"QPushButton:hover {\n"
"	background-color:  rgb(150 ,150, 150);\n"
"}")

        self.horizontalLayout_8.addWidget(self.binary_training)

        self.binary_history = QPushButton(self.frame_4)
        self.binary_history.setObjectName(u"binary_history")
        self.binary_history.setMinimumSize(QSize(150, 40))
        self.binary_history.setMaximumSize(QSize(150, 16777215))
        self.binary_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_history.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(100, 100, 100); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"} \n"
"QPushButton:hover {\n"
"	background-color:  rgb(150 ,150, 150);\n"
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
        self.verticalLayout_71 = QVBoxLayout(self.page_binary_list)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.page_binary_list)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31_1232 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_31_1232.setSpacing(5)
        self.horizontalLayout_31_1232.setObjectName(u"horizontalLayout_31_1232")
        self.horizontalLayout_31_1232.setContentsMargins(9, 9, 9, 9)
        self.frame_70 = QFrame(self.frame_52)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.Box)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48_12321 = QVBoxLayout(self.frame_70)
        self.verticalLayout_48_12321.setSpacing(5)
        self.verticalLayout_48_12321.setObjectName(u"verticalLayout_48_12321")
        self.verticalLayout_48_12321.setContentsMargins(0, 0, 0, 0)
        self.frame_91_123 = QFrame(self.frame_70)
        self.frame_91_123.setObjectName(u"frame_91_123")
        self.frame_91_123.setMinimumSize(QSize(0, 300))
        self.frame_91_123.setMaximumSize(QSize(16777215, 300))
        self.frame_91_123.setFrameShape(QFrame.StyledPanel)
        self.frame_91_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51_12433 = QVBoxLayout(self.frame_91_123)
        self.verticalLayout_51_12433.setSpacing(0)
        self.verticalLayout_51_12433.setObjectName(u"verticalLayout_51_12433")
        self.verticalLayout_51_12433.setContentsMargins(0, 0, 0, 0)
        self.datasets_table_binarylist = QTableWidget(self.frame_91_123)
        if (self.datasets_table_binarylist.columnCount() < 3):
            self.datasets_table_binarylist.setColumnCount(3)
        self.datasets_table_binarylist.setObjectName(u"datasets_table_binarylist")
        self.datasets_table_binarylist.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.datasets_table_binarylist.setColumnCount(3)
        self.datasets_table_binarylist.horizontalHeader().setCascadingSectionResizes(True)
        self.datasets_table_binarylist.horizontalHeader().setMinimumSectionSize(200)
        self.datasets_table_binarylist.horizontalHeader().setDefaultSectionSize(250)
        self.datasets_table_binarylist.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_51_12433.addWidget(self.datasets_table_binarylist)

        self.frame_94_213213 = QFrame(self.frame_91_123)
        self.frame_94_213213.setObjectName(u"frame_94_213213")
        self.frame_94_213213.setFrameShape(QFrame.NoFrame)
        self.frame_94_213213.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42_123213 = QHBoxLayout(self.frame_94_213213)
        self.horizontalLayout_42_123213.setSpacing(0)
        self.horizontalLayout_42_123213.setObjectName(u"horizontalLayout_42_123213")
        self.horizontalLayout_42_123213.setContentsMargins(0, 0, 0, 0)
        self.frame_95_123213 = QFrame(self.frame_94_213213)
        self.frame_95_123213.setObjectName(u"frame_95_123213")
        self.frame_95_123213.setMinimumSize(QSize(0, 40))
        self.frame_95_123213.setMaximumSize(QSize(16777215, 40))
        self.frame_95_123213.setFrameShape(QFrame.Panel)
        self.frame_95_123213.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41_34234 = QHBoxLayout(self.frame_95_123213)
        self.horizontalLayout_41_34234.setSpacing(10)
        self.horizontalLayout_41_34234.setObjectName(u"horizontalLayout_41_34234")
        self.horizontalLayout_41_34234.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_46_213213 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41_34234.addItem(self.horizontalSpacer_46_213213)

        self.binary_list_show_btn = QPushButton(self.frame_95_123213)
        self.binary_list_show_btn.setObjectName(u"binary_list_show_btn")
        self.binary_list_show_btn.setMinimumSize(QSize(80, 30))
        self.binary_list_show_btn.setMaximumSize(QSize(80, 30))
        self.binary_list_show_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_41_34234.addWidget(self.binary_list_show_btn)

        self.line_12_21321 = QFrame(self.frame_95_123213)
        self.line_12_21321.setObjectName(u"line_12_21321")
        self.line_12_21321.setFrameShape(QFrame.VLine)
        self.line_12_21321.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_41_34234.addWidget(self.line_12_21321)

        self.warning_binarylist_page = QLabel(self.frame_95_123213)
        self.warning_binarylist_page.setObjectName(u"warning_binarylist_page")
        self.warning_binarylist_page.setMinimumSize(QSize(600, 30))
        self.warning_binarylist_page.setMaximumSize(QSize(600, 30))
        self.warning_binarylist_page.setFrameShape(QFrame.Panel)
        self.warning_binarylist_page.setFrameShadow(QFrame.Sunken)
        self.warning_binarylist_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41_34234.addWidget(self.warning_binarylist_page)

        self.horizontalSpacer_47_12321 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41_34234.addItem(self.horizontalSpacer_47_12321)


        self.horizontalLayout_42_123213.addWidget(self.frame_95_123213)


        self.verticalLayout_51_12433.addWidget(self.frame_94_213213)


        self.verticalLayout_48_12321.addWidget(self.frame_91_123)

        self.frame_89_123 = QFrame(self.frame_70)
        self.frame_89_123.setObjectName(u"frame_89_123")
        self.frame_89_123.setFrameShape(QFrame.StyledPanel)
        self.frame_89_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50_21321 = QVBoxLayout(self.frame_89_123)
        self.verticalLayout_50_21321.setSpacing(5)
        self.verticalLayout_50_21321.setObjectName(u"verticalLayout_50_21321")
        self.verticalLayout_50_21321.setContentsMargins(0, 0, 0, 0)
        self.frame_93_1223 = QFrame(self.frame_89_123)
        self.frame_93_1223.setObjectName(u"frame_93_1223")
        self.frame_93_1223.setFrameShape(QFrame.Panel)
        self.frame_93_1223.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40_12312 = QHBoxLayout(self.frame_93_1223)
        self.horizontalLayout_40_12312.setSpacing(5)
        self.horizontalLayout_40_12312.setObjectName(u"horizontalLayout_40_12312")
        self.horizontalLayout_40_12312.setContentsMargins(5, 5, 5, 5)
        self.binary_list_perfect_prev_btn = QPushButton(self.frame_93_1223)
        self.binary_list_perfect_prev_btn.setObjectName(u"binary_list_perfect_prev_btn")
        self.binary_list_perfect_prev_btn.setEnabled(False)
        self.binary_list_perfect_prev_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_perfect_prev_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_perfect_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_perfect_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.binary_list_perfect_prev_btn.setIcon(icon16)
        self.binary_list_perfect_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_40_12312.addWidget(self.binary_list_perfect_prev_btn)

        self.binary_list_perfect_frame = QLabel(self.frame_93_1223)
        self.binary_list_perfect_frame.setObjectName(u"binary_list_perfect_frame")
        self.binary_list_perfect_frame.setStyleSheet(u"border: 3px solid rgb(78, 154, 6);")
        self.binary_list_perfect_frame.setFrameShape(QFrame.Panel)
        self.binary_list_perfect_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_40_12312.addWidget(self.binary_list_perfect_frame)

        self.binary_list_perfect_next_btn = QPushButton(self.frame_93_1223)
        self.binary_list_perfect_next_btn.setObjectName(u"binary_list_perfect_next_btn")
        self.binary_list_perfect_next_btn.setEnabled(False)
        self.binary_list_perfect_next_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_perfect_next_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_perfect_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_perfect_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.binary_list_perfect_next_btn.setIcon(icon15)
        self.binary_list_perfect_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_40_12312.addWidget(self.binary_list_perfect_next_btn)


        self.verticalLayout_50_21321.addWidget(self.frame_93_1223)

        self.frame_92_1_23 = QFrame(self.frame_89_123)
        self.frame_92_1_23.setObjectName(u"frame_92_1_23")
        self.frame_92_1_23.setFrameShape(QFrame.Panel)
        self.frame_92_1_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32_1232 = QHBoxLayout(self.frame_92_1_23)
        self.horizontalLayout_32_1232.setSpacing(5)
        self.horizontalLayout_32_1232.setObjectName(u"horizontalLayout_32_1232")
        self.horizontalLayout_32_1232.setContentsMargins(5, 5, 5, 5)
        self.binary_list_defect_prev_btn = QPushButton(self.frame_92_1_23)
        self.binary_list_defect_prev_btn.setObjectName(u"binary_list_defect_prev_btn")
        self.binary_list_defect_prev_btn.setEnabled(False)
        self.binary_list_defect_prev_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_defect_prev_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_defect_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_defect_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.binary_list_defect_prev_btn.setIcon(icon16)
        self.binary_list_defect_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_32_1232.addWidget(self.binary_list_defect_prev_btn)

        self.binary_list_defect_frame = QLabel(self.frame_92_1_23)
        self.binary_list_defect_frame.setObjectName(u"binary_list_defect_frame")
        self.binary_list_defect_frame.setStyleSheet(u"border: 3px solid #ff0000;\n"
"border-color: rgb(164, 0, 0);")
        self.binary_list_defect_frame.setFrameShape(QFrame.Panel)
        self.binary_list_defect_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_32_1232.addWidget(self.binary_list_defect_frame)

        self.binary_list_defect_next_btn = QPushButton(self.frame_92_1_23)
        self.binary_list_defect_next_btn.setObjectName(u"binary_list_defect_next_btn")
        self.binary_list_defect_next_btn.setEnabled(False)
        self.binary_list_defect_next_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_defect_next_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_defect_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_defect_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.binary_list_defect_next_btn.setIcon(icon15)
        self.binary_list_defect_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_32_1232.addWidget(self.binary_list_defect_next_btn)


        self.verticalLayout_50_21321.addWidget(self.frame_92_1_23)


        self.verticalLayout_48_12321.addWidget(self.frame_89_123)


        self.horizontalLayout_31_1232.addWidget(self.frame_70)

        self.frame_88_1232 = QFrame(self.frame_52)
        self.frame_88_1232.setObjectName(u"frame_88_1232")
        self.frame_88_1232.setMinimumSize(QSize(400, 0))
        self.frame_88_1232.setMaximumSize(QSize(400, 16777215))
        self.frame_88_1232.setFrameShape(QFrame.Panel)
        self.frame_88_1232.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59_123 = QVBoxLayout(self.frame_88_1232)
        self.verticalLayout_59_123.setSpacing(0)
        self.verticalLayout_59_123.setObjectName(u"verticalLayout_59_123")
        self.verticalLayout_59_123.setContentsMargins(0, 0, 0, 0)
        self.frame_96_123 = QFrame(self.frame_88_1232)
        self.frame_96_123.setObjectName(u"frame_96_123")
        self.frame_96_123.setMinimumSize(QSize(400, 0))
        self.frame_96_123.setMaximumSize(QSize(400, 16777215))
        self.frame_96_123.setFrameShape(QFrame.Box)
        self.frame_96_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58_123123 = QVBoxLayout(self.frame_96_123)
        self.verticalLayout_58_123123.setSpacing(5)
        self.verticalLayout_58_123123.setObjectName(u"verticalLayout_58_123123")
        self.verticalLayout_58_123123.setContentsMargins(0, 0, 0, 0)
        self.frame_443 = QFrame(self.frame_96_123)
        self.frame_443.setObjectName(u"frame_443")
        self.frame_443.setMinimumSize(QSize(0, 0))
        self.frame_443.setMaximumSize(QSize(16777215, 16777215))
        self.frame_443.setFrameShape(QFrame.Panel)
        self.frame_443.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_443)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.binarylist_chart_frame = QGroupBox(self.frame_443)
        self.binarylist_chart_frame.setObjectName(u"binarylist_chart_frame")
        self.binarylist_chart_frame.setMinimumSize(QSize(0, 267))

        self.verticalLayout_109.addWidget(self.binarylist_chart_frame)

        self.binarylist_chart_frame_2 = QGroupBox(self.frame_443)
        self.binarylist_chart_frame_2.setObjectName(u"binarylist_chart_frame_2")
        self.binarylist_chart_frame_2.setMinimumSize(QSize(0, 266))

        self.verticalLayout_109.addWidget(self.binarylist_chart_frame_2)


        self.verticalLayout_58_123123.addWidget(self.frame_443)


        self.verticalLayout_59_123.addWidget(self.frame_96_123)


        self.horizontalLayout_31_1232.addWidget(self.frame_88_1232)


        self.verticalLayout_71.addWidget(self.frame_52)

        self.stackedWidget_binary.addWidget(self.page_binary_list)
        self.page_binary_training = QWidget()
        self.page_binary_training.setObjectName(u"page_binary_training")
        self.horizontalLayout_126 = QHBoxLayout(self.page_binary_training)
        self.horizontalLayout_126.setSpacing(6)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(9, 9, 9, 9)
        self.frame_56 = QFrame(self.page_binary_training)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy10)
        self.frame_56.setMinimumSize(QSize(350, 50))
        self.frame_56.setMaximumSize(QSize(320, 16777215))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_56)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy2.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy2)
        self.frame_57.setMinimumSize(QSize(330, 50))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_57)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.label_137 = QLabel(self.frame_57)
        self.label_137.setObjectName(u"label_137")

        self.horizontalLayout_127.addWidget(self.label_137, 0, Qt.AlignLeft)

        self.b_algorithms = QComboBox(self.frame_57)
        self.b_algorithms.setObjectName(u"b_algorithms")

        self.horizontalLayout_127.addWidget(self.b_algorithms)


        self.verticalLayout_82.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_144 = QLabel(self.frame_57)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_128.addWidget(self.label_144)

        self.input_size1 = QSpinBox(self.frame_57)
        self.input_size1.setObjectName(u"input_size1")
        self.input_size1.setMinimum(64)
        self.input_size1.setMaximum(2048)
        self.input_size1.setSingleStep(32)
        self.input_size1.setValue(256)

        self.horizontalLayout_128.addWidget(self.input_size1)

        self.label_298 = QLabel(self.frame_57)
        self.label_298.setObjectName(u"label_298")
        sizePolicy.setHeightForWidth(self.label_298.sizePolicy().hasHeightForWidth())
        self.label_298.setSizePolicy(sizePolicy)

        self.horizontalLayout_128.addWidget(self.label_298)

        self.input_size2 = QSpinBox(self.frame_57)
        self.input_size2.setObjectName(u"input_size2")
        self.input_size2.setMinimum(64)
        self.input_size2.setMaximum(2048)
        self.input_size2.setSingleStep(32)
        self.input_size2.setValue(256)

        self.horizontalLayout_128.addWidget(self.input_size2)


        self.verticalLayout_82.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.label_7 = QLabel(self.frame_57)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_129.addWidget(self.label_7)

        self.input_type_resize = QRadioButton(self.frame_57)
        self.input_type_resize.setObjectName(u"input_type_resize")
        self.input_type_resize.setStyleSheet(u"")

        self.horizontalLayout_129.addWidget(self.input_type_resize)

        self.input_type_split = QRadioButton(self.frame_57)
        self.input_type_split.setObjectName(u"input_type_split")
        self.input_type_split.setStyleSheet(u"")

        self.horizontalLayout_129.addWidget(self.input_type_split)


        self.verticalLayout_82.addLayout(self.horizontalLayout_129)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_138 = QLabel(self.frame_57)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_130.addWidget(self.label_138, 0, Qt.AlignLeft)

        self.b_epochs = QLineEdit(self.frame_57)
        self.b_epochs.setObjectName(u"b_epochs")
        self.b_epochs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_130.addWidget(self.b_epochs)


        self.verticalLayout_82.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.label_139 = QLabel(self.frame_57)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_131.addWidget(self.label_139, 0, Qt.AlignLeft)

        self.b_batch = QLineEdit(self.frame_57)
        self.b_batch.setObjectName(u"b_batch")
        self.b_batch.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_131.addWidget(self.b_batch)


        self.verticalLayout_82.addLayout(self.horizontalLayout_131)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.label_140 = QLabel(self.frame_57)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_132.addWidget(self.label_140)

        self.b_lr = QLineEdit(self.frame_57)
        self.b_lr.setObjectName(u"b_lr")
        self.b_lr.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_132.addWidget(self.b_lr)


        self.verticalLayout_82.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.label_141 = QLabel(self.frame_57)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_133.addWidget(self.label_141)

        self.b_te = QLineEdit(self.frame_57)
        self.b_te.setObjectName(u"b_te")
        self.b_te.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_133.addWidget(self.b_te)


        self.verticalLayout_82.addLayout(self.horizontalLayout_133)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.label_142 = QLabel(self.frame_57)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_134.addWidget(self.label_142)

        self.b_vs = QLineEdit(self.frame_57)
        self.b_vs.setObjectName(u"b_vs")
        self.b_vs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_134.addWidget(self.b_vs)


        self.verticalLayout_82.addLayout(self.horizontalLayout_134)

        self.horizontalLayout_321 = QHBoxLayout()
        self.horizontalLayout_321.setObjectName(u"horizontalLayout_321")
        self.label_130 = QLabel(self.frame_57)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_321.addWidget(self.label_130)

        self.b_gpu = QComboBox(self.frame_57)
        self.b_gpu.addItem("")
        self.b_gpu.addItem("")
        self.b_gpu.addItem("")
        self.b_gpu.addItem("")
        self.b_gpu.setObjectName(u"b_gpu")

        self.horizontalLayout_321.addWidget(self.b_gpu)


        self.verticalLayout_82.addLayout(self.horizontalLayout_321)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.label_143 = QLabel(self.frame_57)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_135.addWidget(self.label_143)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_21)

        self.b_select_dp = QPushButton(self.frame_57)
        self.b_select_dp.setObjectName(u"b_select_dp")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.b_select_dp.sizePolicy().hasHeightForWidth())
        self.b_select_dp.setSizePolicy(sizePolicy11)
        self.b_select_dp.setMinimumSize(QSize(120, 0))
        self.b_select_dp.setStyleSheet(u"color:white;")

        self.horizontalLayout_135.addWidget(self.b_select_dp)


        self.verticalLayout_82.addLayout(self.horizontalLayout_135)

        self.b_dp = QTextEdit(self.frame_57)
        self.b_dp.setObjectName(u"b_dp")
        sizePolicy.setHeightForWidth(self.b_dp.sizePolicy().hasHeightForWidth())
        self.b_dp.setSizePolicy(sizePolicy)
        self.b_dp.setMinimumSize(QSize(20, 20))
        self.b_dp.setMaximumSize(QSize(310, 16777215))
        self.b_dp.setStyleSheet(u"")
        self.b_dp.setReadOnly(True)

        self.verticalLayout_82.addWidget(self.b_dp)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.b_ds_num = QSpinBox(self.frame_57)
        self.b_ds_num.setObjectName(u"b_ds_num")
        self.b_ds_num.setMaximumSize(QSize(140, 16777215))
        self.b_ds_num.setMinimum(1)

        self.horizontalLayout_136.addWidget(self.b_ds_num)

        self.b_delete_ds = QPushButton(self.frame_57)
        self.b_delete_ds.setObjectName(u"b_delete_ds")
        self.b_delete_ds.setMaximumSize(QSize(65, 16777215))
        self.b_delete_ds.setStyleSheet(u"color:white;")

        self.horizontalLayout_136.addWidget(self.b_delete_ds)

        self.b_add_ds = QPushButton(self.frame_57)
        self.b_add_ds.setObjectName(u"b_add_ds")
        self.b_add_ds.setMaximumSize(QSize(65, 16777215))
        self.b_add_ds.setStyleSheet(u"color:white;")

        self.horizontalLayout_136.addWidget(self.b_add_ds)


        self.verticalLayout_82.addLayout(self.horizontalLayout_136)


        self.verticalLayout_81.addWidget(self.frame_57)

        self.b_add_ds_frame = QFrame(self.frame_56)
        self.b_add_ds_frame.setObjectName(u"b_add_ds_frame")
        self.b_add_ds_frame.setMaximumSize(QSize(16777215, 0))
        self.b_add_ds_frame.setFrameShape(QFrame.StyledPanel)
        self.b_add_ds_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.b_add_ds_frame)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.b_add_ds_lineedit = QLineEdit(self.b_add_ds_frame)
        self.b_add_ds_lineedit.setObjectName(u"b_add_ds_lineedit")
        sizePolicy2.setHeightForWidth(self.b_add_ds_lineedit.sizePolicy().hasHeightForWidth())
        self.b_add_ds_lineedit.setSizePolicy(sizePolicy2)
        self.b_add_ds_lineedit.setMaximumSize(QSize(280, 16777215))

        self.verticalLayout_83.addWidget(self.b_add_ds_lineedit)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.b_add_ok = QPushButton(self.b_add_ds_frame)
        self.b_add_ok.setObjectName(u"b_add_ok")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.b_add_ok.sizePolicy().hasHeightForWidth())
        self.b_add_ok.setSizePolicy(sizePolicy12)
        self.b_add_ok.setMinimumSize(QSize(0, 20))
        self.b_add_ok.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_137.addWidget(self.b_add_ok)

        self.b_add_cancel = QPushButton(self.b_add_ds_frame)
        self.b_add_cancel.setObjectName(u"b_add_cancel")
        self.b_add_cancel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_137.addWidget(self.b_add_cancel)


        self.verticalLayout_83.addLayout(self.horizontalLayout_137)


        self.verticalLayout_81.addWidget(self.b_add_ds_frame)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_81.addItem(self.verticalSpacer_10)

        self.frame_66 = QFrame(self.frame_56)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_66)
        self.verticalLayout_47.setSpacing(20)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.binary_train = QPushButton(self.frame_66)
        self.binary_train.setObjectName(u"binary_train")
        self.binary_train.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.binary_train.sizePolicy().hasHeightForWidth())
        self.binary_train.setSizePolicy(sizePolicy1)
        self.binary_train.setMinimumSize(QSize(180, 35))
        self.binary_train.setMaximumSize(QSize(16777215, 16777215))
        self.binary_train.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_train.setAcceptDrops(False)
        self.binary_train.setToolTipDuration(-1)
        self.binary_train.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.binary_train.setAutoDefault(False)

        self.verticalLayout_47.addWidget(self.binary_train, 0, Qt.AlignHCenter)

        self.binary_chart_checkbox = QCheckBox(self.frame_66)
        self.binary_chart_checkbox.setObjectName(u"binary_chart_checkbox")
        self.binary_chart_checkbox.setEnabled(False)
        self.binary_chart_checkbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_47.addWidget(self.binary_chart_checkbox, 0, Qt.AlignHCenter)

        self.binary_train_progressBar = QProgressBar(self.frame_66)
        self.binary_train_progressBar.setObjectName(u"binary_train_progressBar")
        self.binary_train_progressBar.setValue(0)

        self.verticalLayout_47.addWidget(self.binary_train_progressBar)


        self.verticalLayout_81.addWidget(self.frame_66)

        self.warning_train_page = QTextEdit(self.frame_56)
        self.warning_train_page.setObjectName(u"warning_train_page")
        self.warning_train_page.setStyleSheet(u"")
        self.warning_train_page.setReadOnly(True)

        self.verticalLayout_81.addWidget(self.warning_train_page)


        self.horizontalLayout_126.addWidget(self.frame_56)

        self.frame_68 = QFrame(self.page_binary_training)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_68)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_67)

        self.frame_72 = QFrame(self.frame_68)
        self.frame_72.setObjectName(u"frame_72")
        sizePolicy10.setHeightForWidth(self.frame_72.sizePolicy().hasHeightForWidth())
        self.frame_72.setSizePolicy(sizePolicy10)
        self.frame_72.setMaximumSize(QSize(16777215, 20))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_296 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.horizontalLayout_296.setContentsMargins(0, 0, 0, 0)
        self.label_295 = QLabel(self.frame_72)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setMaximumSize(QSize(15, 15))
        self.label_295.setPixmap(QPixmap(u"images/train_iamge.jpg"))

        self.horizontalLayout_296.addWidget(self.label_295)

        self.label_8_2 = QLabel(self.frame_72)
        self.label_8_2.setObjectName(u"label_8_2")
        self.label_8_2.setFont(font1)

        self.horizontalLayout_296.addWidget(self.label_8_2)

        self.horizontalSpacer_19_5 = QSpacerItem(47, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_296.addItem(self.horizontalSpacer_19_5)

        self.label_13_4 = QLabel(self.frame_72)
        self.label_13_4.setObjectName(u"label_13_4")
        self.label_13_4.setMaximumSize(QSize(15, 15))
        self.label_13_4.setPixmap(QPixmap(u"images/val_iamge.jpg"))

        self.horizontalLayout_296.addWidget(self.label_13_4)

        self.label_11 = QLabel(self.frame_72)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_296.addWidget(self.label_11)


        self.horizontalLayout_101.addWidget(self.frame_72)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_66)


        self.verticalLayout_54.addLayout(self.horizontalLayout_101)

        self.frame_114 = QFrame(self.frame_68)
        self.frame_114.setObjectName(u"frame_114")
        sizePolicy4.setHeightForWidth(self.frame_114.sizePolicy().hasHeightForWidth())
        self.frame_114.setSizePolicy(sizePolicy4)
        self.frame_114.setMaximumSize(QSize(16777215, 16777215))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_114)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.binary_chart_loss_frame = QFrame(self.frame_114)
        self.binary_chart_loss_frame.setObjectName(u"binary_chart_loss_frame")
        self.binary_chart_loss_frame.setStyleSheet(u"")
        self.binary_chart_loss_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_loss_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_loss_frame, 0, 0, 1, 1)

        self.binary_chart_acc_frame = QFrame(self.frame_114)
        self.binary_chart_acc_frame.setObjectName(u"binary_chart_acc_frame")
        self.binary_chart_acc_frame.setStyleSheet(u"")
        self.binary_chart_acc_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_acc_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_acc_frame, 0, 1, 1, 1)

        self.binary_chart_recall_frame = QFrame(self.frame_114)
        self.binary_chart_recall_frame.setObjectName(u"binary_chart_recall_frame")
        self.binary_chart_recall_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_recall_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_recall_frame, 2, 0, 1, 1)

        self.binary_chart_prec_frame = QFrame(self.frame_114)
        self.binary_chart_prec_frame.setObjectName(u"binary_chart_prec_frame")
        self.binary_chart_prec_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_prec_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_prec_frame, 2, 1, 1, 1)


        self.verticalLayout_54.addWidget(self.frame_114)

        self.binary_chart_scrollbar = QScrollBar(self.frame_68)
        self.binary_chart_scrollbar.setObjectName(u"binary_chart_scrollbar")
        self.binary_chart_scrollbar.setCursor(QCursor(Qt.OpenHandCursor))
        self.binary_chart_scrollbar.setMaximum(0)
        self.binary_chart_scrollbar.setPageStep(1)
        self.binary_chart_scrollbar.setOrientation(Qt.Horizontal)

        self.verticalLayout_54.addWidget(self.binary_chart_scrollbar)


        self.horizontalLayout_126.addWidget(self.frame_68)

        self.stackedWidget_binary.addWidget(self.page_binary_training)
        self.page_binary_history = QWidget()
        self.page_binary_history.setObjectName(u"page_binary_history")
        self.horizontalLayout_140 = QHBoxLayout(self.page_binary_history)
        self.horizontalLayout_140.setSpacing(6)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.frame_115 = QFrame(self.page_binary_history)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(340, 0))
        self.frame_115.setMaximumSize(QSize(340, 16777215))
        self.frame_115.setFrameShape(QFrame.Panel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45_12321 = QVBoxLayout(self.frame_115)
        self.verticalLayout_45_12321.setSpacing(0)
        self.verticalLayout_45_12321.setObjectName(u"verticalLayout_45_12321")
        self.verticalLayout_45_12321.setContentsMargins(0, 0, 0, 0)
        self.groupBox_33 = QGroupBox(self.frame_115)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setMinimumSize(QSize(0, 0))
        self.groupBox_33.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_72 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_72.setSpacing(2)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.label_102 = QLabel(self.groupBox_33)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(16777215, 20))
        self.label_102.setFont(font1)

        self.horizontalLayout_141.addWidget(self.label_102)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.binary_name_filter_combo = QComboBox(self.groupBox_33)
        self.binary_name_filter_combo.setObjectName(u"binary_name_filter_combo")

        self.horizontalLayout_142.addWidget(self.binary_name_filter_combo)


        self.horizontalLayout_141.addLayout(self.horizontalLayout_142)


        self.verticalLayout_72.addLayout(self.horizontalLayout_141)

        self.line_25 = QFrame(self.groupBox_33)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_25)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.label_109 = QLabel(self.groupBox_33)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(110, 0))
        self.label_109.setMaximumSize(QSize(110, 16777215))
        self.label_109.setFont(font1)

        self.horizontalLayout_143.addWidget(self.label_109)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_23)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setSpacing(10)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_111_2 = QHBoxLayout()
        self.horizontalLayout_111_2.setObjectName(u"horizontalLayout_111_2")
        self.label_112 = QLabel(self.groupBox_33)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMaximumSize(QSize(16777215, 20))
        self.label_112.setFont(font1)

        self.horizontalLayout_111_2.addWidget(self.label_112)

        self.binary_epoch_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_epoch_min_filter_lineedit.setObjectName(u"binary_epoch_min_filter_lineedit")
        self.binary_epoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_epoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_epoch_min_filter_lineedit.setFont(font1)
        self.binary_epoch_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_2.addWidget(self.binary_epoch_min_filter_lineedit)


        self.horizontalLayout_144.addLayout(self.horizontalLayout_111_2)

        self.horizontalLayout_121_2 = QHBoxLayout()
        self.horizontalLayout_121_2.setObjectName(u"horizontalLayout_121_2")
        self.label_120 = QLabel(self.groupBox_33)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMaximumSize(QSize(16777215, 20))
        self.label_120.setFont(font1)

        self.horizontalLayout_121_2.addWidget(self.label_120)

        self.binary_epoch_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_epoch_max_filter_lineedit.setObjectName(u"binary_epoch_max_filter_lineedit")
        self.binary_epoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_epoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_epoch_max_filter_lineedit.setFont(font1)
        self.binary_epoch_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_2.addWidget(self.binary_epoch_max_filter_lineedit)


        self.horizontalLayout_144.addLayout(self.horizontalLayout_121_2)


        self.horizontalLayout_143.addLayout(self.horizontalLayout_144)

        self.line_16 = QFrame(self.groupBox_33)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_143.addWidget(self.line_16)


        self.verticalLayout_72.addLayout(self.horizontalLayout_143)

        self.line_47_2 = QFrame(self.groupBox_33)
        self.line_47_2.setObjectName(u"line_47_2")
        self.line_47_2.setFrameShape(QFrame.HLine)
        self.line_47_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_47_2)

        self.horizontalLayout_128_2 = QHBoxLayout()
        self.horizontalLayout_128_2.setSpacing(0)
        self.horizontalLayout_128_2.setObjectName(u"horizontalLayout_128_2")
        self.label_134_2 = QLabel(self.groupBox_33)
        self.label_134_2.setObjectName(u"label_134_2")
        sizePolicy10.setHeightForWidth(self.label_134_2.sizePolicy().hasHeightForWidth())
        self.label_134_2.setSizePolicy(sizePolicy10)
        self.label_134_2.setMinimumSize(QSize(110, 0))
        self.label_134_2.setMaximumSize(QSize(110, 16777215))
        self.label_134_2.setFont(font1)

        self.horizontalLayout_128_2.addWidget(self.label_134_2)

        self.horizontalSpacer_22_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_128_2.addItem(self.horizontalSpacer_22_3)

        self.horizontalLayout_48_3 = QHBoxLayout()
        self.horizontalLayout_48_3.setSpacing(10)
        self.horizontalLayout_48_3.setObjectName(u"horizontalLayout_48_3")
        self.horizontalLayout_123_3 = QHBoxLayout()
        self.horizontalLayout_123_3.setObjectName(u"horizontalLayout_123_3")
        self.label_85_2 = QLabel(self.groupBox_33)
        self.label_85_2.setObjectName(u"label_85_2")
        self.label_85_2.setMaximumSize(QSize(16777215, 20))
        self.label_85_2.setFont(font1)

        self.horizontalLayout_123_3.addWidget(self.label_85_2)

        self.binary_tepoch_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_tepoch_min_filter_lineedit.setObjectName(u"binary_tepoch_min_filter_lineedit")
        self.binary_tepoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_tepoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_tepoch_min_filter_lineedit.setFont(font1)
        self.binary_tepoch_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_123_3.addWidget(self.binary_tepoch_min_filter_lineedit)


        self.horizontalLayout_48_3.addLayout(self.horizontalLayout_123_3)

        self.horizontalLayout_124_2 = QHBoxLayout()
        self.horizontalLayout_124_2.setObjectName(u"horizontalLayout_124_2")
        self.label_133 = QLabel(self.groupBox_33)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMaximumSize(QSize(16777215, 20))
        self.label_133.setFont(font1)

        self.horizontalLayout_124_2.addWidget(self.label_133)

        self.binary_tepoch_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_tepoch_max_filter_lineedit.setObjectName(u"binary_tepoch_max_filter_lineedit")
        self.binary_tepoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_tepoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_tepoch_max_filter_lineedit.setFont(font1)
        self.binary_tepoch_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_124_2.addWidget(self.binary_tepoch_max_filter_lineedit)


        self.horizontalLayout_48_3.addLayout(self.horizontalLayout_124_2)


        self.horizontalLayout_128_2.addLayout(self.horizontalLayout_48_3)

        self.line_18 = QFrame(self.groupBox_33)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_128_2.addWidget(self.line_18)


        self.verticalLayout_72.addLayout(self.horizontalLayout_128_2)

        self.line_47 = QFrame(self.groupBox_33)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_47)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setSpacing(0)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.label_134 = QLabel(self.groupBox_33)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(110, 0))
        self.label_134.setMaximumSize(QSize(110, 16777215))
        self.label_134.setFont(font1)

        self.horizontalLayout_145.addWidget(self.label_134)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_24)

        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setSpacing(10)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_135 = QLabel(self.groupBox_33)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMaximumSize(QSize(16777215, 20))
        self.label_135.setFont(font1)

        self.horizontalLayout_147.addWidget(self.label_135)

        self.binary_batch_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_batch_min_filter_lineedit.setObjectName(u"binary_batch_min_filter_lineedit")
        self.binary_batch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_batch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_batch_min_filter_lineedit.setFont(font1)
        self.binary_batch_min_filter_lineedit.setInputMethodHints(Qt.ImhNone)
        self.binary_batch_min_filter_lineedit.setMaxLength(3)
        self.binary_batch_min_filter_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_147.addWidget(self.binary_batch_min_filter_lineedit)


        self.horizontalLayout_146.addLayout(self.horizontalLayout_147)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.label_136 = QLabel(self.groupBox_33)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMaximumSize(QSize(16777215, 20))
        self.label_136.setFont(font1)

        self.horizontalLayout_152.addWidget(self.label_136)

        self.binary_batch_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_batch_max_filter_lineedit.setObjectName(u"binary_batch_max_filter_lineedit")
        self.binary_batch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_batch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_batch_max_filter_lineedit.setFont(font1)
        self.binary_batch_max_filter_lineedit.setMaxLength(3)

        self.horizontalLayout_152.addWidget(self.binary_batch_max_filter_lineedit)


        self.horizontalLayout_146.addLayout(self.horizontalLayout_152)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_146)

        self.line_40_2 = QFrame(self.groupBox_33)
        self.line_40_2.setObjectName(u"line_40_2")
        self.line_40_2.setFrameShape(QFrame.HLine)
        self.line_40_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_145.addWidget(self.line_40_2)


        self.verticalLayout_72.addLayout(self.horizontalLayout_145)

        self.line_130 = QFrame(self.groupBox_33)
        self.line_130.setObjectName(u"line_130")
        self.line_130.setFrameShape(QFrame.HLine)
        self.line_130.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_130)

        self.horizontalLayout_322 = QHBoxLayout()
        self.horizontalLayout_322.setSpacing(0)
        self.horizontalLayout_322.setObjectName(u"horizontalLayout_322")
        self.label_145 = QLabel(self.groupBox_33)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(110, 0))
        self.label_145.setMaximumSize(QSize(110, 16777215))
        self.label_145.setFont(font1)

        self.horizontalLayout_322.addWidget(self.label_145)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_322.addItem(self.horizontalSpacer_25)

        self.horizontalLayout_323 = QHBoxLayout()
        self.horizontalLayout_323.setSpacing(10)
        self.horizontalLayout_323.setObjectName(u"horizontalLayout_323")
        self.horizontalLayout_324 = QHBoxLayout()
        self.horizontalLayout_324.setObjectName(u"horizontalLayout_324")
        self.label_146 = QLabel(self.groupBox_33)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMaximumSize(QSize(16777215, 20))
        self.label_146.setFont(font1)

        self.horizontalLayout_324.addWidget(self.label_146)

        self.binary_split_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_split_min_filter_lineedit.setObjectName(u"binary_split_min_filter_lineedit")
        self.binary_split_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_split_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_split_min_filter_lineedit.setFont(font1)
        self.binary_split_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_324.addWidget(self.binary_split_min_filter_lineedit)


        self.horizontalLayout_323.addLayout(self.horizontalLayout_324)

        self.horizontalLayout_325 = QHBoxLayout()
        self.horizontalLayout_325.setObjectName(u"horizontalLayout_325")
        self.label_147 = QLabel(self.groupBox_33)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMaximumSize(QSize(16777215, 20))
        self.label_147.setFont(font1)

        self.horizontalLayout_325.addWidget(self.label_147)

        self.binary_split_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_split_max_filter_lineedit.setObjectName(u"binary_split_max_filter_lineedit")
        self.binary_split_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_split_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_split_max_filter_lineedit.setFont(font1)
        self.binary_split_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_325.addWidget(self.binary_split_max_filter_lineedit)


        self.horizontalLayout_323.addLayout(self.horizontalLayout_325)


        self.horizontalLayout_322.addLayout(self.horizontalLayout_323)

        self.line_33_2 = QFrame(self.groupBox_33)
        self.line_33_2.setObjectName(u"line_33_2")
        self.line_33_2.setFrameShape(QFrame.HLine)
        self.line_33_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_322.addWidget(self.line_33_2)


        self.verticalLayout_72.addLayout(self.horizontalLayout_322)

        self.line_131 = QFrame(self.groupBox_33)
        self.line_131.setObjectName(u"line_131")
        self.line_131.setFrameShape(QFrame.HLine)
        self.line_131.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_131)

        self.horizontalLayout_326 = QHBoxLayout()
        self.horizontalLayout_326.setSpacing(0)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.label_148 = QLabel(self.groupBox_33)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(110, 0))
        self.label_148.setMaximumSize(QSize(110, 16777215))
        self.label_148.setFont(font1)

        self.horizontalLayout_326.addWidget(self.label_148)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_326.addItem(self.horizontalSpacer_26)

        self.horizontalLayout_327 = QHBoxLayout()
        self.horizontalLayout_327.setSpacing(10)
        self.horizontalLayout_327.setObjectName(u"horizontalLayout_327")
        self.horizontalLayout_328 = QHBoxLayout()
        self.horizontalLayout_328.setObjectName(u"horizontalLayout_328")
        self.label_132_2 = QLabel(self.groupBox_33)
        self.label_132_2.setObjectName(u"label_132_2")
        self.label_132_2.setMaximumSize(QSize(16777215, 20))
        self.label_132_2.setFont(font1)

        self.horizontalLayout_328.addWidget(self.label_132_2)

        self.binary_loss_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_loss_min_filter_lineedit.setObjectName(u"binary_loss_min_filter_lineedit")
        self.binary_loss_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_loss_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_loss_min_filter_lineedit.setFont(font1)
        self.binary_loss_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_328.addWidget(self.binary_loss_min_filter_lineedit)


        self.horizontalLayout_327.addLayout(self.horizontalLayout_328)

        self.horizontalLayout_329 = QHBoxLayout()
        self.horizontalLayout_329.setObjectName(u"horizontalLayout_329")
        self.label_149 = QLabel(self.groupBox_33)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMaximumSize(QSize(16777215, 20))
        self.label_149.setFont(font1)

        self.horizontalLayout_329.addWidget(self.label_149)

        self.binary_loss_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_loss_max_filter_lineedit.setObjectName(u"binary_loss_max_filter_lineedit")
        self.binary_loss_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_loss_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_loss_max_filter_lineedit.setFont(font1)
        self.binary_loss_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_329.addWidget(self.binary_loss_max_filter_lineedit)


        self.horizontalLayout_327.addLayout(self.horizontalLayout_329)


        self.horizontalLayout_326.addLayout(self.horizontalLayout_327)

        self.line_42 = QFrame(self.groupBox_33)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.HLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_326.addWidget(self.line_42)


        self.verticalLayout_72.addLayout(self.horizontalLayout_326)

        self.line_132 = QFrame(self.groupBox_33)
        self.line_132.setObjectName(u"line_132")
        self.line_132.setFrameShape(QFrame.HLine)
        self.line_132.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_132)

        self.horizontalLayout_330 = QHBoxLayout()
        self.horizontalLayout_330.setSpacing(0)
        self.horizontalLayout_330.setObjectName(u"horizontalLayout_330")
        self.label_150 = QLabel(self.groupBox_33)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(110, 0))
        self.label_150.setMaximumSize(QSize(110, 16777215))
        self.label_150.setFont(font1)

        self.horizontalLayout_330.addWidget(self.label_150)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_330.addItem(self.horizontalSpacer_27)

        self.horizontalLayout_331 = QHBoxLayout()
        self.horizontalLayout_331.setSpacing(10)
        self.horizontalLayout_331.setObjectName(u"horizontalLayout_331")
        self.horizontalLayout_332 = QHBoxLayout()
        self.horizontalLayout_332.setObjectName(u"horizontalLayout_332")
        self.label_151 = QLabel(self.groupBox_33)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMaximumSize(QSize(16777215, 20))
        self.label_151.setFont(font1)

        self.horizontalLayout_332.addWidget(self.label_151)

        self.binary_acc_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_acc_min_filter_lineedit.setObjectName(u"binary_acc_min_filter_lineedit")
        self.binary_acc_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_acc_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_acc_min_filter_lineedit.setFont(font1)
        self.binary_acc_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_332.addWidget(self.binary_acc_min_filter_lineedit)


        self.horizontalLayout_331.addLayout(self.horizontalLayout_332)

        self.horizontalLayout_333 = QHBoxLayout()
        self.horizontalLayout_333.setObjectName(u"horizontalLayout_333")
        self.label_152 = QLabel(self.groupBox_33)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMaximumSize(QSize(16777215, 20))
        self.label_152.setFont(font1)

        self.horizontalLayout_333.addWidget(self.label_152)

        self.binary_acc_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_acc_max_filter_lineedit.setObjectName(u"binary_acc_max_filter_lineedit")
        self.binary_acc_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_acc_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_acc_max_filter_lineedit.setFont(font1)
        self.binary_acc_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_333.addWidget(self.binary_acc_max_filter_lineedit)


        self.horizontalLayout_331.addLayout(self.horizontalLayout_333)


        self.horizontalLayout_330.addLayout(self.horizontalLayout_331)

        self.line_43 = QFrame(self.groupBox_33)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_330.addWidget(self.line_43)


        self.verticalLayout_72.addLayout(self.horizontalLayout_330)

        self.line_133 = QFrame(self.groupBox_33)
        self.line_133.setObjectName(u"line_133")
        self.line_133.setFrameShape(QFrame.HLine)
        self.line_133.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_133)

        self.horizontalLayout_334 = QHBoxLayout()
        self.horizontalLayout_334.setSpacing(0)
        self.horizontalLayout_334.setObjectName(u"horizontalLayout_334")
        self.label_153 = QLabel(self.groupBox_33)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(110, 0))
        self.label_153.setMaximumSize(QSize(110, 16777215))
        self.label_153.setFont(font1)

        self.horizontalLayout_334.addWidget(self.label_153)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_334.addItem(self.horizontalSpacer_28)

        self.horizontalLayout_335 = QHBoxLayout()
        self.horizontalLayout_335.setSpacing(10)
        self.horizontalLayout_335.setObjectName(u"horizontalLayout_335")
        self.horizontalLayout_336 = QHBoxLayout()
        self.horizontalLayout_336.setObjectName(u"horizontalLayout_336")
        self.label_158 = QLabel(self.groupBox_33)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMaximumSize(QSize(16777215, 20))
        self.label_158.setFont(font1)

        self.horizontalLayout_336.addWidget(self.label_158)

        self.binary_prec_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_prec_min_filter_lineedit.setObjectName(u"binary_prec_min_filter_lineedit")
        self.binary_prec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_prec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_prec_min_filter_lineedit.setFont(font1)
        self.binary_prec_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_336.addWidget(self.binary_prec_min_filter_lineedit)


        self.horizontalLayout_335.addLayout(self.horizontalLayout_336)

        self.horizontalLayout_337 = QHBoxLayout()
        self.horizontalLayout_337.setObjectName(u"horizontalLayout_337")
        self.label_308 = QLabel(self.groupBox_33)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setMaximumSize(QSize(16777215, 20))
        self.label_308.setFont(font1)

        self.horizontalLayout_337.addWidget(self.label_308)

        self.binary_prec_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_prec_max_filter_lineedit.setObjectName(u"binary_prec_max_filter_lineedit")
        self.binary_prec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_prec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_prec_max_filter_lineedit.setFont(font1)
        self.binary_prec_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_337.addWidget(self.binary_prec_max_filter_lineedit)


        self.horizontalLayout_335.addLayout(self.horizontalLayout_337)


        self.horizontalLayout_334.addLayout(self.horizontalLayout_335)

        self.line_44 = QFrame(self.groupBox_33)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.HLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_334.addWidget(self.line_44)


        self.verticalLayout_72.addLayout(self.horizontalLayout_334)

        self.line_134 = QFrame(self.groupBox_33)
        self.line_134.setObjectName(u"line_134")
        self.line_134.setFrameShape(QFrame.HLine)
        self.line_134.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_134)

        self.horizontalLayout_338 = QHBoxLayout()
        self.horizontalLayout_338.setSpacing(0)
        self.horizontalLayout_338.setObjectName(u"horizontalLayout_338")
        self.label_309 = QLabel(self.groupBox_33)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setMinimumSize(QSize(110, 0))
        self.label_309.setMaximumSize(QSize(110, 16777215))
        self.label_309.setFont(font1)

        self.horizontalLayout_338.addWidget(self.label_309)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_338.addItem(self.horizontalSpacer_33)

        self.horizontalLayout_339 = QHBoxLayout()
        self.horizontalLayout_339.setSpacing(10)
        self.horizontalLayout_339.setObjectName(u"horizontalLayout_339")
        self.horizontalLayout_340 = QHBoxLayout()
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.label_310 = QLabel(self.groupBox_33)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setMaximumSize(QSize(16777215, 20))
        self.label_310.setFont(font1)

        self.horizontalLayout_340.addWidget(self.label_310)

        self.binary_rec_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_rec_min_filter_lineedit.setObjectName(u"binary_rec_min_filter_lineedit")
        self.binary_rec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_rec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_rec_min_filter_lineedit.setFont(font1)
        self.binary_rec_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_340.addWidget(self.binary_rec_min_filter_lineedit)


        self.horizontalLayout_339.addLayout(self.horizontalLayout_340)

        self.horizontalLayout_341 = QHBoxLayout()
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.label_311 = QLabel(self.groupBox_33)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setMaximumSize(QSize(16777215, 20))
        self.label_311.setFont(font1)

        self.horizontalLayout_341.addWidget(self.label_311)

        self.binary_rec_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_rec_max_filter_lineedit.setObjectName(u"binary_rec_max_filter_lineedit")
        self.binary_rec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_rec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_rec_max_filter_lineedit.setFont(font1)
        self.binary_rec_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_341.addWidget(self.binary_rec_max_filter_lineedit)


        self.horizontalLayout_339.addLayout(self.horizontalLayout_341)


        self.horizontalLayout_338.addLayout(self.horizontalLayout_339)

        self.line_45 = QFrame(self.groupBox_33)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_338.addWidget(self.line_45)


        self.verticalLayout_72.addLayout(self.horizontalLayout_338)

        self.line_135 = QFrame(self.groupBox_33)
        self.line_135.setObjectName(u"line_135")
        self.line_135.setFrameShape(QFrame.HLine)
        self.line_135.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_135)

        self.frame_80_1243123 = QFrame(self.groupBox_33)
        self.frame_80_1243123.setObjectName(u"frame_80_1243123")
        self.frame_80_1243123.setFrameShape(QFrame.StyledPanel)
        self.frame_80_1243123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47_123423 = QVBoxLayout(self.frame_80_1243123)
        self.verticalLayout_47_123423.setSpacing(0)
        self.verticalLayout_47_123423.setObjectName(u"verticalLayout_47_123423")
        self.verticalLayout_47_123423.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46_123 = QVBoxLayout()
        self.verticalLayout_46_123.setSpacing(2)
        self.verticalLayout_46_123.setObjectName(u"verticalLayout_46_123")
        self.horizontalLayout_197_213 = QHBoxLayout()
        self.horizontalLayout_197_213.setSpacing(5)
        self.horizontalLayout_197_213.setObjectName(u"horizontalLayout_197_213")
        self.label_312 = QLabel(self.frame_80_1243123)
        self.label_312.setObjectName(u"label_312")
        self.label_312.setMinimumSize(QSize(150, 0))
        self.label_312.setMaximumSize(QSize(150, 20))
        self.label_312.setFont(font1)

        self.horizontalLayout_197_213.addWidget(self.label_312)

        self.binary_start_year_lineedit = QLineEdit(self.frame_80_1243123)
        self.binary_start_year_lineedit.setObjectName(u"binary_start_year_lineedit")
        sizePolicy8.setHeightForWidth(self.binary_start_year_lineedit.sizePolicy().hasHeightForWidth())
        self.binary_start_year_lineedit.setSizePolicy(sizePolicy8)
        self.binary_start_year_lineedit.setMinimumSize(QSize(70, 0))
        self.binary_start_year_lineedit.setMaximumSize(QSize(70, 16777215))
        self.binary_start_year_lineedit.setFont(font1)
        self.binary_start_year_lineedit.setMaxLength(32767)
        self.binary_start_year_lineedit.setCursorPosition(0)
        self.binary_start_year_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_197_213.addWidget(self.binary_start_year_lineedit)

        self.label_313 = QLabel(self.frame_80_1243123)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setMinimumSize(QSize(5, 0))
        self.label_313.setMaximumSize(QSize(5, 20))
        self.label_313.setFont(font1)

        self.horizontalLayout_197_213.addWidget(self.label_313)

        self.binary_start_month_lineedit = QLineEdit(self.frame_80_1243123)
        self.binary_start_month_lineedit.setObjectName(u"binary_start_month_lineedit")
        sizePolicy8.setHeightForWidth(self.binary_start_month_lineedit.sizePolicy().hasHeightForWidth())
        self.binary_start_month_lineedit.setSizePolicy(sizePolicy8)
        self.binary_start_month_lineedit.setMinimumSize(QSize(40, 0))
        self.binary_start_month_lineedit.setMaximumSize(QSize(40, 16777215))
        self.binary_start_month_lineedit.setFont(font1)
        self.binary_start_month_lineedit.setMaxLength(32767)
        self.binary_start_month_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_197_213.addWidget(self.binary_start_month_lineedit)

        self.label_314 = QLabel(self.frame_80_1243123)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setMinimumSize(QSize(5, 0))
        self.label_314.setMaximumSize(QSize(5, 20))
        self.label_314.setFont(font1)

        self.horizontalLayout_197_213.addWidget(self.label_314)

        self.binary_start_day_lineedit = QLineEdit(self.frame_80_1243123)
        self.binary_start_day_lineedit.setObjectName(u"binary_start_day_lineedit")
        sizePolicy8.setHeightForWidth(self.binary_start_day_lineedit.sizePolicy().hasHeightForWidth())
        self.binary_start_day_lineedit.setSizePolicy(sizePolicy8)
        self.binary_start_day_lineedit.setMinimumSize(QSize(40, 0))
        self.binary_start_day_lineedit.setMaximumSize(QSize(40, 16777215))
        self.binary_start_day_lineedit.setFont(font1)
        self.binary_start_day_lineedit.setMaxLength(32767)
        self.binary_start_day_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_197_213.addWidget(self.binary_start_day_lineedit)


        self.verticalLayout_46_123.addLayout(self.horizontalLayout_197_213)

        self.horizontalLayout_198_123421 = QHBoxLayout()
        self.horizontalLayout_198_123421.setSpacing(5)
        self.horizontalLayout_198_123421.setObjectName(u"horizontalLayout_198_123421")
        self.label_315 = QLabel(self.frame_80_1243123)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setMinimumSize(QSize(150, 0))
        self.label_315.setMaximumSize(QSize(150, 20))
        self.label_315.setFont(font1)

        self.horizontalLayout_198_123421.addWidget(self.label_315)

        self.binary_end_year_lineedit = QLineEdit(self.frame_80_1243123)
        self.binary_end_year_lineedit.setObjectName(u"binary_end_year_lineedit")
        sizePolicy8.setHeightForWidth(self.binary_end_year_lineedit.sizePolicy().hasHeightForWidth())
        self.binary_end_year_lineedit.setSizePolicy(sizePolicy8)
        self.binary_end_year_lineedit.setMinimumSize(QSize(70, 0))
        self.binary_end_year_lineedit.setMaximumSize(QSize(70, 16777215))
        self.binary_end_year_lineedit.setFont(font1)
        self.binary_end_year_lineedit.setMaxLength(32767)
        self.binary_end_year_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_198_123421.addWidget(self.binary_end_year_lineedit)

        self.label_316 = QLabel(self.frame_80_1243123)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setMinimumSize(QSize(5, 0))
        self.label_316.setMaximumSize(QSize(5, 20))
        self.label_316.setFont(font1)

        self.horizontalLayout_198_123421.addWidget(self.label_316)

        self.binary_end_month_lineedit = QLineEdit(self.frame_80_1243123)
        self.binary_end_month_lineedit.setObjectName(u"binary_end_month_lineedit")
        sizePolicy8.setHeightForWidth(self.binary_end_month_lineedit.sizePolicy().hasHeightForWidth())
        self.binary_end_month_lineedit.setSizePolicy(sizePolicy8)
        self.binary_end_month_lineedit.setMinimumSize(QSize(40, 0))
        self.binary_end_month_lineedit.setMaximumSize(QSize(40, 16777215))
        self.binary_end_month_lineedit.setFont(font1)
        self.binary_end_month_lineedit.setMaxLength(32767)
        self.binary_end_month_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_198_123421.addWidget(self.binary_end_month_lineedit)

        self.label_317 = QLabel(self.frame_80_1243123)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setMinimumSize(QSize(5, 0))
        self.label_317.setMaximumSize(QSize(5, 20))
        self.label_317.setFont(font1)

        self.horizontalLayout_198_123421.addWidget(self.label_317)

        self.binary_end_day_lineedit = QLineEdit(self.frame_80_1243123)
        self.binary_end_day_lineedit.setObjectName(u"binary_end_day_lineedit")
        sizePolicy8.setHeightForWidth(self.binary_end_day_lineedit.sizePolicy().hasHeightForWidth())
        self.binary_end_day_lineedit.setSizePolicy(sizePolicy8)
        self.binary_end_day_lineedit.setMinimumSize(QSize(40, 0))
        self.binary_end_day_lineedit.setMaximumSize(QSize(40, 16777215))
        self.binary_end_day_lineedit.setFont(font1)
        self.binary_end_day_lineedit.setMaxLength(32767)
        self.binary_end_day_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_198_123421.addWidget(self.binary_end_day_lineedit)


        self.verticalLayout_46_123.addLayout(self.horizontalLayout_198_123421)


        self.verticalLayout_47_123423.addLayout(self.verticalLayout_46_123)


        self.verticalLayout_72.addWidget(self.frame_80_1243123)

        self.line_136 = QFrame(self.groupBox_33)
        self.line_136.setObjectName(u"line_136")
        self.line_136.setFrameShape(QFrame.HLine)
        self.line_136.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_72.addWidget(self.line_136)

        self.horizontalLayout_342 = QHBoxLayout()
        self.horizontalLayout_342.setSpacing(20)
        self.horizontalLayout_342.setObjectName(u"horizontalLayout_342")
        self.binary_filter_btn = QPushButton(self.groupBox_33)
        self.binary_filter_btn.setObjectName(u"binary_filter_btn")
        self.binary_filter_btn.setMinimumSize(QSize(0, 30))
        self.binary_filter_btn.setMaximumSize(QSize(16777215, 30))
        self.binary_filter_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_342.addWidget(self.binary_filter_btn)

        self.binary_clearfilter_btn = QPushButton(self.groupBox_33)
        self.binary_clearfilter_btn.setObjectName(u"binary_clearfilter_btn")
        self.binary_clearfilter_btn.setMinimumSize(QSize(0, 30))
        self.binary_clearfilter_btn.setMaximumSize(QSize(16777215, 30))
        self.binary_clearfilter_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_342.addWidget(self.binary_clearfilter_btn)


        self.verticalLayout_72.addLayout(self.horizontalLayout_342)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_5)


        self.verticalLayout_45_12321.addWidget(self.groupBox_33)


        self.horizontalLayout_140.addWidget(self.frame_115)

        self.frame_116 = QFrame(self.page_binary_history)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97_2 = QVBoxLayout(self.frame_116)
        self.verticalLayout_97_2.setSpacing(0)
        self.verticalLayout_97_2.setObjectName(u"verticalLayout_97_2")
        self.verticalLayout_97_2.setContentsMargins(0, 0, 0, 0)
        self.binary_history_tabel = QTableWidget(self.frame_116)
        if (self.binary_history_tabel.columnCount() < 19):
            self.binary_history_tabel.setColumnCount(19)
        self.binary_history_tabel.setObjectName(u"binary_history_tabel")
        self.binary_history_tabel.setEnabled(True)
        self.binary_history_tabel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.binary_history_tabel.setRowCount(0)
        self.binary_history_tabel.setColumnCount(19)
        self.binary_history_tabel.horizontalHeader().setCascadingSectionResizes(True)
        self.binary_history_tabel.horizontalHeader().setMinimumSectionSize(150)
        self.binary_history_tabel.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_97_2.addWidget(self.binary_history_tabel)

        self.frame_68_2 = QFrame(self.frame_116)
        self.frame_68_2.setObjectName(u"frame_68_2")
        self.frame_68_2.setFrameShape(QFrame.StyledPanel)
        self.frame_68_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_343 = QHBoxLayout(self.frame_68_2)
        self.horizontalLayout_343.setObjectName(u"horizontalLayout_343")
        self.binary_table_refresh_btn = QPushButton(self.frame_68_2)
        self.binary_table_refresh_btn.setObjectName(u"binary_table_refresh_btn")
        self.binary_table_refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_table_refresh_btn.setLayoutDirection(Qt.RightToLeft)
        self.binary_table_refresh_btn.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.binary_table_refresh_btn.setIcon(icon25)
        self.binary_table_refresh_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_343.addWidget(self.binary_table_refresh_btn)

        self.line_137 = QFrame(self.frame_68_2)
        self.line_137.setObjectName(u"line_137")
        self.line_137.setFrameShape(QFrame.VLine)
        self.line_137.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_343.addWidget(self.line_137)

        self.binary_tabel_prev = QPushButton(self.frame_68_2)
        self.binary_tabel_prev.setObjectName(u"binary_tabel_prev")
        self.binary_tabel_prev.setEnabled(False)
        self.binary_tabel_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_tabel_prev.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.binary_tabel_prev.setIcon(icon16)
        self.binary_tabel_prev.setIconSize(QSize(30, 30))

        self.horizontalLayout_343.addWidget(self.binary_tabel_prev)

        self.binary_tabel_page = QLineEdit(self.frame_68_2)
        self.binary_tabel_page.setObjectName(u"binary_tabel_page")
        self.binary_tabel_page.setEnabled(False)
        self.binary_tabel_page.setMinimumSize(QSize(50, 30))
        self.binary_tabel_page.setMaximumSize(QSize(50, 30))
        self.binary_tabel_page.setStyleSheet(u"padding:0;")
        self.binary_tabel_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_343.addWidget(self.binary_tabel_page)

        self.binary_tabel_next = QPushButton(self.frame_68_2)
        self.binary_tabel_next.setObjectName(u"binary_tabel_next")
        self.binary_tabel_next.setEnabled(True)
        self.binary_tabel_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_tabel_next.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.binary_tabel_next.setIcon(icon15)
        self.binary_tabel_next.setIconSize(QSize(30, 30))

        self.horizontalLayout_343.addWidget(self.binary_tabel_next)

        self.line_138 = QFrame(self.frame_68_2)
        self.line_138.setObjectName(u"line_138")
        self.line_138.setFrameShape(QFrame.VLine)
        self.line_138.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_343.addWidget(self.line_138)

        self.binary_tabel_label = QLabel(self.frame_68_2)
        self.binary_tabel_label.setObjectName(u"binary_tabel_label")
        sizePolicy3.setHeightForWidth(self.binary_tabel_label.sizePolicy().hasHeightForWidth())
        self.binary_tabel_label.setSizePolicy(sizePolicy3)
        self.binary_tabel_label.setMinimumSize(QSize(0, 0))
        self.binary_tabel_label.setMaximumSize(QSize(16777215, 16777215))
        self.binary_tabel_label.setFrameShape(QFrame.Panel)
        self.binary_tabel_label.setFrameShadow(QFrame.Sunken)
        self.binary_tabel_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_343.addWidget(self.binary_tabel_label)


        self.verticalLayout_97_2.addWidget(self.frame_68_2)


        self.horizontalLayout_140.addWidget(self.frame_116)

        self.stackedWidget_binary.addWidget(self.page_binary_history)

        self.verticalLayout_22.addWidget(self.stackedWidget_binary)

        self.stackedWidget.addWidget(self.page_Binary)
        self.page_Localization = QWidget()
        self.page_Localization.setObjectName(u"page_Localization")
        self.verticalLayout_23 = QVBoxLayout(self.page_Localization)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_Localization)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"border: None")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.localization_training = QPushButton(self.frame_5)
        self.localization_training.setObjectName(u"localization_training")
        self.localization_training.setMinimumSize(QSize(150, 40))
        self.localization_training.setMaximumSize(QSize(150, 16777215))
        self.localization_training.setCursor(QCursor(Qt.PointingHandCursor))
        self.localization_training.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170 ,170, 170); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 ,195, 196);\n"
"}")

        self.horizontalLayout_18.addWidget(self.localization_training)

        self.localization_history = QPushButton(self.frame_5)
        self.localization_history.setObjectName(u"localization_history")
        self.localization_history.setMinimumSize(QSize(150, 40))
        self.localization_history.setMaximumSize(QSize(150, 16777215))
        self.localization_history.setFont(font1)
        self.localization_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.localization_history.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(100, 100, 100); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"} \n"
"QPushButton:hover {\n"
"	background-color:  rgb(150 ,150, 150);\n"
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
        self.page_localization_training = QWidget()
        self.page_localization_training.setObjectName(u"page_localization_training")
        self.horizontalLayout_62 = QHBoxLayout(self.page_localization_training)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_58 = QFrame(self.page_localization_training)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy10)
        self.frame_58.setMinimumSize(QSize(350, 50))
        self.frame_58.setMaximumSize(QSize(320, 16777215))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_58)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        sizePolicy2.setHeightForWidth(self.frame_60.sizePolicy().hasHeightForWidth())
        self.frame_60.setSizePolicy(sizePolicy2)
        self.frame_60.setMinimumSize(QSize(330, 50))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_60)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.horizontalLayout_234 = QHBoxLayout()
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.label_242 = QLabel(self.frame_60)
        self.label_242.setObjectName(u"label_242")

        self.horizontalLayout_234.addWidget(self.label_242, 0, Qt.AlignLeft)

        self.l_algorithms = QComboBox(self.frame_60)
        self.l_algorithms.setObjectName(u"l_algorithms")

        self.horizontalLayout_234.addWidget(self.l_algorithms)


        self.verticalLayout_104.addLayout(self.horizontalLayout_234)

        self.horizontalLayout_297 = QHBoxLayout()
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.label_301 = QLabel(self.frame_60)
        self.label_301.setObjectName(u"label_301")

        self.horizontalLayout_297.addWidget(self.label_301)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_297.addItem(self.horizontalSpacer_68)

        self.l_select_prep = QPushButton(self.frame_60)
        self.l_select_prep.setObjectName(u"l_select_prep")
        self.l_select_prep.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.l_select_prep.sizePolicy().hasHeightForWidth())
        self.l_select_prep.setSizePolicy(sizePolicy3)
        self.l_select_prep.setMinimumSize(QSize(102, 0))
        self.l_select_prep.setCursor(QCursor(Qt.PointingHandCursor))
        self.l_select_prep.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_297.addWidget(self.l_select_prep)


        self.verticalLayout_104.addLayout(self.horizontalLayout_297)

        self.l_prep = QTextEdit(self.frame_60)
        self.l_prep.setObjectName(u"l_prep")
        self.l_prep.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.l_prep.sizePolicy().hasHeightForWidth())
        self.l_prep.setSizePolicy(sizePolicy2)
        self.l_prep.setMinimumSize(QSize(20, 20))
        self.l_prep.setMaximumSize(QSize(310, 16777215))
        self.l_prep.setStyleSheet(u"QTextEdit:disabled  {\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(160, 160, 160);\n"
"}")
        self.l_prep.setReadOnly(True)

        self.verticalLayout_104.addWidget(self.l_prep)

        self.horizontalLayout_236 = QHBoxLayout()
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.label_243 = QLabel(self.frame_60)
        self.label_243.setObjectName(u"label_243")

        self.horizontalLayout_236.addWidget(self.label_243)

        self.l_input_size1 = QSpinBox(self.frame_60)
        self.l_input_size1.setObjectName(u"l_input_size1")
        self.l_input_size1.setMinimum(64)
        self.l_input_size1.setMaximum(2048)
        self.l_input_size1.setSingleStep(32)
        self.l_input_size1.setValue(256)

        self.horizontalLayout_236.addWidget(self.l_input_size1)

        self.label_297 = QLabel(self.frame_60)
        self.label_297.setObjectName(u"label_297")
        sizePolicy.setHeightForWidth(self.label_297.sizePolicy().hasHeightForWidth())
        self.label_297.setSizePolicy(sizePolicy)

        self.horizontalLayout_236.addWidget(self.label_297)

        self.l_input_size2 = QSpinBox(self.frame_60)
        self.l_input_size2.setObjectName(u"l_input_size2")
        self.l_input_size2.setMinimum(64)
        self.l_input_size2.setMaximum(2048)
        self.l_input_size2.setSingleStep(32)
        self.l_input_size2.setValue(256)

        self.horizontalLayout_236.addWidget(self.l_input_size2)


        self.verticalLayout_104.addLayout(self.horizontalLayout_236)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_33 = QLabel(self.frame_60)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_82.addWidget(self.label_33)

        self.l_input_type_resize = QRadioButton(self.frame_60)
        self.l_input_type_resize.setObjectName(u"l_input_type_resize")
        self.l_input_type_resize.setStyleSheet(u"")

        self.horizontalLayout_82.addWidget(self.l_input_type_resize)

        self.l_input_type_split = QRadioButton(self.frame_60)
        self.l_input_type_split.setObjectName(u"l_input_type_split")
        self.l_input_type_split.setStyleSheet(u"")

        self.horizontalLayout_82.addWidget(self.l_input_type_split)


        self.verticalLayout_104.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_237 = QHBoxLayout()
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.label_244 = QLabel(self.frame_60)
        self.label_244.setObjectName(u"label_244")

        self.horizontalLayout_237.addWidget(self.label_244, 0, Qt.AlignLeft)

        self.l_epochs = QLineEdit(self.frame_60)
        self.l_epochs.setObjectName(u"l_epochs")
        self.l_epochs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_237.addWidget(self.l_epochs)


        self.verticalLayout_104.addLayout(self.horizontalLayout_237)

        self.horizontalLayout_238 = QHBoxLayout()
        self.horizontalLayout_238.setObjectName(u"horizontalLayout_238")
        self.label_245 = QLabel(self.frame_60)
        self.label_245.setObjectName(u"label_245")

        self.horizontalLayout_238.addWidget(self.label_245, 0, Qt.AlignLeft)

        self.l_batch = QLineEdit(self.frame_60)
        self.l_batch.setObjectName(u"l_batch")
        self.l_batch.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_238.addWidget(self.l_batch)


        self.verticalLayout_104.addLayout(self.horizontalLayout_238)

        self.horizontalLayout_239 = QHBoxLayout()
        self.horizontalLayout_239.setObjectName(u"horizontalLayout_239")
        self.label_246 = QLabel(self.frame_60)
        self.label_246.setObjectName(u"label_246")

        self.horizontalLayout_239.addWidget(self.label_246)

        self.l_lr = QLineEdit(self.frame_60)
        self.l_lr.setObjectName(u"l_lr")
        self.l_lr.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_239.addWidget(self.l_lr)


        self.verticalLayout_104.addLayout(self.horizontalLayout_239)

        self.horizontalLayout_241 = QHBoxLayout()
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.label_248 = QLabel(self.frame_60)
        self.label_248.setObjectName(u"label_248")

        self.horizontalLayout_241.addWidget(self.label_248)

        self.l_vs = QLineEdit(self.frame_60)
        self.l_vs.setObjectName(u"l_vs")
        self.l_vs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_241.addWidget(self.l_vs)


        self.verticalLayout_104.addLayout(self.horizontalLayout_241)

        self.horizontalLayout_242 = QHBoxLayout()
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.label_249 = QLabel(self.frame_60)
        self.label_249.setObjectName(u"label_249")

        self.horizontalLayout_242.addWidget(self.label_249)

        self.l_gpu = QComboBox(self.frame_60)
        self.l_gpu.addItem("")
        self.l_gpu.addItem("")
        self.l_gpu.addItem("")
        self.l_gpu.addItem("")
        self.l_gpu.setObjectName(u"l_gpu")

        self.horizontalLayout_242.addWidget(self.l_gpu)


        self.verticalLayout_104.addLayout(self.horizontalLayout_242)

        self.horizontalLayout_243 = QHBoxLayout()
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.label_250 = QLabel(self.frame_60)
        self.label_250.setObjectName(u"label_250")

        self.horizontalLayout_243.addWidget(self.label_250)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_243.addItem(self.horizontalSpacer_19)

        self.l_select_dp = QPushButton(self.frame_60)
        self.l_select_dp.setObjectName(u"l_select_dp")
        sizePolicy3.setHeightForWidth(self.l_select_dp.sizePolicy().hasHeightForWidth())
        self.l_select_dp.setSizePolicy(sizePolicy3)
        self.l_select_dp.setMinimumSize(QSize(102, 0))
        self.l_select_dp.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}color:white;")

        self.horizontalLayout_243.addWidget(self.l_select_dp)


        self.verticalLayout_104.addLayout(self.horizontalLayout_243)

        self.l_dp = QTextEdit(self.frame_60)
        self.l_dp.setObjectName(u"l_dp")
        sizePolicy.setHeightForWidth(self.l_dp.sizePolicy().hasHeightForWidth())
        self.l_dp.setSizePolicy(sizePolicy)
        self.l_dp.setMinimumSize(QSize(20, 20))
        self.l_dp.setMaximumSize(QSize(310, 16777215))
        self.l_dp.setStyleSheet(u"")
        self.l_dp.setReadOnly(True)

        self.verticalLayout_104.addWidget(self.l_dp)

        self.horizontalLayout_244 = QHBoxLayout()
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalLayout_244.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.l_ds_num = QSpinBox(self.frame_60)
        self.l_ds_num.setObjectName(u"l_ds_num")
        self.l_ds_num.setMaximumSize(QSize(140, 16777215))
        self.l_ds_num.setMinimum(1)

        self.horizontalLayout_244.addWidget(self.l_ds_num)

        self.l_delete_ds = QPushButton(self.frame_60)
        self.l_delete_ds.setObjectName(u"l_delete_ds")
        sizePolicy12.setHeightForWidth(self.l_delete_ds.sizePolicy().hasHeightForWidth())
        self.l_delete_ds.setSizePolicy(sizePolicy12)
        self.l_delete_ds.setMaximumSize(QSize(65, 16777215))
        self.l_delete_ds.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_244.addWidget(self.l_delete_ds)

        self.l_add_ds = QPushButton(self.frame_60)
        self.l_add_ds.setObjectName(u"l_add_ds")
        sizePolicy12.setHeightForWidth(self.l_add_ds.sizePolicy().hasHeightForWidth())
        self.l_add_ds.setSizePolicy(sizePolicy12)
        self.l_add_ds.setMaximumSize(QSize(65, 16777215))
        self.l_add_ds.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_244.addWidget(self.l_add_ds)


        self.verticalLayout_104.addLayout(self.horizontalLayout_244)


        self.verticalLayout_103.addWidget(self.frame_60)

        self.l_add_ds_frame = QFrame(self.frame_58)
        self.l_add_ds_frame.setObjectName(u"l_add_ds_frame")
        self.l_add_ds_frame.setMinimumSize(QSize(0, 0))
        self.l_add_ds_frame.setMaximumSize(QSize(16777215, 0))
        self.l_add_ds_frame.setFrameShape(QFrame.StyledPanel)
        self.l_add_ds_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.l_add_ds_frame)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.l_add_ds_lineedit = QLineEdit(self.l_add_ds_frame)
        self.l_add_ds_lineedit.setObjectName(u"l_add_ds_lineedit")
        sizePolicy2.setHeightForWidth(self.l_add_ds_lineedit.sizePolicy().hasHeightForWidth())
        self.l_add_ds_lineedit.setSizePolicy(sizePolicy2)
        self.l_add_ds_lineedit.setMaximumSize(QSize(280, 16777215))

        self.verticalLayout_105.addWidget(self.l_add_ds_lineedit)

        self.horizontalLayout_245 = QHBoxLayout()
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.l_add_ok = QPushButton(self.l_add_ds_frame)
        self.l_add_ok.setObjectName(u"l_add_ok")
        sizePolicy12.setHeightForWidth(self.l_add_ok.sizePolicy().hasHeightForWidth())
        self.l_add_ok.setSizePolicy(sizePolicy12)
        self.l_add_ok.setMinimumSize(QSize(0, 20))
        self.l_add_ok.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_245.addWidget(self.l_add_ok)

        self.l_add_cancel = QPushButton(self.l_add_ds_frame)
        self.l_add_cancel.setObjectName(u"l_add_cancel")
        sizePolicy12.setHeightForWidth(self.l_add_cancel.sizePolicy().hasHeightForWidth())
        self.l_add_cancel.setSizePolicy(sizePolicy12)
        self.l_add_cancel.setMinimumSize(QSize(0, 20))
        self.l_add_cancel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_245.addWidget(self.l_add_cancel)


        self.verticalLayout_105.addLayout(self.horizontalLayout_245)


        self.verticalLayout_103.addWidget(self.l_add_ds_frame)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_103.addItem(self.verticalSpacer_12)

        self.frame_74 = QFrame(self.frame_58)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_74)
        self.verticalLayout_75.setSpacing(20)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.localization_train = QPushButton(self.frame_74)
        self.localization_train.setObjectName(u"localization_train")
        self.localization_train.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.localization_train.sizePolicy().hasHeightForWidth())
        self.localization_train.setSizePolicy(sizePolicy1)
        self.localization_train.setMinimumSize(QSize(180, 35))
        self.localization_train.setMaximumSize(QSize(16777215, 16777215))
        self.localization_train.setCursor(QCursor(Qt.PointingHandCursor))
        self.localization_train.setAcceptDrops(False)
        self.localization_train.setToolTipDuration(-1)
        self.localization_train.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"	text-align: center\n"
"}\n"
"\n"
"QPushButton:disabled  {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.localization_train.setAutoDefault(False)

        self.verticalLayout_75.addWidget(self.localization_train, 0, Qt.AlignHCenter)

        self.localization_chart_checkbox = QCheckBox(self.frame_74)
        self.localization_chart_checkbox.setObjectName(u"localization_chart_checkbox")
        self.localization_chart_checkbox.setEnabled(False)
        self.localization_chart_checkbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_75.addWidget(self.localization_chart_checkbox, 0, Qt.AlignHCenter)

        self.localization_train_progressBar = QProgressBar(self.frame_74)
        self.localization_train_progressBar.setObjectName(u"localization_train_progressBar")
        self.localization_train_progressBar.setValue(0)

        self.verticalLayout_75.addWidget(self.localization_train_progressBar)


        self.verticalLayout_103.addWidget(self.frame_74)

        self.l_warning_train_page = QTextEdit(self.frame_58)
        self.l_warning_train_page.setObjectName(u"l_warning_train_page")
        self.l_warning_train_page.setStyleSheet(u"")
        self.l_warning_train_page.setReadOnly(True)

        self.verticalLayout_103.addWidget(self.l_warning_train_page)


        self.horizontalLayout_62.addWidget(self.frame_58)

        self.frame_61 = QFrame(self.page_localization_training)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_61)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(9, 0, 9, 0)
        self.frame_71 = QFrame(self.frame_61)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMaximumSize(QSize(16777215, 20))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_246 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalLayout_246.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_71)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(15, 15))
        self.label_18.setPixmap(QPixmap(u"images/train_iamge.jpg"))

        self.horizontalLayout_246.addWidget(self.label_18)

        self.label_8_3 = QLabel(self.frame_71)
        self.label_8_3.setObjectName(u"label_8_3")
        self.label_8_3.setFont(font1)

        self.horizontalLayout_246.addWidget(self.label_8_3)

        self.horizontalSpacer_19_4 = QSpacerItem(47, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_246.addItem(self.horizontalSpacer_19_4)

        self.label_13_3 = QLabel(self.frame_71)
        self.label_13_3.setObjectName(u"label_13_3")
        self.label_13_3.setMaximumSize(QSize(15, 15))
        self.label_13_3.setPixmap(QPixmap(u"images/val_iamge.jpg"))

        self.horizontalLayout_246.addWidget(self.label_13_3)

        self.label_19 = QLabel(self.frame_71)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_246.addWidget(self.label_19)


        self.verticalLayout_106.addWidget(self.frame_71, 0, Qt.AlignHCenter)

        self.frame_65 = QFrame(self.frame_61)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(16777215, 16777215))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_65)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.localization_chart_recall_frame = QFrame(self.frame_65)
        self.localization_chart_recall_frame.setObjectName(u"localization_chart_recall_frame")
        self.localization_chart_recall_frame.setFrameShape(QFrame.Panel)
        self.localization_chart_recall_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.localization_chart_recall_frame, 2, 0, 1, 1)

        self.localization_chart_loss_frame = QFrame(self.frame_65)
        self.localization_chart_loss_frame.setObjectName(u"localization_chart_loss_frame")
        self.localization_chart_loss_frame.setStyleSheet(u"")
        self.localization_chart_loss_frame.setFrameShape(QFrame.Panel)
        self.localization_chart_loss_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.localization_chart_loss_frame, 0, 0, 1, 1)

        self.localization_chart_acc_frame = QFrame(self.frame_65)
        self.localization_chart_acc_frame.setObjectName(u"localization_chart_acc_frame")
        self.localization_chart_acc_frame.setStyleSheet(u"")
        self.localization_chart_acc_frame.setFrameShape(QFrame.Panel)
        self.localization_chart_acc_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.localization_chart_acc_frame, 0, 1, 1, 1)

        self.localization_chart_prec_frame = QFrame(self.frame_65)
        self.localization_chart_prec_frame.setObjectName(u"localization_chart_prec_frame")
        self.localization_chart_prec_frame.setFrameShape(QFrame.Panel)
        self.localization_chart_prec_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.localization_chart_prec_frame, 2, 1, 1, 1)


        self.verticalLayout_106.addWidget(self.frame_65)

        self.localization_chart_scrollbar = QScrollBar(self.frame_61)
        self.localization_chart_scrollbar.setObjectName(u"localization_chart_scrollbar")
        self.localization_chart_scrollbar.setCursor(QCursor(Qt.OpenHandCursor))
        self.localization_chart_scrollbar.setMaximum(0)
        self.localization_chart_scrollbar.setPageStep(1)
        self.localization_chart_scrollbar.setOrientation(Qt.Horizontal)

        self.verticalLayout_106.addWidget(self.localization_chart_scrollbar)


        self.horizontalLayout_62.addWidget(self.frame_61)

        self.stackedWidget_localization.addWidget(self.page_localization_training)
        self.page_localization_history = QWidget()
        self.page_localization_history.setObjectName(u"page_localization_history")
        self.horizontalLayout_59 = QHBoxLayout(self.page_localization_history)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.page_localization_history)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(340, 0))
        self.frame_32.setMaximumSize(QSize(340, 16777215))
        self.frame_32.setFrameShape(QFrame.Panel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_32)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.groupBox_35 = QGroupBox(self.frame_32)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setMinimumSize(QSize(0, 0))
        self.groupBox_35.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_35.setStyleSheet(u"")
        self.verticalLayout_62 = QVBoxLayout(self.groupBox_35)
        self.verticalLayout_62.setSpacing(2)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_90 = QLabel(self.groupBox_35)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMaximumSize(QSize(16777215, 20))
        self.label_90.setFont(font1)

        self.horizontalLayout_54.addWidget(self.label_90)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.localization_name_filter_combo = QComboBox(self.groupBox_35)
        self.localization_name_filter_combo.setObjectName(u"localization_name_filter_combo")

        self.horizontalLayout_55.addWidget(self.localization_name_filter_combo)


        self.horizontalLayout_54.addLayout(self.horizontalLayout_55)


        self.verticalLayout_62.addLayout(self.horizontalLayout_54)

        self.line_28 = QFrame(self.groupBox_35)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_28)

        self.horizontalLayout_240 = QHBoxLayout()
        self.horizontalLayout_240.setSpacing(0)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.label_91 = QLabel(self.groupBox_35)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(110, 0))
        self.label_91.setMaximumSize(QSize(110, 16777215))
        self.label_91.setFont(font1)

        self.horizontalLayout_240.addWidget(self.label_91)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_240.addItem(self.horizontalSpacer_22)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setSpacing(10)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_111_4 = QHBoxLayout()
        self.horizontalLayout_111_4.setObjectName(u"horizontalLayout_111_4")
        self.label_92 = QLabel(self.groupBox_35)
        self.label_92.setObjectName(u"label_92")
        sizePolicy2.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy2)
        self.label_92.setMaximumSize(QSize(16777215, 20))
        self.label_92.setFont(font1)

        self.horizontalLayout_111_4.addWidget(self.label_92)

        self.localization_epoch_min_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_epoch_min_filter_lineedit.setObjectName(u"localization_epoch_min_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_epoch_min_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_epoch_min_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_epoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_epoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_epoch_min_filter_lineedit.setFont(font1)
        self.localization_epoch_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_4.addWidget(self.localization_epoch_min_filter_lineedit)


        self.horizontalLayout_56.addLayout(self.horizontalLayout_111_4)

        self.horizontalLayout_121_4 = QHBoxLayout()
        self.horizontalLayout_121_4.setObjectName(u"horizontalLayout_121_4")
        self.label_93 = QLabel(self.groupBox_35)
        self.label_93.setObjectName(u"label_93")
        sizePolicy2.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy2)
        self.label_93.setMaximumSize(QSize(16777215, 20))
        self.label_93.setFont(font1)

        self.horizontalLayout_121_4.addWidget(self.label_93)

        self.localization_epoch_max_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_epoch_max_filter_lineedit.setObjectName(u"localization_epoch_max_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_epoch_max_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_epoch_max_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_epoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_epoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_epoch_max_filter_lineedit.setFont(font1)
        self.localization_epoch_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_4.addWidget(self.localization_epoch_max_filter_lineedit)


        self.horizontalLayout_56.addLayout(self.horizontalLayout_121_4)


        self.horizontalLayout_240.addLayout(self.horizontalLayout_56)

        self.line_19 = QFrame(self.groupBox_35)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_240.addWidget(self.line_19)


        self.verticalLayout_62.addLayout(self.horizontalLayout_240)

        self.line_47_4 = QFrame(self.groupBox_35)
        self.line_47_4.setObjectName(u"line_47_4")
        self.line_47_4.setFrameShape(QFrame.HLine)
        self.line_47_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_47_4)

        self.horizontalLayout_247 = QHBoxLayout()
        self.horizontalLayout_247.setSpacing(0)
        self.horizontalLayout_247.setObjectName(u"horizontalLayout_247")
        self.label_2471 = QLabel(self.groupBox_35)
        self.label_2471.setObjectName(u"label_2471")
        self.label_2471.setMinimumSize(QSize(110, 0))
        self.label_2471.setMaximumSize(QSize(110, 16777215))
        self.label_2471.setFont(font1)

        self.horizontalLayout_247.addWidget(self.label_2471)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_247.addItem(self.horizontalSpacer_29)

        self.horizontalLayout_248 = QHBoxLayout()
        self.horizontalLayout_248.setSpacing(10)
        self.horizontalLayout_248.setObjectName(u"horizontalLayout_248")
        self.horizontalLayout_249 = QHBoxLayout()
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.label_2511 = QLabel(self.groupBox_35)
        self.label_2511.setObjectName(u"label_2511")
        sizePolicy2.setHeightForWidth(self.label_2511.sizePolicy().hasHeightForWidth())
        self.label_2511.setSizePolicy(sizePolicy2)
        self.label_2511.setMaximumSize(QSize(16777215, 20))
        self.label_2511.setFont(font1)

        self.horizontalLayout_249.addWidget(self.label_2511)

        self.localization_batch_min_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_batch_min_filter_lineedit.setObjectName(u"localization_batch_min_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_batch_min_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_batch_min_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_batch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_batch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_batch_min_filter_lineedit.setFont(font1)
        self.localization_batch_min_filter_lineedit.setInputMethodHints(Qt.ImhNone)
        self.localization_batch_min_filter_lineedit.setMaxLength(3)
        self.localization_batch_min_filter_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_249.addWidget(self.localization_batch_min_filter_lineedit)


        self.horizontalLayout_248.addLayout(self.horizontalLayout_249)

        self.horizontalLayout_250 = QHBoxLayout()
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.label_252 = QLabel(self.groupBox_35)
        self.label_252.setObjectName(u"label_252")
        sizePolicy2.setHeightForWidth(self.label_252.sizePolicy().hasHeightForWidth())
        self.label_252.setSizePolicy(sizePolicy2)
        self.label_252.setMaximumSize(QSize(16777215, 20))
        self.label_252.setFont(font1)

        self.horizontalLayout_250.addWidget(self.label_252)

        self.localization_batch_max_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_batch_max_filter_lineedit.setObjectName(u"localization_batch_max_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_batch_max_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_batch_max_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_batch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_batch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_batch_max_filter_lineedit.setFont(font1)
        self.localization_batch_max_filter_lineedit.setMaxLength(3)

        self.horizontalLayout_250.addWidget(self.localization_batch_max_filter_lineedit)


        self.horizontalLayout_248.addLayout(self.horizontalLayout_250)


        self.horizontalLayout_247.addLayout(self.horizontalLayout_248)

        self.line_40_4 = QFrame(self.groupBox_35)
        self.line_40_4.setObjectName(u"line_40_4")
        self.line_40_4.setFrameShape(QFrame.HLine)
        self.line_40_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_247.addWidget(self.line_40_4)


        self.verticalLayout_62.addLayout(self.horizontalLayout_247)

        self.line_86 = QFrame(self.groupBox_35)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setFrameShape(QFrame.HLine)
        self.line_86.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_86)

        self.horizontalLayout_251 = QHBoxLayout()
        self.horizontalLayout_251.setSpacing(0)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.label_95 = QLabel(self.groupBox_35)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(110, 0))
        self.label_95.setMaximumSize(QSize(110, 16777215))
        self.label_95.setFont(font1)

        self.horizontalLayout_251.addWidget(self.label_95)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_251.addItem(self.horizontalSpacer_43)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(10)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_252 = QHBoxLayout()
        self.horizontalLayout_252.setObjectName(u"horizontalLayout_252")
        self.label_96 = QLabel(self.groupBox_35)
        self.label_96.setObjectName(u"label_96")
        sizePolicy2.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy2)
        self.label_96.setMaximumSize(QSize(16777215, 20))
        self.label_96.setFont(font1)

        self.horizontalLayout_252.addWidget(self.label_96)

        self.localization_split_min_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_split_min_filter_lineedit.setObjectName(u"localization_split_min_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_split_min_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_split_min_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_split_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_split_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_split_min_filter_lineedit.setFont(font1)
        self.localization_split_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_252.addWidget(self.localization_split_min_filter_lineedit)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_252)

        self.horizontalLayout_253 = QHBoxLayout()
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.label_97 = QLabel(self.groupBox_35)
        self.label_97.setObjectName(u"label_97")
        sizePolicy2.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy2)
        self.label_97.setMaximumSize(QSize(16777215, 20))
        self.label_97.setFont(font1)

        self.horizontalLayout_253.addWidget(self.label_97)

        self.localization_split_max_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_split_max_filter_lineedit.setObjectName(u"localization_split_max_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_split_max_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_split_max_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_split_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_split_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_split_max_filter_lineedit.setFont(font1)
        self.localization_split_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_253.addWidget(self.localization_split_max_filter_lineedit)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_253)


        self.horizontalLayout_251.addLayout(self.horizontalLayout_57)

        self.line_33_4 = QFrame(self.groupBox_35)
        self.line_33_4.setObjectName(u"line_33_4")
        self.line_33_4.setFrameShape(QFrame.HLine)
        self.line_33_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_251.addWidget(self.line_33_4)


        self.verticalLayout_62.addLayout(self.horizontalLayout_251)

        self.line_87 = QFrame(self.groupBox_35)
        self.line_87.setObjectName(u"line_87")
        self.line_87.setFrameShape(QFrame.HLine)
        self.line_87.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_87)

        self.horizontalLayout_254 = QHBoxLayout()
        self.horizontalLayout_254.setSpacing(0)
        self.horizontalLayout_254.setObjectName(u"horizontalLayout_254")
        self.label_110 = QLabel(self.groupBox_35)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(110, 0))
        self.label_110.setMaximumSize(QSize(110, 16777215))
        self.label_110.setFont(font1)

        self.horizontalLayout_254.addWidget(self.label_110)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_254.addItem(self.horizontalSpacer_47)

        self.horizontalLayout_255 = QHBoxLayout()
        self.horizontalLayout_255.setSpacing(10)
        self.horizontalLayout_255.setObjectName(u"horizontalLayout_255")
        self.horizontalLayout_256 = QHBoxLayout()
        self.horizontalLayout_256.setObjectName(u"horizontalLayout_256")
        self.label_132_4 = QLabel(self.groupBox_35)
        self.label_132_4.setObjectName(u"label_132_4")
        sizePolicy2.setHeightForWidth(self.label_132_4.sizePolicy().hasHeightForWidth())
        self.label_132_4.setSizePolicy(sizePolicy2)
        self.label_132_4.setMaximumSize(QSize(16777215, 20))
        self.label_132_4.setFont(font1)

        self.horizontalLayout_256.addWidget(self.label_132_4)

        self.localization_loss_min_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_loss_min_filter_lineedit.setObjectName(u"localization_loss_min_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_loss_min_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_loss_min_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_loss_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_loss_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_loss_min_filter_lineedit.setFont(font1)
        self.localization_loss_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_256.addWidget(self.localization_loss_min_filter_lineedit)


        self.horizontalLayout_255.addLayout(self.horizontalLayout_256)

        self.horizontalLayout_257 = QHBoxLayout()
        self.horizontalLayout_257.setObjectName(u"horizontalLayout_257")
        self.label_253 = QLabel(self.groupBox_35)
        self.label_253.setObjectName(u"label_253")
        sizePolicy2.setHeightForWidth(self.label_253.sizePolicy().hasHeightForWidth())
        self.label_253.setSizePolicy(sizePolicy2)
        self.label_253.setMaximumSize(QSize(16777215, 20))
        self.label_253.setFont(font1)

        self.horizontalLayout_257.addWidget(self.label_253)

        self.localization_loss_max_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_loss_max_filter_lineedit.setObjectName(u"localization_loss_max_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_loss_max_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_loss_max_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_loss_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_loss_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_loss_max_filter_lineedit.setFont(font1)
        self.localization_loss_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_257.addWidget(self.localization_loss_max_filter_lineedit)


        self.horizontalLayout_255.addLayout(self.horizontalLayout_257)


        self.horizontalLayout_254.addLayout(self.horizontalLayout_255)

        self.line_88 = QFrame(self.groupBox_35)
        self.line_88.setObjectName(u"line_88")
        self.line_88.setFrameShape(QFrame.HLine)
        self.line_88.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_254.addWidget(self.line_88)


        self.verticalLayout_62.addLayout(self.horizontalLayout_254)

        self.line_89 = QFrame(self.groupBox_35)
        self.line_89.setObjectName(u"line_89")
        self.line_89.setFrameShape(QFrame.HLine)
        self.line_89.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_89)

        self.horizontalLayout_258 = QHBoxLayout()
        self.horizontalLayout_258.setSpacing(0)
        self.horizontalLayout_258.setObjectName(u"horizontalLayout_258")
        self.label_254 = QLabel(self.groupBox_35)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setMinimumSize(QSize(110, 0))
        self.label_254.setMaximumSize(QSize(110, 16777215))
        self.label_254.setFont(font1)

        self.horizontalLayout_258.addWidget(self.label_254)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_258.addItem(self.horizontalSpacer_48)

        self.horizontalLayout_259 = QHBoxLayout()
        self.horizontalLayout_259.setSpacing(10)
        self.horizontalLayout_259.setObjectName(u"horizontalLayout_259")
        self.horizontalLayout_260 = QHBoxLayout()
        self.horizontalLayout_260.setObjectName(u"horizontalLayout_260")
        self.label_255 = QLabel(self.groupBox_35)
        self.label_255.setObjectName(u"label_255")
        sizePolicy2.setHeightForWidth(self.label_255.sizePolicy().hasHeightForWidth())
        self.label_255.setSizePolicy(sizePolicy2)
        self.label_255.setMaximumSize(QSize(16777215, 20))
        self.label_255.setFont(font1)

        self.horizontalLayout_260.addWidget(self.label_255)

        self.localization_acc_min_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_acc_min_filter_lineedit.setObjectName(u"localization_acc_min_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_acc_min_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_acc_min_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_acc_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_acc_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_acc_min_filter_lineedit.setFont(font1)
        self.localization_acc_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_260.addWidget(self.localization_acc_min_filter_lineedit)


        self.horizontalLayout_259.addLayout(self.horizontalLayout_260)

        self.horizontalLayout_261 = QHBoxLayout()
        self.horizontalLayout_261.setObjectName(u"horizontalLayout_261")
        self.label_256 = QLabel(self.groupBox_35)
        self.label_256.setObjectName(u"label_256")
        sizePolicy2.setHeightForWidth(self.label_256.sizePolicy().hasHeightForWidth())
        self.label_256.setSizePolicy(sizePolicy2)
        self.label_256.setMaximumSize(QSize(16777215, 20))
        self.label_256.setFont(font1)

        self.horizontalLayout_261.addWidget(self.label_256)

        self.localization_acc_max_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_acc_max_filter_lineedit.setObjectName(u"localization_acc_max_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_acc_max_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_acc_max_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_acc_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_acc_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_acc_max_filter_lineedit.setFont(font1)
        self.localization_acc_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_261.addWidget(self.localization_acc_max_filter_lineedit)


        self.horizontalLayout_259.addLayout(self.horizontalLayout_261)


        self.horizontalLayout_258.addLayout(self.horizontalLayout_259)

        self.line_90 = QFrame(self.groupBox_35)
        self.line_90.setObjectName(u"line_90")
        self.line_90.setFrameShape(QFrame.HLine)
        self.line_90.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_258.addWidget(self.line_90)


        self.verticalLayout_62.addLayout(self.horizontalLayout_258)

        self.line_91 = QFrame(self.groupBox_35)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setFrameShape(QFrame.HLine)
        self.line_91.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_91)

        self.horizontalLayout_262 = QHBoxLayout()
        self.horizontalLayout_262.setSpacing(0)
        self.horizontalLayout_262.setObjectName(u"horizontalLayout_262")
        self.label_257 = QLabel(self.groupBox_35)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setMinimumSize(QSize(110, 0))
        self.label_257.setMaximumSize(QSize(110, 16777215))
        self.label_257.setFont(font1)

        self.horizontalLayout_262.addWidget(self.label_257)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_262.addItem(self.horizontalSpacer_49)

        self.horizontalLayout_263 = QHBoxLayout()
        self.horizontalLayout_263.setSpacing(10)
        self.horizontalLayout_263.setObjectName(u"horizontalLayout_263")
        self.horizontalLayout_264 = QHBoxLayout()
        self.horizontalLayout_264.setObjectName(u"horizontalLayout_264")
        self.label_258 = QLabel(self.groupBox_35)
        self.label_258.setObjectName(u"label_258")
        sizePolicy2.setHeightForWidth(self.label_258.sizePolicy().hasHeightForWidth())
        self.label_258.setSizePolicy(sizePolicy2)
        self.label_258.setMaximumSize(QSize(16777215, 20))
        self.label_258.setFont(font1)

        self.horizontalLayout_264.addWidget(self.label_258)

        self.localization_iou_min_filter_lineedit_2 = QLineEdit(self.groupBox_35)
        self.localization_iou_min_filter_lineedit_2.setObjectName(u"localization_iou_min_filter_lineedit_2")
        sizePolicy2.setHeightForWidth(self.localization_iou_min_filter_lineedit_2.sizePolicy().hasHeightForWidth())
        self.localization_iou_min_filter_lineedit_2.setSizePolicy(sizePolicy2)
        self.localization_iou_min_filter_lineedit_2.setMinimumSize(QSize(50, 0))
        self.localization_iou_min_filter_lineedit_2.setMaximumSize(QSize(50, 30))
        self.localization_iou_min_filter_lineedit_2.setFont(font1)
        self.localization_iou_min_filter_lineedit_2.setMaxLength(4)

        self.horizontalLayout_264.addWidget(self.localization_iou_min_filter_lineedit_2)


        self.horizontalLayout_263.addLayout(self.horizontalLayout_264)

        self.horizontalLayout_265 = QHBoxLayout()
        self.horizontalLayout_265.setObjectName(u"horizontalLayout_265")
        self.label_259 = QLabel(self.groupBox_35)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setMaximumSize(QSize(16777215, 20))
        self.label_259.setFont(font1)

        self.horizontalLayout_265.addWidget(self.label_259)

        self.localization_iou_max_filter_lineedit_2 = QLineEdit(self.groupBox_35)
        self.localization_iou_max_filter_lineedit_2.setObjectName(u"localization_iou_max_filter_lineedit_2")
        sizePolicy2.setHeightForWidth(self.localization_iou_max_filter_lineedit_2.sizePolicy().hasHeightForWidth())
        self.localization_iou_max_filter_lineedit_2.setSizePolicy(sizePolicy2)
        self.localization_iou_max_filter_lineedit_2.setMinimumSize(QSize(50, 0))
        self.localization_iou_max_filter_lineedit_2.setMaximumSize(QSize(50, 30))
        self.localization_iou_max_filter_lineedit_2.setFont(font1)
        self.localization_iou_max_filter_lineedit_2.setMaxLength(4)

        self.horizontalLayout_265.addWidget(self.localization_iou_max_filter_lineedit_2)


        self.horizontalLayout_263.addLayout(self.horizontalLayout_265)


        self.horizontalLayout_262.addLayout(self.horizontalLayout_263)

        self.line_92 = QFrame(self.groupBox_35)
        self.line_92.setObjectName(u"line_92")
        self.line_92.setFrameShape(QFrame.HLine)
        self.line_92.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_262.addWidget(self.line_92)


        self.verticalLayout_62.addLayout(self.horizontalLayout_262)

        self.line_93 = QFrame(self.groupBox_35)
        self.line_93.setObjectName(u"line_93")
        self.line_93.setFrameShape(QFrame.HLine)
        self.line_93.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_93)

        self.horizontalLayout_266 = QHBoxLayout()
        self.horizontalLayout_266.setSpacing(0)
        self.horizontalLayout_266.setObjectName(u"horizontalLayout_266")
        self.label_260 = QLabel(self.groupBox_35)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setMinimumSize(QSize(110, 0))
        self.label_260.setMaximumSize(QSize(110, 16777215))
        self.label_260.setFont(font1)

        self.horizontalLayout_266.addWidget(self.label_260)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_266.addItem(self.horizontalSpacer_50)

        self.horizontalLayout_267 = QHBoxLayout()
        self.horizontalLayout_267.setSpacing(10)
        self.horizontalLayout_267.setObjectName(u"horizontalLayout_267")
        self.horizontalLayout_268 = QHBoxLayout()
        self.horizontalLayout_268.setObjectName(u"horizontalLayout_268")
        self.label_261 = QLabel(self.groupBox_35)
        self.label_261.setObjectName(u"label_261")
        sizePolicy2.setHeightForWidth(self.label_261.sizePolicy().hasHeightForWidth())
        self.label_261.setSizePolicy(sizePolicy2)
        self.label_261.setMaximumSize(QSize(16777215, 20))
        self.label_261.setFont(font1)

        self.horizontalLayout_268.addWidget(self.label_261)

        self.localization_fscore_min_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_fscore_min_filter_lineedit.setObjectName(u"localization_fscore_min_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_fscore_min_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_fscore_min_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_fscore_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_fscore_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_fscore_min_filter_lineedit.setFont(font1)
        self.localization_fscore_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_268.addWidget(self.localization_fscore_min_filter_lineedit)


        self.horizontalLayout_267.addLayout(self.horizontalLayout_268)

        self.horizontalLayout_269 = QHBoxLayout()
        self.horizontalLayout_269.setObjectName(u"horizontalLayout_269")
        self.label_262 = QLabel(self.groupBox_35)
        self.label_262.setObjectName(u"label_262")
        sizePolicy2.setHeightForWidth(self.label_262.sizePolicy().hasHeightForWidth())
        self.label_262.setSizePolicy(sizePolicy2)
        self.label_262.setMaximumSize(QSize(16777215, 20))
        self.label_262.setFont(font1)

        self.horizontalLayout_269.addWidget(self.label_262)

        self.localization_fscore_max_filter_lineedit = QLineEdit(self.groupBox_35)
        self.localization_fscore_max_filter_lineedit.setObjectName(u"localization_fscore_max_filter_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_fscore_max_filter_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_fscore_max_filter_lineedit.setSizePolicy(sizePolicy2)
        self.localization_fscore_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.localization_fscore_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.localization_fscore_max_filter_lineedit.setFont(font1)
        self.localization_fscore_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_269.addWidget(self.localization_fscore_max_filter_lineedit)


        self.horizontalLayout_267.addLayout(self.horizontalLayout_269)


        self.horizontalLayout_266.addLayout(self.horizontalLayout_267)

        self.line_94 = QFrame(self.groupBox_35)
        self.line_94.setObjectName(u"line_94")
        self.line_94.setFrameShape(QFrame.HLine)
        self.line_94.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_266.addWidget(self.line_94)


        self.verticalLayout_62.addLayout(self.horizontalLayout_266)

        self.line_95 = QFrame(self.groupBox_35)
        self.line_95.setObjectName(u"line_95")
        self.line_95.setFrameShape(QFrame.HLine)
        self.line_95.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_95)

        self.frame_80_1243124 = QFrame(self.groupBox_35)
        self.frame_80_1243124.setObjectName(u"frame_80_1243124")
        self.frame_80_1243124.setFrameShape(QFrame.StyledPanel)
        self.frame_80_1243124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47_123424 = QVBoxLayout(self.frame_80_1243124)
        self.verticalLayout_47_123424.setSpacing(0)
        self.verticalLayout_47_123424.setObjectName(u"verticalLayout_47_123424")
        self.verticalLayout_47_123424.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46_124 = QVBoxLayout()
        self.verticalLayout_46_124.setSpacing(2)
        self.verticalLayout_46_124.setObjectName(u"verticalLayout_46_124")
        self.horizontalLayout_197_214 = QHBoxLayout()
        self.horizontalLayout_197_214.setSpacing(5)
        self.horizontalLayout_197_214.setObjectName(u"horizontalLayout_197_214")
        self.label_263 = QLabel(self.frame_80_1243124)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setMinimumSize(QSize(150, 0))
        self.label_263.setMaximumSize(QSize(150, 20))
        self.label_263.setFont(font1)

        self.horizontalLayout_197_214.addWidget(self.label_263)

        self.localization_start_year_lineedit = QLineEdit(self.frame_80_1243124)
        self.localization_start_year_lineedit.setObjectName(u"localization_start_year_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_start_year_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_start_year_lineedit.setSizePolicy(sizePolicy2)
        self.localization_start_year_lineedit.setMinimumSize(QSize(70, 0))
        self.localization_start_year_lineedit.setMaximumSize(QSize(70, 16777215))
        self.localization_start_year_lineedit.setFont(font1)
        self.localization_start_year_lineedit.setMaxLength(4)

        self.horizontalLayout_197_214.addWidget(self.localization_start_year_lineedit)

        self.label_264 = QLabel(self.frame_80_1243124)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setMinimumSize(QSize(5, 0))
        self.label_264.setMaximumSize(QSize(5, 20))
        self.label_264.setFont(font1)

        self.horizontalLayout_197_214.addWidget(self.label_264)

        self.localization_start_month_lineedit = QLineEdit(self.frame_80_1243124)
        self.localization_start_month_lineedit.setObjectName(u"localization_start_month_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_start_month_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_start_month_lineedit.setSizePolicy(sizePolicy2)
        self.localization_start_month_lineedit.setMinimumSize(QSize(40, 0))
        self.localization_start_month_lineedit.setMaximumSize(QSize(40, 16777215))
        self.localization_start_month_lineedit.setFont(font1)
        self.localization_start_month_lineedit.setMaxLength(2)

        self.horizontalLayout_197_214.addWidget(self.localization_start_month_lineedit)

        self.label_265 = QLabel(self.frame_80_1243124)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setMinimumSize(QSize(5, 0))
        self.label_265.setMaximumSize(QSize(5, 20))
        self.label_265.setFont(font1)

        self.horizontalLayout_197_214.addWidget(self.label_265)

        self.localization_start_day_lineedit = QLineEdit(self.frame_80_1243124)
        self.localization_start_day_lineedit.setObjectName(u"localization_start_day_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_start_day_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_start_day_lineedit.setSizePolicy(sizePolicy2)
        self.localization_start_day_lineedit.setMinimumSize(QSize(40, 0))
        self.localization_start_day_lineedit.setMaximumSize(QSize(40, 16777215))
        self.localization_start_day_lineedit.setFont(font1)
        self.localization_start_day_lineedit.setMaxLength(2)

        self.horizontalLayout_197_214.addWidget(self.localization_start_day_lineedit)


        self.verticalLayout_46_124.addLayout(self.horizontalLayout_197_214)

        self.horizontalLayout_198_123422 = QHBoxLayout()
        self.horizontalLayout_198_123422.setSpacing(5)
        self.horizontalLayout_198_123422.setObjectName(u"horizontalLayout_198_123422")
        self.label_266 = QLabel(self.frame_80_1243124)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setMinimumSize(QSize(150, 0))
        self.label_266.setMaximumSize(QSize(150, 20))
        self.label_266.setFont(font1)

        self.horizontalLayout_198_123422.addWidget(self.label_266)

        self.localization_end_year_lineedit = QLineEdit(self.frame_80_1243124)
        self.localization_end_year_lineedit.setObjectName(u"localization_end_year_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_end_year_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_end_year_lineedit.setSizePolicy(sizePolicy2)
        self.localization_end_year_lineedit.setMinimumSize(QSize(70, 0))
        self.localization_end_year_lineedit.setMaximumSize(QSize(70, 16777215))
        self.localization_end_year_lineedit.setFont(font1)
        self.localization_end_year_lineedit.setMaxLength(4)

        self.horizontalLayout_198_123422.addWidget(self.localization_end_year_lineedit)

        self.label_267 = QLabel(self.frame_80_1243124)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setMinimumSize(QSize(5, 0))
        self.label_267.setMaximumSize(QSize(5, 20))
        self.label_267.setFont(font1)

        self.horizontalLayout_198_123422.addWidget(self.label_267)

        self.localization_end_month_lineedit = QLineEdit(self.frame_80_1243124)
        self.localization_end_month_lineedit.setObjectName(u"localization_end_month_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_end_month_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_end_month_lineedit.setSizePolicy(sizePolicy2)
        self.localization_end_month_lineedit.setMinimumSize(QSize(40, 0))
        self.localization_end_month_lineedit.setMaximumSize(QSize(40, 16777215))
        self.localization_end_month_lineedit.setFont(font1)
        self.localization_end_month_lineedit.setMaxLength(2)

        self.horizontalLayout_198_123422.addWidget(self.localization_end_month_lineedit)

        self.label_268 = QLabel(self.frame_80_1243124)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setMinimumSize(QSize(5, 0))
        self.label_268.setMaximumSize(QSize(5, 20))
        self.label_268.setFont(font1)

        self.horizontalLayout_198_123422.addWidget(self.label_268)

        self.localization_end_day_lineedit = QLineEdit(self.frame_80_1243124)
        self.localization_end_day_lineedit.setObjectName(u"localization_end_day_lineedit")
        sizePolicy2.setHeightForWidth(self.localization_end_day_lineedit.sizePolicy().hasHeightForWidth())
        self.localization_end_day_lineedit.setSizePolicy(sizePolicy2)
        self.localization_end_day_lineedit.setMinimumSize(QSize(40, 0))
        self.localization_end_day_lineedit.setMaximumSize(QSize(40, 16777215))
        self.localization_end_day_lineedit.setFont(font1)
        self.localization_end_day_lineedit.setMaxLength(2)

        self.horizontalLayout_198_123422.addWidget(self.localization_end_day_lineedit)


        self.verticalLayout_46_124.addLayout(self.horizontalLayout_198_123422)


        self.verticalLayout_47_123424.addLayout(self.verticalLayout_46_124)


        self.verticalLayout_62.addWidget(self.frame_80_1243124)

        self.line_98 = QFrame(self.groupBox_35)
        self.line_98.setObjectName(u"line_98")
        self.line_98.setFrameShape(QFrame.HLine)
        self.line_98.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_62.addWidget(self.line_98)

        self.horizontalLayout_270 = QHBoxLayout()
        self.horizontalLayout_270.setSpacing(20)
        self.horizontalLayout_270.setObjectName(u"horizontalLayout_270")
        self.localization_filter_btn = QPushButton(self.groupBox_35)
        self.localization_filter_btn.setObjectName(u"localization_filter_btn")
        self.localization_filter_btn.setMinimumSize(QSize(0, 30))
        self.localization_filter_btn.setMaximumSize(QSize(16777215, 30))
        self.localization_filter_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_270.addWidget(self.localization_filter_btn)

        self.localization_clearfilter_btn = QPushButton(self.groupBox_35)
        self.localization_clearfilter_btn.setObjectName(u"localization_clearfilter_btn")
        self.localization_clearfilter_btn.setMinimumSize(QSize(0, 30))
        self.localization_clearfilter_btn.setMaximumSize(QSize(16777215, 30))
        self.localization_clearfilter_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_270.addWidget(self.localization_clearfilter_btn)


        self.verticalLayout_62.addLayout(self.horizontalLayout_270)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_6)


        self.verticalLayout_63.addWidget(self.groupBox_35)


        self.horizontalLayout_59.addWidget(self.frame_32)

        self.frame_34 = QFrame(self.page_localization_history)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97_3 = QVBoxLayout(self.frame_34)
        self.verticalLayout_97_3.setSpacing(0)
        self.verticalLayout_97_3.setObjectName(u"verticalLayout_97_3")
        self.verticalLayout_97_3.setContentsMargins(0, 0, 0, 0)
        self.localization_history_tabel = QTableWidget(self.frame_34)
        if (self.localization_history_tabel.columnCount() < 19):
            self.localization_history_tabel.setColumnCount(19)
        self.localization_history_tabel.setObjectName(u"localization_history_tabel")
        self.localization_history_tabel.setRowCount(0)
        self.localization_history_tabel.setColumnCount(19)
        self.localization_history_tabel.horizontalHeader().setCascadingSectionResizes(True)
        self.localization_history_tabel.horizontalHeader().setMinimumSectionSize(150)
        self.localization_history_tabel.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_97_3.addWidget(self.localization_history_tabel)

        self.frame_68_4 = QFrame(self.frame_34)
        self.frame_68_4.setObjectName(u"frame_68_4")
        self.frame_68_4.setFrameShape(QFrame.StyledPanel)
        self.frame_68_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_68_4)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.localization_table_refresh_btn = QPushButton(self.frame_68_4)
        self.localization_table_refresh_btn.setObjectName(u"localization_table_refresh_btn")
        self.localization_table_refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.localization_table_refresh_btn.setLayoutDirection(Qt.RightToLeft)
        self.localization_table_refresh_btn.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        icon26 = QIcon()
        icon26.addFile(u"images/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.localization_table_refresh_btn.setIcon(icon26)
        self.localization_table_refresh_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_58.addWidget(self.localization_table_refresh_btn)

        self.line_14 = QFrame(self.frame_68_4)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_58.addWidget(self.line_14)

        self.localization_tabel_prev = QPushButton(self.frame_68_4)
        self.localization_tabel_prev.setObjectName(u"localization_tabel_prev")
        self.localization_tabel_prev.setEnabled(False)
        self.localization_tabel_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.localization_tabel_prev.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.localization_tabel_prev.setIcon(icon16)
        self.localization_tabel_prev.setIconSize(QSize(30, 30))

        self.horizontalLayout_58.addWidget(self.localization_tabel_prev)

        self.localization_tabel_page = QLineEdit(self.frame_68_4)
        self.localization_tabel_page.setObjectName(u"localization_tabel_page")
        self.localization_tabel_page.setEnabled(False)
        self.localization_tabel_page.setMinimumSize(QSize(50, 30))
        self.localization_tabel_page.setMaximumSize(QSize(50, 30))
        self.localization_tabel_page.setStyleSheet(u"padding:0;")
        self.localization_tabel_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.localization_tabel_page)

        self.localization_tabel_next = QPushButton(self.frame_68_4)
        self.localization_tabel_next.setObjectName(u"localization_tabel_next")
        self.localization_tabel_next.setEnabled(True)
        self.localization_tabel_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.localization_tabel_next.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.localization_tabel_next.setIcon(icon15)
        self.localization_tabel_next.setIconSize(QSize(30, 30))

        self.horizontalLayout_58.addWidget(self.localization_tabel_next)

        self.line_21 = QFrame(self.frame_68_4)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_58.addWidget(self.line_21)

        self.localization_tabel_label = QLabel(self.frame_68_4)
        self.localization_tabel_label.setObjectName(u"localization_tabel_label")
        self.localization_tabel_label.setMinimumSize(QSize(600, 0))
        self.localization_tabel_label.setMaximumSize(QSize(600, 16777215))
        self.localization_tabel_label.setFrameShape(QFrame.Panel)
        self.localization_tabel_label.setFrameShadow(QFrame.Sunken)
        self.localization_tabel_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.localization_tabel_label)

        self.horizontalSpacer_20_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_20_4)


        self.verticalLayout_97_3.addWidget(self.frame_68_4)


        self.horizontalLayout_59.addWidget(self.frame_34)

        self.stackedWidget_localization.addWidget(self.page_localization_history)

        self.verticalLayout_23.addWidget(self.stackedWidget_localization)

        self.stackedWidget.addWidget(self.page_Localization)
        self.page_Classification = QWidget()
        self.page_Classification.setObjectName(u"page_Classification")
        self.verticalLayout_33 = QVBoxLayout(self.page_Classification)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
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
        self.classification_class_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.classification_class_list.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170 ,170, 170); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 ,195, 196);\n"
"}")

        self.horizontalLayout_19.addWidget(self.classification_class_list)

        self.classification_training = QPushButton(self.frame_10)
        self.classification_training.setObjectName(u"classification_training")
        self.classification_training.setMinimumSize(QSize(150, 40))
        self.classification_training.setMaximumSize(QSize(150, 16777215))
        self.classification_training.setCursor(QCursor(Qt.PointingHandCursor))
        self.classification_training.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(100, 100, 100); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"} \n"
"QPushButton:hover {\n"
"	background-color:  rgb(150 ,150, 150);\n"
"}")

        self.horizontalLayout_19.addWidget(self.classification_training)

        self.classification_history = QPushButton(self.frame_10)
        self.classification_history.setObjectName(u"classification_history")
        self.classification_history.setMinimumSize(QSize(150, 40))
        self.classification_history.setMaximumSize(QSize(150, 16777215))
        self.classification_history.setFont(font1)
        self.classification_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.classification_history.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(100, 100, 100); \n"
"	color: rgb(0,0,0); \n"
"	border: none;\n"
"} \n"
"QPushButton:hover {\n"
"	background-color:  rgb(150 ,150, 150);\n"
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
        self.stackedWidget_classification.setMinimumSize(QSize(0, 100))
        self.page_classification_class_list = QWidget()
        self.page_classification_class_list.setObjectName(u"page_classification_class_list")
        self.verticalLayout_29 = QVBoxLayout(self.page_classification_class_list)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_classification_class_list)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_21 = QFrame(self.frame_9)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_21)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setMaximumSize(QSize(16777215, 400))
        self.frame_22.setFrameShape(QFrame.Panel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.groupBox_80 = QGroupBox(self.frame_22)
        self.groupBox_80.setObjectName(u"groupBox_80")
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_80)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.classes_table = QTableWidget(self.groupBox_80)
        if (self.classes_table.columnCount() < 8):
            self.classes_table.setColumnCount(8)
        self.classes_table.setObjectName(u"classes_table")
        self.classes_table.setRowCount(0)
        self.classes_table.setColumnCount(8)
        self.classes_table.horizontalHeader().setCascadingSectionResizes(True)
        self.classes_table.horizontalHeader().setMinimumSectionSize(120)

        self.verticalLayout_30.addWidget(self.classes_table)


        self.horizontalLayout_23.addWidget(self.groupBox_80)

        self.groupBox_88 = QGroupBox(self.frame_22)
        self.groupBox_88.setObjectName(u"groupBox_88")
        self.groupBox_88.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_88)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.datasets_table = QTableWidget(self.groupBox_88)
        if (self.datasets_table.columnCount() < 3):
            self.datasets_table.setColumnCount(3)
        self.datasets_table.setObjectName(u"datasets_table")
        self.datasets_table.setColumnCount(3)
        self.datasets_table.horizontalHeader().setCascadingSectionResizes(True)
        self.datasets_table.horizontalHeader().setMinimumSectionSize(120)

        self.horizontalLayout_17.addWidget(self.datasets_table)


        self.horizontalLayout_23.addWidget(self.groupBox_88)


        self.verticalLayout_28.addWidget(self.frame_22)

        self.frame_90 = QFrame(self.frame_21)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 40))
        self.frame_90.setMaximumSize(QSize(16777215, 40))
        self.frame_90.setFrameShape(QFrame.Panel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_44)

        self.classlist_show_related_img_btn = QPushButton(self.frame_90)
        self.classlist_show_related_img_btn.setObjectName(u"classlist_show_related_img_btn")
        self.classlist_show_related_img_btn.setMinimumSize(QSize(80, 30))
        self.classlist_show_related_img_btn.setMaximumSize(QSize(80, 30))
        self.classlist_show_related_img_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_25.addWidget(self.classlist_show_related_img_btn)

        self.line_7_12342 = QFrame(self.frame_90)
        self.line_7_12342.setObjectName(u"line_7_12342")
        self.line_7_12342.setFrameShape(QFrame.VLine)
        self.line_7_12342.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_7_12342)

        self.classlist_msg_label = QLabel(self.frame_90)
        self.classlist_msg_label.setObjectName(u"classlist_msg_label")
        self.classlist_msg_label.setMinimumSize(QSize(600, 30))
        self.classlist_msg_label.setMaximumSize(QSize(600, 30))
        self.classlist_msg_label.setFrameShape(QFrame.Panel)
        self.classlist_msg_label.setFrameShadow(QFrame.Sunken)
        self.classlist_msg_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.classlist_msg_label)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_45)


        self.verticalLayout_28.addWidget(self.frame_90)

        self.frame_79 = QFrame(self.frame_21)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 200))
        self.frame_79.setFrameShape(QFrame.Panel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.classlist_prev_btn = QPushButton(self.frame_79)
        self.classlist_prev_btn.setObjectName(u"classlist_prev_btn")
        self.classlist_prev_btn.setEnabled(False)
        self.classlist_prev_btn.setMinimumSize(QSize(30, 30))
        self.classlist_prev_btn.setMaximumSize(QSize(30, 30))
        self.classlist_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.classlist_prev_btn.setIcon(icon16)
        self.classlist_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.classlist_prev_btn)

        self.class_list_slider_frame = QLabel(self.frame_79)
        self.class_list_slider_frame.setObjectName(u"class_list_slider_frame")
        self.class_list_slider_frame.setFrameShape(QFrame.Panel)
        self.class_list_slider_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.class_list_slider_frame)

        self.classlist_next_btn = QPushButton(self.frame_79)
        self.classlist_next_btn.setObjectName(u"classlist_next_btn")
        self.classlist_next_btn.setEnabled(False)
        self.classlist_next_btn.setMinimumSize(QSize(30, 30))
        self.classlist_next_btn.setMaximumSize(QSize(30, 30))
        self.classlist_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        self.classlist_next_btn.setIcon(icon15)
        self.classlist_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.classlist_next_btn)


        self.verticalLayout_28.addWidget(self.frame_79)


        self.horizontalLayout_16.addWidget(self.frame_21)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(400, 0))
        self.frame_14.setMaximumSize(QSize(400, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_14)
        self.verticalLayout_43.setSpacing(5)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_441 = QFrame(self.frame_14)
        self.frame_441.setObjectName(u"frame_441")
        self.frame_441.setMinimumSize(QSize(0, 0))
        self.frame_441.setMaximumSize(QSize(16777215, 16777215))
        self.frame_441.setFrameShape(QFrame.Panel)
        self.frame_441.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_441)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.binary_chart_frame = QGroupBox(self.frame_441)
        self.binary_chart_frame.setObjectName(u"binary_chart_frame")

        self.horizontalLayout_26.addWidget(self.binary_chart_frame)


        self.verticalLayout_43.addWidget(self.frame_441)

        self.frame_544 = QFrame(self.frame_14)
        self.frame_544.setObjectName(u"frame_544")
        self.frame_544.setFrameShape(QFrame.Panel)
        self.frame_544.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_544)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.classlist_chart_frame = QGroupBox(self.frame_544)
        self.classlist_chart_frame.setObjectName(u"classlist_chart_frame")

        self.horizontalLayout_30.addWidget(self.classlist_chart_frame)


        self.verticalLayout_43.addWidget(self.frame_544)


        self.horizontalLayout_16.addWidget(self.frame_14)


        self.verticalLayout_29.addWidget(self.frame_9)

        self.stackedWidget_classification.addWidget(self.page_classification_class_list)
        self.page_classification_training = QWidget()
        self.page_classification_training.setObjectName(u"page_classification_training")
        self.horizontalLayout_33 = QHBoxLayout(self.page_classification_training)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.page_classification_training)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 310))
        self.frame_23.setMaximumSize(QSize(310, 16777215))
        self.frame_23.setFrameShape(QFrame.Panel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_23)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(5, 5, 5, 5)
        self.groupBox_25 = QGroupBox(self.frame_23)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(0, 310))
        self.groupBox_25.setMaximumSize(QSize(310, 16777215))
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_31.setSpacing(2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.groupBox_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(290, 200))
        self.frame_26.setMaximumSize(QSize(290, 16777215))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, -1, -1, 0)
        self.label_67 = QLabel(self.frame_26)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 25))
        self.label_67.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_64.addWidget(self.label_67, 0, Qt.AlignLeft)

        self.classification_algo_combo = QComboBox(self.frame_26)
        self.classification_algo_combo.setObjectName(u"classification_algo_combo")
        self.classification_algo_combo.setMinimumSize(QSize(120, 25))
        self.classification_algo_combo.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_64.addWidget(self.classification_algo_combo)


        self.verticalLayout_32.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_72 = QLabel(self.frame_26)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 25))
        self.label_72.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_69.addWidget(self.label_72, 0, Qt.AlignLeft)

        self.class_epoch_lineedit = QLineEdit(self.frame_26)
        self.class_epoch_lineedit.setObjectName(u"class_epoch_lineedit")
        self.class_epoch_lineedit.setMinimumSize(QSize(0, 25))
        self.class_epoch_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_69.addWidget(self.class_epoch_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_74 = QLabel(self.frame_26)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 25))
        self.label_74.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_71.addWidget(self.label_74, 0, Qt.AlignLeft)

        self.class_batch_lineedit = QLineEdit(self.frame_26)
        self.class_batch_lineedit.setObjectName(u"class_batch_lineedit")
        self.class_batch_lineedit.setMinimumSize(QSize(0, 25))
        self.class_batch_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_71.addWidget(self.class_batch_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_69 = QLabel(self.frame_26)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 25))
        self.label_69.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_66.addWidget(self.label_69)

        self.class_lr_lineedit = QLineEdit(self.frame_26)
        self.class_lr_lineedit.setObjectName(u"class_lr_lineedit")
        self.class_lr_lineedit.setMinimumSize(QSize(0, 25))
        self.class_lr_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_66.addWidget(self.class_lr_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_71 = QLabel(self.frame_26)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 25))
        self.label_71.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_68.addWidget(self.label_71)

        self.class_tepoch_lineedit = QLineEdit(self.frame_26)
        self.class_tepoch_lineedit.setObjectName(u"class_tepoch_lineedit")
        self.class_tepoch_lineedit.setMinimumSize(QSize(0, 25))
        self.class_tepoch_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_68.addWidget(self.class_tepoch_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_68 = QLabel(self.frame_26)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(0, 25))
        self.label_68.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_65.addWidget(self.label_68)

        self.class_split_lineedit = QLineEdit(self.frame_26)
        self.class_split_lineedit.setObjectName(u"class_split_lineedit")
        self.class_split_lineedit.setMinimumSize(QSize(0, 25))
        self.class_split_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_65.addWidget(self.class_split_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_73 = QLabel(self.frame_26)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(0, 25))
        self.label_73.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_70.addWidget(self.label_73)

        self.pushButton_22 = QPushButton(self.frame_26)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(100, 25))
        self.pushButton_22.setMaximumSize(QSize(100, 25))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_70.addWidget(self.pushButton_22)


        self.verticalLayout_32.addLayout(self.horizontalLayout_70)

        self.textEdit = QTextEdit(self.frame_26)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_32.addWidget(self.textEdit)


        self.verticalLayout_31.addWidget(self.frame_26)

        self.frame_82 = QFrame(self.groupBox_25)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(290, 0))
        self.frame_82.setMaximumSize(QSize(290, 16777215))
        self.frame_82.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_82.setFrameShape(QFrame.NoFrame)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_82)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_82)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(100, 0))
        self.label_52.setStyleSheet(u"text-align: center;")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_52)

        self.table_classification_select_class = QTableWidget(self.frame_82)
        if (self.table_classification_select_class.columnCount() < 3):
            self.table_classification_select_class.setColumnCount(3)
        self.table_classification_select_class.setObjectName(u"table_classification_select_class")
        self.table_classification_select_class.setRowCount(0)
        self.table_classification_select_class.setColumnCount(3)

        self.verticalLayout_40.addWidget(self.table_classification_select_class)


        self.verticalLayout_31.addWidget(self.frame_82)

        self.line_6 = QFrame(self.groupBox_25)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_6)

        self.frame_84 = QFrame(self.groupBox_25)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.Panel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.class_check_train_btn = QPushButton(self.frame_84)
        self.class_check_train_btn.setObjectName(u"class_check_train_btn")
        self.class_check_train_btn.setMinimumSize(QSize(120, 25))
        self.class_check_train_btn.setMaximumSize(QSize(120, 25))
        self.class_check_train_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.class_check_train_btn)

        self.pushButton_19 = QPushButton(self.frame_84)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setEnabled(False)
        self.pushButton_19.setMinimumSize(QSize(120, 25))
        self.pushButton_19.setMaximumSize(QSize(120, 25))
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.pushButton_19)


        self.verticalLayout_31.addWidget(self.frame_84)

        self.classification_train_msg_label = QLabel(self.groupBox_25)
        self.classification_train_msg_label.setObjectName(u"classification_train_msg_label")
        self.classification_train_msg_label.setMinimumSize(QSize(0, 25))
        self.classification_train_msg_label.setMaximumSize(QSize(16777215, 25))
        self.classification_train_msg_label.setFrameShape(QFrame.Panel)
        self.classification_train_msg_label.setFrameShadow(QFrame.Sunken)
        self.classification_train_msg_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.classification_train_msg_label)


        self.verticalLayout_87.addWidget(self.groupBox_25)


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
        self.verticalLayout_61 = QVBoxLayout(self.frame_24)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_24)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 30))
        self.frame_83.setMaximumSize(QSize(16777215, 30))
        self.frame_83.setFrameShape(QFrame.Panel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_34)

        self.label_31 = QLabel(self.frame_83)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(15, 15))
        self.label_31.setMaximumSize(QSize(15, 15))
        self.label_31.setPixmap(QPixmap(u"images/train_iamge.jpg"))
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_83)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 15))
        self.label_32.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_27.addWidget(self.label_32)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_35)

        self.label_34 = QLabel(self.frame_83)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(15, 15))
        self.label_34.setMaximumSize(QSize(15, 15))
        self.label_34.setPixmap(QPixmap(u"images/val_iamge.jpg"))

        self.horizontalLayout_27.addWidget(self.label_34)

        self.label_38 = QLabel(self.frame_83)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 15))
        self.label_38.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_27.addWidget(self.label_38)

        self.line_49 = QFrame(self.frame_83)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.VLine)
        self.line_49.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_27.addWidget(self.line_49)

        self.cls_chart_checkbox = QCheckBox(self.frame_83)
        self.cls_chart_checkbox.setObjectName(u"cls_chart_checkbox")
        self.cls_chart_checkbox.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.cls_chart_checkbox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_7)


        self.verticalLayout_61.addWidget(self.frame_83)

        self.frame_81 = QFrame(self.frame_24)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_81)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cls_chart_recall_frame = QFrame(self.frame_81)
        self.cls_chart_recall_frame.setObjectName(u"cls_chart_recall_frame")
        self.cls_chart_recall_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_recall_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_recall_frame, 2, 0, 1, 1)

        self.cls_chart_prec_frame = QFrame(self.frame_81)
        self.cls_chart_prec_frame.setObjectName(u"cls_chart_prec_frame")
        self.cls_chart_prec_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_prec_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_prec_frame, 2, 1, 1, 1)

        self.cls_chart_loss_frame = QFrame(self.frame_81)
        self.cls_chart_loss_frame.setObjectName(u"cls_chart_loss_frame")
        self.cls_chart_loss_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_loss_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_loss_frame, 1, 0, 1, 1)

        self.cls_chart_acc_frame = QFrame(self.frame_81)
        self.cls_chart_acc_frame.setObjectName(u"cls_chart_acc_frame")
        self.cls_chart_acc_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_acc_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_acc_frame, 1, 1, 1, 1)


        self.verticalLayout_61.addWidget(self.frame_81)

        self.cls_chart_scrollbar = QScrollBar(self.frame_24)
        self.cls_chart_scrollbar.setObjectName(u"cls_chart_scrollbar")
        self.cls_chart_scrollbar.setCursor(QCursor(Qt.OpenHandCursor))
        self.cls_chart_scrollbar.setMaximum(0)
        self.cls_chart_scrollbar.setPageStep(1)
        self.cls_chart_scrollbar.setOrientation(Qt.Horizontal)

        self.verticalLayout_61.addWidget(self.cls_chart_scrollbar)


        self.horizontalLayout_33.addWidget(self.frame_24)

        self.stackedWidget_classification.addWidget(self.page_classification_training)
        self.page_classification_history = QWidget()
        self.page_classification_history.setObjectName(u"page_classification_history")
        self.horizontalLayout_38 = QHBoxLayout(self.page_classification_history)
        self.horizontalLayout_38.setSpacing(6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.page_classification_history)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(300, 16777215))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_27)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(300, 0))
        self.frame_29.setMaximumSize(QSize(300, 16777215))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Plain)
        self.frame_29.setLineWidth(1)
        self.verticalLayout_42 = QVBoxLayout(self.frame_29)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.groupBox_34 = QGroupBox(self.frame_29)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setMinimumSize(QSize(300, 0))
        self.groupBox_34.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_102 = QVBoxLayout(self.groupBox_34)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_160 = QLabel(self.groupBox_34)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(16777215, 20))
        self.label_160.setFont(font1)

        self.horizontalLayout_50.addWidget(self.label_160)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.cls_name_filter_combo = QComboBox(self.groupBox_34)
        self.cls_name_filter_combo.setObjectName(u"cls_name_filter_combo")
        self.cls_name_filter_combo.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_51.addWidget(self.cls_name_filter_combo)


        self.horizontalLayout_50.addLayout(self.horizontalLayout_51)


        self.verticalLayout_102.addLayout(self.horizontalLayout_50)

        self.line_26 = QFrame(self.groupBox_34)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_26)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setSpacing(0)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.label_161 = QLabel(self.groupBox_34)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font1)

        self.horizontalLayout_167.addWidget(self.label_161)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_36)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setSpacing(10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_111_3 = QHBoxLayout()
        self.horizontalLayout_111_3.setObjectName(u"horizontalLayout_111_3")
        self.label_162 = QLabel(self.groupBox_34)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMaximumSize(QSize(16777215, 20))
        self.label_162.setFont(font1)

        self.horizontalLayout_111_3.addWidget(self.label_162)

        self.cls_epoch_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_epoch_min_filter_lineedit.setObjectName(u"cls_epoch_min_filter_lineedit")
        self.cls_epoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_epoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_epoch_min_filter_lineedit.setFont(font1)
        self.cls_epoch_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_111_3.addWidget(self.cls_epoch_min_filter_lineedit)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_111_3)

        self.horizontalLayout_121_3 = QHBoxLayout()
        self.horizontalLayout_121_3.setObjectName(u"horizontalLayout_121_3")
        self.label_163 = QLabel(self.groupBox_34)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(16777215, 20))
        self.label_163.setFont(font1)

        self.horizontalLayout_121_3.addWidget(self.label_163)

        self.cls_epoch_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_epoch_max_filter_lineedit.setObjectName(u"cls_epoch_max_filter_lineedit")
        self.cls_epoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_epoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_epoch_max_filter_lineedit.setFont(font1)
        self.cls_epoch_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_121_3.addWidget(self.cls_epoch_max_filter_lineedit)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_121_3)


        self.horizontalLayout_167.addLayout(self.horizontalLayout_52)

        self.line_54 = QFrame(self.groupBox_34)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_167.addWidget(self.line_54)


        self.verticalLayout_102.addLayout(self.horizontalLayout_167)

        self.line_55 = QFrame(self.groupBox_34)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_55)

        self.horizontalLayout_122_3 = QHBoxLayout()
        self.horizontalLayout_122_3.setSpacing(0)
        self.horizontalLayout_122_3.setObjectName(u"horizontalLayout_122_3")
        self.label_164 = QLabel(self.groupBox_34)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setFont(font1)

        self.horizontalLayout_122_3.addWidget(self.label_164)

        self.horizontalSpacer_22_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_122_3.addItem(self.horizontalSpacer_22_4)

        self.horizontalLayout_48_4 = QHBoxLayout()
        self.horizontalLayout_48_4.setSpacing(10)
        self.horizontalLayout_48_4.setObjectName(u"horizontalLayout_48_4")
        self.horizontalLayout_123_4 = QHBoxLayout()
        self.horizontalLayout_123_4.setObjectName(u"horizontalLayout_123_4")
        self.label_165 = QLabel(self.groupBox_34)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMaximumSize(QSize(16777215, 20))
        self.label_165.setFont(font1)

        self.horizontalLayout_123_4.addWidget(self.label_165)

        self.cls_tepoch_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_tepoch_min_filter_lineedit.setObjectName(u"cls_tepoch_min_filter_lineedit")
        self.cls_tepoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_tepoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_tepoch_min_filter_lineedit.setFont(font1)
        self.cls_tepoch_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_123_4.addWidget(self.cls_tepoch_min_filter_lineedit)


        self.horizontalLayout_48_4.addLayout(self.horizontalLayout_123_4)

        self.horizontalLayout_124_4 = QHBoxLayout()
        self.horizontalLayout_124_4.setObjectName(u"horizontalLayout_124_4")
        self.label_86_3 = QLabel(self.groupBox_34)
        self.label_86_3.setObjectName(u"label_86_3")
        self.label_86_3.setMaximumSize(QSize(16777215, 20))
        self.label_86_3.setFont(font1)

        self.horizontalLayout_124_4.addWidget(self.label_86_3)

        self.cls_tepoch_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_tepoch_max_filter_lineedit.setObjectName(u"cls_tepoch_max_filter_lineedit")
        self.cls_tepoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_tepoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_tepoch_max_filter_lineedit.setFont(font1)
        self.cls_tepoch_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_124_4.addWidget(self.cls_tepoch_max_filter_lineedit)


        self.horizontalLayout_48_4.addLayout(self.horizontalLayout_124_4)


        self.horizontalLayout_122_3.addLayout(self.horizontalLayout_48_4)

        self.line_18_3 = QFrame(self.groupBox_34)
        self.line_18_3.setObjectName(u"line_18_3")
        self.line_18_3.setFrameShape(QFrame.HLine)
        self.line_18_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_122_3.addWidget(self.line_18_3)


        self.verticalLayout_102.addLayout(self.horizontalLayout_122_3)

        self.line_47_3 = QFrame(self.groupBox_34)
        self.line_47_3.setObjectName(u"line_47_3")
        self.line_47_3.setFrameShape(QFrame.HLine)
        self.line_47_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_47_3)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setSpacing(0)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.label_167 = QLabel(self.groupBox_34)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font1)

        self.horizontalLayout_169.addWidget(self.label_167)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_37)

        self.horizontalLayout_170 = QHBoxLayout()
        self.horizontalLayout_170.setSpacing(10)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_171 = QHBoxLayout()
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.label_168 = QLabel(self.groupBox_34)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMaximumSize(QSize(16777215, 20))
        self.label_168.setFont(font1)

        self.horizontalLayout_171.addWidget(self.label_168)

        self.cls_batch_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_batch_min_filter_lineedit.setObjectName(u"cls_batch_min_filter_lineedit")
        self.cls_batch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_batch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_batch_min_filter_lineedit.setFont(font1)
        self.cls_batch_min_filter_lineedit.setInputMethodHints(Qt.ImhNone)
        self.cls_batch_min_filter_lineedit.setMaxLength(3)
        self.cls_batch_min_filter_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_171.addWidget(self.cls_batch_min_filter_lineedit)


        self.horizontalLayout_170.addLayout(self.horizontalLayout_171)

        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.label_169 = QLabel(self.groupBox_34)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMaximumSize(QSize(16777215, 20))
        self.label_169.setFont(font1)

        self.horizontalLayout_172.addWidget(self.label_169)

        self.cls_batch_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_batch_max_filter_lineedit.setObjectName(u"cls_batch_max_filter_lineedit")
        self.cls_batch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_batch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_batch_max_filter_lineedit.setFont(font1)
        self.cls_batch_max_filter_lineedit.setMaxLength(3)

        self.horizontalLayout_172.addWidget(self.cls_batch_max_filter_lineedit)


        self.horizontalLayout_170.addLayout(self.horizontalLayout_172)


        self.horizontalLayout_169.addLayout(self.horizontalLayout_170)

        self.line_40_3 = QFrame(self.groupBox_34)
        self.line_40_3.setObjectName(u"line_40_3")
        self.line_40_3.setFrameShape(QFrame.HLine)
        self.line_40_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_169.addWidget(self.line_40_3)


        self.verticalLayout_102.addLayout(self.horizontalLayout_169)

        self.line_78 = QFrame(self.groupBox_34)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setFrameShape(QFrame.HLine)
        self.line_78.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_78)

        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setSpacing(0)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.label_170 = QLabel(self.groupBox_34)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setFont(font1)

        self.horizontalLayout_173.addWidget(self.label_170)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_38)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.label_171 = QLabel(self.groupBox_34)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMaximumSize(QSize(16777215, 20))
        self.label_171.setFont(font1)

        self.horizontalLayout_174.addWidget(self.label_171)

        self.cls_split_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_split_min_filter_lineedit.setObjectName(u"cls_split_min_filter_lineedit")
        self.cls_split_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_split_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_split_min_filter_lineedit.setFont(font1)
        self.cls_split_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_174.addWidget(self.cls_split_min_filter_lineedit)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_174)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.label_172 = QLabel(self.groupBox_34)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(16777215, 20))
        self.label_172.setFont(font1)

        self.horizontalLayout_175.addWidget(self.label_172)

        self.cls_split_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_split_max_filter_lineedit.setObjectName(u"cls_split_max_filter_lineedit")
        self.cls_split_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_split_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_split_max_filter_lineedit.setFont(font1)
        self.cls_split_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_175.addWidget(self.cls_split_max_filter_lineedit)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_175)


        self.horizontalLayout_173.addLayout(self.horizontalLayout_53)

        self.line_33_3 = QFrame(self.groupBox_34)
        self.line_33_3.setObjectName(u"line_33_3")
        self.line_33_3.setFrameShape(QFrame.HLine)
        self.line_33_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_173.addWidget(self.line_33_3)


        self.verticalLayout_102.addLayout(self.horizontalLayout_173)

        self.line_79 = QFrame(self.groupBox_34)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setFrameShape(QFrame.HLine)
        self.line_79.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_79)

        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.label_173 = QLabel(self.groupBox_34)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setFont(font1)

        self.horizontalLayout_176.addWidget(self.label_173)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_176.addItem(self.horizontalSpacer_39)

        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setSpacing(10)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_178 = QHBoxLayout()
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.label_132_3 = QLabel(self.groupBox_34)
        self.label_132_3.setObjectName(u"label_132_3")
        self.label_132_3.setMaximumSize(QSize(16777215, 20))
        self.label_132_3.setFont(font1)

        self.horizontalLayout_178.addWidget(self.label_132_3)

        self.cls_loss_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_loss_min_filter_lineedit.setObjectName(u"cls_loss_min_filter_lineedit")
        self.cls_loss_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_loss_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_loss_min_filter_lineedit.setFont(font1)
        self.cls_loss_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_178.addWidget(self.cls_loss_min_filter_lineedit)


        self.horizontalLayout_177.addLayout(self.horizontalLayout_178)

        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.label_174 = QLabel(self.groupBox_34)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMaximumSize(QSize(16777215, 20))
        self.label_174.setFont(font1)

        self.horizontalLayout_179.addWidget(self.label_174)

        self.cls_loss_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_loss_max_filter_lineedit.setObjectName(u"cls_loss_max_filter_lineedit")
        self.cls_loss_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_loss_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_loss_max_filter_lineedit.setFont(font1)
        self.cls_loss_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_179.addWidget(self.cls_loss_max_filter_lineedit)


        self.horizontalLayout_177.addLayout(self.horizontalLayout_179)


        self.horizontalLayout_176.addLayout(self.horizontalLayout_177)

        self.line_58 = QFrame(self.groupBox_34)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_176.addWidget(self.line_58)


        self.verticalLayout_102.addLayout(self.horizontalLayout_176)

        self.line_80 = QFrame(self.groupBox_34)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setFrameShape(QFrame.HLine)
        self.line_80.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_80)

        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setSpacing(0)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.label_175 = QLabel(self.groupBox_34)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font1)

        self.horizontalLayout_180.addWidget(self.label_175)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_180.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setSpacing(10)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.label_176 = QLabel(self.groupBox_34)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMaximumSize(QSize(16777215, 20))
        self.label_176.setFont(font1)

        self.horizontalLayout_182.addWidget(self.label_176)

        self.cls_acc_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_acc_min_filter_lineedit.setObjectName(u"cls_acc_min_filter_lineedit")
        self.cls_acc_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_acc_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_acc_min_filter_lineedit.setFont(font1)
        self.cls_acc_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_182.addWidget(self.cls_acc_min_filter_lineedit)


        self.horizontalLayout_181.addLayout(self.horizontalLayout_182)

        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.label_177 = QLabel(self.groupBox_34)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMaximumSize(QSize(16777215, 20))
        self.label_177.setFont(font1)

        self.horizontalLayout_183.addWidget(self.label_177)

        self.cls_acc_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_acc_max_filter_lineedit.setObjectName(u"cls_acc_max_filter_lineedit")
        self.cls_acc_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_acc_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_acc_max_filter_lineedit.setFont(font1)
        self.cls_acc_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_183.addWidget(self.cls_acc_max_filter_lineedit)


        self.horizontalLayout_181.addLayout(self.horizontalLayout_183)


        self.horizontalLayout_180.addLayout(self.horizontalLayout_181)

        self.line_59 = QFrame(self.groupBox_34)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_180.addWidget(self.line_59)


        self.verticalLayout_102.addLayout(self.horizontalLayout_180)

        self.line_81 = QFrame(self.groupBox_34)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setFrameShape(QFrame.HLine)
        self.line_81.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_81)

        self.horizontalLayout_184 = QHBoxLayout()
        self.horizontalLayout_184.setSpacing(0)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.label_178 = QLabel(self.groupBox_34)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setFont(font1)

        self.horizontalLayout_184.addWidget(self.label_178)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_41)

        self.horizontalLayout_185 = QHBoxLayout()
        self.horizontalLayout_185.setSpacing(10)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.label_179 = QLabel(self.groupBox_34)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMaximumSize(QSize(16777215, 20))
        self.label_179.setFont(font1)

        self.horizontalLayout_186.addWidget(self.label_179)

        self.cls_prec_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_prec_min_filter_lineedit.setObjectName(u"cls_prec_min_filter_lineedit")
        self.cls_prec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_prec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_prec_min_filter_lineedit.setFont(font1)
        self.cls_prec_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_186.addWidget(self.cls_prec_min_filter_lineedit)


        self.horizontalLayout_185.addLayout(self.horizontalLayout_186)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.label_180 = QLabel(self.groupBox_34)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setMaximumSize(QSize(16777215, 20))
        self.label_180.setFont(font1)

        self.horizontalLayout_187.addWidget(self.label_180)

        self.cls_prec_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_prec_max_filter_lineedit.setObjectName(u"cls_prec_max_filter_lineedit")
        self.cls_prec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_prec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_prec_max_filter_lineedit.setFont(font1)
        self.cls_prec_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_187.addWidget(self.cls_prec_max_filter_lineedit)


        self.horizontalLayout_185.addLayout(self.horizontalLayout_187)


        self.horizontalLayout_184.addLayout(self.horizontalLayout_185)

        self.line_60 = QFrame(self.groupBox_34)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_184.addWidget(self.line_60)


        self.verticalLayout_102.addLayout(self.horizontalLayout_184)

        self.line_82 = QFrame(self.groupBox_34)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setFrameShape(QFrame.HLine)
        self.line_82.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_82)

        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setSpacing(0)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.label_181 = QLabel(self.groupBox_34)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setFont(font1)

        self.horizontalLayout_188.addWidget(self.label_181)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_188.addItem(self.horizontalSpacer_42)

        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setSpacing(10)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_190 = QHBoxLayout()
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.label_182 = QLabel(self.groupBox_34)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMaximumSize(QSize(16777215, 20))
        self.label_182.setFont(font1)

        self.horizontalLayout_190.addWidget(self.label_182)

        self.cls_rec_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_rec_min_filter_lineedit.setObjectName(u"cls_rec_min_filter_lineedit")
        self.cls_rec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_rec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_rec_min_filter_lineedit.setFont(font1)
        self.cls_rec_min_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_190.addWidget(self.cls_rec_min_filter_lineedit)


        self.horizontalLayout_189.addLayout(self.horizontalLayout_190)

        self.horizontalLayout_191 = QHBoxLayout()
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.label_183 = QLabel(self.groupBox_34)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setMaximumSize(QSize(16777215, 20))
        self.label_183.setFont(font1)

        self.horizontalLayout_191.addWidget(self.label_183)

        self.cls_rec_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_rec_max_filter_lineedit.setObjectName(u"cls_rec_max_filter_lineedit")
        self.cls_rec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_rec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_rec_max_filter_lineedit.setFont(font1)
        self.cls_rec_max_filter_lineedit.setMaxLength(4)

        self.horizontalLayout_191.addWidget(self.cls_rec_max_filter_lineedit)


        self.horizontalLayout_189.addLayout(self.horizontalLayout_191)


        self.horizontalLayout_188.addLayout(self.horizontalLayout_189)

        self.line_61 = QFrame(self.groupBox_34)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_188.addWidget(self.line_61)


        self.verticalLayout_102.addLayout(self.horizontalLayout_188)

        self.line_83 = QFrame(self.groupBox_34)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setFrameShape(QFrame.HLine)
        self.line_83.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_83)

        self.horizontalLayout_192 = QHBoxLayout()
        self.horizontalLayout_192.setSpacing(0)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.verticalLayout_44_213 = QVBoxLayout()
        self.verticalLayout_44_213.setSpacing(2)
        self.verticalLayout_44_213.setObjectName(u"verticalLayout_44_213")
        self.horizontalLayout_195 = QHBoxLayout()
        self.horizontalLayout_195.setSpacing(5)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.label_186 = QLabel(self.groupBox_34)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setMaximumSize(QSize(16777215, 20))
        self.label_186.setFont(font1)

        self.horizontalLayout_195.addWidget(self.label_186)

        self.cls_start_year_lineedit = QLineEdit(self.groupBox_34)
        self.cls_start_year_lineedit.setObjectName(u"cls_start_year_lineedit")
        self.cls_start_year_lineedit.setMinimumSize(QSize(55, 0))
        self.cls_start_year_lineedit.setMaximumSize(QSize(55, 30))
        self.cls_start_year_lineedit.setFont(font1)
        self.cls_start_year_lineedit.setMaxLength(4)

        self.horizontalLayout_195.addWidget(self.cls_start_year_lineedit)

        self.label_187 = QLabel(self.groupBox_34)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setMinimumSize(QSize(5, 0))
        self.label_187.setMaximumSize(QSize(5, 20))
        self.label_187.setFont(font1)

        self.horizontalLayout_195.addWidget(self.label_187)

        self.cls_start_month_lineedit = QLineEdit(self.groupBox_34)
        self.cls_start_month_lineedit.setObjectName(u"cls_start_month_lineedit")
        self.cls_start_month_lineedit.setMinimumSize(QSize(30, 0))
        self.cls_start_month_lineedit.setMaximumSize(QSize(30, 30))
        self.cls_start_month_lineedit.setFont(font1)
        self.cls_start_month_lineedit.setMaxLength(2)

        self.horizontalLayout_195.addWidget(self.cls_start_month_lineedit)

        self.label_188 = QLabel(self.groupBox_34)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setMinimumSize(QSize(5, 0))
        self.label_188.setMaximumSize(QSize(5, 20))
        self.label_188.setFont(font1)

        self.horizontalLayout_195.addWidget(self.label_188)

        self.cls_start_day_lineedit = QLineEdit(self.groupBox_34)
        self.cls_start_day_lineedit.setObjectName(u"cls_start_day_lineedit")
        self.cls_start_day_lineedit.setMinimumSize(QSize(30, 0))
        self.cls_start_day_lineedit.setMaximumSize(QSize(30, 30))
        self.cls_start_day_lineedit.setFont(font1)
        self.cls_start_day_lineedit.setMaxLength(2)

        self.horizontalLayout_195.addWidget(self.cls_start_day_lineedit)


        self.verticalLayout_44_213.addLayout(self.horizontalLayout_195)

        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setSpacing(5)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.label_185 = QLabel(self.groupBox_34)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMaximumSize(QSize(16777215, 20))
        self.label_185.setFont(font1)

        self.horizontalLayout_194.addWidget(self.label_185)

        self.cls_end_year_lineedit = QLineEdit(self.groupBox_34)
        self.cls_end_year_lineedit.setObjectName(u"cls_end_year_lineedit")
        self.cls_end_year_lineedit.setMinimumSize(QSize(55, 0))
        self.cls_end_year_lineedit.setMaximumSize(QSize(55, 30))
        self.cls_end_year_lineedit.setFont(font1)
        self.cls_end_year_lineedit.setMaxLength(4)

        self.horizontalLayout_194.addWidget(self.cls_end_year_lineedit)

        self.label_189 = QLabel(self.groupBox_34)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMinimumSize(QSize(5, 0))
        self.label_189.setMaximumSize(QSize(5, 20))
        self.label_189.setFont(font1)

        self.horizontalLayout_194.addWidget(self.label_189)

        self.cls_end_month_lineedit = QLineEdit(self.groupBox_34)
        self.cls_end_month_lineedit.setObjectName(u"cls_end_month_lineedit")
        self.cls_end_month_lineedit.setMinimumSize(QSize(30, 0))
        self.cls_end_month_lineedit.setMaximumSize(QSize(30, 30))
        self.cls_end_month_lineedit.setFont(font1)
        self.cls_end_month_lineedit.setMaxLength(2)

        self.horizontalLayout_194.addWidget(self.cls_end_month_lineedit)

        self.label_190 = QLabel(self.groupBox_34)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMinimumSize(QSize(5, 0))
        self.label_190.setMaximumSize(QSize(5, 20))
        self.label_190.setFont(font1)

        self.horizontalLayout_194.addWidget(self.label_190)

        self.cls_end_day_lineedit = QLineEdit(self.groupBox_34)
        self.cls_end_day_lineedit.setObjectName(u"cls_end_day_lineedit")
        self.cls_end_day_lineedit.setMinimumSize(QSize(30, 0))
        self.cls_end_day_lineedit.setMaximumSize(QSize(30, 30))
        self.cls_end_day_lineedit.setFont(font1)
        self.cls_end_day_lineedit.setMaxLength(2)

        self.horizontalLayout_194.addWidget(self.cls_end_day_lineedit)


        self.verticalLayout_44_213.addLayout(self.horizontalLayout_194)


        self.horizontalLayout_192.addLayout(self.verticalLayout_44_213)

        self.line_62 = QFrame(self.groupBox_34)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_192.addWidget(self.line_62)


        self.verticalLayout_102.addLayout(self.horizontalLayout_192)

        self.line_97 = QFrame(self.groupBox_34)
        self.line_97.setObjectName(u"line_97")
        self.line_97.setFrameShape(QFrame.HLine)
        self.line_97.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_102.addWidget(self.line_97)

        self.label_39 = QLabel(self.groupBox_34)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_102.addWidget(self.label_39)

        self.table_classification_filter_class = QTableWidget(self.groupBox_34)
        if (self.table_classification_filter_class.columnCount() < 3):
            self.table_classification_filter_class.setColumnCount(3)
        self.table_classification_filter_class.setObjectName(u"table_classification_filter_class")
        self.table_classification_filter_class.setColumnCount(3)

        self.verticalLayout_102.addWidget(self.table_classification_filter_class)

        self.frame_87 = QFrame(self.groupBox_34)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.Panel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_196 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_196.setSpacing(20)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.cls_filter_btn = QPushButton(self.frame_87)
        self.cls_filter_btn.setObjectName(u"cls_filter_btn")
        self.cls_filter_btn.setMinimumSize(QSize(0, 30))
        self.cls_filter_btn.setMaximumSize(QSize(16777215, 30))
        self.cls_filter_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_196.addWidget(self.cls_filter_btn)

        self.cls_clearfilter_btn = QPushButton(self.frame_87)
        self.cls_clearfilter_btn.setObjectName(u"cls_clearfilter_btn")
        self.cls_clearfilter_btn.setMinimumSize(QSize(0, 30))
        self.cls_clearfilter_btn.setMaximumSize(QSize(16777215, 30))
        self.cls_clearfilter_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_196.addWidget(self.cls_clearfilter_btn)


        self.verticalLayout_102.addWidget(self.frame_87)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_102.addItem(self.verticalSpacer_11)


        self.verticalLayout_42.addWidget(self.groupBox_34)


        self.verticalLayout_49.addWidget(self.frame_29)


        self.horizontalLayout_38.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.page_classification_history)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_28)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.frame_28)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.cls_history_tabel = QTableWidget(self.frame_86)
        if (self.cls_history_tabel.columnCount() < 20):
            self.cls_history_tabel.setColumnCount(20)
        self.cls_history_tabel.setObjectName(u"cls_history_tabel")
        self.cls_history_tabel.setFrameShape(QFrame.Panel)
        self.cls_history_tabel.setFrameShadow(QFrame.Raised)
        self.cls_history_tabel.setRowCount(0)
        self.cls_history_tabel.setColumnCount(20)
        self.cls_history_tabel.horizontalHeader().setCascadingSectionResizes(True)
        self.cls_history_tabel.horizontalHeader().setMinimumSectionSize(150)
        self.cls_history_tabel.horizontalHeader().setDefaultSectionSize(150)

        self.horizontalLayout_48.addWidget(self.cls_history_tabel)


        self.verticalLayout_93.addWidget(self.frame_86)

        self.frame_85 = QFrame(self.frame_28)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_68_3 = QFrame(self.frame_85)
        self.frame_68_3.setObjectName(u"frame_68_3")
        self.frame_68_3.setFrameShape(QFrame.Panel)
        self.frame_68_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109_3 = QHBoxLayout(self.frame_68_3)
        self.horizontalLayout_109_3.setSpacing(5)
        self.horizontalLayout_109_3.setObjectName(u"horizontalLayout_109_3")
        self.horizontalLayout_109_3.setContentsMargins(5, 5, 5, 5)
        self.cls_table_refresh_btn = QPushButton(self.frame_68_3)
        self.cls_table_refresh_btn.setObjectName(u"cls_table_refresh_btn")
        self.cls_table_refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cls_table_refresh_btn.setLayoutDirection(Qt.RightToLeft)
        self.cls_table_refresh_btn.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.cls_table_refresh_btn.setIcon(icon26)
        self.cls_table_refresh_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_109_3.addWidget(self.cls_table_refresh_btn)

        self.line_52 = QFrame(self.frame_68_3)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.VLine)
        self.line_52.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_109_3.addWidget(self.line_52)

        self.cls_tabel_prev = QPushButton(self.frame_68_3)
        self.cls_tabel_prev.setObjectName(u"cls_tabel_prev")
        self.cls_tabel_prev.setEnabled(False)
        self.cls_tabel_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.cls_tabel_prev.setLayoutDirection(Qt.LeftToRight)
        self.cls_tabel_prev.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.cls_tabel_prev.setIcon(icon16)
        self.cls_tabel_prev.setIconSize(QSize(30, 30))

        self.horizontalLayout_109_3.addWidget(self.cls_tabel_prev)

        self.cls_tabel_page = QLineEdit(self.frame_68_3)
        self.cls_tabel_page.setObjectName(u"cls_tabel_page")
        self.cls_tabel_page.setEnabled(False)
        self.cls_tabel_page.setMinimumSize(QSize(50, 30))
        self.cls_tabel_page.setMaximumSize(QSize(50, 30))
        self.cls_tabel_page.setStyleSheet(u"padding:0;")
        self.cls_tabel_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109_3.addWidget(self.cls_tabel_page)

        self.cls_tabel_next = QPushButton(self.frame_68_3)
        self.cls_tabel_next.setObjectName(u"cls_tabel_next")
        self.cls_tabel_next.setEnabled(False)
        self.cls_tabel_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.cls_tabel_next.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.cls_tabel_next.setIcon(icon15)
        self.cls_tabel_next.setIconSize(QSize(30, 30))

        self.horizontalLayout_109_3.addWidget(self.cls_tabel_next)

        self.line_53 = QFrame(self.frame_68_3)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.VLine)
        self.line_53.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_109_3.addWidget(self.line_53)

        self.cls_tabel_label = QLabel(self.frame_68_3)
        self.cls_tabel_label.setObjectName(u"cls_tabel_label")
        self.cls_tabel_label.setMinimumSize(QSize(600, 0))
        self.cls_tabel_label.setMaximumSize(QSize(600, 16777215))
        self.cls_tabel_label.setFrameShape(QFrame.Panel)
        self.cls_tabel_label.setFrameShadow(QFrame.Sunken)
        self.cls_tabel_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109_3.addWidget(self.cls_tabel_label)

        self.horizontalSpacer_20_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109_3.addItem(self.horizontalSpacer_20_3)


        self.horizontalLayout_29.addWidget(self.frame_68_3)


        self.verticalLayout_93.addWidget(self.frame_85)


        self.horizontalLayout_38.addWidget(self.frame_28)

        self.stackedWidget_classification.addWidget(self.page_classification_history)

        self.verticalLayout_33.addWidget(self.stackedWidget_classification)

        self.stackedWidget.addWidget(self.page_Classification)
        self.page_software_setting = QWidget()
        self.page_software_setting.setObjectName(u"page_software_setting")
        self.verticalLayout = QVBoxLayout(self.page_software_setting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_232 = QHBoxLayout()
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.groupBox_10 = QGroupBox(self.page_software_setting)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(340, 0))
        self.groupBox_10.setMaximumSize(QSize(600, 16777215))
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_13 = QFrame(self.groupBox_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2931 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_2931.setObjectName(u"horizontalLayout_2931")
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2931.addWidget(self.label_5)

        self.combo_change_language = QComboBox(self.frame_13)
        self.combo_change_language.setObjectName(u"combo_change_language")
        self.combo_change_language.setMinimumSize(QSize(140, 0))
        self.combo_change_language.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_2931.addWidget(self.combo_change_language)

        self.label_language = QLabel(self.frame_13)
        self.label_language.setObjectName(u"label_language")
        self.label_language.setMinimumSize(QSize(47, 50))
        self.label_language.setMaximumSize(QSize(47, 50))
        self.label_language.setStyleSheet(u"")
        self.label_language.setPixmap(QPixmap(u"../../trainApp_oxin8 (copy)/UI/C:/Users/DORSA-PC1/Desktop/UI/images/persian.png"))
        self.label_language.setScaledContents(True)

        self.horizontalLayout_2931.addWidget(self.label_language)


        self.verticalLayout_36.addWidget(self.frame_13)

        self.frame_17 = QFrame(self.groupBox_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2941 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_2941.setObjectName(u"horizontalLayout_2941")
        self.label_281 = QLabel(self.frame_17)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setMinimumSize(QSize(75, 0))
        self.label_281.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2941.addWidget(self.label_281)

        self.fontComboBox = QFontComboBox(self.frame_17)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMinimumSize(QSize(140, 0))
        self.fontComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.fontComboBox.setStyleSheet(u"")

        self.horizontalLayout_2941.addWidget(self.fontComboBox)

        self.label_language_2 = QLabel(self.frame_17)
        self.label_language_2.setObjectName(u"label_language_2")
        self.label_language_2.setMinimumSize(QSize(47, 50))
        self.label_language_2.setMaximumSize(QSize(47, 50))
        self.label_language_2.setStyleSheet(u"")
        self.label_language_2.setPixmap(QPixmap(u"../../trainApp_oxin8 (copy)/UI/C:/Users/DORSA-PC1/Desktop/UI/images/persian.png"))
        self.label_language_2.setScaledContents(True)

        self.horizontalLayout_2941.addWidget(self.label_language_2)


        self.verticalLayout_36.addWidget(self.frame_17)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_3)

        self.appearance_btn = QPushButton(self.groupBox_10)
        self.appearance_btn.setObjectName(u"appearance_btn")
        self.appearance_btn.setMinimumSize(QSize(0, 35))
        self.appearance_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_36.addWidget(self.appearance_btn)


        self.horizontalLayout_232.addWidget(self.groupBox_10)

        self.groupBox_5 = QGroupBox(self.page_software_setting)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(300, 0))
        self.groupBox_5.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_461 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_461.setObjectName(u"verticalLayout_461")
        self.manual_plc_check = QCheckBox(self.groupBox_5)
        self.manual_plc_check.setObjectName(u"manual_plc_check")
        self.manual_plc_check.setStyleSheet(u"")
        self.manual_plc_check.setChecked(True)

        self.verticalLayout_461.addWidget(self.manual_plc_check)

        self.frame_19 = QFrame(self.groupBox_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.connect_plc_btn = QPushButton(self.frame_19)
        self.connect_plc_btn.setObjectName(u"connect_plc_btn")
        self.connect_plc_btn.setEnabled(False)
        self.connect_plc_btn.setMinimumSize(QSize(80, 0))
        self.connect_plc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_plc_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_92.addWidget(self.connect_plc_btn)

        self.disconnect_plc_btn = QPushButton(self.frame_19)
        self.disconnect_plc_btn.setObjectName(u"disconnect_plc_btn")
        self.disconnect_plc_btn.setEnabled(False)
        self.disconnect_plc_btn.setMinimumSize(QSize(80, 0))
        self.disconnect_plc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnect_plc_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_92.addWidget(self.disconnect_plc_btn)


        self.verticalLayout_461.addWidget(self.frame_19)

        self.frame_30 = QFrame(self.groupBox_5)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.label_4 = QLabel(self.frame_30)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_117.addWidget(self.label_4)

        self.plc_status_line = QLabel(self.frame_30)
        self.plc_status_line.setObjectName(u"plc_status_line")
        self.plc_status_line.setMinimumSize(QSize(135, 0))
        self.plc_status_line.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_117.addWidget(self.plc_status_line, 0, Qt.AlignLeft)


        self.verticalLayout_461.addWidget(self.frame_30)

        self.frame_351 = QFrame(self.groupBox_5)
        self.frame_351.setObjectName(u"frame_351")
        self.frame_351.setFrameShape(QFrame.StyledPanel)
        self.frame_351.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_351)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_10 = QLabel(self.frame_351)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_161.addWidget(self.label_10)

        self.plc_ip_line = QLineEdit(self.frame_351)
        self.plc_ip_line.setObjectName(u"plc_ip_line")
        self.plc_ip_line.setReadOnly(True)

        self.horizontalLayout_161.addWidget(self.plc_ip_line)


        self.verticalLayout_461.addWidget(self.frame_351)

        self.frame_41 = QFrame(self.groupBox_5)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_230 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_230.setObjectName(u"horizontalLayout_230")
        self.label = QLabel(self.frame_41)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_230.addWidget(self.label)

        self.update_timer_plc_spinBox = QSpinBox(self.frame_41)
        self.update_timer_plc_spinBox.setObjectName(u"update_timer_plc_spinBox")
        sizePolicy1.setHeightForWidth(self.update_timer_plc_spinBox.sizePolicy().hasHeightForWidth())
        self.update_timer_plc_spinBox.setSizePolicy(sizePolicy1)
        self.update_timer_plc_spinBox.setMinimum(100)
        self.update_timer_plc_spinBox.setMaximum(10000)
        self.update_timer_plc_spinBox.setValue(2000)

        self.horizontalLayout_230.addWidget(self.update_timer_plc_spinBox)

        self.label_240 = QLabel(self.frame_41)
        self.label_240.setObjectName(u"label_240")

        self.horizontalLayout_230.addWidget(self.label_240)


        self.verticalLayout_461.addWidget(self.frame_41)

        self.frame_43 = QFrame(self.groupBox_5)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_224 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_224.setObjectName(u"horizontalLayout_224")
        self.label_29 = QLabel(self.frame_43)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_224.addWidget(self.label_29)

        self.update_wind_plc_spinBox = QSpinBox(self.frame_43)
        self.update_wind_plc_spinBox.setObjectName(u"update_wind_plc_spinBox")
        sizePolicy1.setHeightForWidth(self.update_wind_plc_spinBox.sizePolicy().hasHeightForWidth())
        self.update_wind_plc_spinBox.setSizePolicy(sizePolicy1)
        self.update_wind_plc_spinBox.setMinimum(1)
        self.update_wind_plc_spinBox.setMaximum(30)
        self.update_wind_plc_spinBox.setValue(30)

        self.horizontalLayout_224.addWidget(self.update_wind_plc_spinBox)

        self.label_238 = QLabel(self.frame_43)
        self.label_238.setObjectName(u"label_238")

        self.horizontalLayout_224.addWidget(self.label_238)


        self.verticalLayout_461.addWidget(self.frame_43)

        self.auto_wind_check = QCheckBox(self.groupBox_5)
        self.auto_wind_check.setObjectName(u"auto_wind_check")
        self.auto_wind_check.setStyleSheet(u"")
        self.auto_wind_check.setChecked(True)

        self.verticalLayout_461.addWidget(self.auto_wind_check)

        self.frame_49 = QFrame(self.groupBox_5)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_298 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.label_299 = QLabel(self.frame_49)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_298.addWidget(self.label_299)

        self.update_auto_wind_plc_spinBox = QSpinBox(self.frame_49)
        self.update_auto_wind_plc_spinBox.setObjectName(u"update_auto_wind_plc_spinBox")
        sizePolicy1.setHeightForWidth(self.update_auto_wind_plc_spinBox.sizePolicy().hasHeightForWidth())
        self.update_auto_wind_plc_spinBox.setSizePolicy(sizePolicy1)
        self.update_auto_wind_plc_spinBox.setMinimum(100)
        self.update_auto_wind_plc_spinBox.setMaximum(60000)
        self.update_auto_wind_plc_spinBox.setValue(5000)

        self.horizontalLayout_298.addWidget(self.update_auto_wind_plc_spinBox)

        self.label_300 = QLabel(self.frame_49)
        self.label_300.setObjectName(u"label_300")

        self.horizontalLayout_298.addWidget(self.label_300)


        self.verticalLayout_461.addWidget(self.frame_49)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_461.addItem(self.verticalSpacer_4)

        self.plc_btn = QPushButton(self.groupBox_5)
        self.plc_btn.setObjectName(u"plc_btn")
        self.plc_btn.setMinimumSize(QSize(0, 35))
        self.plc_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_461.addWidget(self.plc_btn)


        self.horizontalLayout_232.addWidget(self.groupBox_5)

        self.groupBox_9 = QGroupBox(self.page_software_setting)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(300, 0))
        self.groupBox_9.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.manual_cameras_check = QCheckBox(self.groupBox_9)
        self.manual_cameras_check.setObjectName(u"manual_cameras_check")
        self.manual_cameras_check.setStyleSheet(u"")
        self.manual_cameras_check.setChecked(True)

        self.verticalLayout_20.addWidget(self.manual_cameras_check)

        self.frame_45 = QFrame(self.groupBox_9)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_231 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_231.setObjectName(u"horizontalLayout_231")
        self.label_46 = QLabel(self.frame_45)
        self.label_46.setObjectName(u"label_46")
        sizePolicy3.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy3)
        self.label_46.setMinimumSize(QSize(170, 0))

        self.horizontalLayout_231.addWidget(self.label_46)

        self.frame_rate_spinBox = QSpinBox(self.frame_45)
        self.frame_rate_spinBox.setObjectName(u"frame_rate_spinBox")
        sizePolicy1.setHeightForWidth(self.frame_rate_spinBox.sizePolicy().hasHeightForWidth())
        self.frame_rate_spinBox.setSizePolicy(sizePolicy1)
        self.frame_rate_spinBox.setMinimum(1)
        self.frame_rate_spinBox.setMaximum(100)
        self.frame_rate_spinBox.setValue(7)

        self.horizontalLayout_231.addWidget(self.frame_rate_spinBox)

        self.label_239 = QLabel(self.frame_45)
        self.label_239.setObjectName(u"label_239")

        self.horizontalLayout_231.addWidget(self.label_239)


        self.verticalLayout_20.addWidget(self.frame_45)

        self.frame_501 = QFrame(self.groupBox_9)
        self.frame_501.setObjectName(u"frame_501")
        self.frame_501.setFrameShape(QFrame.StyledPanel)
        self.frame_501.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_601 = QHBoxLayout(self.frame_501)
        self.horizontalLayout_601.setObjectName(u"horizontalLayout_601")
        self.label_197 = QLabel(self.frame_501)
        self.label_197.setObjectName(u"label_197")
        sizePolicy3.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy3)
        self.label_197.setMinimumSize(QSize(170, 0))
        self.label_197.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_601.addWidget(self.label_197)

        self.update_timer_live_frame_spinBox = QSpinBox(self.frame_501)
        self.update_timer_live_frame_spinBox.setObjectName(u"update_timer_live_frame_spinBox")
        sizePolicy1.setHeightForWidth(self.update_timer_live_frame_spinBox.sizePolicy().hasHeightForWidth())
        self.update_timer_live_frame_spinBox.setSizePolicy(sizePolicy1)
        self.update_timer_live_frame_spinBox.setMinimum(10)
        self.update_timer_live_frame_spinBox.setMaximum(60000)
        self.update_timer_live_frame_spinBox.setValue(100)

        self.horizontalLayout_601.addWidget(self.update_timer_live_frame_spinBox)

        self.label_241 = QLabel(self.frame_501)
        self.label_241.setObjectName(u"label_241")

        self.horizontalLayout_601.addWidget(self.label_241)


        self.verticalLayout_20.addWidget(self.frame_501)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)

        self.cameras_btn = QPushButton(self.groupBox_9)
        self.cameras_btn.setObjectName(u"cameras_btn")
        self.cameras_btn.setMinimumSize(QSize(0, 35))
        self.cameras_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.cameras_btn)


        self.horizontalLayout_232.addWidget(self.groupBox_9)


        self.verticalLayout.addLayout(self.horizontalLayout_232)

        self.frame_147 = QFrame(self.page_software_setting)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(0, 70))
        self.frame_147.setMaximumSize(QSize(16777215, 70))
        self.frame_147.setFrameShape(QFrame.WinPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_204 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_204.setSpacing(5)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(15, 5, 15, 5)
        self.label_277 = QLabel(self.frame_147)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setMinimumSize(QSize(70, 0))
        self.label_277.setMaximumSize(QSize(70, 16777215))
        self.label_277.setFont(font5)
        self.label_277.setStyleSheet(u" font-weight: bold;")

        self.horizontalLayout_204.addWidget(self.label_277)

        self.setting_msg_label = QLabel(self.frame_147)
        self.setting_msg_label.setObjectName(u"setting_msg_label")
        self.setting_msg_label.setMinimumSize(QSize(0, 40))
        self.setting_msg_label.setMaximumSize(QSize(16777215, 40))
        self.setting_msg_label.setFont(font1)
        self.setting_msg_label.setStyleSheet(u"QLabel{\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"")
        self.setting_msg_label.setFrameShape(QFrame.WinPanel)
        self.setting_msg_label.setFrameShadow(QFrame.Sunken)
        self.setting_msg_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_204.addWidget(self.setting_msg_label)


        self.verticalLayout.addWidget(self.frame_147)

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
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
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
        self.bottomBar.setMinimumSize(QSize(0, 72))
        self.bottomBar.setMaximumSize(QSize(16777215, 72))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        sizePolicy.setHeightForWidth(self.creditsLabel.sizePolicy().hasHeightForWidth())
        self.creditsLabel.setSizePolicy(sizePolicy)
        self.creditsLabel.setMaximumSize(QSize(16777215, 16777215))
        self.creditsLabel.setFont(font1)
        self.creditsLabel.setStyleSheet(u"")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setSpacing(3)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(-1, 8, -1, -1)
        self.label_287 = QLabel(self.bottomBar)
        self.label_287.setObjectName(u"label_287")
        sizePolicy.setHeightForWidth(self.label_287.sizePolicy().hasHeightForWidth())
        self.label_287.setSizePolicy(sizePolicy)
        self.label_287.setMaximumSize(QSize(45, 16777215))
        self.label_287.setStyleSheet(u"color: white;\n"
"font-size: 12px")
        self.label_287.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_74.addWidget(self.label_287)

        self.label_289 = QLabel(self.bottomBar)
        self.label_289.setObjectName(u"label_289")
        sizePolicy.setHeightForWidth(self.label_289.sizePolicy().hasHeightForWidth())
        self.label_289.setSizePolicy(sizePolicy)
        self.label_289.setMaximumSize(QSize(45, 16777215))
        self.label_289.setStyleSheet(u"color: white;\n"
"font-size: 12px")
        self.label_289.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_74.addWidget(self.label_289)

        self.label_290 = QLabel(self.bottomBar)
        self.label_290.setObjectName(u"label_290")
        sizePolicy2.setHeightForWidth(self.label_290.sizePolicy().hasHeightForWidth())
        self.label_290.setSizePolicy(sizePolicy2)
        self.label_290.setMinimumSize(QSize(0, 16))
        self.label_290.setMaximumSize(QSize(50, 16))

        self.verticalLayout_74.addWidget(self.label_290)


        self.horizontalLayout_5.addLayout(self.verticalLayout_74)

        self.storage_chart_frame = QFrame(self.bottomBar)
        self.storage_chart_frame.setObjectName(u"storage_chart_frame")
        sizePolicy3.setHeightForWidth(self.storage_chart_frame.sizePolicy().hasHeightForWidth())
        self.storage_chart_frame.setSizePolicy(sizePolicy3)
        self.storage_chart_frame.setMinimumSize(QSize(0, 0))
        self.storage_chart_frame.setMaximumSize(QSize(16777215, 16777215))
        self.storage_chart_frame.setStyleSheet(u"")
        self.storage_chart_frame.setFrameShape(QFrame.NoFrame)
        self.storage_chart_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.storage_chart_frame)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 6, 0, 0)

        self.horizontalLayout_5.addWidget(self.storage_chart_frame)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_94.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.live_tabWidget.setCurrentIndex(0)
        self.stackedWidget_defect.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)
        self.stackedWidget_pbt.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_binary.setCurrentIndex(0)
        self.binary_train.setDefault(False)
        self.stackedWidget_localization.setCurrentIndex(0)
        self.localization_train.setDefault(False)
        self.stackedWidget_classification.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"SENSE", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"    Trainer App", None))
#if QT_CONFIG(tooltip)
        self.Data_auquzation_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Auquzation", None))
#endif // QT_CONFIG(tooltip)
        self.Data_auquzation_btn.setText(QCoreApplication.translate("MainWindow", u"Data Auquzation", None))
#if QT_CONFIG(tooltip)
        self.label_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Label", None))
#endif // QT_CONFIG(tooltip)
        self.label_btn.setText(QCoreApplication.translate("MainWindow", u"Label", None))
#if QT_CONFIG(tooltip)
        self.tuning_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Tuning", None))
#endif // QT_CONFIG(tooltip)
        self.tuning_btn.setText(QCoreApplication.translate("MainWindow", u" Tuning", None))
#if QT_CONFIG(tooltip)
        self.pbt_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Pipeline Build & Test", None))
#endif // QT_CONFIG(tooltip)
        self.pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Pipline Build and Test", None))
#if QT_CONFIG(tooltip)
        self.log_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Logs", None))
#endif // QT_CONFIG(tooltip)
        self.log_btn.setText(QCoreApplication.translate("MainWindow", u"Show Logs", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Tuning", None))
        self.Binary_btn.setText(QCoreApplication.translate("MainWindow", u"Binary             ", None))
        self.Localization_btn.setText(QCoreApplication.translate("MainWindow", u"Localization   ", None))
        self.Classification_btn.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.label_dorsa.setText("")
        self.titleRightInfo.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Please Login", None))
        self.user_name.setText("")
        self.label_app_erors.setText("")
#if QT_CONFIG(tooltip)
        self.login_btn.setToolTip(QCoreApplication.translate("MainWindow", u"User", None))
#endif // QT_CONFIG(tooltip)
        self.login_btn.setText("")
#if QT_CONFIG(tooltip)
        self.setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText("")
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
        self.setting_eror.setText("")
        self.btn_software_setting.setText(QCoreApplication.translate("MainWindow", u"Software Settings", None))
        self.btn_user_profile.setText(QCoreApplication.translate("MainWindow", u"User Profile", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.camera_connection_msg.setText("")
        self.connect_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"C01", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"C02", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"C03", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"C04", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"C05", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"C06", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"C07", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"C08", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"C09", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"C10", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"C11", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"C12", None))
        self.camera01_btn.setText("")
        self.camera02_btn.setText("")
        self.camera03_btn.setText("")
        self.camera04_btn.setText("")
        self.camera05_btn.setText("")
        self.camera06_btn.setText("")
        self.camera07_btn.setText("")
        self.camera08_btn.setText("")
        self.camera09_btn.setText("")
        self.camera10_btn.setText("")
        self.camera11_btn.setText("")
        self.camera12_btn.setText("")
        self.camera13_btn.setText("")
        self.camera14_btn.setText("")
        self.camera15_btn.setText("")
        self.camera16_btn.setText("")
        self.camera17_btn.setText("")
        self.camera18_btn.setText("")
        self.camera19_btn.setText("")
        self.camera20_btn.setText("")
        self.camera21_btn.setText("")
        self.camera22_btn.setText("")
        self.camera23_btn.setText("")
        self.camera24_btn.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"C13", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"C14", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"C15", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"C16", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"C17", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"C18", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"C19", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"C20", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"C21", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"C22", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"C23", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"C24", None))
        self.checkBox_top.setText(QCoreApplication.translate("MainWindow", u"Top Cameras", None))
        self.checkBox_bottom.setText(QCoreApplication.translate("MainWindow", u"Bottom Cameras", None))
        self.checkBox_all.setText(QCoreApplication.translate("MainWindow", u"All Cameras", None))
        self.start_capture_btn.setText(QCoreApplication.translate("MainWindow", u"Start Capture", None))
        self.stop_capture_btn.setText(QCoreApplication.translate("MainWindow", u"Stop Capture", None))
        self.checkBox_save_images.setText(QCoreApplication.translate("MainWindow", u"Save Images", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Detect Sensor :", None))
        self.detect_sensor_check_box.setText("")
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"Air Cleaning  :", None))
        self.start_wind_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Temperature  :", None))
        self.label_up_temperature.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_down_temperature.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"PLC Status :", None))
        self.plc_warnings.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Sheet ID :", None))
        self.label_sheet_id.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_heat_number_5.setText(QCoreApplication.translate("MainWindow", u"Heat Number :", None))
        self.label_heat_number.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Ps Number :", None))
        self.label_ps_number.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Pdl Number :", None))
        self.label_pdl_number.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"length :", None))
        self.label_length.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Width :", None))
        self.label_width.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Thickness :", None))
        self.label_thickness.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sheet_label.setText("")
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Camera Number :", None))
        self.live.setText("")
        self.live_tabWidget.setTabText(self.live_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Single Camera", None))
        self.tlive1.setText("")
        self.tlive2.setText("")
        self.tlive3.setText("")
        self.tlive4.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.tlive5.setText("")
        self.tlive6.setText("")
        self.tlive7.setText("")
        self.tlive8.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"6", None))
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
        self.live_tabWidget.setTabText(self.live_tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Top Cameras", None))
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
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.blive21.setText("")
        self.blive22.setText("")
        self.blive23.setText("")
        self.blive24.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.live_tabWidget.setTabText(self.live_tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Bottom Cameras", None))
        self.live1.setText("")
        self.live2.setText("")
        self.live3.setText("")
        self.live4.setText("")
        self.live5.setText("")
        self.live6.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.live7.setText("")
        self.live8.setText("")
        self.live9.setText("")
        self.live10.setText("")
        self.live11.setText("")
        self.live12.setText("")
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.live13.setText("")
        self.live14.setText("")
        self.live15.setText("")
        self.live16.setText("")
        self.live17.setText("")
        self.live18.setText("")
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.live19.setText("")
        self.live20.setText("")
        self.live21.setText("")
        self.live22.setText("")
        self.live23.setText("")
        self.live24.setText("")
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.live_tabWidget.setTabText(self.live_tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"All Cameras", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"LIVE", None))
#if QT_CONFIG(tooltip)
        self.load_coil_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.load_coil_btn.setText(QCoreApplication.translate("MainWindow", u"Load Sheet", None))
#if QT_CONFIG(tooltip)
        self.next_coil_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Next Sheet", None))
#endif // QT_CONFIG(tooltip)
        self.next_coil_btn.setText("")
#if QT_CONFIG(tooltip)
        self.prev_coil_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Previous Sheet", None))
#endif // QT_CONFIG(tooltip)
        self.prev_coil_btn.setText("")
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Sheet ID :", None))
        self.label_sheet_id_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_heat_number_3.setText(QCoreApplication.translate("MainWindow", u"Heat Number :", None))
        self.label_heat_number_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"Ps Number :", None))
        self.label_ps_number_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Pdl Number :", None))
        self.label_pdl_number_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"length :", None))
        self.label_length_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Width :", None))
        self.label_width_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Thickness :", None))
        self.label_thickness_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sheet_label_2.setText("")
        self.checkBox_suggested_defects.setText(QCoreApplication.translate("MainWindow", u"Show suggested defects", None))
        self.crop_image.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.label_234.setText("")
        self.label_221.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.current_pos_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_233.setText("")
        self.label_224.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.current_pos_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.warning_data_page.setText("")
#if QT_CONFIG(tooltip)
        self.add_btn_SI.setToolTip(QCoreApplication.translate("MainWindow", u"Add Image", None))
#endif // QT_CONFIG(tooltip)
        self.add_btn_SI.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Append", None))
#if QT_CONFIG(tooltip)
        self.remove_btn_SI.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Image", None))
#endif // QT_CONFIG(tooltip)
        self.remove_btn_SI.setText("")
        self.checkBox_select.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.label_btn_SI.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.checkBox_all_imgs_SI.setText(QCoreApplication.translate("MainWindow", u"All Images", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Side", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Camera Number", None))
        self.label_ncamera_SI.setText("")
        self.checkBox_all_camera_SI.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Frame Number", None))
        self.label_nframe_SI.setText("")
        self.checkBox_all_frame_SI.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.add_filter_btn_SI.setText(QCoreApplication.translate("MainWindow", u"Append with filter", None))
        self.select_filter_btn_SI.setText(QCoreApplication.translate("MainWindow", u"Select with filter", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Technical View", None))
        self.label_1291.setText(QCoreApplication.translate("MainWindow", u"40  cm", None))
        self.label_1311.setText("")
#if QT_CONFIG(tooltip)
        self.label_6_1.setToolTip(QCoreApplication.translate("MainWindow", u"Top Side Technical View", None))
#endif // QT_CONFIG(tooltip)
        self.label_6_1.setText(QCoreApplication.translate("MainWindow", u"TOP Side", None))
        self.up_side_technical.setText("")
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"40  cm", None))
        self.label_125.setText("")
#if QT_CONFIG(tooltip)
        self.label_119.setToolTip(QCoreApplication.translate("MainWindow", u"Bottom Side Technical View", None))
#endif // QT_CONFIG(tooltip)
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"BOTTOM Side", None))
        self.down_side_technical.setText("")
        self.next_img_label_btn.setText("")
        self.prev_img_label_btn.setText("")
        self.zoomIn_btn.setText("")
        self.zoomOut_btn.setText("")
        self.drag_btn.setText("")
        self.polygon_btn.setText("")
        self.suggested_defects_btn.setText("")
#if QT_CONFIG(tooltip)
        self.heatmap_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Suggested Defects HeatMap", None))
#endif // QT_CONFIG(tooltip)
        self.heatmap_btn.setText("")
        self.delete_btn.setText("")
        self.image.setText("")
        self.label_show_help_btn.setText("")
        self.labeling_help_1.setText("")
        self.labeling_help_2.setText("")
        self.labeling_help_3.setText("")
        self.labeling_help_4.setText("")
        self.labeling_help_5.setText("")
        self.labeling_help_6.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.plabel_date_txt.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Coil number :", None))
        self.plabel_coil_num_txt.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Cam number :", None))
        self.plabel_cam_txt.setText("")
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"Frame number :", None))
        self.plabel_frame_txt.setText("")
        self.checkBox_show_neighbours.setText(QCoreApplication.translate("MainWindow", u"Show Neighbours", None))
        self.checkBox_show_neighbours_labels.setText(QCoreApplication.translate("MainWindow", u"Show Neighbours labels", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"Line Thickness :  ", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"Point Thickness :", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Defect :", None))
        self.no_defect.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.yes_defect.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"Masks :", None))
        ___qtablewidgetitem = self.mask_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Defect ID", None));
        ___qtablewidgetitem1 = self.mask_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Defect Name", None));
        ___qtablewidgetitem2 = self.mask_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Image has no Defect", None))
        self.save_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_all_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
        self.binary_chart_frame_label.setTitle(QCoreApplication.translate("MainWindow", u"Defect/Perfect Count PieChart", None))
        self.user_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.user_name_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u" ID :", None))
        self.user_id.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Role :", None))
        self.role.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Date Created :", None))
        self.date_created.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Default Dataset :", None))
        self.default_dataset.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.mainHelp.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:600; background-color:transparent;\">Welcome to SENS TRAINER App</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">To start working with the software, click on the desired key from the left menu. To see the details "
                        "of each key, click on the three dots icon or hold the mouse pointer over the desired key.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">First, click on the Data Auquzation button. From the Live tab, check the connection of the cameras and view and save the images taken from the sheets live.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">Then, in the Technical View tab, load the sheets whose images are saved and add the images you want for labeling. Enter the labeling page by clicking on the Label button on this page.</span></p>\n"
"<p style=\" margin-top:12px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">On the Label page, specify the defects of the selected images and the type of defects and save the images.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">By clicking on the Tuning key, select one of the three keys, Binary, Localization or Classification, and by clicking on it, go to the corresponding page and train your desired model.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; ba"
                        "ckground-color:transparent;\">On the Pipeline Build &amp; Test page, set up and test your desired pipeline using the trained models.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">On the top bar of the page, click on the gear icon to see the keys related to software settings and user profile (current page) and go to the desired page by clicking on each key.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">On the software settings page, make settings for the program, PLC and cameras.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; li"
                        "ne-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">On the user profile page, view the created datasets and select your dataset to save the images (otherwise the images will be saved in the default dataset).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">Log in or out of the program using your username and password by clicking the login icon on the top bar.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;\">On each of the pages, click on the question mark icon at the top of the page to see t"
                        "he details of how to work with that page.</span></p></body></html>", None))
        self.create_new_database.setText(QCoreApplication.translate("MainWindow", u"Create New Dataset", None))
        self.all_databases.setText(QCoreApplication.translate("MainWindow", u"All Datasets", None))
        self.my_databases_2.setText(QCoreApplication.translate("MainWindow", u"My Datasets", None))
        self.my_databases_3.setText(QCoreApplication.translate("MainWindow", u"Piplines", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Today  Date:", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Creator Username :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dataset Name:", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Location :", None))
        self.lineEdit_path_dataset.setText("")
        self.toolButton_select_directory.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.create_database_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Select Dataset :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.all_ds_id.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Dataset Name:", None))
        self.all_ds_name.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Owner User:", None))
        self.all_ds_owner_user.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.all_ds_path.setText("")
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Select Dataset :", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.my_ds_id.setText("")
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Dataset Name:", None))
        self.my_ds_name.setText("")
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"Owner User:", None))
        self.my_ds_owner_user.setText("")
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.my_ds_path.setText("")
        self.set_default_database_btn.setText(QCoreApplication.translate("MainWindow", u"Set As Default", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"All Piplines :", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"My Piplines :", None))
        self.show_details_pipline.setText(QCoreApplication.translate("MainWindow", u"Show Details", None))
        self.remove_pipline.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_pipline_details.setText("")
        self.binary_chart_frame_profile.setTitle(QCoreApplication.translate("MainWindow", u"Defect/Perfect PieChart", None))
        self.classlist_chart_frame_profile.setTitle(QCoreApplication.translate("MainWindow", u"Defect Classes BarChart", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.profile_msg_label.setText("")
        self.pipeline_pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Pipeline", None))
        self.load_dataset_pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.history_pbt_btn.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.radioButton_one.setText(QCoreApplication.translate("MainWindow", u"One", None))
        self.radioButton_two.setText(QCoreApplication.translate("MainWindow", u"Two", None))
        self.label_12_3.setText(QCoreApplication.translate("MainWindow", u"Binary : ", None))
        self.toolButton_binary.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_12_5.setText(QCoreApplication.translate("MainWindow", u"Yolo : ", None))
        self.toolButton_yolo.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Localization : ", None))
        self.toolButton_localiztion.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Classification :", None))
        self.toolButton_multiClassification.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.BTN_of_goToPreviouspage_in_PBT_page.setText("")
        self.lineEdit_of_pageNumber_displayment_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.BTN_of_goToNextpage_in_PBT_page.setText("")
        self.label_12_4.setText(QCoreApplication.translate("MainWindow", u"Binary : ", None))
        self.LBL_of_selected_binary_classifaction_model_in_PBT_page.setText("")
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"Classification :", None))
        self.LBL_of_selected_multiClassification_model_in_PBT_page.setText("")
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Localization : ", None))
        self.LBL_of_selected_localization_model_in_PBT_page.setText("")
        self.label_12_6.setText(QCoreApplication.translate("MainWindow", u"Yolo :", None))
        self.LBL_of_selected_binary_yolo_model_in_PBT_page.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Name of Pipiline  :", None))
        self.pipline_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Example : Date/Mix of weights/....", None))
        self.pipline_name_status.setText(QCoreApplication.translate("MainWindow", u"Please Enter Valid Name", None))
        self.BTN_apply_of_binary_classifaction_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.BTN_refreshing_pipline_page_in_PBT.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Select Dataset / Image", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Dataset :", None))
        self.chbox_defectdata_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Defect", None))
        self.chbox_prefectdata_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Perfect", None))
        self.BTN_load_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.BTN_set_directory_image_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.BTN_load_image_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.LBL_of_data_is_ready_in_PBT_page_2.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Select Pipeline", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Pipeline :", None))
        self.BTN_set_pipline_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.BTN_evaluate_image_in_PBT_page_2.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.BTN_refresh_loadDataset_tab_in_PBT.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.GBox_model_evaluation_details.setTitle(QCoreApplication.translate("MainWindow", u"Evaluated Details", None))
        self.LBL_of_data_is_ready_in_PBT_page.setText("")
        self.LBL_of_pipline_is_ready_in_PBT_page.setText("")
        self.LBL_of_evalution_of_binary_model_in_PBT_page.setText("")
        self.LBL_of_evalution_of_classification_model_in_PBT_page.setText("")
        self.BTN_prev_original_image_in_PBT_page.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Orginal Images", None))
        self.original_image_list_frame.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Evaluated Images", None))
        self.evaluated_image_list_frame.setText("")
        self.BTN_next_original_image_in_PBT_page.setText("")
        self.LBL_piplines_name_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"Name  :", None))
        self.LBL_binary_model_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"binary model  :", None))
        self.LBL_binary_accuracy_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"binary acc  :", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_binary_precision_in_PBT_page_2.setText(QCoreApplication.translate("MainWindow", u"binary precision  :", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_binary_recall_in_PBT_page_3.setText(QCoreApplication.translate("MainWindow", u"binary recall  :", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_binary_f1_in_PBT_page_5.setText(QCoreApplication.translate("MainWindow", u"binary f1  :", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_localization_model_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"localization model  :", None))
        self.LBL_localiztion_dice_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"localization dice  :", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_localiztion_iou_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"localization iou  :", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_classification_model_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"classify model  :", None))
        self.LBL_classification_accuracy_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"classify acc  :", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_classification_precision_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"classify precision  :", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_classification_recall_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"classify recall  :", None))
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.LBL_classification_f1_in_PBT_page.setText(QCoreApplication.translate("MainWindow", u"classify f1  :", None))
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"Date  :", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"Time  :", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.BTN_clear_filter_in_PBT.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.BTN_search_and_filter_in_PBT.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.pipline_table_refresh_btn.setText("")
        self.pipline_tabel_prev_PBT.setText("")
        self.lineEdit_in_history_of_pipline.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pipline_tabel_next_PBT.setText("")
        self.binary_tabel_label_3.setText("")
        self.binary_list.setText(QCoreApplication.translate("MainWindow", u"Binary list", None))
        self.binary_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.binary_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.binary_list_show_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.warning_binarylist_page.setText("")
        self.binary_list_perfect_prev_btn.setText("")
        self.binary_list_perfect_frame.setText("")
        self.binary_list_perfect_next_btn.setText("")
        self.binary_list_defect_prev_btn.setText("")
        self.binary_list_defect_frame.setText("")
        self.binary_list_defect_next_btn.setText("")
        self.binarylist_chart_frame.setTitle(QCoreApplication.translate("MainWindow", u"Defect/Perfect PieChart", None))
        self.binarylist_chart_frame_2.setTitle(QCoreApplication.translate("MainWindow", u"Defect/Perfect BarChart", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name:", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Input Size:", None))
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Input Type:", None))
        self.input_type_resize.setText(QCoreApplication.translate("MainWindow", u"resize", None))
        self.input_type_split.setText(QCoreApplication.translate("MainWindow", u"split", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Epochs:", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Batch Size:", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Learning Rate:", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Tuning Epochs:", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Validation Split %:", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Train Processor:", None))
        self.b_gpu.setItemText(0, QCoreApplication.translate("MainWindow", u"CPU", None))
        self.b_gpu.setItemText(1, QCoreApplication.translate("MainWindow", u"GPU 0", None))
        self.b_gpu.setItemText(2, QCoreApplication.translate("MainWindow", u"GPU 1", None))
        self.b_gpu.setItemText(3, QCoreApplication.translate("MainWindow", u"GPU 2", None))

        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Dataset Path:", None))
        self.b_select_dp.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.b_delete_ds.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.b_add_ds.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.b_add_ds_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dataset Path", None))
        self.b_add_ok.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.b_add_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.binary_train.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.binary_chart_checkbox.setText(QCoreApplication.translate("MainWindow", u"Chart Full View", None))
        self.label_295.setText("")
        self.label_8_2.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_13_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Training Records", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_134_2.setText(QCoreApplication.translate("MainWindow", u"Tune Epochs", None))
        self.label_85_2.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Batch Size", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Split Ratio", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.label_132_2.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"Recall", None))
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.binary_start_year_lineedit.setInputMask("")
        self.binary_start_year_lineedit.setText("")
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.binary_start_month_lineedit.setInputMask("")
        self.binary_start_month_lineedit.setText("")
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.binary_start_day_lineedit.setInputMask("")
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.binary_end_year_lineedit.setInputMask("")
        self.binary_end_year_lineedit.setText("")
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.binary_end_month_lineedit.setInputMask("")
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.binary_end_day_lineedit.setInputMask("")
        self.binary_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.binary_clearfilter_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.binary_table_refresh_btn.setText("")
        self.binary_tabel_prev.setText("")
        self.binary_tabel_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.binary_tabel_next.setText("")
        self.binary_tabel_label.setText("")
        self.localization_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.localization_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name:", None))
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"Pretrained weights path:", None))
        self.l_select_prep.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.l_prep.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Input Size:", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Input Type:", None))
        self.l_input_type_resize.setText(QCoreApplication.translate("MainWindow", u"resize", None))
        self.l_input_type_split.setText(QCoreApplication.translate("MainWindow", u"split", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Epochs:", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"Batch Size:", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"Learning Rate:", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"Validation Split %:", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"Train GPU:", None))
        self.l_gpu.setItemText(0, QCoreApplication.translate("MainWindow", u"CPU", None))
        self.l_gpu.setItemText(1, QCoreApplication.translate("MainWindow", u"GPU 0", None))
        self.l_gpu.setItemText(2, QCoreApplication.translate("MainWindow", u"GPU 1", None))
        self.l_gpu.setItemText(3, QCoreApplication.translate("MainWindow", u"GPU 2", None))

        self.label_250.setText(QCoreApplication.translate("MainWindow", u"Dataset Path:", None))
        self.l_select_dp.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.l_delete_ds.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.l_add_ds.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.l_add_ds_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dataset Path", None))
        self.l_add_ok.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.l_add_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.localization_train.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.localization_chart_checkbox.setText(QCoreApplication.translate("MainWindow", u"Chart Full View", None))
        self.label_18.setText("")
        self.label_8_3.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_13_3.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Training Records", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_2471.setText(QCoreApplication.translate("MainWindow", u"Batch Size", None))
        self.label_2511.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Split Ratio", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.label_132_4.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"FScore", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.localization_end_year_lineedit.setText("")
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.localization_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.localization_clearfilter_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.localization_table_refresh_btn.setText("")
        self.localization_tabel_prev.setText("")
        self.localization_tabel_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.localization_tabel_next.setText("")
        self.localization_tabel_label.setText("")
        self.classification_class_list.setText(QCoreApplication.translate("MainWindow", u"Classes list", None))
        self.classification_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.classification_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.groupBox_80.setTitle(QCoreApplication.translate("MainWindow", u"Defect Classes", None))
        self.groupBox_88.setTitle(QCoreApplication.translate("MainWindow", u"Datasets", None))
        self.classlist_show_related_img_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.classlist_msg_label.setText("")
        self.classlist_prev_btn.setText("")
        self.class_list_slider_frame.setText("")
        self.classlist_next_btn.setText("")
        self.binary_chart_frame.setTitle(QCoreApplication.translate("MainWindow", u"Defect/Perfect PieChart", None))
        self.classlist_chart_frame.setTitle(QCoreApplication.translate("MainWindow", u"Defect Classes PieChart", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Training Records", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name :", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Epochs :", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Learning Rate :", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Tuning Epochs :", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Validation Split % :", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Dataset Path", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Classes to Train:", None))
        self.class_check_train_btn.setText(QCoreApplication.translate("MainWindow", u"Check Parameters", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.classification_train_msg_label.setText("")
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_34.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.cls_chart_checkbox.setText(QCoreApplication.translate("MainWindow", u"Chart Full View", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Traning Records", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Tune Epochs", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_86_3.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Batch-Size", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Split-Size", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.label_132_3.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Recall", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.cls_end_year_lineedit.setText("")
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Including Class(s)", None))
        self.cls_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.cls_clearfilter_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.cls_table_refresh_btn.setText("")
        self.cls_tabel_prev.setText("")
        self.cls_tabel_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.cls_tabel_next.setText("")
        self.cls_tabel_label.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"App appearance", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Language :", None))
        self.label_language.setText("")
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"Font :", None))
        self.fontComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Ubuntu", None))
        self.label_language_2.setText("")
        self.appearance_btn.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"PLC", None))
        self.manual_plc_check.setText(QCoreApplication.translate("MainWindow", u"Manual ", None))
        self.connect_plc_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect_plc_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PLC Status :", None))
        self.plc_status_line.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PLC IP :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Update Time :", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Wind duration :", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Sec", None))
        self.auto_wind_check.setText(QCoreApplication.translate("MainWindow", u"Automatic wind", None))
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"Automatic wind intervals :", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.plc_btn.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.manual_cameras_check.setText(QCoreApplication.translate("MainWindow", u"Manual ", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Frame Rate :", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Live show update time :", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.cameras_btn.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.setting_msg_label.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Dorsa-co", None))
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"SSD", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"HDD", None))
        self.label_290.setText("")
    # retranslateUi

