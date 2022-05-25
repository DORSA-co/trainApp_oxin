# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oxin.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

from mplwidget import MplWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1359, 676)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(120, 30))
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
""
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
"	border-"
                        "radius: 4px\n"
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
"    min-heigh"
                        "t: 25px;\n"
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
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 7px;\n"
"	height: 7px;\n"
""
                        "	border-radius: 10px;\n"
"    background: rgb(255, 255, 255);\n"
"\n"
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
"	"
                        "background-color: rgb(255, 255, 255);\n"
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
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radi"
                        "us: 5px;\n"
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
"    background-color: rgb(255, 121, 198);\n"
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
""
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
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"\n"
"}\n"
" QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
" QPushButton:pr"
                        "essed {	\n"
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.Data_auquzation_btn.sizePolicy().hasHeightForWidth())
        self.Data_auquzation_btn.setSizePolicy(sizePolicy1)
        self.Data_auquzation_btn.setMinimumSize(QSize(0, 45))
        self.Data_auquzation_btn.setFont(font)
        self.Data_auquzation_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Data_auquzation_btn.setLayoutDirection(Qt.LeftToRight)
        self.Data_auquzation_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/graber.png);")

        self.verticalLayout_8.addWidget(self.Data_auquzation_btn)

        self.label_btn = QPushButton(self.topMenu)
        self.label_btn.setObjectName(u"label_btn")
        sizePolicy1.setHeightForWidth(self.label_btn.sizePolicy().hasHeightForWidth())
        self.label_btn.setSizePolicy(sizePolicy1)
        self.label_btn.setMinimumSize(QSize(0, 45))
        self.label_btn.setFont(font)
        self.label_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_btn.setLayoutDirection(Qt.LeftToRight)
        self.label_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/label.png);")

        self.verticalLayout_8.addWidget(self.label_btn)

        self.tuning_btn = QPushButton(self.topMenu)
        self.tuning_btn.setObjectName(u"tuning_btn")
        sizePolicy1.setHeightForWidth(self.tuning_btn.sizePolicy().hasHeightForWidth())
        self.tuning_btn.setSizePolicy(sizePolicy1)
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
        self.pbt_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pbt_btn.sizePolicy().hasHeightForWidth())
        self.pbt_btn.setSizePolicy(sizePolicy1)
        self.pbt_btn.setMinimumSize(QSize(0, 45))
        self.pbt_btn.setFont(font)
        self.pbt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbt_btn.setLayoutDirection(Qt.LeftToRight)
        self.pbt_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/pbt.png)")

        self.verticalLayout_8.addWidget(self.pbt_btn)

        self.btn_about_us = QPushButton(self.topMenu)
        self.btn_about_us.setObjectName(u"btn_about_us")
        self.btn_about_us.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btn_about_us.sizePolicy().hasHeightForWidth())
        self.btn_about_us.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
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
        self.extraLeftBox.setEnabled(True)
        self.extraLeftBox.setMinimumSize(QSize(28, 0))
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
        self.extraContent.setMinimumSize(QSize(5, 0))
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
        self.extraCenter.setMinimumSize(QSize(0, 0))
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Binary_btn = QPushButton(self.extraCenter)
        self.Binary_btn.setObjectName(u"Binary_btn")
        self.Binary_btn.setEnabled(True)
        self.Binary_btn.setMinimumSize(QSize(0, 45))
        self.Binary_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Binary_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;\n"
"border:None;")

        self.verticalLayout_10.addWidget(self.Binary_btn)

        self.line_64 = QFrame(self.extraCenter)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.HLine)
        self.line_64.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_64)

        self.Localization_btn = QPushButton(self.extraCenter)
        self.Localization_btn.setObjectName(u"Localization_btn")
        self.Localization_btn.setMinimumSize(QSize(0, 45))
        self.Localization_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Localization_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;\n"
"border:none;")

        self.verticalLayout_10.addWidget(self.Localization_btn, 0, Qt.AlignLeft)

        self.line_65 = QFrame(self.extraCenter)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.HLine)
        self.line_65.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_65)

        self.Classification_btn = QPushButton(self.extraCenter)
        self.Classification_btn.setObjectName(u"Classification_btn")
        self.Classification_btn.setMinimumSize(QSize(0, 45))
        self.Classification_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Classification_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;\n"
"border:none;")

        self.verticalLayout_10.addWidget(self.Classification_btn, 0, Qt.AlignLeft)

        self.line_66 = QFrame(self.extraCenter)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.HLine)
        self.line_66.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_66)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setMinimumSize(QSize(0, 0))
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_dorsa = QLabel(self.leftBox)
        self.label_dorsa.setObjectName(u"label_dorsa")
        self.label_dorsa.setMaximumSize(QSize(0, 16777215))
        self.label_dorsa.setPixmap(QPixmap(u"images/images/whitew.png"))
        self.label_dorsa.setScaledContents(True)
        self.label_dorsa.setMargin(-11)

        self.horizontalLayout_3.addWidget(self.label_dorsa, 0, Qt.AlignLeft)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMinimumSize(QSize(0, 0))
        self.titleRightInfo.setMaximumSize(QSize(20, 45))
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
        self.label_app_erors = QLabel(self.rightButtons)
        self.label_app_erors.setObjectName(u"label_app_erors")

        self.horizontalLayout_2.addWidget(self.label_app_erors)

        self.user_name = QLabel(self.rightButtons)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setMinimumSize(QSize(80, 0))
        self.user_name.setMaximumSize(QSize(129, 16777215))

        self.horizontalLayout_2.addWidget(self.user_name, 0, Qt.AlignRight)

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
        self.frame_settin2.setMinimumSize(QSize(188, 37))
        self.frame_settin2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settin2.setStyleSheet(u"background-color: rgb(33, 37, 50);")
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

        self.pushButton_9 = QPushButton(self.frame_settin2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(188, 0))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
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

        self.btn_user_proflie = QPushButton(self.frame_settin2)
        self.btn_user_proflie.setObjectName(u"btn_user_proflie")
        self.btn_user_proflie.setMinimumSize(QSize(150, 0))
        self.btn_user_proflie.setMaximumSize(QSize(150, 16777215))
        self.btn_user_proflie.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_user_proflie.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_37.addWidget(self.btn_user_proflie)

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
        self.verticalLayout_97 = QVBoxLayout(self.tab_5)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(3, 3, 3, 3)
        self.frame_73 = QFrame(self.tab_5)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(16777215, 96))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_111.setSpacing(6)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, -1)
        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(186, 0))
        self.frame_75.setMaximumSize(QSize(220, 16777215))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_75)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.comboBox_cam_select = QComboBox(self.frame_76)
        self.comboBox_cam_select.setObjectName(u"comboBox_cam_select")
        self.comboBox_cam_select.setMaximumSize(QSize(70, 25))
        self.comboBox_cam_select.setStyleSheet(u"QComboBox{\n"
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
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox_cam_select.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_121.addWidget(self.comboBox_cam_select)

        self.frame_411 = QFrame(self.frame_76)
        self.frame_411.setObjectName(u"frame_411")
        self.frame_411.setFrameShape(QFrame.StyledPanel)
        self.frame_411.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_411)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.connect_camera_btn = QPushButton(self.frame_411)
        self.connect_camera_btn.setObjectName(u"connect_camera_btn")
        self.connect_camera_btn.setMaximumSize(QSize(70, 16777215))
        self.connect_camera_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_camera_btn.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);")

        self.verticalLayout_101.addWidget(self.connect_camera_btn)

        self.disconnect_camera_btn = QPushButton(self.frame_411)
        self.disconnect_camera_btn.setObjectName(u"disconnect_camera_btn")
        self.disconnect_camera_btn.setMaximumSize(QSize(70, 16777215))
        self.disconnect_camera_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnect_camera_btn.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);")

        self.verticalLayout_101.addWidget(self.disconnect_camera_btn)


        self.horizontalLayout_121.addWidget(self.frame_411)


        self.verticalLayout_98.addWidget(self.frame_76)


        self.horizontalLayout_111.addWidget(self.frame_75)

        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(66, 0))
        self.frame_74.setMaximumSize(QSize(611, 16777215))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_74)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setSpacing(20)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.camera1_btn_2 = QPushButton(self.frame_74)
        self.camera1_btn_2.setObjectName(u"camera1_btn_2")
        self.camera1_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        icon6 = QIcon()
        icon6.addFile(u"../../SettingApp_oxin/images/camtop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera1_btn_2.setIcon(icon6)
        self.camera1_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera1_btn_2)

        self.camera2_btn_2 = QPushButton(self.frame_74)
        self.camera2_btn_2.setObjectName(u"camera2_btn_2")
        self.camera2_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera2_btn_2.setIcon(icon6)
        self.camera2_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera2_btn_2)

        self.camera3_btn_2 = QPushButton(self.frame_74)
        self.camera3_btn_2.setObjectName(u"camera3_btn_2")
        self.camera3_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera3_btn_2.setIcon(icon6)
        self.camera3_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera3_btn_2)

        self.camera4_btn_2 = QPushButton(self.frame_74)
        self.camera4_btn_2.setObjectName(u"camera4_btn_2")
        self.camera4_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera4_btn_2.setIcon(icon6)
        self.camera4_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera4_btn_2)

        self.camera5_btn_2 = QPushButton(self.frame_74)
        self.camera5_btn_2.setObjectName(u"camera5_btn_2")
        self.camera5_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera5_btn_2.setIcon(icon6)
        self.camera5_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera5_btn_2)

        self.camera6_btn_2 = QPushButton(self.frame_74)
        self.camera6_btn_2.setObjectName(u"camera6_btn_2")
        self.camera6_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera6_btn_2.setIcon(icon6)
        self.camera6_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera6_btn_2)

        self.camera7_btn_2 = QPushButton(self.frame_74)
        self.camera7_btn_2.setObjectName(u"camera7_btn_2")
        self.camera7_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera7_btn_2.setIcon(icon6)
        self.camera7_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera7_btn_2)

        self.camera8_btn_2 = QPushButton(self.frame_74)
        self.camera8_btn_2.setObjectName(u"camera8_btn_2")
        self.camera8_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera8_btn_2.setIcon(icon6)
        self.camera8_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera8_btn_2)

        self.camera9_btn_2 = QPushButton(self.frame_74)
        self.camera9_btn_2.setObjectName(u"camera9_btn_2")
        self.camera9_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera9_btn_2.setIcon(icon6)
        self.camera9_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera9_btn_2)

        self.camera10_btn_2 = QPushButton(self.frame_74)
        self.camera10_btn_2.setObjectName(u"camera10_btn_2")
        self.camera10_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera10_btn_2.setIcon(icon6)
        self.camera10_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera10_btn_2)

        self.camera11_btn_2 = QPushButton(self.frame_74)
        self.camera11_btn_2.setObjectName(u"camera11_btn_2")
        self.camera11_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera11_btn_2.setIcon(icon6)
        self.camera11_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera11_btn_2)

        self.camera12_btn_2 = QPushButton(self.frame_74)
        self.camera12_btn_2.setObjectName(u"camera12_btn_2")
        self.camera12_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera12_btn_2.setIcon(icon6)
        self.camera12_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_122.addWidget(self.camera12_btn_2)


        self.verticalLayout_99.addLayout(self.horizontalLayout_122)

        self.line_40 = QFrame(self.frame_74)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_99.addWidget(self.line_40)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setSpacing(20)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.camera13_btn_2 = QPushButton(self.frame_74)
        self.camera13_btn_2.setObjectName(u"camera13_btn_2")
        self.camera13_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        icon7 = QIcon()
        icon7.addFile(u"../../SettingApp_oxin/images/cambtm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera13_btn_2.setIcon(icon7)
        self.camera13_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera13_btn_2)

        self.camera14_btn_2 = QPushButton(self.frame_74)
        self.camera14_btn_2.setObjectName(u"camera14_btn_2")
        self.camera14_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera14_btn_2.setIcon(icon7)
        self.camera14_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera14_btn_2)

        self.camera15_btn_2 = QPushButton(self.frame_74)
        self.camera15_btn_2.setObjectName(u"camera15_btn_2")
        self.camera15_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera15_btn_2.setIcon(icon7)
        self.camera15_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera15_btn_2)

        self.camera16_btn_2 = QPushButton(self.frame_74)
        self.camera16_btn_2.setObjectName(u"camera16_btn_2")
        self.camera16_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera16_btn_2.setIcon(icon7)
        self.camera16_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera16_btn_2)

        self.camera17_btn_2 = QPushButton(self.frame_74)
        self.camera17_btn_2.setObjectName(u"camera17_btn_2")
        self.camera17_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera17_btn_2.setIcon(icon7)
        self.camera17_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera17_btn_2)

        self.camera18_btn_2 = QPushButton(self.frame_74)
        self.camera18_btn_2.setObjectName(u"camera18_btn_2")
        self.camera18_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera18_btn_2.setIcon(icon7)
        self.camera18_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera18_btn_2)

        self.camera19_btn_2 = QPushButton(self.frame_74)
        self.camera19_btn_2.setObjectName(u"camera19_btn_2")
        self.camera19_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera19_btn_2.setIcon(icon7)
        self.camera19_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera19_btn_2)

        self.camera20_btn_2 = QPushButton(self.frame_74)
        self.camera20_btn_2.setObjectName(u"camera20_btn_2")
        self.camera20_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera20_btn_2.setIcon(icon7)
        self.camera20_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera20_btn_2)

        self.camera21_btn_2 = QPushButton(self.frame_74)
        self.camera21_btn_2.setObjectName(u"camera21_btn_2")
        self.camera21_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera21_btn_2.setIcon(icon7)
        self.camera21_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera21_btn_2)

        self.camera22_btn_2 = QPushButton(self.frame_74)
        self.camera22_btn_2.setObjectName(u"camera22_btn_2")
        self.camera22_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera22_btn_2.setIcon(icon7)
        self.camera22_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera22_btn_2)

        self.camera23_btn_2 = QPushButton(self.frame_74)
        self.camera23_btn_2.setObjectName(u"camera23_btn_2")
        self.camera23_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera23_btn_2.setIcon(icon7)
        self.camera23_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera23_btn_2)

        self.camera24_btn_2 = QPushButton(self.frame_74)
        self.camera24_btn_2.setObjectName(u"camera24_btn_2")
        self.camera24_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera24_btn_2.setIcon(icon7)
        self.camera24_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_123.addWidget(self.camera24_btn_2)


        self.verticalLayout_99.addLayout(self.horizontalLayout_123)


        self.horizontalLayout_111.addWidget(self.frame_74)

        self.camera_connection_msg = QLabel(self.frame_73)
        self.camera_connection_msg.setObjectName(u"camera_connection_msg")

        self.horizontalLayout_111.addWidget(self.camera_connection_msg)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_20)


        self.verticalLayout_97.addWidget(self.frame_73)

        self.tabWidget = QTabWidget(self.tab_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_100 = QVBoxLayout(self.tab_3)
        self.verticalLayout_100.setSpacing(6)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(4, 7, 4, -1)
        self.frame_77 = QFrame(self.tab_3)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMaximumSize(QSize(16777214, 24))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_132 = QLabel(self.frame_77)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(110, 0))
        self.label_132.setMaximumSize(QSize(110, 23))

        self.horizontalLayout_124.addWidget(self.label_132)

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
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_124.addWidget(self.comboBox_connected_cams)


        self.verticalLayout_100.addWidget(self.frame_77, 0, Qt.AlignLeft)

        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setScaledContents(True)

        self.verticalLayout_100.addWidget(self.label_21)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout_97.addWidget(self.tabWidget)

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
        self.verticalLayout_85 = QVBoxLayout(self.frame_44)
        self.verticalLayout_85.setSpacing(6)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 8, 0, 1)
        self.frame_69 = QFrame(self.frame_44)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.verticalLayout_85.addWidget(self.frame_69)

        self.frame_59 = QFrame(self.frame_44)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(400, 0))
        self.frame_59.setMaximumSize(QSize(16777215, 37))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(3, 5, -1, 0)
        self.load_coil_btn = QPushButton(self.frame_59)
        self.load_coil_btn.setObjectName(u"load_coil_btn")
        self.load_coil_btn.setMinimumSize(QSize(100, 25))
        self.load_coil_btn.setMaximumSize(QSize(130, 30))
        self.load_coil_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_coil_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_89.addWidget(self.load_coil_btn)

        self.frame_3 = QFrame(self.frame_59)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(15, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_3)
        self.verticalLayout_76.setSpacing(2)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.next_coil_btn = QPushButton(self.frame_3)
        self.next_coil_btn.setObjectName(u"next_coil_btn")
        self.next_coil_btn.setMaximumSize(QSize(20, 16777215))
        self.next_coil_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_coil_btn.setStyleSheet(u"background-color: rgb(0,0,255);")
        icon8 = QIcon()
        icon8.addFile(u"images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_coil_btn.setIcon(icon8)

        self.verticalLayout_76.addWidget(self.next_coil_btn)

        self.prev_coil_btn = QPushButton(self.frame_3)
        self.prev_coil_btn.setObjectName(u"prev_coil_btn")
        self.prev_coil_btn.setMaximumSize(QSize(20, 15))
        self.prev_coil_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_coil_btn.setStyleSheet(u"background-color: rgb(0,0,255);")
        icon9 = QIcon()
        icon9.addFile(u"images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_coil_btn.setIcon(icon9)

        self.verticalLayout_76.addWidget(self.prev_coil_btn)


        self.horizontalLayout_89.addWidget(self.frame_3)

        self.scrollArea_2 = QScrollArea(self.frame_59)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 242, 27))
        self.horizontalLayout_92 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.details_label = QLabel(self.scrollAreaWidgetContents_4)
        self.details_label.setObjectName(u"details_label")
        self.details_label.setMinimumSize(QSize(242, 27))
        self.details_label.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_92.addWidget(self.details_label)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_89.addWidget(self.scrollArea_2)

        self.show_side = QLabel(self.frame_59)
        self.show_side.setObjectName(u"show_side")

        self.horizontalLayout_89.addWidget(self.show_side)


        self.verticalLayout_85.addWidget(self.frame_59)

        self.line_31 = QFrame(self.frame_44)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_85.addWidget(self.line_31)

        self.crop_image = QLabel(self.frame_44)
        self.crop_image.setObjectName(u"crop_image")
        self.crop_image.setMinimumSize(QSize(125, 100))
        self.crop_image.setMaximumSize(QSize(1920, 16777215))
        self.crop_image.setBaseSize(QSize(240, 130))
        self.crop_image.setFrameShape(QFrame.Box)
        self.crop_image.setFrameShadow(QFrame.Plain)
        self.crop_image.setPixmap(QPixmap(u"2.jpg"))
        self.crop_image.setScaledContents(True)
        self.crop_image.setWordWrap(False)
        self.crop_image.setMargin(2)

        self.verticalLayout_85.addWidget(self.crop_image)

        self.line_30 = QFrame(self.frame_44)
        self.line_30.setObjectName(u"line_30")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(57)
        sizePolicy4.setVerticalStretch(25)
        sizePolicy4.setHeightForWidth(self.line_30.sizePolicy().hasHeightForWidth())
        self.line_30.setSizePolicy(sizePolicy4)
        self.line_30.setMinimumSize(QSize(600, 0))
        self.line_30.setFrameShadow(QFrame.Raised)
        self.line_30.setFrameShape(QFrame.HLine)

        self.verticalLayout_85.addWidget(self.line_30)

        self.frame_62 = QFrame(self.frame_44)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(234, 28))
        self.frame_62.setMaximumSize(QSize(16777215, 11))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_117.setSpacing(6)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.show_tools_btn = QPushButton(self.frame_62)
        self.show_tools_btn.setObjectName(u"show_tools_btn")
        self.show_tools_btn.setMaximumSize(QSize(28, 16777215))
        self.show_tools_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_tools_btn.setStyleSheet(u" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                   stop: 0 rgb(0,0,0), stop: 1 rgb(120,120,120));\n"
" border: 2px solid gray;\n"
" border-radius: 5px;")
        icon10 = QIcon()
        icon10.addFile(u"images/icons/cil-caret-top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_tools_btn.setIcon(icon10)

        self.horizontalLayout_117.addWidget(self.show_tools_btn)

        self.horizontalSpacer_15 = QSpacerItem(9, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_15)

        self.warning_data_page = QLabel(self.frame_62)
        self.warning_data_page.setObjectName(u"warning_data_page")
        self.warning_data_page.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_117.addWidget(self.warning_data_page)

        self.progressBar_SI = QProgressBar(self.frame_62)
        self.progressBar_SI.setObjectName(u"progressBar_SI")
        self.progressBar_SI.setMaximumSize(QSize(0, 16777215))
        self.progressBar_SI.setValue(0)
        self.progressBar_SI.setTextVisible(False)

        self.horizontalLayout_117.addWidget(self.progressBar_SI)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_10)


        self.verticalLayout_85.addWidget(self.frame_62)

        self.frame_tools_technical = QFrame(self.frame_44)
        self.frame_tools_technical.setObjectName(u"frame_tools_technical")
        self.frame_tools_technical.setMinimumSize(QSize(0, 220))
        self.frame_tools_technical.setMaximumSize(QSize(16777215, 220))
        self.frame_tools_technical.setFrameShape(QFrame.Panel)
        self.frame_tools_technical.setFrameShadow(QFrame.Raised)
        self.frame_tools_technical.setLineWidth(2)
        self.verticalLayout_89 = QVBoxLayout(self.frame_tools_technical)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(6, 5, 6, 5)
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(3)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalSpacer_14 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_14)

        self.frame_67 = QFrame(self.frame_tools_technical)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(80, 0))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_67)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_67)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(78, 0))
        self.groupBox_2.setMaximumSize(QSize(50, 16777215))
        self.groupBox_2.setStyleSheet(u" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                   stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
" border: 2px solid gray;\n"
" border-radius: 5px;\n"
" margin-top: 1ex; /* leave space at the top for the title */")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_90 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_90.setSpacing(2)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(2, 1, 2, 3)
        self.save_btn_SI = QPushButton(self.groupBox_2)
        self.save_btn_SI.setObjectName(u"save_btn_SI")
        self.save_btn_SI.setMinimumSize(QSize(68, 25))
        self.save_btn_SI.setMaximumSize(QSize(120, 30))
        self.save_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_btn_SI.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_90.addWidget(self.save_btn_SI)

        self.label_btn_SI = QPushButton(self.groupBox_2)
        self.label_btn_SI.setObjectName(u"label_btn_SI")
        self.label_btn_SI.setMinimumSize(QSize(68, 25))
        self.label_btn_SI.setMaximumSize(QSize(130, 30))
        self.label_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_btn_SI.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_90.addWidget(self.label_btn_SI)


        self.verticalLayout_94.addWidget(self.groupBox_2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_94.addItem(self.verticalSpacer_9)


        self.horizontalLayout_93.addWidget(self.frame_67)

        self.groupBox = QGroupBox(self.frame_tools_technical)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(168, 0))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setStyleSheet(u" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                   stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
" border: 2px solid gray;\n"
" border-radius: 5px;\n"
" margin-top: 1ex; /* leave space at the top for the title */")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_88 = QVBoxLayout(self.groupBox)
        self.verticalLayout_88.setSpacing(2)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(2, 3, 2, 2)
        self.verticalLayout_77 = QVBoxLayout()
        self.verticalLayout_77.setSpacing(1)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.add_btn_SI = QPushButton(self.groupBox)
        self.add_btn_SI.setObjectName(u"add_btn_SI")
        self.add_btn_SI.setMinimumSize(QSize(30, 30))
        self.add_btn_SI.setMaximumSize(QSize(30, 30))
        self.add_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_btn_SI.setMouseTracking(True)
        self.add_btn_SI.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
" margin-top: 1ex; /* leave space at the top for the title */")
        icon11 = QIcon()
        icon11.addFile(u"images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn_SI.setIcon(icon11)
        self.add_btn_SI.setIconSize(QSize(26, 26))

        self.horizontalLayout_91.addWidget(self.add_btn_SI)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(72, 24))
        self.label_2.setMaximumSize(QSize(81, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font4)
        self.label_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet(u" background-color:black;\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)

        self.horizontalLayout_91.addWidget(self.label_2)

        self.remove_btn_SI = QPushButton(self.groupBox)
        self.remove_btn_SI.setObjectName(u"remove_btn_SI")
        self.remove_btn_SI.setMinimumSize(QSize(30, 30))
        self.remove_btn_SI.setMaximumSize(QSize(30, 30))
        self.remove_btn_SI.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_btn_SI.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
" margin-top: 1ex; /* leave space at the top for the title */")
        icon12 = QIcon()
        icon12.addFile(u"images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_btn_SI.setIcon(icon12)
        self.remove_btn_SI.setIconSize(QSize(26, 26))

        self.horizontalLayout_91.addWidget(self.remove_btn_SI)


        self.verticalLayout_77.addLayout(self.horizontalLayout_91)

        self.line_41 = QFrame(self.groupBox)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.HLine)
        self.line_41.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_77.addWidget(self.line_41)

        self.frame_63 = QFrame(self.groupBox)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 28))
        self.frame_63.setStyleSheet(u"border:None;\n"
"background-color:rgb(200,200,200);")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(8, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_120.addItem(self.horizontalSpacer_17)

        self.checkBox_select = QCheckBox(self.frame_63)
        self.checkBox_select.setObjectName(u"checkBox_select")
        self.checkBox_select.setStyleSheet(u"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	border-radius: 0px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"	height: 13px;\n"
"}\n"
"")

        self.horizontalLayout_120.addWidget(self.checkBox_select)


        self.verticalLayout_77.addWidget(self.frame_63)


        self.verticalLayout_88.addLayout(self.verticalLayout_77)

        self.line_32 = QFrame(self.groupBox)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_88.addWidget(self.line_32)

        self.listWidget_append_img_list = QTableWidget(self.groupBox)
        if (self.listWidget_append_img_list.columnCount() < 1):
            self.listWidget_append_img_list.setColumnCount(1)
        self.listWidget_append_img_list.setObjectName(u"listWidget_append_img_list")
        self.listWidget_append_img_list.setStyleSheet(u"border:None;")
        self.listWidget_append_img_list.setRowCount(0)
        self.listWidget_append_img_list.setColumnCount(1)
        self.listWidget_append_img_list.horizontalHeader().setVisible(False)
        self.listWidget_append_img_list.horizontalHeader().setCascadingSectionResizes(False)
        self.listWidget_append_img_list.horizontalHeader().setDefaultSectionSize(200)
        self.listWidget_append_img_list.horizontalHeader().setProperty("showSortIndicator", False)
        self.listWidget_append_img_list.verticalHeader().setVisible(False)

        self.verticalLayout_88.addWidget(self.listWidget_append_img_list)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacer_7)


        self.horizontalLayout_93.addWidget(self.groupBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_16 = QSpacerItem(750, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_16)

        self.groupBox_3 = QGroupBox(self.frame_tools_technical)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(156, 146))
        self.groupBox_3.setMaximumSize(QSize(106, 146))
        self.groupBox_3.setStyleSheet(u" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                   stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
" border: 2px solid gray;\n"
" border-radius: 5px;\n"
" margin-top: 1ex; /* leave space at the top for the title */")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.verticalLayout_91 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(128, 24))
        self.label_3.setMaximumSize(QSize(72, 16777215))
        self.label_3.setFont(font4)
        self.label_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_3.setAcceptDrops(False)
        self.label_3.setStyleSheet(u" background-color:black;\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:white;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)

        self.verticalLayout_91.addWidget(self.label_3)

        self.frame_61 = QFrame(self.groupBox_3)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_61)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 2, 3, -1)
        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.label_30 = QLabel(self.frame_61)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(29, 22))
        self.label_30.setMaximumSize(QSize(29, 22))
        self.label_30.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius:5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")
        self.label_30.setPixmap(QPixmap(u"images/pngaaa.com-4780825.png"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_115.addWidget(self.label_30)

        self.label_126 = QLabel(self.frame_61)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMaximumSize(QSize(13, 23))
        self.label_126.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_115.addWidget(self.label_126)

        self.current_pos_x = QLabel(self.frame_61)
        self.current_pos_x.setObjectName(u"current_pos_x")
        self.current_pos_x.setMinimumSize(QSize(40, 30))
        self.current_pos_x.setMaximumSize(QSize(40, 30))
        self.current_pos_x.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")

        self.horizontalLayout_115.addWidget(self.current_pos_x)

        self.label_23 = QLabel(self.frame_61)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_115.addWidget(self.label_23)


        self.verticalLayout_21.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.label_127 = QLabel(self.frame_61)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMaximumSize(QSize(19, 30))
        self.label_127.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius:5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")
        self.label_127.setPixmap(QPixmap(u"images/pngaaa.com-4780825 - Copy.png"))
        self.label_127.setScaledContents(True)

        self.horizontalLayout_116.addWidget(self.label_127)

        self.horizontalSpacer_12 = QSpacerItem(9, 22, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_116.addItem(self.horizontalSpacer_12)

        self.label_128 = QLabel(self.frame_61)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(13, 23))
        self.label_128.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_116.addWidget(self.label_128)

        self.current_pos_y = QLabel(self.frame_61)
        self.current_pos_y.setObjectName(u"current_pos_y")
        self.current_pos_y.setMinimumSize(QSize(40, 30))
        self.current_pos_y.setMaximumSize(QSize(40, 30))
        self.current_pos_y.setStyleSheet(u" border: 2px solid gray;\n"
" border-radius: 5px;\n"
"/* margin-top: 1ex; /* leave space at the top for the title */\n"
"text-Align:left;\n"
"color:black;")

        self.horizontalLayout_116.addWidget(self.current_pos_y)

        self.label_130 = QLabel(self.frame_61)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setStyleSheet(u" background-color: Transparent;\n"
" border: 0px solid gray;\n"
" border-radius: 0px;\n"
"")

        self.horizontalLayout_116.addWidget(self.label_130)


        self.verticalLayout_21.addLayout(self.horizontalLayout_116)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_8)


        self.verticalLayout_91.addWidget(self.frame_61)


        self.horizontalLayout_93.addWidget(self.groupBox_3, 0, Qt.AlignTop)


        self.verticalLayout_89.addLayout(self.horizontalLayout_93)


        self.verticalLayout_85.addWidget(self.frame_tools_technical)


        self.verticalLayout_84.addWidget(self.frame_44)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.horizontalLayout_86.addWidget(self.tabWidget_2)

        self.frame_413 = QFrame(self.main)
        self.frame_413.setObjectName(u"frame_413")
        self.frame_413.setMaximumSize(QSize(1920, 1200))
        self.frame_413.setFrameShape(QFrame.StyledPanel)
        self.frame_413.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_1103 = QHBoxLayout(self.frame_413)
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
        self.verticalLayout_4.setContentsMargins(1, 0, 1, 0)
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
        self.label_1291.setFont(font)

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
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_6_1.setFont(font5)
        self.label_6_1.setStyleSheet(u"font-weight: bold; \n"
"font-size: 30%;")

        self.horizontalLayout_1191.addWidget(self.label_6_1)


        self.verticalLayout_4.addWidget(self.frame_651)

        self.scrollArea_up_side_4 = QScrollArea(self.frame_2_3)
        self.scrollArea_up_side_4.setObjectName(u"scrollArea_up_side_4")
        self.scrollArea_up_side_4.setMinimumSize(QSize(288, 0))
        self.scrollArea_up_side_4.setMaximumSize(QSize(290, 16777215))
        self.scrollArea_up_side_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_up_side_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 288, 481))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(288, 0))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(280, 16777215))
        self.horizontalLayout_90_2 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_90_2.setObjectName(u"horizontalLayout_90_2")
        self.horizontalLayout_90_2.setContentsMargins(0, 0, 0, 0)
        self.up_side_technical = QLabel(self.scrollAreaWidgetContents_2)
        self.up_side_technical.setObjectName(u"up_side_technical")
        self.up_side_technical.setMinimumSize(QSize(288, 0))
        self.up_side_technical.setMaximumSize(QSize(280, 16777215))
        self.up_side_technical.setPixmap(QPixmap(u"../train/oxin/03-11-2021 09-43-52-296900__0.jpg"))
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
        self.verticalLayout_87_2.setContentsMargins(1, 0, 1, 0)
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
        self.label_124.setFont(font)

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

        self.horizontalLayout_118_2.addWidget(self.label_119)


        self.verticalLayout_87_2.addWidget(self.frame_60_2)

        self.scrollArea_up_side_3 = QScrollArea(self.frame_16_2)
        self.scrollArea_up_side_3.setObjectName(u"scrollArea_up_side_3")
        self.scrollArea_up_side_3.setMinimumSize(QSize(288, 0))
        self.scrollArea_up_side_3.setMaximumSize(QSize(290, 16777215))
        self.scrollArea_up_side_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_up_side_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_51 = QWidget()
        self.scrollAreaWidgetContents_51.setObjectName(u"scrollAreaWidgetContents_51")
        self.scrollAreaWidgetContents_51.setGeometry(QRect(0, 0, 288, 481))
        self.scrollAreaWidgetContents_51.setMinimumSize(QSize(288, 0))
        self.scrollAreaWidgetContents_51.setMaximumSize(QSize(280, 16777215))
        self.horizontalLayout_1141 = QHBoxLayout(self.scrollAreaWidgetContents_51)
        self.horizontalLayout_1141.setObjectName(u"horizontalLayout_1141")
        self.horizontalLayout_1141.setContentsMargins(0, 0, 0, 0)
        self.down_side_technical = QLabel(self.scrollAreaWidgetContents_51)
        self.down_side_technical.setObjectName(u"down_side_technical")
        self.down_side_technical.setEnabled(True)
        self.down_side_technical.setMinimumSize(QSize(288, 0))
        self.down_side_technical.setMaximumSize(QSize(280, 16777215))
        self.down_side_technical.setPixmap(QPixmap(u"../train/oxin/03-11-2021 09-43-52-296900__0.jpg"))
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
        self.verticalLayout_38 = QVBoxLayout(self.frame)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_27_2.setObjectName(u"verticalLayout_27_2")
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
        icon13 = QIcon()
        icon13.addFile(u"images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon13)
        self.pushButton_28.setIconSize(QSize(20, 28))

        self.verticalLayout_27_2.addWidget(self.pushButton_28)

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
        icon14 = QIcon()
        icon14.addFile(u"images/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon14)
        self.pushButton_2.setIconSize(QSize(24, 31))

        self.verticalLayout_27_2.addWidget(self.pushButton_2)

        self.line_34 = QFrame(self.frame_7)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27_2.addWidget(self.line_34)

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
        self.zoomIn_btn.setToolTip(u"Zoom in")
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
        self.zoomOut_btn.setToolTip(u"Zoom back")
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

        self.bounding_btn = QPushButton(self.frame_7)
        self.bounding_btn.setObjectName(u"bounding_btn")
        self.bounding_btn.setEnabled(False)
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
        icon21 = QIcon()
        icon21.addFile(u"images/noun-rectangle-667504.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bounding_btn.setIcon(icon21)
        self.bounding_btn.setIconSize(QSize(31, 29))

        self.verticalLayout_27_2.addWidget(self.bounding_btn)

        self.heatmap_btn = QPushButton(self.frame_7)
        self.heatmap_btn.setObjectName(u"heatmap_btn")
        self.heatmap_btn.setEnabled(False)
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
        self.delete_btn.setToolTip(u"Delete Rec")
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
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_8)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.Box)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.frame_58.setLineWidth(2)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_87.setSpacing(2)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.image = QLabel(self.frame_58)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(0, 0))
        self.image.setMaximumSize(QSize(16777215, 16777215))
        self.image.setFrameShape(QFrame.NoFrame)
        self.image.setFrameShadow(QFrame.Plain)
        self.image.setLineWidth(2)
        self.image.setPixmap(QPixmap(u"../images/image.png"))
        self.image.setScaledContents(True)
        self.image.setMargin(0)
        self.image.setIndent(0)

        self.horizontalLayout_87.addWidget(self.image)


        self.horizontalLayout_15.addWidget(self.frame_58)


        self.horizontalLayout_14.addWidget(self.frame_8)


        self.verticalLayout_38.addWidget(self.frame_6)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_38.addWidget(self.line_2)

        self.scrollArea_3 = QScrollArea(self.frame)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 152))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 152))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1356, 143))
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_1011 = QVBoxLayout()
        self.verticalLayout_1011.setObjectName(u"verticalLayout_1011")
        self.image_up_left = QLabel(self.scrollAreaWidgetContents_3)
        self.image_up_left.setObjectName(u"image_up_left")
        self.image_up_left.setMinimumSize(QSize(160, 100))
        self.image_up_left.setMaximumSize(QSize(160, 100))
        self.image_up_left.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_up_left.setScaledContents(True)

        self.verticalLayout_1011.addWidget(self.image_up_left)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_1011.addWidget(self.label_29)


        self.horizontalLayout_13.addLayout(self.verticalLayout_1011)

        self.verticalLayout_1001 = QVBoxLayout()
        self.verticalLayout_1001.setObjectName(u"verticalLayout_1001")
        self.image_up = QLabel(self.scrollAreaWidgetContents_3)
        self.image_up.setObjectName(u"image_up")
        self.image_up.setMinimumSize(QSize(160, 100))
        self.image_up.setMaximumSize(QSize(160, 100))
        self.image_up.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_up.setScaledContents(True)

        self.verticalLayout_1001.addWidget(self.image_up)

        self.label_211 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setScaledContents(True)
        self.label_211.setAlignment(Qt.AlignCenter)

        self.verticalLayout_1001.addWidget(self.label_211)


        self.horizontalLayout_13.addLayout(self.verticalLayout_1001)

        self.verticalLayout_991 = QVBoxLayout()
        self.verticalLayout_991.setObjectName(u"verticalLayout_991")
        self.image_up_right = QLabel(self.scrollAreaWidgetContents_3)
        self.image_up_right.setObjectName(u"image_up_right")
        self.image_up_right.setMinimumSize(QSize(160, 100))
        self.image_up_right.setMaximumSize(QSize(160, 100))
        self.image_up_right.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_up_right.setScaledContents(True)

        self.verticalLayout_991.addWidget(self.image_up_right)

        self.label_1091 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_1091.setObjectName(u"label_1091")
        self.label_1091.setScaledContents(True)
        self.label_1091.setAlignment(Qt.AlignCenter)

        self.verticalLayout_991.addWidget(self.label_1091)


        self.horizontalLayout_13.addLayout(self.verticalLayout_991)

        self.verticalLayout_981 = QVBoxLayout()
        self.verticalLayout_981.setObjectName(u"verticalLayout_981")
        self.image_left = QLabel(self.scrollAreaWidgetContents_3)
        self.image_left.setObjectName(u"image_left")
        self.image_left.setMinimumSize(QSize(160, 100))
        self.image_left.setMaximumSize(QSize(160, 100))
        self.image_left.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_left.setScaledContents(True)

        self.verticalLayout_981.addWidget(self.image_left)

        self.label_81_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_81_2.setObjectName(u"label_81_2")
        self.label_81_2.setScaledContents(True)
        self.label_81_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_981.addWidget(self.label_81_2)


        self.horizontalLayout_13.addLayout(self.verticalLayout_981)

        self.verticalLayout_971 = QVBoxLayout()
        self.verticalLayout_971.setObjectName(u"verticalLayout_971")
        self.image_right = QLabel(self.scrollAreaWidgetContents_3)
        self.image_right.setObjectName(u"image_right")
        self.image_right.setMinimumSize(QSize(160, 100))
        self.image_right.setMaximumSize(QSize(160, 100))
        self.image_right.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_right.setScaledContents(True)

        self.verticalLayout_971.addWidget(self.image_right)

        self.label_111 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setScaledContents(True)
        self.label_111.setAlignment(Qt.AlignCenter)

        self.verticalLayout_971.addWidget(self.label_111)


        self.horizontalLayout_13.addLayout(self.verticalLayout_971)

        self.verticalLayout_961 = QVBoxLayout()
        self.verticalLayout_961.setObjectName(u"verticalLayout_961")
        self.image_bottom_left = QLabel(self.scrollAreaWidgetContents_3)
        self.image_bottom_left.setObjectName(u"image_bottom_left")
        self.image_bottom_left.setMinimumSize(QSize(160, 100))
        self.image_bottom_left.setMaximumSize(QSize(160, 100))
        self.image_bottom_left.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_bottom_left.setScaledContents(True)

        self.verticalLayout_961.addWidget(self.image_bottom_left)

        self.label_121 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setScaledContents(True)
        self.label_121.setAlignment(Qt.AlignCenter)

        self.verticalLayout_961.addWidget(self.label_121)


        self.horizontalLayout_13.addLayout(self.verticalLayout_961)

        self.verticalLayout_271 = QVBoxLayout()
        self.verticalLayout_271.setObjectName(u"verticalLayout_271")
        self.image_bottom = QLabel(self.scrollAreaWidgetContents_3)
        self.image_bottom.setObjectName(u"image_bottom")
        self.image_bottom.setMinimumSize(QSize(160, 100))
        self.image_bottom.setMaximumSize(QSize(160, 100))
        self.image_bottom.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")
        self.image_bottom.setScaledContents(True)

        self.verticalLayout_271.addWidget(self.image_bottom)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_271.addWidget(self.label_13)


        self.horizontalLayout_13.addLayout(self.verticalLayout_271)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.image_bottom_right = QLabel(self.scrollAreaWidgetContents_3)
        self.image_bottom_right.setObjectName(u"image_bottom_right")
        self.image_bottom_right.setMinimumSize(QSize(160, 100))
        self.image_bottom_right.setMaximumSize(QSize(160, 100))
        self.image_bottom_right.setStyleSheet(u"border: 2px solid rgb(0, 0, 0);")

        self.verticalLayout_26.addWidget(self.image_bottom_right)

        self.label_1321 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_1321.setObjectName(u"label_1321")
        self.label_1321.setScaledContents(True)
        self.label_1321.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_1321)


        self.horizontalLayout_13.addLayout(self.verticalLayout_26)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_38.addWidget(self.scrollArea_3)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_11 = QFrame(self.page_label)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 0))
        self.frame_11.setMaximumSize(QSize(330, 16777215))
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.frame_11.setLineWidth(1)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 40))
        self.frame_12.setFrameShape(QFrame.Panel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(2)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_27 = QLabel(self.frame_12)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_20.addWidget(self.label_27)

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

        self.horizontalLayout_20.addWidget(self.yes_defect)

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
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_95 = QVBoxLayout(self.tab)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.mask_table_widget = QTableWidget(self.tab)
        if (self.mask_table_widget.columnCount() < 1):
            self.mask_table_widget.setColumnCount(1)
        self.mask_table_widget.setObjectName(u"mask_table_widget")
        self.mask_table_widget.setColumnCount(1)

        self.verticalLayout_95.addWidget(self.mask_table_widget)

        self.tabWidget_defect.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_831 = QVBoxLayout(self.tab_2)
        self.verticalLayout_831.setObjectName(u"verticalLayout_831")
        self.bbox_table_widget = QTableWidget(self.tab_2)
        if (self.bbox_table_widget.columnCount() < 1):
            self.bbox_table_widget.setColumnCount(1)
        self.bbox_table_widget.setObjectName(u"bbox_table_widget")
        self.bbox_table_widget.setColumnCount(1)

        self.verticalLayout_831.addWidget(self.bbox_table_widget)

        self.tabWidget_defect.addTab(self.tab_2, "")

        self.verticalLayout_36.addWidget(self.tabWidget_defect)


        self.verticalLayout_35.addWidget(self.frame_13)

        self.frame_add_label = QFrame(self.page_yes)
        self.frame_add_label.setObjectName(u"frame_add_label")
        self.frame_add_label.setMinimumSize(QSize(0, 0))
        self.frame_add_label.setMaximumSize(QSize(16777215, 0))
        self.frame_add_label.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_add_label.setFrameShape(QFrame.Panel)
        self.frame_add_label.setFrameShadow(QFrame.Sunken)
        self.frame_add_label.setLineWidth(2)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_add_label)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.add_label_text = QLineEdit(self.frame_add_label)
        self.add_label_text.setObjectName(u"add_label_text")
        self.add_label_text.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_113.addWidget(self.add_label_text)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_11)

        self.add_label_btn = QPushButton(self.frame_add_label)
        self.add_label_btn.setObjectName(u"add_label_btn")
        self.add_label_btn.setMinimumSize(QSize(30, 0))
        self.add_label_btn.setMaximumSize(QSize(30, 16777215))
        self.add_label_btn.setStyleSheet(u"    background: Transparent;")
        icon24 = QIcon()
        icon24.addFile(u"images/rounded-adjust-button-with-plus-and-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_label_btn.setIcon(icon24)
        self.add_label_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_113.addWidget(self.add_label_btn)


        self.verticalLayout_35.addWidget(self.frame_add_label)

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
        self.frame_17.setMinimumSize(QSize(0, 100))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_17)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.warning_label_page = QLabel(self.frame_17)
        self.warning_label_page.setObjectName(u"warning_label_page")

        self.verticalLayout_39.addWidget(self.warning_label_page, 0, Qt.AlignHCenter)

        self.save_dataset_btn = QPushButton(self.frame_17)
        self.save_dataset_btn.setObjectName(u"save_dataset_btn")
        self.save_dataset_btn.setMinimumSize(QSize(200, 30))
        self.save_dataset_btn.setMaximumSize(QSize(150, 16777215))
        self.save_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_dataset_btn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_39.addWidget(self.save_dataset_btn, 0, Qt.AlignHCenter)

        self.pieChart = MplWidget(self.frame_17)
        self.pieChart.setObjectName(u"pieChart")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pieChart.sizePolicy().hasHeightForWidth())
        self.pieChart.setSizePolicy(sizePolicy5)

        self.verticalLayout_39.addWidget(self.pieChart)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 60))
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
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
        self.plabel_date_txt = QLabel(self.frame_19)
        self.plabel_date_txt.setObjectName(u"plabel_date_txt")

        self.verticalLayout_25.addWidget(self.plabel_date_txt)

        self.plabel_coil_num_txt = QLabel(self.frame_19)
        self.plabel_coil_num_txt.setObjectName(u"plabel_coil_num_txt")

        self.verticalLayout_25.addWidget(self.plabel_coil_num_txt)

        self.plabel_cam_txt = QLabel(self.frame_19)
        self.plabel_cam_txt.setObjectName(u"plabel_cam_txt")

        self.verticalLayout_25.addWidget(self.plabel_cam_txt)


        self.horizontalLayout_10.addLayout(self.verticalLayout_25)


        self.verticalLayout_39.addWidget(self.frame_19)


        self.verticalLayout_34.addWidget(self.frame_17)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_label)
        self.page_user_profile = QWidget()
        self.page_user_profile.setObjectName(u"page_user_profile")
        self.verticalLayout_27 = QVBoxLayout(self.page_user_profile)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_2 = QFrame(self.page_user_profile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_24.addWidget(self.label_6)

        self.user_name_2 = QLabel(self.frame_2)
        self.user_name_2.setObjectName(u"user_name_2")

        self.horizontalLayout_24.addWidget(self.user_name_2)


        self.horizontalLayout_114.addLayout(self.horizontalLayout_24)

        self.horizontalSpacer_30 = QSpacerItem(23, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_30)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_88.addWidget(self.label_15)

        self.user_id = QLabel(self.frame_2)
        self.user_id.setObjectName(u"user_id")

        self.horizontalLayout_88.addWidget(self.user_id)


        self.horizontalLayout_114.addLayout(self.horizontalLayout_88)

        self.horizontalSpacer_31 = QSpacerItem(23, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_31)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_165.addWidget(self.label_16)

        self.role = QLabel(self.frame_2)
        self.role.setObjectName(u"role")

        self.horizontalLayout_165.addWidget(self.role)


        self.horizontalLayout_114.addLayout(self.horizontalLayout_165)

        self.horizontalSpacer_32 = QSpacerItem(23, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_32)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(88, 0))

        self.horizontalLayout_90.addWidget(self.label_17)

        self.date_created = QLabel(self.frame_2)
        self.date_created.setObjectName(u"date_created")

        self.horizontalLayout_90.addWidget(self.date_created)


        self.horizontalLayout_114.addLayout(self.horizontalLayout_90)

        self.horizontalSpacer_33 = QSpacerItem(23, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_33)

        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.label_79 = QLabel(self.frame_2)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_166.addWidget(self.label_79)

        self.default_dataset = QLabel(self.frame_2)
        self.default_dataset.setObjectName(u"default_dataset")

        self.horizontalLayout_166.addWidget(self.default_dataset)


        self.horizontalLayout_114.addLayout(self.horizontalLayout_166)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_6)


        self.verticalLayout_27.addWidget(self.frame_2)

        self.line_15 = QFrame(self.page_user_profile)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_15)

        self.frame_16 = QFrame(self.page_user_profile)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_16)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 86))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(-1, 0, -1, 0)
        self.frame_41 = QFrame(self.frame_18)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(76, 0))
        self.frame_41.setMaximumSize(QSize(16777215, 76))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_41)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(87, 0))

        self.horizontalLayout_119.addWidget(self.label_24)

        self.comboBox_all_datasets = QComboBox(self.frame_41)
        self.comboBox_all_datasets.setObjectName(u"comboBox_all_datasets")
        self.comboBox_all_datasets.setMinimumSize(QSize(140, 0))
        self.comboBox_all_datasets.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_119.addWidget(self.comboBox_all_datasets)

        self.pushButton_3 = QPushButton(self.frame_41)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(67, 0))
        self.pushButton_3.setStyleSheet(u"color:white;")

        self.horizontalLayout_119.addWidget(self.pushButton_3)


        self.horizontalLayout_118.addWidget(self.frame_41, 0, Qt.AlignTop)

        self.tableWidget_all_dataset = QTableWidget(self.frame_18)
        if (self.tableWidget_all_dataset.columnCount() < 4):
            self.tableWidget_all_dataset.setColumnCount(4)
        self.tableWidget_all_dataset.setObjectName(u"tableWidget_all_dataset")
        self.tableWidget_all_dataset.setColumnCount(4)

        self.horizontalLayout_118.addWidget(self.tableWidget_all_dataset)


        self.verticalLayout_41.addWidget(self.frame_18)

        self.frame_60 = QFrame(self.frame_16)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 34))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.my_databases_2 = QPushButton(self.frame_60)
        self.my_databases_2.setObjectName(u"my_databases_2")
        self.my_databases_2.setMinimumSize(QSize(151, 22))
        self.my_databases_2.setStyleSheet(u"color:white")

        self.horizontalLayout_156.addWidget(self.my_databases_2)

        self.create_new_database = QPushButton(self.frame_60)
        self.create_new_database.setObjectName(u"create_new_database")
        self.create_new_database.setMinimumSize(QSize(151, 22))
        self.create_new_database.setStyleSheet(u"color:white")

        self.horizontalLayout_156.addWidget(self.create_new_database)


        self.verticalLayout_41.addWidget(self.frame_60, 0, Qt.AlignLeft)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_20)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_20)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.create_database = QWidget()
        self.create_database.setObjectName(u"create_database")
        self.horizontalLayout_157 = QHBoxLayout(self.create_database)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.frame_65 = QFrame(self.create_database)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.frame_64 = QFrame(self.frame_65)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setGeometry(QRect(0, 20, 401, 241))
        self.frame_64.setFrameShape(QFrame.Box)
        self.frame_64.setFrameShadow(QFrame.Plain)
        self.frame_64.setLineWidth(2)
        self.verticalLayout_55 = QVBoxLayout(self.frame_64)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_25 = QLabel(self.frame_64)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_162.addWidget(self.label_25)

        self.lineEdit_name_dataset = QLineEdit(self.frame_64)
        self.lineEdit_name_dataset.setObjectName(u"lineEdit_name_dataset")
        self.lineEdit_name_dataset.setMaximumSize(QSize(245, 16777215))

        self.horizontalLayout_162.addWidget(self.lineEdit_name_dataset)


        self.verticalLayout_55.addLayout(self.horizontalLayout_162)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_78 = QLabel(self.frame_64)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_158.addWidget(self.label_78)

        self.today_date = QLabel(self.frame_64)
        self.today_date.setObjectName(u"today_date")

        self.horizontalLayout_158.addWidget(self.today_date, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_129 = QLabel(self.frame_64)
        self.label_129.setObjectName(u"label_129")

        self.horizontalLayout_159.addWidget(self.label_129)

        self.user_name_3 = QLabel(self.frame_64)
        self.user_name_3.setObjectName(u"user_name_3")

        self.horizontalLayout_159.addWidget(self.user_name_3, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_157 = QLabel(self.frame_64)
        self.label_157.setObjectName(u"label_157")

        self.horizontalLayout_160.addWidget(self.label_157)

        self.lineEdit_path_dataset = QLineEdit(self.frame_64)
        self.lineEdit_path_dataset.setObjectName(u"lineEdit_path_dataset")

        self.horizontalLayout_160.addWidget(self.lineEdit_path_dataset)

        self.label_20 = QLabel(self.frame_64)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_160.addWidget(self.label_20)

        self.label_8 = QLabel(self.frame_64)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_160.addWidget(self.label_8)

        self.label_14 = QLabel(self.frame_64)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_160.addWidget(self.label_14)

        self.toolButton_select_directory = QToolButton(self.frame_64)
        self.toolButton_select_directory.setObjectName(u"toolButton_select_directory")

        self.horizontalLayout_160.addWidget(self.toolButton_select_directory)


        self.verticalLayout_55.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_158 = QLabel(self.frame_64)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_161.addWidget(self.label_158)

        self.comboBox_max_size = QComboBox(self.frame_64)
        self.comboBox_max_size.setObjectName(u"comboBox_max_size")
        self.comboBox_max_size.setMaximumSize(QSize(16777215, 28))

        self.horizontalLayout_161.addWidget(self.comboBox_max_size)


        self.verticalLayout_55.addLayout(self.horizontalLayout_161)

        self.create_database_btn = QPushButton(self.frame_64)
        self.create_database_btn.setObjectName(u"create_database_btn")
        self.create_database_btn.setMinimumSize(QSize(151, 22))
        self.create_database_btn.setStyleSheet(u"color:white")

        self.verticalLayout_55.addWidget(self.create_database_btn, 0, Qt.AlignHCenter)


        self.horizontalLayout_157.addWidget(self.frame_65)

        self.stackedWidget_2.addWidget(self.create_database)
        self.my_databases = QWidget()
        self.my_databases.setObjectName(u"my_databases")
        self.verticalLayout_56 = QVBoxLayout(self.my_databases)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_66 = QFrame(self.my_databases)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(800, 50))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_163 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.label_26 = QLabel(self.frame_66)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(47, 0))
        self.label_26.setMaximumSize(QSize(39, 16777215))

        self.horizontalLayout_163.addWidget(self.label_26)

        self.comboBox_user_datasets = QComboBox(self.frame_66)
        self.comboBox_user_datasets.setObjectName(u"comboBox_user_datasets")
        self.comboBox_user_datasets.setMinimumSize(QSize(120, 0))
        self.comboBox_user_datasets.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_163.addWidget(self.comboBox_user_datasets)

        self.pushButton_8 = QPushButton(self.frame_66)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(67, 0))
        self.pushButton_8.setMaximumSize(QSize(50, 16777215))
        self.pushButton_8.setStyleSheet(u"color:white;")

        self.horizontalLayout_163.addWidget(self.pushButton_8)

        self.horizontalSpacer_22 = QSpacerItem(163, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_22)

        self.frame_78asd = QFrame(self.frame_66)
        self.frame_78asd.setObjectName(u"frame_78asd")
        self.frame_78asd.setMinimumSize(QSize(0, 29))
        self.frame_78asd.setMaximumSize(QSize(499, 56))
        self.frame_78asd.setFrameShape(QFrame.StyledPanel)
        self.frame_78asd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_78asd)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.label_159 = QLabel(self.frame_78asd)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMinimumSize(QSize(47, 0))
        self.label_159.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_168.addWidget(self.label_159)

        self.comboBox_default_dataset = QComboBox(self.frame_78asd)
        self.comboBox_default_dataset.setObjectName(u"comboBox_default_dataset")
        self.comboBox_default_dataset.setMinimumSize(QSize(120, 0))
        self.comboBox_default_dataset.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_168.addWidget(self.comboBox_default_dataset)

        self.set_default_database_btn = QPushButton(self.frame_78asd)
        self.set_default_database_btn.setObjectName(u"set_default_database_btn")
        self.set_default_database_btn.setMinimumSize(QSize(67, 0))
        self.set_default_database_btn.setMaximumSize(QSize(50, 16777215))
        self.set_default_database_btn.setStyleSheet(u"color:white;")

        self.horizontalLayout_168.addWidget(self.set_default_database_btn)


        self.horizontalLayout_163.addWidget(self.frame_78asd)


        self.verticalLayout_56.addWidget(self.frame_66)

        self.tableWidget_user_dataset = QTableWidget(self.my_databases)
        if (self.tableWidget_user_dataset.columnCount() < 4):
            self.tableWidget_user_dataset.setColumnCount(4)
        self.tableWidget_user_dataset.setObjectName(u"tableWidget_user_dataset")
        self.tableWidget_user_dataset.setMaximumSize(QSize(16777215, 83))
        self.tableWidget_user_dataset.setColumnCount(4)

        self.verticalLayout_56.addWidget(self.tableWidget_user_dataset)

        self.load_dataset_btn = QPushButton(self.my_databases)
        self.load_dataset_btn.setObjectName(u"load_dataset_btn")
        self.load_dataset_btn.setMaximumSize(QSize(140, 16777215))
        self.load_dataset_btn.setStyleSheet(u"color:white")

        self.verticalLayout_56.addWidget(self.load_dataset_btn)

        self.frame_71 = QFrame(self.my_databases)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.groupBox_4 = QGroupBox(self.frame_71)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(226, 16777215))

        self.horizontalLayout_164.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_71)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_57 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_72 = QFrame(self.groupBox_5)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)

        self.verticalLayout_57.addWidget(self.frame_72)


        self.horizontalLayout_164.addWidget(self.groupBox_5)


        self.verticalLayout_56.addWidget(self.frame_71)

        self.stackedWidget_2.addWidget(self.my_databases)

        self.verticalLayout_54.addWidget(self.stackedWidget_2)


        self.verticalLayout_41.addWidget(self.frame_20)


        self.verticalLayout_27.addWidget(self.frame_16)

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
        self.verticalLayout_44 = QVBoxLayout(self.page_pipeline)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_46 = QFrame(self.page_pipeline)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_46)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_52)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.checkBox_2 = QCheckBox(self.frame_52)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_96.addWidget(self.checkBox_2)

        self.label_12_3 = QLabel(self.frame_52)
        self.label_12_3.setObjectName(u"label_12_3")
        self.label_12_3.setMinimumSize(QSize(80, 25))
        self.label_12_3.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_96.addWidget(self.label_12_3)

        self.comboBox_pbt_binary_algo = QComboBox(self.frame_52)
        self.comboBox_pbt_binary_algo.setObjectName(u"comboBox_pbt_binary_algo")
        self.comboBox_pbt_binary_algo.setMinimumSize(QSize(200, 25))
        self.comboBox_pbt_binary_algo.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_96.addWidget(self.comboBox_pbt_binary_algo)

        self.toolButton = QToolButton(self.frame_52)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_96.addWidget(self.toolButton)


        self.verticalLayout_45.addLayout(self.horizontalLayout_96)

        self.line_10 = QFrame(self.frame_52)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_10)

        self.tableWidget_2 = QTableWidget(self.frame_52)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setColumnCount(10)

        self.verticalLayout_45.addWidget(self.tableWidget_2)

        self.frame_29 = QFrame(self.frame_52)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 29))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_29)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(34, 0))
        self.pushButton_4.setStyleSheet(u"color:white;")

        self.horizontalLayout_28.addWidget(self.pushButton_4)

        self.lineEdit_3 = QLineEdit(self.frame_29)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.lineEdit_3)


        self.verticalLayout_45.addWidget(self.frame_29)


        self.horizontalLayout_29.addWidget(self.frame_52)

        self.line_13 = QFrame(self.frame_46)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_13)

        self.frame_53 = QFrame(self.frame_46)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_53)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.checkBox_3 = QCheckBox(self.frame_53)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_97.addWidget(self.checkBox_3)

        self.label_122 = QLabel(self.frame_53)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(110, 25))
        self.label_122.setMaximumSize(QSize(110, 25))

        self.horizontalLayout_97.addWidget(self.label_122)

        self.comboBox_pbt_local_algo = QComboBox(self.frame_53)
        self.comboBox_pbt_local_algo.setObjectName(u"comboBox_pbt_local_algo")
        self.comboBox_pbt_local_algo.setMinimumSize(QSize(200, 25))
        self.comboBox_pbt_local_algo.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_97.addWidget(self.comboBox_pbt_local_algo)

        self.toolButton_2 = QToolButton(self.frame_53)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_97.addWidget(self.toolButton_2)


        self.verticalLayout_46.addLayout(self.horizontalLayout_97)

        self.line_11 = QFrame(self.frame_53)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_11)

        self.tableWidget_3 = QTableWidget(self.frame_53)
        if (self.tableWidget_3.columnCount() < 10):
            self.tableWidget_3.setColumnCount(10)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setColumnCount(10)

        self.verticalLayout_46.addWidget(self.tableWidget_3)

        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 29))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_55)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(34, 0))
        self.pushButton_5.setStyleSheet(u"color:white;")

        self.horizontalLayout_39.addWidget(self.pushButton_5)

        self.lineEdit_9 = QLineEdit(self.frame_55)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setReadOnly(True)

        self.horizontalLayout_39.addWidget(self.lineEdit_9)


        self.verticalLayout_46.addWidget(self.frame_55)


        self.horizontalLayout_29.addWidget(self.frame_53)

        self.line_39 = QFrame(self.frame_46)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.VLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_39)

        self.frame_54 = QFrame(self.frame_46)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_54)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.checkBox_4 = QCheckBox(self.frame_54)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_98.addWidget(self.checkBox_4)

        self.label_123 = QLabel(self.frame_54)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(120, 25))
        self.label_123.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_98.addWidget(self.label_123)

        self.comboBox_pbt_classification_algo = QComboBox(self.frame_54)
        self.comboBox_pbt_classification_algo.setObjectName(u"comboBox_pbt_classification_algo")
        self.comboBox_pbt_classification_algo.setMinimumSize(QSize(200, 25))
        self.comboBox_pbt_classification_algo.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_98.addWidget(self.comboBox_pbt_classification_algo)

        self.toolButton_3 = QToolButton(self.frame_54)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_98.addWidget(self.toolButton_3)


        self.verticalLayout_47.addLayout(self.horizontalLayout_98)

        self.line_12 = QFrame(self.frame_54)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_12)

        self.tableWidget_4 = QTableWidget(self.frame_54)
        if (self.tableWidget_4.columnCount() < 10):
            self.tableWidget_4.setColumnCount(10)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setColumnCount(10)

        self.verticalLayout_47.addWidget(self.tableWidget_4)

        self.frame_79 = QFrame(self.frame_54)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 29))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_79)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(34, 0))
        self.pushButton_6.setStyleSheet(u"color:white;")

        self.horizontalLayout_40.addWidget(self.pushButton_6)

        self.lineEdit_10 = QLineEdit(self.frame_79)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFrame(True)
        self.lineEdit_10.setReadOnly(True)

        self.horizontalLayout_40.addWidget(self.lineEdit_10)


        self.verticalLayout_47.addWidget(self.frame_79)


        self.horizontalLayout_29.addWidget(self.frame_54)


        self.verticalLayout_44.addWidget(self.frame_46)

        self.frame_80 = QFrame(self.page_pipeline)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(250, 30))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.pushButton_11 = QPushButton(self.frame_80)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(34, 0))
        self.pushButton_11.setStyleSheet(u"color:white;")

        self.horizontalLayout_41.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_80)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(34, 0))
        self.pushButton_10.setStyleSheet(u"color:white;")

        self.horizontalLayout_41.addWidget(self.pushButton_10)


        self.verticalLayout_44.addWidget(self.frame_80, 0, Qt.AlignHCenter)

        self.stackedWidget_pbt.addWidget(self.page_pipeline)
        self.page_load_dataset = QWidget()
        self.page_load_dataset.setObjectName(u"page_load_dataset")
        self.verticalLayout_48 = QVBoxLayout(self.page_load_dataset)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_81 = QFrame(self.page_load_dataset)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMaximumSize(QSize(16777215, 100))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_7 = QGroupBox(self.frame_81)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(800, 0))
        self.groupBox_7.setMaximumSize(QSize(800, 80))
        self.horizontalLayout_53 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_84 = QFrame(self.groupBox_7)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(271, 47))
        self.frame_84.setMaximumSize(QSize(16777215, 56))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, 0)
        self.label_39 = QLabel(self.frame_84)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_42.addWidget(self.label_39)

        self.comboBox_3 = QComboBox(self.frame_84)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(144, 0))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_42.addWidget(self.comboBox_3)

        self.frame_87 = QFrame(self.frame_84)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_87)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.checkBox_6 = QCheckBox(self.frame_87)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_49.addWidget(self.checkBox_6)

        self.checkBox_5 = QCheckBox(self.frame_87)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_49.addWidget(self.checkBox_5)


        self.horizontalLayout_42.addWidget(self.frame_87)

        self.pushButton_12 = QPushButton(self.frame_84)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(48, 0))
        self.pushButton_12.setStyleSheet(u"color:white;")

        self.horizontalLayout_42.addWidget(self.pushButton_12)


        self.horizontalLayout_53.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.groupBox_7)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, 0)
        self.label_40 = QLabel(self.frame_85)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(94, 0))

        self.horizontalLayout_43.addWidget(self.label_40)

        self.lineEdit_5 = QLineEdit(self.frame_85)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_43.addWidget(self.lineEdit_5)

        self.toolButton_4 = QToolButton(self.frame_85)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_43.addWidget(self.toolButton_4)


        self.horizontalLayout_53.addWidget(self.frame_85)


        self.horizontalLayout_72.addWidget(self.groupBox_7)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_41)

        self.groupBox_8 = QGroupBox(self.frame_81)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(331, 0))
        self.groupBox_8.setMaximumSize(QSize(331, 80))
        self.horizontalLayout_67 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_41 = QLabel(self.groupBox_8)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 80))

        self.horizontalLayout_67.addWidget(self.label_41)

        self.comboBox_4 = QComboBox(self.groupBox_8)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_67.addWidget(self.comboBox_4)

        self.pushButton_13 = QPushButton(self.groupBox_8)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(50, 16777215))
        self.pushButton_13.setStyleSheet(u"color:white;")

        self.horizontalLayout_67.addWidget(self.pushButton_13)


        self.horizontalLayout_72.addWidget(self.groupBox_8)


        self.verticalLayout_48.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.page_load_dataset)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(-1, 0, -1, -1)
        self.frame_88 = QFrame(self.frame_82)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(255, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_88)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 16)
        self.groupBox_9 = QGroupBox(self.frame_88)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 100))

        self.verticalLayout_51.addWidget(self.groupBox_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_3)


        self.horizontalLayout_112.addWidget(self.frame_88)

        self.line_63 = QFrame(self.frame_82)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.VLine)
        self.line_63.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_112.addWidget(self.line_63)

        self.frame_86 = QFrame(self.frame_82)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_86)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.dfgdr_2 = QGroupBox(self.frame_86)
        self.dfgdr_2.setObjectName(u"dfgdr_2")
        self.dfgdr_2.setMinimumSize(QSize(0, 100))
        self.dfgdr_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_196 = QHBoxLayout(self.dfgdr_2)
        self.horizontalLayout_196.setSpacing(10)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(10, 10, 10, 10)
        self.binary_list_defect_prev_btn_2 = QPushButton(self.dfgdr_2)
        self.binary_list_defect_prev_btn_2.setObjectName(u"binary_list_defect_prev_btn_2")
        self.binary_list_defect_prev_btn_2.setEnabled(False)
        self.binary_list_defect_prev_btn_2.setMinimumSize(QSize(30, 30))
        self.binary_list_defect_prev_btn_2.setMaximumSize(QSize(30, 30))
        self.binary_list_defect_prev_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_defect_prev_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_defect_prev_btn_2.setIcon(icon16)
        self.binary_list_defect_prev_btn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_196.addWidget(self.binary_list_defect_prev_btn_2)

        self.binary_list_defect_frame_2 = QFrame(self.dfgdr_2)
        self.binary_list_defect_frame_2.setObjectName(u"binary_list_defect_frame_2")
        self.binary_list_defect_frame_2.setFrameShape(QFrame.Panel)
        self.binary_list_defect_frame_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_196.addWidget(self.binary_list_defect_frame_2)

        self.binary_list_defect_next_btn_2 = QPushButton(self.dfgdr_2)
        self.binary_list_defect_next_btn_2.setObjectName(u"binary_list_defect_next_btn_2")
        self.binary_list_defect_next_btn_2.setEnabled(False)
        self.binary_list_defect_next_btn_2.setMinimumSize(QSize(30, 30))
        self.binary_list_defect_next_btn_2.setMaximumSize(QSize(30, 30))
        self.binary_list_defect_next_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_defect_next_btn_2.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_defect_next_btn_2.setIcon(icon15)
        self.binary_list_defect_next_btn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_196.addWidget(self.binary_list_defect_next_btn_2)


        self.verticalLayout_50.addWidget(self.dfgdr_2)

        self.dfg_2 = QGroupBox(self.frame_86)
        self.dfg_2.setObjectName(u"dfg_2")
        self.dfg_2.setMinimumSize(QSize(0, 100))
        self.dfg_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_195 = QHBoxLayout(self.dfg_2)
        self.horizontalLayout_195.setSpacing(10)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(10, 10, 10, 10)
        self.binary_list_perfect_prev_btn_3 = QPushButton(self.dfg_2)
        self.binary_list_perfect_prev_btn_3.setObjectName(u"binary_list_perfect_prev_btn_3")
        self.binary_list_perfect_prev_btn_3.setEnabled(False)
        self.binary_list_perfect_prev_btn_3.setMinimumSize(QSize(30, 30))
        self.binary_list_perfect_prev_btn_3.setMaximumSize(QSize(30, 30))
        self.binary_list_perfect_prev_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_perfect_prev_btn_3.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_perfect_prev_btn_3.setIcon(icon16)
        self.binary_list_perfect_prev_btn_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_195.addWidget(self.binary_list_perfect_prev_btn_3)

        self.binary_list_perfect_frame_3 = QFrame(self.dfg_2)
        self.binary_list_perfect_frame_3.setObjectName(u"binary_list_perfect_frame_3")
        self.binary_list_perfect_frame_3.setFrameShape(QFrame.Panel)
        self.binary_list_perfect_frame_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_195.addWidget(self.binary_list_perfect_frame_3)

        self.binary_list_perfect_next_btn_3 = QPushButton(self.dfg_2)
        self.binary_list_perfect_next_btn_3.setObjectName(u"binary_list_perfect_next_btn_3")
        self.binary_list_perfect_next_btn_3.setEnabled(False)
        self.binary_list_perfect_next_btn_3.setMinimumSize(QSize(30, 30))
        self.binary_list_perfect_next_btn_3.setMaximumSize(QSize(30, 30))
        self.binary_list_perfect_next_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_perfect_next_btn_3.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_perfect_next_btn_3.setIcon(icon15)
        self.binary_list_perfect_next_btn_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_195.addWidget(self.binary_list_perfect_next_btn_3)


        self.verticalLayout_50.addWidget(self.dfg_2)


        self.horizontalLayout_112.addWidget(self.frame_86)


        self.verticalLayout_48.addWidget(self.frame_82)

        self.stackedWidget_pbt.addWidget(self.page_load_dataset)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.verticalLayout_109 = QVBoxLayout(self.page_history)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
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
        self.verticalLayout_53 = QVBoxLayout(self.page_binary_list)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_33 = QFrame(self.page_binary_list)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 200))
        self.frame_33.setMaximumSize(QSize(16777215, 200))
        self.frame_33.setFrameShape(QFrame.Box)
        self.frame_33.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_158_2 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_158_2.setSpacing(10)
        self.horizontalLayout_158_2.setObjectName(u"horizontalLayout_158_2")
        self.horizontalLayout_158_2.setContentsMargins(0, 0, 0, 0)
        self.frame_74_2 = QFrame(self.frame_33)
        self.frame_74_2.setObjectName(u"frame_74_2")
        self.frame_74_2.setFrameShape(QFrame.Panel)
        self.frame_74_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55_2 = QVBoxLayout(self.frame_74_2)
        self.verticalLayout_55_2.setSpacing(0)
        self.verticalLayout_55_2.setObjectName(u"verticalLayout_55_2")
        self.verticalLayout_55_2.setContentsMargins(10, 10, 10, 10)
        self.frame_69_2 = QFrame(self.frame_74_2)
        self.frame_69_2.setObjectName(u"frame_69_2")
        self.frame_69_2.setMinimumSize(QSize(720, 80))
        self.frame_69_2.setMaximumSize(QSize(720, 80))
        self.frame_69_2.setFrameShape(QFrame.StyledPanel)
        self.frame_69_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54_2 = QVBoxLayout(self.frame_69_2)
        self.verticalLayout_54_2.setSpacing(0)
        self.verticalLayout_54_2.setObjectName(u"verticalLayout_54_2")
        self.verticalLayout_54_2.setContentsMargins(0, 0, 0, 0)
        self.frame_71_2 = QFrame(self.frame_69_2)
        self.frame_71_2.setObjectName(u"frame_71_2")
        self.frame_71_2.setMinimumSize(QSize(0, 30))
        self.frame_71_2.setMaximumSize(QSize(16777215, 30))
        self.frame_71_2.setFrameShape(QFrame.StyledPanel)
        self.frame_71_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156_2 = QHBoxLayout(self.frame_71_2)
        self.horizontalLayout_156_2.setSpacing(0)
        self.horizontalLayout_156_2.setObjectName(u"horizontalLayout_156_2")
        self.horizontalLayout_156_2.setContentsMargins(0, 0, 0, 0)
        self.label_11_2 = QLabel(self.frame_71_2)
        self.label_11_2.setObjectName(u"label_11_2")
        self.label_11_2.setMinimumSize(QSize(110, 30))
        self.label_11_2.setMaximumSize(QSize(110, 30))

        self.horizontalLayout_156_2.addWidget(self.label_11_2)

        self.binarylist_dataset_lineedit = QLineEdit(self.frame_71_2)
        self.binarylist_dataset_lineedit.setObjectName(u"binarylist_dataset_lineedit")
        self.binarylist_dataset_lineedit.setEnabled(False)
        self.binarylist_dataset_lineedit.setMinimumSize(QSize(500, 30))
        self.binarylist_dataset_lineedit.setMaximumSize(QSize(500, 30))

        self.horizontalLayout_156_2.addWidget(self.binarylist_dataset_lineedit)

        self.horizontalSpacer_30_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_156_2.addItem(self.horizontalSpacer_30_2)

        self.binary_list_dataset_btn = QPushButton(self.frame_71_2)
        self.binary_list_dataset_btn.setObjectName(u"binary_list_dataset_btn")
        self.binary_list_dataset_btn.setMinimumSize(QSize(100, 30))
        self.binary_list_dataset_btn.setMaximumSize(QSize(100, 30))
        self.binary_list_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_156_2.addWidget(self.binary_list_dataset_btn)


        self.verticalLayout_54_2.addWidget(self.frame_71_2)

        self.frame_72_2 = QFrame(self.frame_69_2)
        self.frame_72_2.setObjectName(u"frame_72_2")
        self.frame_72_2.setMinimumSize(QSize(0, 30))
        self.frame_72_2.setMaximumSize(QSize(16777215, 30))
        self.frame_72_2.setFrameShape(QFrame.StyledPanel)
        self.frame_72_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157_2 = QHBoxLayout(self.frame_72_2)
        self.horizontalLayout_157_2.setSpacing(0)
        self.horizontalLayout_157_2.setObjectName(u"horizontalLayout_157_2")
        self.horizontalLayout_157_2.setContentsMargins(0, 0, 0, 0)
        self.label_12_2 = QLabel(self.frame_72_2)
        self.label_12_2.setObjectName(u"label_12_2")
        self.label_12_2.setMinimumSize(QSize(110, 30))
        self.label_12_2.setMaximumSize(QSize(110, 30))

        self.horizontalLayout_157_2.addWidget(self.label_12_2)

        self.binarylist_dataset_annot_lineedit = QLineEdit(self.frame_72_2)
        self.binarylist_dataset_annot_lineedit.setObjectName(u"binarylist_dataset_annot_lineedit")
        self.binarylist_dataset_annot_lineedit.setEnabled(False)
        self.binarylist_dataset_annot_lineedit.setMinimumSize(QSize(500, 30))
        self.binarylist_dataset_annot_lineedit.setMaximumSize(QSize(500, 30))

        self.horizontalLayout_157_2.addWidget(self.binarylist_dataset_annot_lineedit)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_157_2.addItem(self.horizontalSpacer_19)


        self.verticalLayout_54_2.addWidget(self.frame_72_2)


        self.verticalLayout_55_2.addWidget(self.frame_69_2)

        self.frame_70 = QFrame(self.frame_74_2)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.binary_list_show_btn = QPushButton(self.frame_70)
        self.binary_list_show_btn.setObjectName(u"binary_list_show_btn")
        self.binary_list_show_btn.setMinimumSize(QSize(100, 30))
        self.binary_list_show_btn.setMaximumSize(QSize(100, 30))
        self.binary_list_show_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_154.addWidget(self.binary_list_show_btn)

        self.warning_binarylist_page = QLabel(self.frame_70)
        self.warning_binarylist_page.setObjectName(u"warning_binarylist_page")
        self.warning_binarylist_page.setFrameShape(QFrame.Panel)
        self.warning_binarylist_page.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_154.addWidget(self.warning_binarylist_page)


        self.verticalLayout_55_2.addWidget(self.frame_70)


        self.horizontalLayout_158_2.addWidget(self.frame_74_2)

        self.frame_73_2 = QFrame(self.frame_33)
        self.frame_73_2.setObjectName(u"frame_73_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(100)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_73_2.sizePolicy().hasHeightForWidth())
        self.frame_73_2.setSizePolicy(sizePolicy6)
        self.frame_73_2.setMinimumSize(QSize(0, 0))
        self.frame_73_2.setMaximumSize(QSize(1000000, 16777215))
        self.frame_73_2.setFrameShape(QFrame.Panel)
        self.frame_73_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_158_2.addWidget(self.frame_73_2)


        self.verticalLayout_53.addWidget(self.frame_33)

        self.dfg = QGroupBox(self.page_binary_list)
        self.dfg.setObjectName(u"dfg")
        self.dfg.setMinimumSize(QSize(0, 100))
        self.dfg.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_153 = QHBoxLayout(self.dfg)
        self.horizontalLayout_153.setSpacing(10)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(10, 10, 10, 10)
        self.binary_list_perfect_prev_btn = QPushButton(self.dfg)
        self.binary_list_perfect_prev_btn.setObjectName(u"binary_list_perfect_prev_btn")
        self.binary_list_perfect_prev_btn.setEnabled(False)
        self.binary_list_perfect_prev_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_perfect_prev_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_perfect_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_perfect_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_perfect_prev_btn.setIcon(icon16)
        self.binary_list_perfect_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_153.addWidget(self.binary_list_perfect_prev_btn)

        self.binary_list_perfect_frame = QFrame(self.dfg)
        self.binary_list_perfect_frame.setObjectName(u"binary_list_perfect_frame")
        self.binary_list_perfect_frame.setFrameShape(QFrame.Panel)
        self.binary_list_perfect_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_153.addWidget(self.binary_list_perfect_frame)

        self.binary_list_perfect_next_btn = QPushButton(self.dfg)
        self.binary_list_perfect_next_btn.setObjectName(u"binary_list_perfect_next_btn")
        self.binary_list_perfect_next_btn.setEnabled(False)
        self.binary_list_perfect_next_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_perfect_next_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_perfect_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_perfect_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_perfect_next_btn.setIcon(icon15)
        self.binary_list_perfect_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_153.addWidget(self.binary_list_perfect_next_btn)


        self.verticalLayout_53.addWidget(self.dfg)

        self.dfgdr = QGroupBox(self.page_binary_list)
        self.dfgdr.setObjectName(u"dfgdr")
        self.dfgdr.setMinimumSize(QSize(0, 100))
        self.dfgdr.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_155 = QHBoxLayout(self.dfgdr)
        self.horizontalLayout_155.setSpacing(10)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(10, 10, 10, 10)
        self.binary_list_defect_prev_btn = QPushButton(self.dfgdr)
        self.binary_list_defect_prev_btn.setObjectName(u"binary_list_defect_prev_btn")
        self.binary_list_defect_prev_btn.setEnabled(False)
        self.binary_list_defect_prev_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_defect_prev_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_defect_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_defect_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_defect_prev_btn.setIcon(icon16)
        self.binary_list_defect_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_155.addWidget(self.binary_list_defect_prev_btn)

        self.binary_list_defect_frame = QFrame(self.dfgdr)
        self.binary_list_defect_frame.setObjectName(u"binary_list_defect_frame")
        self.binary_list_defect_frame.setFrameShape(QFrame.Panel)
        self.binary_list_defect_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_155.addWidget(self.binary_list_defect_frame)

        self.binary_list_defect_next_btn = QPushButton(self.dfgdr)
        self.binary_list_defect_next_btn.setObjectName(u"binary_list_defect_next_btn")
        self.binary_list_defect_next_btn.setEnabled(False)
        self.binary_list_defect_next_btn.setMinimumSize(QSize(30, 30))
        self.binary_list_defect_next_btn.setMaximumSize(QSize(30, 30))
        self.binary_list_defect_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_list_defect_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.binary_list_defect_next_btn.setIcon(icon15)
        self.binary_list_defect_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_155.addWidget(self.binary_list_defect_next_btn)


        self.verticalLayout_53.addWidget(self.dfgdr)

        self.stackedWidget_binary.addWidget(self.page_binary_list)
        self.page_binary_training = QWidget()
        self.page_binary_training.setObjectName(u"page_binary_training")
        self.horizontalLayout_85 = QHBoxLayout(self.page_binary_training)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_47 = QFrame(self.page_binary_training)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy7)
        self.frame_47.setMinimumSize(QSize(320, 50))
        self.frame_47.setMaximumSize(QSize(130, 16777215))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_47)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy8)
        self.frame_48.setMinimumSize(QSize(300, 50))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_48)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_137 = QLabel(self.frame_48)
        self.label_137.setObjectName(u"label_137")

        self.horizontalLayout_99.addWidget(self.label_137, 0, Qt.AlignLeft)

        self.b_algorithms = QComboBox(self.frame_48)
        self.b_algorithms.setObjectName(u"b_algorithms")

        self.horizontalLayout_99.addWidget(self.b_algorithms)


        self.verticalLayout_82.addLayout(self.horizontalLayout_99)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.label_144 = QLabel(self.frame_48)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_106.addWidget(self.label_144)

        self.input_size1 = QSpinBox(self.frame_48)
        self.input_size1.setObjectName(u"input_size1")
        self.input_size1.setMinimum(100)
        self.input_size1.setMaximum(1200)

        self.horizontalLayout_106.addWidget(self.input_size1)

        self.input_size2 = QSpinBox(self.frame_48)
        self.input_size2.setObjectName(u"input_size2")
        self.input_size2.setMinimum(100)
        self.input_size2.setMaximum(1920)

        self.horizontalLayout_106.addWidget(self.input_size2)


        self.verticalLayout_82.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_7 = QLabel(self.frame_48)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_81.addWidget(self.label_7)

        self.input_type_resize = QRadioButton(self.frame_48)
        self.input_type_resize.setObjectName(u"input_type_resize")
        self.input_type_resize.setStyleSheet(u"QRadioButton {\n"
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
"	background-color:       black;\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")

        self.horizontalLayout_81.addWidget(self.input_type_resize)

        self.input_type_split = QRadioButton(self.frame_48)
        self.input_type_split.setObjectName(u"input_type_split")
        self.input_type_split.setStyleSheet(u"QRadioButton {\n"
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
"    background-color:       black;\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")

        self.horizontalLayout_81.addWidget(self.input_type_split)


        self.verticalLayout_82.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_138 = QLabel(self.frame_48)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_100.addWidget(self.label_138, 0, Qt.AlignLeft)

        self.b_epochs = QLineEdit(self.frame_48)
        self.b_epochs.setObjectName(u"b_epochs")
        self.b_epochs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_100.addWidget(self.b_epochs)


        self.verticalLayout_82.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.label_139 = QLabel(self.frame_48)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_101.addWidget(self.label_139, 0, Qt.AlignLeft)

        self.b_batch = QLineEdit(self.frame_48)
        self.b_batch.setObjectName(u"b_batch")
        self.b_batch.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_101.addWidget(self.b_batch)


        self.verticalLayout_82.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_140 = QLabel(self.frame_48)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_102.addWidget(self.label_140)

        self.b_lr = QLineEdit(self.frame_48)
        self.b_lr.setObjectName(u"b_lr")
        self.b_lr.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_102.addWidget(self.b_lr)


        self.verticalLayout_82.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_141 = QLabel(self.frame_48)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_103.addWidget(self.label_141)

        self.b_te = QLineEdit(self.frame_48)
        self.b_te.setObjectName(u"b_te")
        self.b_te.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_103.addWidget(self.b_te)


        self.verticalLayout_82.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_142 = QLabel(self.frame_48)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_104.addWidget(self.label_142)

        self.b_vs = QLineEdit(self.frame_48)
        self.b_vs.setObjectName(u"b_vs")
        self.b_vs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_104.addWidget(self.b_vs)


        self.verticalLayout_82.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.label_143 = QLabel(self.frame_48)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_105.addWidget(self.label_143)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_18)

        self.b_select_dp = QPushButton(self.frame_48)
        self.b_select_dp.setObjectName(u"b_select_dp")

        self.horizontalLayout_105.addWidget(self.b_select_dp)


        self.verticalLayout_82.addLayout(self.horizontalLayout_105)

        self.b_dp = QTextEdit(self.frame_48)
        self.b_dp.setObjectName(u"b_dp")
        sizePolicy.setHeightForWidth(self.b_dp.sizePolicy().hasHeightForWidth())
        self.b_dp.setSizePolicy(sizePolicy)
        self.b_dp.setMinimumSize(QSize(20, 20))
        self.b_dp.setMaximumSize(QSize(280, 16777215))
        self.b_dp.setStyleSheet(u"")
        self.b_dp.setReadOnly(True)

        self.verticalLayout_82.addWidget(self.b_dp)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.b_ds_num = QSpinBox(self.frame_48)
        self.b_ds_num.setObjectName(u"b_ds_num")
        self.b_ds_num.setMaximumSize(QSize(120, 16777215))
        self.b_ds_num.setMinimum(1)

        self.horizontalLayout_107.addWidget(self.b_ds_num)

        self.b_delete_ds = QPushButton(self.frame_48)
        self.b_delete_ds.setObjectName(u"b_delete_ds")
        self.b_delete_ds.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_107.addWidget(self.b_delete_ds)

        self.b_add_ds = QPushButton(self.frame_48)
        self.b_add_ds.setObjectName(u"b_add_ds")
        self.b_add_ds.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_107.addWidget(self.b_add_ds)


        self.verticalLayout_82.addLayout(self.horizontalLayout_107)


        self.verticalLayout_81.addWidget(self.frame_48)

        self.b_add_ds_frame = QFrame(self.frame_47)
        self.b_add_ds_frame.setObjectName(u"b_add_ds_frame")
        self.b_add_ds_frame.setMaximumSize(QSize(16777215, 0))
        self.b_add_ds_frame.setFrameShape(QFrame.StyledPanel)
        self.b_add_ds_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.b_add_ds_frame)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.b_add_ds_lineedit = QLineEdit(self.b_add_ds_frame)
        self.b_add_ds_lineedit.setObjectName(u"b_add_ds_lineedit")
        sizePolicy8.setHeightForWidth(self.b_add_ds_lineedit.sizePolicy().hasHeightForWidth())
        self.b_add_ds_lineedit.setSizePolicy(sizePolicy8)
        self.b_add_ds_lineedit.setMaximumSize(QSize(280, 16777215))

        self.verticalLayout_83.addWidget(self.b_add_ds_lineedit)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.b_add_ok = QPushButton(self.b_add_ds_frame)
        self.b_add_ok.setObjectName(u"b_add_ok")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.b_add_ok.sizePolicy().hasHeightForWidth())
        self.b_add_ok.setSizePolicy(sizePolicy9)
        self.b_add_ok.setMinimumSize(QSize(0, 20))
        self.b_add_ok.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_108.addWidget(self.b_add_ok)

        self.b_add_cancel = QPushButton(self.b_add_ds_frame)
        self.b_add_cancel.setObjectName(u"b_add_cancel")
        self.b_add_cancel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_108.addWidget(self.b_add_cancel)


        self.verticalLayout_83.addLayout(self.horizontalLayout_108)


        self.verticalLayout_81.addWidget(self.b_add_ds_frame)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_81.addItem(self.verticalSpacer_10)

        self.frame_15 = QFrame(self.frame_47)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.binary_train = QPushButton(self.frame_15)
        self.binary_train.setObjectName(u"binary_train")
        self.binary_train.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.binary_train.sizePolicy().hasHeightForWidth())
        self.binary_train.setSizePolicy(sizePolicy10)
        self.binary_train.setMinimumSize(QSize(120, 30))
        self.binary_train.setMaximumSize(QSize(180, 16777215))
        self.binary_train.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_train.setAcceptDrops(False)
        self.binary_train.setToolTipDuration(-1)
        self.binary_train.setStyleSheet(u"alignment=QtCore.Qt.AlignCenter")
        self.binary_train.setAutoDefault(False)

        self.horizontalLayout_22.addWidget(self.binary_train)

        self.binary_chart_checkbox = QCheckBox(self.frame_15)
        self.binary_chart_checkbox.setObjectName(u"binary_chart_checkbox")
        self.binary_chart_checkbox.setEnabled(False)
        self.binary_chart_checkbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.binary_chart_checkbox)


        self.verticalLayout_81.addWidget(self.frame_15)

        self.warning_train_page = QLabel(self.frame_47)
        self.warning_train_page.setObjectName(u"warning_train_page")

        self.verticalLayout_81.addWidget(self.warning_train_page)


        self.horizontalLayout_85.addWidget(self.frame_47)

        self.line_33 = QFrame(self.page_binary_training)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.VLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_85.addWidget(self.line_33)

        self.frame_49 = QFrame(self.page_binary_training)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_49)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(9, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_49)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMaximumSize(QSize(16777215, 20))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_68)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(15, 15))
        self.label_12.setPixmap(QPixmap(u"images/train_iamge.jpg"))

        self.horizontalLayout_109.addWidget(self.label_12)

        self.label_8_2 = QLabel(self.frame_68)
        self.label_8_2.setObjectName(u"label_8_2")
        self.label_8_2.setFont(font)

        self.horizontalLayout_109.addWidget(self.label_8_2)

        self.horizontalSpacer_19_3 = QSpacerItem(47, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_19_3)

        self.label_13_2 = QLabel(self.frame_68)
        self.label_13_2.setObjectName(u"label_13_2")
        self.label_13_2.setMaximumSize(QSize(15, 15))
        self.label_13_2.setPixmap(QPixmap(u"images/val_iamge.jpg"))

        self.horizontalLayout_109.addWidget(self.label_13_2)

        self.label_11 = QLabel(self.frame_68)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_109.addWidget(self.label_11)


        self.verticalLayout_96.addWidget(self.frame_68, 0, Qt.AlignHCenter)

        self.frame_42 = QFrame(self.frame_49)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 16777215))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_42)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.binary_chart_recall_frame = QFrame(self.frame_42)
        self.binary_chart_recall_frame.setObjectName(u"binary_chart_recall_frame")
        self.binary_chart_recall_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_recall_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_recall_frame, 2, 0, 1, 1)

        self.binary_chart_loss_frame = QFrame(self.frame_42)
        self.binary_chart_loss_frame.setObjectName(u"binary_chart_loss_frame")
        self.binary_chart_loss_frame.setStyleSheet(u"")
        self.binary_chart_loss_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_loss_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_loss_frame, 0, 0, 1, 1)

        self.binary_chart_acc_frame = QFrame(self.frame_42)
        self.binary_chart_acc_frame.setObjectName(u"binary_chart_acc_frame")
        self.binary_chart_acc_frame.setStyleSheet(u"")
        self.binary_chart_acc_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_acc_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_acc_frame, 0, 1, 1, 1)

        self.binary_chart_prec_frame = QFrame(self.frame_42)
        self.binary_chart_prec_frame.setObjectName(u"binary_chart_prec_frame")
        self.binary_chart_prec_frame.setFrameShape(QFrame.Panel)
        self.binary_chart_prec_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.binary_chart_prec_frame, 2, 1, 1, 1)


        self.verticalLayout_96.addWidget(self.frame_42)

        self.binary_chart_scrollbar = QScrollBar(self.frame_49)
        self.binary_chart_scrollbar.setObjectName(u"binary_chart_scrollbar")
        self.binary_chart_scrollbar.setCursor(QCursor(Qt.OpenHandCursor))
        self.binary_chart_scrollbar.setMaximum(0)
        self.binary_chart_scrollbar.setPageStep(1)
        self.binary_chart_scrollbar.setOrientation(Qt.Horizontal)

        self.verticalLayout_96.addWidget(self.binary_chart_scrollbar)


        self.horizontalLayout_85.addWidget(self.frame_49)

        self.line_29 = QFrame(self.page_binary_training)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.VLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_85.addWidget(self.line_29)

        self.stackedWidget_binary.addWidget(self.page_binary_training)
        self.page_binary_history = QWidget()
        self.page_binary_history.setObjectName(u"page_binary_history")
        self.horizontalLayout_44 = QHBoxLayout(self.page_binary_history)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.groupBox_33 = QGroupBox(self.page_binary_history)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setMinimumSize(QSize(300, 0))
        self.groupBox_33.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_52.setSpacing(7)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_80 = QLabel(self.groupBox_33)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(16777215, 20))
        self.label_80.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_80)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.binary_name_filter_combo = QComboBox(self.groupBox_33)
        self.binary_name_filter_combo.setObjectName(u"binary_name_filter_combo")

        self.horizontalLayout_46.addWidget(self.binary_name_filter_combo)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_46)


        self.verticalLayout_52.addLayout(self.horizontalLayout_45)

        self.line_25 = QFrame(self.groupBox_33)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_25)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.label_81 = QLabel(self.groupBox_33)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font)

        self.horizontalLayout_110.addWidget(self.label_81)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_21)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_111_2 = QHBoxLayout()
        self.horizontalLayout_111_2.setObjectName(u"horizontalLayout_111_2")
        self.label_82 = QLabel(self.groupBox_33)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(16777215, 20))
        self.label_82.setFont(font)

        self.horizontalLayout_111_2.addWidget(self.label_82)

        self.binary_epoch_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_epoch_min_filter_lineedit.setObjectName(u"binary_epoch_min_filter_lineedit")
        self.binary_epoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_epoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_epoch_min_filter_lineedit.setFont(font)

        self.horizontalLayout_111_2.addWidget(self.binary_epoch_min_filter_lineedit)


        self.horizontalLayout_47.addLayout(self.horizontalLayout_111_2)

        self.horizontalLayout_121_2 = QHBoxLayout()
        self.horizontalLayout_121_2.setObjectName(u"horizontalLayout_121_2")
        self.label_83 = QLabel(self.groupBox_33)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMaximumSize(QSize(16777215, 20))
        self.label_83.setFont(font)

        self.horizontalLayout_121_2.addWidget(self.label_83)

        self.binary_epoch_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_epoch_max_filter_lineedit.setObjectName(u"binary_epoch_max_filter_lineedit")
        self.binary_epoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_epoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_epoch_max_filter_lineedit.setFont(font)

        self.horizontalLayout_121_2.addWidget(self.binary_epoch_max_filter_lineedit)


        self.horizontalLayout_47.addLayout(self.horizontalLayout_121_2)


        self.horizontalLayout_110.addLayout(self.horizontalLayout_47)

        self.line_16 = QFrame(self.groupBox_33)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_110.addWidget(self.line_16)


        self.verticalLayout_52.addLayout(self.horizontalLayout_110)

        self.line_17 = QFrame(self.groupBox_33)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_17)

        self.horizontalLayout_122_2 = QHBoxLayout()
        self.horizontalLayout_122_2.setSpacing(0)
        self.horizontalLayout_122_2.setObjectName(u"horizontalLayout_122_2")
        self.label_84 = QLabel(self.groupBox_33)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font)

        self.horizontalLayout_122_2.addWidget(self.label_84)

        self.horizontalSpacer_22_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_122_2.addItem(self.horizontalSpacer_22_2)

        self.horizontalLayout_48_2 = QHBoxLayout()
        self.horizontalLayout_48_2.setSpacing(10)
        self.horizontalLayout_48_2.setObjectName(u"horizontalLayout_48_2")
        self.horizontalLayout_123_2 = QHBoxLayout()
        self.horizontalLayout_123_2.setObjectName(u"horizontalLayout_123_2")
        self.label_85 = QLabel(self.groupBox_33)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(16777215, 20))
        self.label_85.setFont(font)

        self.horizontalLayout_123_2.addWidget(self.label_85)

        self.binary_tepoch_min_filter_lineedit_2 = QLineEdit(self.groupBox_33)
        self.binary_tepoch_min_filter_lineedit_2.setObjectName(u"binary_tepoch_min_filter_lineedit_2")
        self.binary_tepoch_min_filter_lineedit_2.setMinimumSize(QSize(50, 0))
        self.binary_tepoch_min_filter_lineedit_2.setMaximumSize(QSize(50, 30))
        self.binary_tepoch_min_filter_lineedit_2.setFont(font)

        self.horizontalLayout_123_2.addWidget(self.binary_tepoch_min_filter_lineedit_2)


        self.horizontalLayout_48_2.addLayout(self.horizontalLayout_123_2)

        self.horizontalLayout_124_3 = QHBoxLayout()
        self.horizontalLayout_124_3.setObjectName(u"horizontalLayout_124_3")
        self.label_86_2 = QLabel(self.groupBox_33)
        self.label_86_2.setObjectName(u"label_86_2")
        self.label_86_2.setMaximumSize(QSize(16777215, 20))
        self.label_86_2.setFont(font)

        self.horizontalLayout_124_3.addWidget(self.label_86_2)

        self.binary_tepoch_max_filter_lineedit_2 = QLineEdit(self.groupBox_33)
        self.binary_tepoch_max_filter_lineedit_2.setObjectName(u"binary_tepoch_max_filter_lineedit_2")
        self.binary_tepoch_max_filter_lineedit_2.setMinimumSize(QSize(50, 0))
        self.binary_tepoch_max_filter_lineedit_2.setMaximumSize(QSize(50, 30))
        self.binary_tepoch_max_filter_lineedit_2.setFont(font)

        self.horizontalLayout_124_3.addWidget(self.binary_tepoch_max_filter_lineedit_2)


        self.horizontalLayout_48_2.addLayout(self.horizontalLayout_124_3)


        self.horizontalLayout_122_2.addLayout(self.horizontalLayout_48_2)

        self.line_18_2 = QFrame(self.groupBox_33)
        self.line_18_2.setObjectName(u"line_18_2")
        self.line_18_2.setFrameShape(QFrame.HLine)
        self.line_18_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_122_2.addWidget(self.line_18_2)


        self.verticalLayout_52.addLayout(self.horizontalLayout_122_2)

        self.line_47_2 = QFrame(self.groupBox_33)
        self.line_47_2.setObjectName(u"line_47_2")
        self.line_47_2.setFrameShape(QFrame.HLine)
        self.line_47_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_47_2)

        self.horizontalLayout_128_2 = QHBoxLayout()
        self.horizontalLayout_128_2.setSpacing(0)
        self.horizontalLayout_128_2.setObjectName(u"horizontalLayout_128_2")
        self.label_134_2 = QLabel(self.groupBox_33)
        self.label_134_2.setObjectName(u"label_134_2")
        self.label_134_2.setFont(font)

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
        self.label_85_2.setFont(font)

        self.horizontalLayout_123_3.addWidget(self.label_85_2)

        self.binary_tepoch_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_tepoch_min_filter_lineedit.setObjectName(u"binary_tepoch_min_filter_lineedit")
        self.binary_tepoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_tepoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_tepoch_min_filter_lineedit.setFont(font)

        self.horizontalLayout_123_3.addWidget(self.binary_tepoch_min_filter_lineedit)


        self.horizontalLayout_48_3.addLayout(self.horizontalLayout_123_3)

        self.horizontalLayout_124_2 = QHBoxLayout()
        self.horizontalLayout_124_2.setObjectName(u"horizontalLayout_124_2")
        self.label_86 = QLabel(self.groupBox_33)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMaximumSize(QSize(16777215, 20))
        self.label_86.setFont(font)

        self.horizontalLayout_124_2.addWidget(self.label_86)

        self.binary_tepoch_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_tepoch_max_filter_lineedit.setObjectName(u"binary_tepoch_max_filter_lineedit")
        self.binary_tepoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_tepoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_tepoch_max_filter_lineedit.setFont(font)

        self.horizontalLayout_124_2.addWidget(self.binary_tepoch_max_filter_lineedit)


        self.horizontalLayout_48_3.addLayout(self.horizontalLayout_124_2)


        self.horizontalLayout_128_2.addLayout(self.horizontalLayout_48_3)

        self.line_18 = QFrame(self.groupBox_33)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_128_2.addWidget(self.line_18)


        self.verticalLayout_52.addLayout(self.horizontalLayout_128_2)

        self.line_47 = QFrame(self.groupBox_33)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_47)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_134 = QLabel(self.groupBox_33)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font)

        self.horizontalLayout_128.addWidget(self.label_134)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_128.addItem(self.horizontalSpacer_24)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setSpacing(10)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_135 = QLabel(self.groupBox_33)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMaximumSize(QSize(16777215, 20))
        self.label_135.setFont(font)

        self.horizontalLayout_130.addWidget(self.label_135)

        self.binary_batch_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_batch_min_filter_lineedit.setObjectName(u"binary_batch_min_filter_lineedit")
        self.binary_batch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_batch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_batch_min_filter_lineedit.setFont(font)
        self.binary_batch_min_filter_lineedit.setInputMethodHints(Qt.ImhNone)
        self.binary_batch_min_filter_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_130.addWidget(self.binary_batch_min_filter_lineedit)


        self.horizontalLayout_129.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.label_136 = QLabel(self.groupBox_33)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMaximumSize(QSize(16777215, 20))
        self.label_136.setFont(font)

        self.horizontalLayout_131.addWidget(self.label_136)

        self.binary_batch_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_batch_max_filter_lineedit.setObjectName(u"binary_batch_max_filter_lineedit")
        self.binary_batch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_batch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_batch_max_filter_lineedit.setFont(font)

        self.horizontalLayout_131.addWidget(self.binary_batch_max_filter_lineedit)


        self.horizontalLayout_129.addLayout(self.horizontalLayout_131)


        self.horizontalLayout_128.addLayout(self.horizontalLayout_129)

        self.line_40_2 = QFrame(self.groupBox_33)
        self.line_40_2.setObjectName(u"line_40_2")
        self.line_40_2.setFrameShape(QFrame.HLine)
        self.line_40_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_128.addWidget(self.line_40_2)


        self.verticalLayout_52.addLayout(self.horizontalLayout_128)

        self.line_72 = QFrame(self.groupBox_33)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setFrameShape(QFrame.HLine)
        self.line_72.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_72)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.label_87 = QLabel(self.groupBox_33)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font)

        self.horizontalLayout_125.addWidget(self.label_87)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_125.addItem(self.horizontalSpacer_23)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(10)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.label_88 = QLabel(self.groupBox_33)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(16777215, 20))
        self.label_88.setFont(font)

        self.horizontalLayout_126.addWidget(self.label_88)

        self.binary_split_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_split_min_filter_lineedit.setObjectName(u"binary_split_min_filter_lineedit")
        self.binary_split_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_split_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_split_min_filter_lineedit.setFont(font)

        self.horizontalLayout_126.addWidget(self.binary_split_min_filter_lineedit)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_126)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.label_89 = QLabel(self.groupBox_33)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(16777215, 20))
        self.label_89.setFont(font)

        self.horizontalLayout_127.addWidget(self.label_89)

        self.binary_split_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_split_max_filter_lineedit.setObjectName(u"binary_split_max_filter_lineedit")
        self.binary_split_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_split_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_split_max_filter_lineedit.setFont(font)

        self.horizontalLayout_127.addWidget(self.binary_split_max_filter_lineedit)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_127)


        self.horizontalLayout_125.addLayout(self.horizontalLayout_49)

        self.line_33_2 = QFrame(self.groupBox_33)
        self.line_33_2.setObjectName(u"line_33_2")
        self.line_33_2.setFrameShape(QFrame.HLine)
        self.line_33_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_125.addWidget(self.line_33_2)


        self.verticalLayout_52.addLayout(self.horizontalLayout_125)

        self.line_73 = QFrame(self.groupBox_33)
        self.line_73.setObjectName(u"line_73")
        self.line_73.setFrameShape(QFrame.HLine)
        self.line_73.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_73)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.label_109 = QLabel(self.groupBox_33)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font)

        self.horizontalLayout_132.addWidget(self.label_109)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_132.addItem(self.horizontalSpacer_25)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setSpacing(10)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.label_132_2 = QLabel(self.groupBox_33)
        self.label_132_2.setObjectName(u"label_132_2")
        self.label_132_2.setMaximumSize(QSize(16777215, 20))
        self.label_132_2.setFont(font)

        self.horizontalLayout_134.addWidget(self.label_132_2)

        self.binary_loss_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_loss_min_filter_lineedit.setObjectName(u"binary_loss_min_filter_lineedit")
        self.binary_loss_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_loss_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_loss_min_filter_lineedit.setFont(font)

        self.horizontalLayout_134.addWidget(self.binary_loss_min_filter_lineedit)


        self.horizontalLayout_133.addLayout(self.horizontalLayout_134)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.label_133 = QLabel(self.groupBox_33)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMaximumSize(QSize(16777215, 20))
        self.label_133.setFont(font)

        self.horizontalLayout_135.addWidget(self.label_133)

        self.binary_loss_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_loss_max_filter_lineedit.setObjectName(u"binary_loss_max_filter_lineedit")
        self.binary_loss_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_loss_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_loss_max_filter_lineedit.setFont(font)

        self.horizontalLayout_135.addWidget(self.binary_loss_max_filter_lineedit)


        self.horizontalLayout_133.addLayout(self.horizontalLayout_135)


        self.horizontalLayout_132.addLayout(self.horizontalLayout_133)

        self.line_42 = QFrame(self.groupBox_33)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.HLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_132.addWidget(self.line_42)


        self.verticalLayout_52.addLayout(self.horizontalLayout_132)

        self.line_74 = QFrame(self.groupBox_33)
        self.line_74.setObjectName(u"line_74")
        self.line_74.setFrameShape(QFrame.HLine)
        self.line_74.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_74)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_145 = QLabel(self.groupBox_33)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font)

        self.horizontalLayout_136.addWidget(self.label_145)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_26)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setSpacing(10)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.label_146 = QLabel(self.groupBox_33)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMaximumSize(QSize(16777215, 20))
        self.label_146.setFont(font)

        self.horizontalLayout_138.addWidget(self.label_146)

        self.binary_acc_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_acc_min_filter_lineedit.setObjectName(u"binary_acc_min_filter_lineedit")
        self.binary_acc_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_acc_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_acc_min_filter_lineedit.setFont(font)

        self.horizontalLayout_138.addWidget(self.binary_acc_min_filter_lineedit)


        self.horizontalLayout_137.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_147 = QLabel(self.groupBox_33)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMaximumSize(QSize(16777215, 20))
        self.label_147.setFont(font)

        self.horizontalLayout_139.addWidget(self.label_147)

        self.binary_acc_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_acc_max_filter_lineedit.setObjectName(u"binary_acc_max_filter_lineedit")
        self.binary_acc_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_acc_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_acc_max_filter_lineedit.setFont(font)

        self.horizontalLayout_139.addWidget(self.binary_acc_max_filter_lineedit)


        self.horizontalLayout_137.addLayout(self.horizontalLayout_139)


        self.horizontalLayout_136.addLayout(self.horizontalLayout_137)

        self.line_43 = QFrame(self.groupBox_33)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_136.addWidget(self.line_43)


        self.verticalLayout_52.addLayout(self.horizontalLayout_136)

        self.line_75 = QFrame(self.groupBox_33)
        self.line_75.setObjectName(u"line_75")
        self.line_75.setFrameShape(QFrame.HLine)
        self.line_75.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_75)

        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.label_148 = QLabel(self.groupBox_33)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font)

        self.horizontalLayout_140.addWidget(self.label_148)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_140.addItem(self.horizontalSpacer_27)

        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setSpacing(10)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_149 = QLabel(self.groupBox_33)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMaximumSize(QSize(16777215, 20))
        self.label_149.setFont(font)

        self.horizontalLayout_142.addWidget(self.label_149)

        self.binary_prec_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_prec_min_filter_lineedit.setObjectName(u"binary_prec_min_filter_lineedit")
        self.binary_prec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_prec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_prec_min_filter_lineedit.setFont(font)

        self.horizontalLayout_142.addWidget(self.binary_prec_min_filter_lineedit)


        self.horizontalLayout_141.addLayout(self.horizontalLayout_142)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.label_150 = QLabel(self.groupBox_33)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMaximumSize(QSize(16777215, 20))
        self.label_150.setFont(font)

        self.horizontalLayout_143.addWidget(self.label_150)

        self.binary_prec_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_prec_max_filter_lineedit.setObjectName(u"binary_prec_max_filter_lineedit")
        self.binary_prec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_prec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_prec_max_filter_lineedit.setFont(font)

        self.horizontalLayout_143.addWidget(self.binary_prec_max_filter_lineedit)


        self.horizontalLayout_141.addLayout(self.horizontalLayout_143)


        self.horizontalLayout_140.addLayout(self.horizontalLayout_141)

        self.line_44 = QFrame(self.groupBox_33)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.HLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_140.addWidget(self.line_44)


        self.verticalLayout_52.addLayout(self.horizontalLayout_140)

        self.line_76 = QFrame(self.groupBox_33)
        self.line_76.setObjectName(u"line_76")
        self.line_76.setFrameShape(QFrame.HLine)
        self.line_76.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_76)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setSpacing(0)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_151 = QLabel(self.groupBox_33)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font)

        self.horizontalLayout_144.addWidget(self.label_151)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_28)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setSpacing(10)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_152 = QLabel(self.groupBox_33)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMaximumSize(QSize(16777215, 20))
        self.label_152.setFont(font)

        self.horizontalLayout_146.addWidget(self.label_152)

        self.binary_rec_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_rec_min_filter_lineedit.setObjectName(u"binary_rec_min_filter_lineedit")
        self.binary_rec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_rec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_rec_min_filter_lineedit.setFont(font)

        self.horizontalLayout_146.addWidget(self.binary_rec_min_filter_lineedit)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_146)

        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_153 = QLabel(self.groupBox_33)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMaximumSize(QSize(16777215, 20))
        self.label_153.setFont(font)

        self.horizontalLayout_147.addWidget(self.label_153)

        self.binary_rec_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_rec_max_filter_lineedit.setObjectName(u"binary_rec_max_filter_lineedit")
        self.binary_rec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_rec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_rec_max_filter_lineedit.setFont(font)

        self.horizontalLayout_147.addWidget(self.binary_rec_max_filter_lineedit)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_147)


        self.horizontalLayout_144.addLayout(self.horizontalLayout_145)

        self.line_45 = QFrame(self.groupBox_33)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_144.addWidget(self.line_45)


        self.verticalLayout_52.addLayout(self.horizontalLayout_144)

        self.line_77 = QFrame(self.groupBox_33)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setFrameShape(QFrame.HLine)
        self.line_77.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_77)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_154 = QLabel(self.groupBox_33)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font)

        self.horizontalLayout_148.addWidget(self.label_154)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_29)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setSpacing(10)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_155 = QLabel(self.groupBox_33)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMaximumSize(QSize(16777215, 20))
        self.label_155.setFont(font)

        self.horizontalLayout_150.addWidget(self.label_155)

        self.binary_date_min_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_date_min_filter_lineedit.setObjectName(u"binary_date_min_filter_lineedit")
        self.binary_date_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_date_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_date_min_filter_lineedit.setFont(font)

        self.horizontalLayout_150.addWidget(self.binary_date_min_filter_lineedit)


        self.horizontalLayout_149.addLayout(self.horizontalLayout_150)

        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.label_156 = QLabel(self.groupBox_33)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMaximumSize(QSize(16777215, 20))
        self.label_156.setFont(font)

        self.horizontalLayout_151.addWidget(self.label_156)

        self.binary_date_max_filter_lineedit = QLineEdit(self.groupBox_33)
        self.binary_date_max_filter_lineedit.setObjectName(u"binary_date_max_filter_lineedit")
        self.binary_date_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.binary_date_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.binary_date_max_filter_lineedit.setFont(font)

        self.horizontalLayout_151.addWidget(self.binary_date_max_filter_lineedit)


        self.horizontalLayout_149.addLayout(self.horizontalLayout_151)


        self.horizontalLayout_148.addLayout(self.horizontalLayout_149)

        self.line_46 = QFrame(self.groupBox_33)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.HLine)
        self.line_46.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_148.addWidget(self.line_46)


        self.verticalLayout_52.addLayout(self.horizontalLayout_148)

        self.line_96 = QFrame(self.groupBox_33)
        self.line_96.setObjectName(u"line_96")
        self.line_96.setFrameShape(QFrame.HLine)
        self.line_96.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_96)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setSpacing(20)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.binary_filter_btn = QPushButton(self.groupBox_33)
        self.binary_filter_btn.setObjectName(u"binary_filter_btn")
        self.binary_filter_btn.setMinimumSize(QSize(0, 30))
        self.binary_filter_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_152.addWidget(self.binary_filter_btn)

        self.binary_clearfilter_btn = QPushButton(self.groupBox_33)
        self.binary_clearfilter_btn.setObjectName(u"binary_clearfilter_btn")
        self.binary_clearfilter_btn.setMinimumSize(QSize(0, 30))
        self.binary_clearfilter_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_152.addWidget(self.binary_clearfilter_btn)


        self.verticalLayout_52.addLayout(self.horizontalLayout_152)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_5)


        self.horizontalLayout_44.addWidget(self.groupBox_33)

        self.line_14 = QFrame(self.page_binary_history)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_44.addWidget(self.line_14)

        self.frame_31 = QFrame(self.page_binary_history)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97_2 = QVBoxLayout(self.frame_31)
        self.verticalLayout_97_2.setObjectName(u"verticalLayout_97_2")
        self.binary_history_tabel = QTableWidget(self.frame_31)
        if (self.binary_history_tabel.columnCount() < 19):
            self.binary_history_tabel.setColumnCount(19)
        self.binary_history_tabel.setObjectName(u"binary_history_tabel")
        self.binary_history_tabel.setRowCount(0)
        self.binary_history_tabel.setColumnCount(19)
        self.binary_history_tabel.horizontalHeader().setMinimumSectionSize(120)
        self.binary_history_tabel.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_97_2.addWidget(self.binary_history_tabel)

        self.frame_68_2 = QFrame(self.frame_31)
        self.frame_68_2.setObjectName(u"frame_68_2")
        self.frame_68_2.setFrameShape(QFrame.StyledPanel)
        self.frame_68_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109_2 = QHBoxLayout(self.frame_68_2)
        self.horizontalLayout_109_2.setObjectName(u"horizontalLayout_109_2")
        self.binary_table_refresh_btn = QPushButton(self.frame_68_2)
        self.binary_table_refresh_btn.setObjectName(u"binary_table_refresh_btn")
        self.binary_table_refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_table_refresh_btn.setLayoutDirection(Qt.RightToLeft)
        self.binary_table_refresh_btn.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        icon25 = QIcon()
        icon25.addFile(u"images/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.binary_table_refresh_btn.setIcon(icon25)
        self.binary_table_refresh_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_109_2.addWidget(self.binary_table_refresh_btn)

        self.line_50 = QFrame(self.frame_68_2)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.VLine)
        self.line_50.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_109_2.addWidget(self.line_50)

        self.binary_tabel_prev = QPushButton(self.frame_68_2)
        self.binary_tabel_prev.setObjectName(u"binary_tabel_prev")
        self.binary_tabel_prev.setEnabled(False)
        self.binary_tabel_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_tabel_prev.setLayoutDirection(Qt.LeftToRight)
        self.binary_tabel_prev.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.binary_tabel_prev.setIcon(icon16)
        self.binary_tabel_prev.setIconSize(QSize(30, 30))

        self.horizontalLayout_109_2.addWidget(self.binary_tabel_prev)

        self.binary_tabel_page = QLineEdit(self.frame_68_2)
        self.binary_tabel_page.setObjectName(u"binary_tabel_page")
        self.binary_tabel_page.setEnabled(False)
        self.binary_tabel_page.setMinimumSize(QSize(50, 30))
        self.binary_tabel_page.setMaximumSize(QSize(50, 30))
        self.binary_tabel_page.setStyleSheet(u"padding:0;")
        self.binary_tabel_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109_2.addWidget(self.binary_tabel_page)

        self.binary_tabel_next = QPushButton(self.frame_68_2)
        self.binary_tabel_next.setObjectName(u"binary_tabel_next")
        self.binary_tabel_next.setEnabled(True)
        self.binary_tabel_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.binary_tabel_next.setStyleSheet(u"background-color: Transparent;\n"
"border : 0px;\n"
"color : rgb(0,0,0);")
        self.binary_tabel_next.setIcon(icon15)
        self.binary_tabel_next.setIconSize(QSize(30, 30))

        self.horizontalLayout_109_2.addWidget(self.binary_tabel_next)

        self.line_51 = QFrame(self.frame_68_2)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.VLine)
        self.line_51.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_109_2.addWidget(self.line_51)

        self.binary_tabel_label = QLabel(self.frame_68_2)
        self.binary_tabel_label.setObjectName(u"binary_tabel_label")
        self.binary_tabel_label.setMinimumSize(QSize(300, 0))
        self.binary_tabel_label.setMaximumSize(QSize(300, 16777215))
        self.binary_tabel_label.setFrameShape(QFrame.Panel)
        self.binary_tabel_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_109_2.addWidget(self.binary_tabel_label)

        self.horizontalSpacer_20_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109_2.addItem(self.horizontalSpacer_20_2)


        self.verticalLayout_97_2.addWidget(self.frame_68_2)


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

        self.l_alghorithms = QComboBox(self.frame_38)
        self.l_alghorithms.setObjectName(u"l_alghorithms")

        self.horizontalLayout_73.addWidget(self.l_alghorithms)


        self.verticalLayout_73.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_102 = QLabel(self.frame_38)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_74.addWidget(self.label_102, 0, Qt.AlignLeft)

        self.l_epochs = QLineEdit(self.frame_38)
        self.l_epochs.setObjectName(u"l_epochs")
        self.l_epochs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_74.addWidget(self.l_epochs)


        self.verticalLayout_73.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_103 = QLabel(self.frame_38)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_75.addWidget(self.label_103, 0, Qt.AlignLeft)

        self.l_batch = QLineEdit(self.frame_38)
        self.l_batch.setObjectName(u"l_batch")
        self.l_batch.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_75.addWidget(self.l_batch)


        self.verticalLayout_73.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_104 = QLabel(self.frame_38)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_76.addWidget(self.label_104)

        self.l_lr = QLineEdit(self.frame_38)
        self.l_lr.setObjectName(u"l_lr")
        self.l_lr.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_76.addWidget(self.l_lr)


        self.verticalLayout_73.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_105 = QLabel(self.frame_38)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_77.addWidget(self.label_105)

        self.l_te = QLineEdit(self.frame_38)
        self.l_te.setObjectName(u"l_te")
        self.l_te.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_77.addWidget(self.l_te)


        self.verticalLayout_73.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_106 = QLabel(self.frame_38)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_78.addWidget(self.label_106)

        self.l_vs = QLineEdit(self.frame_38)
        self.l_vs.setObjectName(u"l_vs")
        self.l_vs.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_78.addWidget(self.l_vs)


        self.verticalLayout_73.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_107 = QLabel(self.frame_38)
        self.label_107.setObjectName(u"label_107")

        self.horizontalLayout_79.addWidget(self.label_107)

        self.l_ip = QLineEdit(self.frame_38)
        self.l_ip.setObjectName(u"l_ip")
        self.l_ip.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_79.addWidget(self.l_ip)


        self.verticalLayout_73.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_108 = QLabel(self.frame_38)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_80.addWidget(self.label_108)

        self.l_lp = QLineEdit(self.frame_38)
        self.l_lp.setObjectName(u"l_lp")
        self.l_lp.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_80.addWidget(self.l_lp)


        self.verticalLayout_73.addLayout(self.horizontalLayout_80)


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
        self.label_111_2 = QLabel(self.frame_39)
        self.label_111_2.setObjectName(u"label_111_2")

        self.horizontalLayout_61.addWidget(self.label_111_2)

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

        self.localization_train = QPushButton(self.frame_37)
        self.localization_train.setObjectName(u"localization_train")
        self.localization_train.setMinimumSize(QSize(180, 30))
        self.localization_train.setMaximumSize(QSize(180, 16777215))
        self.localization_train.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_72.addWidget(self.localization_train, 0, Qt.AlignHCenter)


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
        self.verticalLayout_58 = QVBoxLayout(self.page_classification_class_list)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_21 = QFrame(self.page_classification_class_list)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_21)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_9)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.classes_table = QTableWidget(self.frame_9)
        if (self.classes_table.columnCount() < 8):
            self.classes_table.setColumnCount(8)
        self.classes_table.setObjectName(u"classes_table")
        self.classes_table.setMinimumSize(QSize(0, 0))
        self.classes_table.setMaximumSize(QSize(16777215, 16777215))
        self.classes_table.setStyleSheet(u"	background-color: Transparent;")
        self.classes_table.setLineWidth(1)
        self.classes_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.classes_table.setRowCount(0)
        self.classes_table.setColumnCount(8)
        self.classes_table.horizontalHeader().setMinimumSectionSize(150)
        self.classes_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_28.addWidget(self.classes_table)


        self.horizontalLayout_16.addWidget(self.frame_9)

        self.frame_14 = QFrame(self.frame_21)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(300, 0))
        self.frame_14.setMaximumSize(QSize(300, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_14)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.groupBox_21 = QGroupBox(self.frame_14)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(300, 200))
        self.groupBox_21.setMaximumSize(QSize(300, 200))
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.line_7 = QFrame(self.groupBox_21)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_7)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_35 = QLabel(self.groupBox_21)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(100, 26))
        self.label_35.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_23.addWidget(self.label_35)

        self.lineEdit_2 = QLineEdit(self.groupBox_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_23.addWidget(self.lineEdit_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_36 = QLabel(self.groupBox_21)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 26))
        self.label_36.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.label_36)

        self.comboBox_11 = QComboBox(self.groupBox_21)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.horizontalLayout_25.addWidget(self.comboBox_11)


        self.verticalLayout_30.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_42 = QLabel(self.groupBox_21)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(100, 26))
        self.label_42.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_31.addWidget(self.label_42)

        self.lineEdit_4 = QLineEdit(self.groupBox_21)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_31.addWidget(self.lineEdit_4)


        self.verticalLayout_30.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_37 = QLabel(self.groupBox_21)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(100, 26))
        self.label_37.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_26.addWidget(self.label_37)

        self.comboBox_2 = QComboBox(self.groupBox_21)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_26.addWidget(self.comboBox_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_26)

        self.line_37 = QFrame(self.groupBox_21)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_37)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.classification_add_new_class = QPushButton(self.groupBox_21)
        self.classification_add_new_class.setObjectName(u"classification_add_new_class")
        self.classification_add_new_class.setMinimumSize(QSize(120, 30))
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

        self.classification_add_new_class_2 = QPushButton(self.groupBox_21)
        self.classification_add_new_class_2.setObjectName(u"classification_add_new_class_2")
        self.classification_add_new_class_2.setMinimumSize(QSize(120, 30))
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


        self.verticalLayout_30.addLayout(self.horizontalLayout_30)


        self.verticalLayout_29.addWidget(self.groupBox_21)

        self.groupBox_6 = QGroupBox(self.frame_14)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_59 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.classlist_show_related_img_btn = QPushButton(self.groupBox_6)
        self.classlist_show_related_img_btn.setObjectName(u"classlist_show_related_img_btn")
        self.classlist_show_related_img_btn.setMinimumSize(QSize(120, 30))
        self.classlist_show_related_img_btn.setMaximumSize(QSize(70, 16777215))
        self.classlist_show_related_img_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_32.addWidget(self.classlist_show_related_img_btn)

        self.classification_add_new_class_4 = QPushButton(self.groupBox_6)
        self.classification_add_new_class_4.setObjectName(u"classification_add_new_class_4")
        self.classification_add_new_class_4.setMinimumSize(QSize(120, 30))
        self.classification_add_new_class_4.setMaximumSize(QSize(70, 16777215))
        self.classification_add_new_class_4.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_32.addWidget(self.classification_add_new_class_4)


        self.verticalLayout_59.addLayout(self.horizontalLayout_32)

        self.classlist_msg_label = QLabel(self.groupBox_6)
        self.classlist_msg_label.setObjectName(u"classlist_msg_label")
        self.classlist_msg_label.setMinimumSize(QSize(0, 30))
        self.classlist_msg_label.setMaximumSize(QSize(16777215, 30))
        self.classlist_msg_label.setFrameShape(QFrame.Panel)
        self.classlist_msg_label.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_59.addWidget(self.classlist_msg_label)


        self.verticalLayout_29.addWidget(self.groupBox_6)


        self.horizontalLayout_16.addWidget(self.frame_14)


        self.verticalLayout_58.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.page_classification_class_list)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 100))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.classlist_prev_btn = QPushButton(self.frame_22)
        self.classlist_prev_btn.setObjectName(u"classlist_prev_btn")
        self.classlist_prev_btn.setEnabled(False)
        self.classlist_prev_btn.setMinimumSize(QSize(30, 30))
        self.classlist_prev_btn.setMaximumSize(QSize(30, 30))
        self.classlist_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.classlist_prev_btn.setIcon(icon16)
        self.classlist_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.classlist_prev_btn)

        self.class_list_slider_frame = QLabel(self.frame_22)
        self.class_list_slider_frame.setObjectName(u"class_list_slider_frame")
        self.class_list_slider_frame.setFrameShape(QFrame.Panel)
        self.class_list_slider_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.class_list_slider_frame)

        self.classlist_next_btn = QPushButton(self.frame_22)
        self.classlist_next_btn.setObjectName(u"classlist_next_btn")
        self.classlist_next_btn.setEnabled(False)
        self.classlist_next_btn.setMinimumSize(QSize(30, 30))
        self.classlist_next_btn.setMaximumSize(QSize(30, 30))
        self.classlist_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent;")
        self.classlist_next_btn.setIcon(icon15)
        self.classlist_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.classlist_next_btn)


        self.verticalLayout_58.addWidget(self.frame_22)

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
        self.frame_23.setMinimumSize(QSize(0, 310))
        self.frame_23.setMaximumSize(QSize(310, 16777215))
        self.frame_23.setFrameShape(QFrame.Panel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_23)
        self.verticalLayout_31.setSpacing(2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(290, 200))
        self.frame_25.setMaximumSize(QSize(290, 16777215))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_25)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, -1, -1, 0)
        self.label_67 = QLabel(self.frame_25)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 25))
        self.label_67.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_64.addWidget(self.label_67, 0, Qt.AlignLeft)

        self.classification_algo_combo = QComboBox(self.frame_25)
        self.classification_algo_combo.setObjectName(u"classification_algo_combo")
        self.classification_algo_combo.setMinimumSize(QSize(120, 25))
        self.classification_algo_combo.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_64.addWidget(self.classification_algo_combo)


        self.verticalLayout_32.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_72 = QLabel(self.frame_25)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 25))
        self.label_72.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_69.addWidget(self.label_72, 0, Qt.AlignLeft)

        self.class_epoch_lineedit = QLineEdit(self.frame_25)
        self.class_epoch_lineedit.setObjectName(u"class_epoch_lineedit")
        self.class_epoch_lineedit.setMinimumSize(QSize(0, 25))
        self.class_epoch_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_69.addWidget(self.class_epoch_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_74 = QLabel(self.frame_25)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 25))
        self.label_74.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_71.addWidget(self.label_74, 0, Qt.AlignLeft)

        self.class_batch_lineedit = QLineEdit(self.frame_25)
        self.class_batch_lineedit.setObjectName(u"class_batch_lineedit")
        self.class_batch_lineedit.setMinimumSize(QSize(0, 25))
        self.class_batch_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_71.addWidget(self.class_batch_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_69 = QLabel(self.frame_25)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 25))
        self.label_69.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_66.addWidget(self.label_69)

        self.class_lr_lineedit = QLineEdit(self.frame_25)
        self.class_lr_lineedit.setObjectName(u"class_lr_lineedit")
        self.class_lr_lineedit.setMinimumSize(QSize(0, 25))
        self.class_lr_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_66.addWidget(self.class_lr_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_71 = QLabel(self.frame_25)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 25))
        self.label_71.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_68.addWidget(self.label_71)

        self.class_tepoch_lineedit = QLineEdit(self.frame_25)
        self.class_tepoch_lineedit.setObjectName(u"class_tepoch_lineedit")
        self.class_tepoch_lineedit.setMinimumSize(QSize(0, 25))
        self.class_tepoch_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_68.addWidget(self.class_tepoch_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_68 = QLabel(self.frame_25)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(0, 25))
        self.label_68.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_65.addWidget(self.label_68)

        self.class_split_lineedit = QLineEdit(self.frame_25)
        self.class_split_lineedit.setObjectName(u"class_split_lineedit")
        self.class_split_lineedit.setMinimumSize(QSize(0, 25))
        self.class_split_lineedit.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_65.addWidget(self.class_split_lineedit)


        self.verticalLayout_32.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_73 = QLabel(self.frame_25)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(0, 25))
        self.label_73.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_70.addWidget(self.label_73)

        self.pushButton_22 = QPushButton(self.frame_25)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(100, 25))
        self.pushButton_22.setMaximumSize(QSize(100, 25))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_70.addWidget(self.pushButton_22)


        self.verticalLayout_32.addLayout(self.horizontalLayout_70)

        self.textEdit = QTextEdit(self.frame_25)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_32.addWidget(self.textEdit)


        self.verticalLayout_31.addWidget(self.frame_25, 0, Qt.AlignLeft)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(290, 0))
        self.frame_26.setMaximumSize(QSize(290, 16777215))
        self.frame_26.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_26)
        self.verticalLayout_40.setSpacing(0)
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
        self.table_classification_select_class.setObjectName(u"table_classification_select_class")
        self.table_classification_select_class.setRowCount(0)
        self.table_classification_select_class.setColumnCount(3)

        self.verticalLayout_40.addWidget(self.table_classification_select_class)


        self.verticalLayout_31.addWidget(self.frame_26)

        self.line_6 = QFrame(self.frame_23)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_6)

        self.frame_78 = QFrame(self.frame_23)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.Panel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.class_check_train_btn = QPushButton(self.frame_78)
        self.class_check_train_btn.setObjectName(u"class_check_train_btn")
        self.class_check_train_btn.setMinimumSize(QSize(120, 25))
        self.class_check_train_btn.setMaximumSize(QSize(120, 25))
        self.class_check_train_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.class_check_train_btn)

        self.pushButton_18 = QPushButton(self.frame_78)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setMinimumSize(QSize(120, 25))
        self.pushButton_18.setMaximumSize(QSize(120, 25))
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.pushButton_18)


        self.verticalLayout_31.addWidget(self.frame_78)

        self.classification_train_msg_label = QLabel(self.frame_23)
        self.classification_train_msg_label.setObjectName(u"classification_train_msg_label")
        self.classification_train_msg_label.setMinimumSize(QSize(0, 25))
        self.classification_train_msg_label.setMaximumSize(QSize(16777215, 25))
        self.classification_train_msg_label.setFrameShape(QFrame.Panel)
        self.classification_train_msg_label.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.classification_train_msg_label)


        self.horizontalLayout_33.addWidget(self.frame_23)

        self.line_8 = QFrame(self.page_classification_training)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_33.addWidget(self.line_8)

        self.frame_24 = QFrame(self.page_classification_training)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Box)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_24)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cls_chart_recall_frame = QFrame(self.frame_24)
        self.cls_chart_recall_frame.setObjectName(u"cls_chart_recall_frame")
        self.cls_chart_recall_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_recall_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_recall_frame, 2, 0, 1, 1)

        self.cls_chart_acc_frame = QFrame(self.frame_24)
        self.cls_chart_acc_frame.setObjectName(u"cls_chart_acc_frame")
        self.cls_chart_acc_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_acc_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_acc_frame, 1, 1, 1, 1)

        self.cls_chart_prec_frame = QFrame(self.frame_24)
        self.cls_chart_prec_frame.setObjectName(u"cls_chart_prec_frame")
        self.cls_chart_prec_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_prec_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_prec_frame, 2, 1, 1, 1)

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
        self.horizontalSpacer_221234 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_221234)

        self.label_83543 = QLabel(self.frame_83)
        self.label_83543.setObjectName(u"label_83543")
        self.label_83543.setMinimumSize(QSize(15, 15))
        self.label_83543.setMaximumSize(QSize(15, 15))
        self.label_83543.setPixmap(QPixmap(u"images/train_iamge.jpg"))
        self.label_83543.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_83543)

        self.label_31 = QLabel(self.frame_83)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 15))
        self.label_31.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_27.addWidget(self.label_31)

        self.horizontalSpacer_3212342 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_3212342)

        self.label_32 = QLabel(self.frame_83)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(15, 15))
        self.label_32.setMaximumSize(QSize(15, 15))
        self.label_32.setPixmap(QPixmap(u"images/val_iamge.jpg"))

        self.horizontalLayout_27.addWidget(self.label_32)

        self.label_34 = QLabel(self.frame_83)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 15))
        self.label_34.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_27.addWidget(self.label_34)

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


        self.gridLayout_4.addWidget(self.frame_83, 0, 0, 1, 2)

        self.cls_chart_loss_frame = QFrame(self.frame_24)
        self.cls_chart_loss_frame.setObjectName(u"cls_chart_loss_frame")
        self.cls_chart_loss_frame.setFrameShape(QFrame.Panel)
        self.cls_chart_loss_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.cls_chart_loss_frame, 1, 0, 1, 1)

        self.cls_chart_scrollbar = QScrollBar(self.frame_24)
        self.cls_chart_scrollbar.setObjectName(u"cls_chart_scrollbar")
        self.cls_chart_scrollbar.setCursor(QCursor(Qt.OpenHandCursor))
        self.cls_chart_scrollbar.setMaximum(0)
        self.cls_chart_scrollbar.setPageStep(1)
        self.cls_chart_scrollbar.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.cls_chart_scrollbar, 3, 0, 1, 2)


        self.horizontalLayout_33.addWidget(self.frame_24)

        self.stackedWidget_classification.addWidget(self.page_classification_training)
        self.page_classification_history = QWidget()
        self.page_classification_history.setObjectName(u"page_classification_history")
        self.horizontalLayout_38 = QHBoxLayout(self.page_classification_history)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_28 = QFrame(self.page_classification_history)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(300, 0))
        self.frame_28.setMaximumSize(QSize(300, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_28)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.groupBox_34 = QGroupBox(self.frame_28)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setMinimumSize(QSize(300, 0))
        self.groupBox_34.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_60 = QVBoxLayout(self.groupBox_34)
        self.verticalLayout_60.setSpacing(5)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_1593243 = QLabel(self.groupBox_34)
        self.label_1593243.setObjectName(u"label_1593243")
        self.label_1593243.setMaximumSize(QSize(16777215, 20))
        self.label_1593243.setFont(font)

        self.horizontalLayout_48.addWidget(self.label_1593243)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.cls_name_filter_combo = QComboBox(self.groupBox_34)
        self.cls_name_filter_combo.setObjectName(u"cls_name_filter_combo")

        self.horizontalLayout_50.addWidget(self.cls_name_filter_combo)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_50)


        self.verticalLayout_60.addLayout(self.horizontalLayout_48)

        self.line_26 = QFrame(self.groupBox_34)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_26)

        self.horizontalLayout_165123 = QHBoxLayout()
        self.horizontalLayout_165123.setSpacing(0)
        self.horizontalLayout_165123.setObjectName(u"horizontalLayout_165123")
        self.label_160 = QLabel(self.groupBox_34)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font)

        self.horizontalLayout_165123.addWidget(self.label_160)

        self.horizontalSpacer_3312321 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_165123.addItem(self.horizontalSpacer_3312321)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_111_3 = QHBoxLayout()
        self.horizontalLayout_111_3.setObjectName(u"horizontalLayout_111_3")
        self.label_161 = QLabel(self.groupBox_34)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMaximumSize(QSize(16777215, 20))
        self.label_161.setFont(font)

        self.horizontalLayout_111_3.addWidget(self.label_161)

        self.cls_epoch_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_epoch_min_filter_lineedit.setObjectName(u"cls_epoch_min_filter_lineedit")
        self.cls_epoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_epoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_epoch_min_filter_lineedit.setFont(font)

        self.horizontalLayout_111_3.addWidget(self.cls_epoch_min_filter_lineedit)


        self.horizontalLayout_51.addLayout(self.horizontalLayout_111_3)

        self.horizontalLayout_121_3 = QHBoxLayout()
        self.horizontalLayout_121_3.setObjectName(u"horizontalLayout_121_3")
        self.label_162 = QLabel(self.groupBox_34)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMaximumSize(QSize(16777215, 20))
        self.label_162.setFont(font)

        self.horizontalLayout_121_3.addWidget(self.label_162)

        self.cls_epoch_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_epoch_max_filter_lineedit.setObjectName(u"cls_epoch_max_filter_lineedit")
        self.cls_epoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_epoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_epoch_max_filter_lineedit.setFont(font)

        self.horizontalLayout_121_3.addWidget(self.cls_epoch_max_filter_lineedit)


        self.horizontalLayout_51.addLayout(self.horizontalLayout_121_3)


        self.horizontalLayout_165123.addLayout(self.horizontalLayout_51)

        self.line_54 = QFrame(self.groupBox_34)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_165123.addWidget(self.line_54)


        self.verticalLayout_60.addLayout(self.horizontalLayout_165123)

        self.line_55 = QFrame(self.groupBox_34)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_55)

        self.horizontalLayout_122_3 = QHBoxLayout()
        self.horizontalLayout_122_3.setSpacing(0)
        self.horizontalLayout_122_3.setObjectName(u"horizontalLayout_122_3")
        self.label_163 = QLabel(self.groupBox_34)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setFont(font)

        self.horizontalLayout_122_3.addWidget(self.label_163)

        self.horizontalSpacer_22_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_122_3.addItem(self.horizontalSpacer_22_4)

        self.horizontalLayout_48_4 = QHBoxLayout()
        self.horizontalLayout_48_4.setSpacing(10)
        self.horizontalLayout_48_4.setObjectName(u"horizontalLayout_48_4")
        self.horizontalLayout_123_4 = QHBoxLayout()
        self.horizontalLayout_123_4.setObjectName(u"horizontalLayout_123_4")
        self.label_164 = QLabel(self.groupBox_34)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMaximumSize(QSize(16777215, 20))
        self.label_164.setFont(font)

        self.horizontalLayout_123_4.addWidget(self.label_164)

        self.cls_tepoch_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_tepoch_min_filter_lineedit.setObjectName(u"cls_tepoch_min_filter_lineedit")
        self.cls_tepoch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_tepoch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_tepoch_min_filter_lineedit.setFont(font)

        self.horizontalLayout_123_4.addWidget(self.cls_tepoch_min_filter_lineedit)


        self.horizontalLayout_48_4.addLayout(self.horizontalLayout_123_4)

        self.horizontalLayout_124_4 = QHBoxLayout()
        self.horizontalLayout_124_4.setObjectName(u"horizontalLayout_124_4")
        self.label_86_3 = QLabel(self.groupBox_34)
        self.label_86_3.setObjectName(u"label_86_3")
        self.label_86_3.setMaximumSize(QSize(16777215, 20))
        self.label_86_3.setFont(font)

        self.horizontalLayout_124_4.addWidget(self.label_86_3)

        self.cls_tepoch_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_tepoch_max_filter_lineedit.setObjectName(u"cls_tepoch_max_filter_lineedit")
        self.cls_tepoch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_tepoch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_tepoch_max_filter_lineedit.setFont(font)

        self.horizontalLayout_124_4.addWidget(self.cls_tepoch_max_filter_lineedit)


        self.horizontalLayout_48_4.addLayout(self.horizontalLayout_124_4)


        self.horizontalLayout_122_3.addLayout(self.horizontalLayout_48_4)

        self.line_18_3 = QFrame(self.groupBox_34)
        self.line_18_3.setObjectName(u"line_18_3")
        self.line_18_3.setFrameShape(QFrame.HLine)
        self.line_18_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_122_3.addWidget(self.line_18_3)


        self.verticalLayout_60.addLayout(self.horizontalLayout_122_3)

        self.line_47_3 = QFrame(self.groupBox_34)
        self.line_47_3.setObjectName(u"line_47_3")
        self.line_47_3.setFrameShape(QFrame.HLine)
        self.line_47_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_47_3)

        self.horizontalLayout_128_3 = QHBoxLayout()
        self.horizontalLayout_128_3.setSpacing(0)
        self.horizontalLayout_128_3.setObjectName(u"horizontalLayout_128_3")
        self.label_134_3 = QLabel(self.groupBox_34)
        self.label_134_3.setObjectName(u"label_134_3")
        self.label_134_3.setFont(font)

        self.horizontalLayout_128_3.addWidget(self.label_134_3)

        self.horizontalSpacer_22_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_128_3.addItem(self.horizontalSpacer_22_5)

        self.horizontalLayout_48_5 = QHBoxLayout()
        self.horizontalLayout_48_5.setSpacing(10)
        self.horizontalLayout_48_5.setObjectName(u"horizontalLayout_48_5")
        self.horizontalLayout_123_5 = QHBoxLayout()
        self.horizontalLayout_123_5.setObjectName(u"horizontalLayout_123_5")
        self.label_85_3 = QLabel(self.groupBox_34)
        self.label_85_3.setObjectName(u"label_85_3")
        self.label_85_3.setMaximumSize(QSize(16777215, 20))
        self.label_85_3.setFont(font)

        self.horizontalLayout_123_5.addWidget(self.label_85_3)

        self.cls_tepoch_min_filter_lineedit_2 = QLineEdit(self.groupBox_34)
        self.cls_tepoch_min_filter_lineedit_2.setObjectName(u"cls_tepoch_min_filter_lineedit_2")
        self.cls_tepoch_min_filter_lineedit_2.setMinimumSize(QSize(50, 0))
        self.cls_tepoch_min_filter_lineedit_2.setMaximumSize(QSize(50, 30))
        self.cls_tepoch_min_filter_lineedit_2.setFont(font)

        self.horizontalLayout_123_5.addWidget(self.cls_tepoch_min_filter_lineedit_2)


        self.horizontalLayout_48_5.addLayout(self.horizontalLayout_123_5)

        self.horizontalLayout_124_5 = QHBoxLayout()
        self.horizontalLayout_124_5.setObjectName(u"horizontalLayout_124_5")
        self.label_165 = QLabel(self.groupBox_34)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMaximumSize(QSize(16777215, 20))
        self.label_165.setFont(font)

        self.horizontalLayout_124_5.addWidget(self.label_165)

        self.cls_tepoch_max_filter_lineedit_2 = QLineEdit(self.groupBox_34)
        self.cls_tepoch_max_filter_lineedit_2.setObjectName(u"cls_tepoch_max_filter_lineedit_2")
        self.cls_tepoch_max_filter_lineedit_2.setMinimumSize(QSize(50, 0))
        self.cls_tepoch_max_filter_lineedit_2.setMaximumSize(QSize(50, 30))
        self.cls_tepoch_max_filter_lineedit_2.setFont(font)

        self.horizontalLayout_124_5.addWidget(self.cls_tepoch_max_filter_lineedit_2)


        self.horizontalLayout_48_5.addLayout(self.horizontalLayout_124_5)


        self.horizontalLayout_128_3.addLayout(self.horizontalLayout_48_5)

        self.line_56 = QFrame(self.groupBox_34)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.HLine)
        self.line_56.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_128_3.addWidget(self.line_56)


        self.verticalLayout_60.addLayout(self.horizontalLayout_128_3)

        self.line_57 = QFrame(self.groupBox_34)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.HLine)
        self.line_57.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_57)

        self.horizontalLayout_166asdad = QHBoxLayout()
        self.horizontalLayout_166asdad.setSpacing(0)
        self.horizontalLayout_166asdad.setObjectName(u"horizontalLayout_166asdad")
        self.label_166 = QLabel(self.groupBox_34)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setFont(font)

        self.horizontalLayout_166asdad.addWidget(self.label_166)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_166asdad.addItem(self.horizontalSpacer_34)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setSpacing(10)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_168asdas = QHBoxLayout()
        self.horizontalLayout_168asdas.setObjectName(u"horizontalLayout_168asdas")
        self.label_167 = QLabel(self.groupBox_34)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMaximumSize(QSize(16777215, 20))
        self.label_167.setFont(font)

        self.horizontalLayout_168asdas.addWidget(self.label_167)

        self.cls_batch_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_batch_min_filter_lineedit.setObjectName(u"cls_batch_min_filter_lineedit")
        self.cls_batch_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_batch_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_batch_min_filter_lineedit.setFont(font)
        self.cls_batch_min_filter_lineedit.setInputMethodHints(Qt.ImhNone)
        self.cls_batch_min_filter_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_168asdas.addWidget(self.cls_batch_min_filter_lineedit)


        self.horizontalLayout_167.addLayout(self.horizontalLayout_168asdas)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.label_168 = QLabel(self.groupBox_34)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMaximumSize(QSize(16777215, 20))
        self.label_168.setFont(font)

        self.horizontalLayout_169.addWidget(self.label_168)

        self.cls_batch_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_batch_max_filter_lineedit.setObjectName(u"cls_batch_max_filter_lineedit")
        self.cls_batch_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_batch_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_batch_max_filter_lineedit.setFont(font)

        self.horizontalLayout_169.addWidget(self.cls_batch_max_filter_lineedit)


        self.horizontalLayout_167.addLayout(self.horizontalLayout_169)


        self.horizontalLayout_166asdad.addLayout(self.horizontalLayout_167)

        self.line_40_3 = QFrame(self.groupBox_34)
        self.line_40_3.setObjectName(u"line_40_3")
        self.line_40_3.setFrameShape(QFrame.HLine)
        self.line_40_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_166asdad.addWidget(self.line_40_3)


        self.verticalLayout_60.addLayout(self.horizontalLayout_166asdad)

        self.line_78 = QFrame(self.groupBox_34)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setFrameShape(QFrame.HLine)
        self.line_78.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_78)

        self.horizontalLayout_170 = QHBoxLayout()
        self.horizontalLayout_170.setSpacing(0)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.label_169 = QLabel(self.groupBox_34)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setFont(font)

        self.horizontalLayout_170.addWidget(self.label_169)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_35)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setSpacing(10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_171 = QHBoxLayout()
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.label_170 = QLabel(self.groupBox_34)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMaximumSize(QSize(16777215, 20))
        self.label_170.setFont(font)

        self.horizontalLayout_171.addWidget(self.label_170)

        self.cls_split_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_split_min_filter_lineedit.setObjectName(u"cls_split_min_filter_lineedit")
        self.cls_split_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_split_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_split_min_filter_lineedit.setFont(font)

        self.horizontalLayout_171.addWidget(self.cls_split_min_filter_lineedit)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_171)

        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.label_171 = QLabel(self.groupBox_34)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMaximumSize(QSize(16777215, 20))
        self.label_171.setFont(font)

        self.horizontalLayout_172.addWidget(self.label_171)

        self.cls_split_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_split_max_filter_lineedit.setObjectName(u"cls_split_max_filter_lineedit")
        self.cls_split_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_split_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_split_max_filter_lineedit.setFont(font)

        self.horizontalLayout_172.addWidget(self.cls_split_max_filter_lineedit)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_172)


        self.horizontalLayout_170.addLayout(self.horizontalLayout_52)

        self.line_33_3 = QFrame(self.groupBox_34)
        self.line_33_3.setObjectName(u"line_33_3")
        self.line_33_3.setFrameShape(QFrame.HLine)
        self.line_33_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_170.addWidget(self.line_33_3)


        self.verticalLayout_60.addLayout(self.horizontalLayout_170)

        self.line_79 = QFrame(self.groupBox_34)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setFrameShape(QFrame.HLine)
        self.line_79.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_79)

        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setSpacing(0)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.label_172 = QLabel(self.groupBox_34)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setFont(font)

        self.horizontalLayout_173.addWidget(self.label_172)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_36)

        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setSpacing(10)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.label_132_3 = QLabel(self.groupBox_34)
        self.label_132_3.setObjectName(u"label_132_3")
        self.label_132_3.setMaximumSize(QSize(16777215, 20))
        self.label_132_3.setFont(font)

        self.horizontalLayout_175.addWidget(self.label_132_3)

        self.cls_loss_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_loss_min_filter_lineedit.setObjectName(u"cls_loss_min_filter_lineedit")
        self.cls_loss_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_loss_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_loss_min_filter_lineedit.setFont(font)

        self.horizontalLayout_175.addWidget(self.cls_loss_min_filter_lineedit)


        self.horizontalLayout_174.addLayout(self.horizontalLayout_175)

        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.label_173 = QLabel(self.groupBox_34)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMaximumSize(QSize(16777215, 20))
        self.label_173.setFont(font)

        self.horizontalLayout_176.addWidget(self.label_173)

        self.cls_loss_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_loss_max_filter_lineedit.setObjectName(u"cls_loss_max_filter_lineedit")
        self.cls_loss_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_loss_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_loss_max_filter_lineedit.setFont(font)

        self.horizontalLayout_176.addWidget(self.cls_loss_max_filter_lineedit)


        self.horizontalLayout_174.addLayout(self.horizontalLayout_176)


        self.horizontalLayout_173.addLayout(self.horizontalLayout_174)

        self.line_58 = QFrame(self.groupBox_34)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_173.addWidget(self.line_58)


        self.verticalLayout_60.addLayout(self.horizontalLayout_173)

        self.line_80 = QFrame(self.groupBox_34)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setFrameShape(QFrame.HLine)
        self.line_80.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_80)

        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setSpacing(0)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.label_174 = QLabel(self.groupBox_34)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setFont(font)

        self.horizontalLayout_177.addWidget(self.label_174)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_177.addItem(self.horizontalSpacer_37)

        self.horizontalLayout_178 = QHBoxLayout()
        self.horizontalLayout_178.setSpacing(10)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.label_175 = QLabel(self.groupBox_34)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMaximumSize(QSize(16777215, 20))
        self.label_175.setFont(font)

        self.horizontalLayout_179.addWidget(self.label_175)

        self.cls_acc_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_acc_min_filter_lineedit.setObjectName(u"cls_acc_min_filter_lineedit")
        self.cls_acc_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_acc_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_acc_min_filter_lineedit.setFont(font)

        self.horizontalLayout_179.addWidget(self.cls_acc_min_filter_lineedit)


        self.horizontalLayout_178.addLayout(self.horizontalLayout_179)

        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.label_176 = QLabel(self.groupBox_34)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMaximumSize(QSize(16777215, 20))
        self.label_176.setFont(font)

        self.horizontalLayout_180.addWidget(self.label_176)

        self.cls_acc_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_acc_max_filter_lineedit.setObjectName(u"cls_acc_max_filter_lineedit")
        self.cls_acc_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_acc_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_acc_max_filter_lineedit.setFont(font)

        self.horizontalLayout_180.addWidget(self.cls_acc_max_filter_lineedit)


        self.horizontalLayout_178.addLayout(self.horizontalLayout_180)


        self.horizontalLayout_177.addLayout(self.horizontalLayout_178)

        self.line_59 = QFrame(self.groupBox_34)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_177.addWidget(self.line_59)


        self.verticalLayout_60.addLayout(self.horizontalLayout_177)

        self.line_81 = QFrame(self.groupBox_34)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setFrameShape(QFrame.HLine)
        self.line_81.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_81)

        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setSpacing(0)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.label_177 = QLabel(self.groupBox_34)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setFont(font)

        self.horizontalLayout_181.addWidget(self.label_177)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_181.addItem(self.horizontalSpacer_38)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setSpacing(10)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.label_178 = QLabel(self.groupBox_34)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMaximumSize(QSize(16777215, 20))
        self.label_178.setFont(font)

        self.horizontalLayout_183.addWidget(self.label_178)

        self.cls_prec_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_prec_min_filter_lineedit.setObjectName(u"cls_prec_min_filter_lineedit")
        self.cls_prec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_prec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_prec_min_filter_lineedit.setFont(font)

        self.horizontalLayout_183.addWidget(self.cls_prec_min_filter_lineedit)


        self.horizontalLayout_182.addLayout(self.horizontalLayout_183)

        self.horizontalLayout_184 = QHBoxLayout()
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.label_179 = QLabel(self.groupBox_34)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMaximumSize(QSize(16777215, 20))
        self.label_179.setFont(font)

        self.horizontalLayout_184.addWidget(self.label_179)

        self.cls_prec_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_prec_max_filter_lineedit.setObjectName(u"cls_prec_max_filter_lineedit")
        self.cls_prec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_prec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_prec_max_filter_lineedit.setFont(font)

        self.horizontalLayout_184.addWidget(self.cls_prec_max_filter_lineedit)


        self.horizontalLayout_182.addLayout(self.horizontalLayout_184)


        self.horizontalLayout_181.addLayout(self.horizontalLayout_182)

        self.line_60 = QFrame(self.groupBox_34)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_181.addWidget(self.line_60)


        self.verticalLayout_60.addLayout(self.horizontalLayout_181)

        self.line_82 = QFrame(self.groupBox_34)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setFrameShape(QFrame.HLine)
        self.line_82.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_82)

        self.horizontalLayout_185 = QHBoxLayout()
        self.horizontalLayout_185.setSpacing(0)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.label_180 = QLabel(self.groupBox_34)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setFont(font)

        self.horizontalLayout_185.addWidget(self.label_180)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_185.addItem(self.horizontalSpacer_39)

        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setSpacing(10)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.label_181 = QLabel(self.groupBox_34)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMaximumSize(QSize(16777215, 20))
        self.label_181.setFont(font)

        self.horizontalLayout_187.addWidget(self.label_181)

        self.cls_rec_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_rec_min_filter_lineedit.setObjectName(u"cls_rec_min_filter_lineedit")
        self.cls_rec_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_rec_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_rec_min_filter_lineedit.setFont(font)

        self.horizontalLayout_187.addWidget(self.cls_rec_min_filter_lineedit)


        self.horizontalLayout_186.addLayout(self.horizontalLayout_187)

        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.label_182 = QLabel(self.groupBox_34)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMaximumSize(QSize(16777215, 20))
        self.label_182.setFont(font)

        self.horizontalLayout_188.addWidget(self.label_182)

        self.cls_rec_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_rec_max_filter_lineedit.setObjectName(u"cls_rec_max_filter_lineedit")
        self.cls_rec_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_rec_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_rec_max_filter_lineedit.setFont(font)

        self.horizontalLayout_188.addWidget(self.cls_rec_max_filter_lineedit)


        self.horizontalLayout_186.addLayout(self.horizontalLayout_188)


        self.horizontalLayout_185.addLayout(self.horizontalLayout_186)

        self.line_61 = QFrame(self.groupBox_34)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_185.addWidget(self.line_61)


        self.verticalLayout_60.addLayout(self.horizontalLayout_185)

        self.line_83 = QFrame(self.groupBox_34)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setFrameShape(QFrame.HLine)
        self.line_83.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_83)

        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setSpacing(0)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.label_183 = QLabel(self.groupBox_34)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setFont(font)

        self.horizontalLayout_189.addWidget(self.label_183)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_189.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_190 = QHBoxLayout()
        self.horizontalLayout_190.setSpacing(10)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_191 = QHBoxLayout()
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.label_184 = QLabel(self.groupBox_34)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setMaximumSize(QSize(16777215, 20))
        self.label_184.setFont(font)

        self.horizontalLayout_191.addWidget(self.label_184)

        self.cls_date_min_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_date_min_filter_lineedit.setObjectName(u"cls_date_min_filter_lineedit")
        self.cls_date_min_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_date_min_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_date_min_filter_lineedit.setFont(font)

        self.horizontalLayout_191.addWidget(self.cls_date_min_filter_lineedit)


        self.horizontalLayout_190.addLayout(self.horizontalLayout_191)

        self.horizontalLayout_192 = QHBoxLayout()
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.label_185 = QLabel(self.groupBox_34)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMaximumSize(QSize(16777215, 20))
        self.label_185.setFont(font)

        self.horizontalLayout_192.addWidget(self.label_185)

        self.cls_date_max_filter_lineedit = QLineEdit(self.groupBox_34)
        self.cls_date_max_filter_lineedit.setObjectName(u"cls_date_max_filter_lineedit")
        self.cls_date_max_filter_lineedit.setMinimumSize(QSize(50, 0))
        self.cls_date_max_filter_lineedit.setMaximumSize(QSize(50, 30))
        self.cls_date_max_filter_lineedit.setFont(font)

        self.horizontalLayout_192.addWidget(self.cls_date_max_filter_lineedit)


        self.horizontalLayout_190.addLayout(self.horizontalLayout_192)


        self.horizontalLayout_189.addLayout(self.horizontalLayout_190)

        self.line_62 = QFrame(self.groupBox_34)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_189.addWidget(self.line_62)


        self.verticalLayout_60.addLayout(self.horizontalLayout_189)

        self.line_97 = QFrame(self.groupBox_34)
        self.line_97.setObjectName(u"line_97")
        self.line_97.setFrameShape(QFrame.HLine)
        self.line_97.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_97)

        self.label_38 = QLabel(self.groupBox_34)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_60.addWidget(self.label_38)

        self.table_classification_filter_class = QTableWidget(self.groupBox_34)
        if (self.table_classification_filter_class.columnCount() < 3):
            self.table_classification_filter_class.setColumnCount(3)
        self.table_classification_filter_class.setObjectName(u"table_classification_filter_class")
        self.table_classification_filter_class.setColumnCount(3)

        self.verticalLayout_60.addWidget(self.table_classification_filter_class)

        self.frame123 = QFrame(self.groupBox_34)
        self.frame123.setObjectName(u"frame123")
        self.frame123.setFrameShape(QFrame.Panel)
        self.frame123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_193 = QHBoxLayout(self.frame123)
        self.horizontalLayout_193.setSpacing(20)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.cls_filter_btn = QPushButton(self.frame123)
        self.cls_filter_btn.setObjectName(u"cls_filter_btn")
        self.cls_filter_btn.setMinimumSize(QSize(0, 30))
        self.cls_filter_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_193.addWidget(self.cls_filter_btn)

        self.cls_clearfilter_btn = QPushButton(self.frame123)
        self.cls_clearfilter_btn.setObjectName(u"cls_clearfilter_btn")
        self.cls_clearfilter_btn.setMinimumSize(QSize(0, 30))
        self.cls_clearfilter_btn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_193.addWidget(self.cls_clearfilter_btn)


        self.verticalLayout_60.addWidget(self.frame123)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_11)


        self.verticalLayout_43.addWidget(self.groupBox_34)


        self.horizontalLayout_38.addWidget(self.frame_28)

        self.line_9 = QFrame(self.page_classification_history)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_38.addWidget(self.line_9)

        self.frame_27 = QFrame(self.page_classification_history)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setMaximumSize(QSize(16777215, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_27)
        self.verticalLayout_42.setSpacing(5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.cls_history_tabel = QTableWidget(self.frame_27)
        if (self.cls_history_tabel.columnCount() < 20):
            self.cls_history_tabel.setColumnCount(20)
        self.cls_history_tabel.setObjectName(u"cls_history_tabel")
        self.cls_history_tabel.setFrameShape(QFrame.Panel)
        self.cls_history_tabel.setFrameShadow(QFrame.Raised)
        self.cls_history_tabel.setRowCount(0)
        self.cls_history_tabel.setColumnCount(20)
        self.cls_history_tabel.horizontalHeader().setMinimumSectionSize(120)
        self.cls_history_tabel.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_42.addWidget(self.cls_history_tabel)

        self.frame_68_3 = QFrame(self.frame_27)
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
        self.cls_table_refresh_btn.setIcon(icon25)
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
        self.cls_tabel_label.setMinimumSize(QSize(300, 0))
        self.cls_tabel_label.setMaximumSize(QSize(300, 16777215))
        self.cls_tabel_label.setFrameShape(QFrame.Panel)
        self.cls_tabel_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_109_3.addWidget(self.cls_tabel_label)

        self.horizontalSpacer_20_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109_3.addItem(self.horizontalSpacer_20_3)


        self.verticalLayout_42.addWidget(self.frame_68_3)


        self.horizontalLayout_38.addWidget(self.frame_27)

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
        icon26 = QIcon()
        icon26.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon26)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 406, 218))
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
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon27 = QIcon()
        icon27.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon27)

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
        font6 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
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
        sizePolicy5.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy5)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
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
        self.fontComboBox.setGeometry(QRect(130, 120, 187, 22))

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
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
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
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
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
        self.lineEdit_name_dataset.textChanged.connect(self.label_8.setText)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_defect.setCurrentIndex(0)
        self.tabWidget_defect.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_pbt.setCurrentIndex(2)
        self.stackedWidget_binary.setCurrentIndex(1)
        self.binary_train.setDefault(False)
        self.stackedWidget_localization.setCurrentIndex(0)
        self.stackedWidget_classification.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"SABA", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"    Trainer", None))
        self.Data_auquzation_btn.setText(QCoreApplication.translate("MainWindow", u"Data Auquzation", None))
        self.label_btn.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.tuning_btn.setText(QCoreApplication.translate("MainWindow", u" Tuning", None))
        self.pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Pipline Build & Test", None))
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
        self.label_dorsa.setText("")
        self.titleRightInfo.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Please Login", None))
        self.label_app_erors.setText("")
        self.user_name.setText("")
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
        self.setting_eror.setText("")
        self.btn_software_setting.setText(QCoreApplication.translate("MainWindow", u"Software setting", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Tuning Ultra Setting", None))
        self.btn_user_proflie.setText(QCoreApplication.translate("MainWindow", u"User Profile", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Storage Setting", None))
        self.connect_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnet", None))
        self.camera1_btn_2.setText("")
        self.camera2_btn_2.setText("")
        self.camera3_btn_2.setText("")
        self.camera4_btn_2.setText("")
        self.camera5_btn_2.setText("")
        self.camera6_btn_2.setText("")
        self.camera7_btn_2.setText("")
        self.camera8_btn_2.setText("")
        self.camera9_btn_2.setText("")
        self.camera10_btn_2.setText("")
        self.camera11_btn_2.setText("")
        self.camera12_btn_2.setText("")
        self.camera13_btn_2.setText("")
        self.camera14_btn_2.setText("")
        self.camera15_btn_2.setText("")
        self.camera16_btn_2.setText("")
        self.camera17_btn_2.setText("")
        self.camera18_btn_2.setText("")
        self.camera19_btn_2.setText("")
        self.camera20_btn_2.setText("")
        self.camera21_btn_2.setText("")
        self.camera22_btn_2.setText("")
        self.camera23_btn_2.setText("")
        self.camera24_btn_2.setText("")
        self.camera_connection_msg.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Camera Number :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"1 x 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"3 x 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"12 * 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"LIVE", None))
        self.load_coil_btn.setText(QCoreApplication.translate("MainWindow", u"Load Sheet", None))
        self.next_coil_btn.setText("")
        self.prev_coil_btn.setText("")
        self.details_label.setText("")
        self.show_side.setText("")
        self.crop_image.setText("")
        self.show_tools_btn.setText("")
        self.warning_data_page.setText("")
        self.groupBox_2.setTitle("")
        self.save_btn_SI.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_btn_SI.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.groupBox.setTitle("")
        self.add_btn_SI.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.remove_btn_SI.setText("")
        self.checkBox_select.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.groupBox_3.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Position", None))
        self.label_30.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.current_pos_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_127.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.current_pos_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Technical View", None))
        self.label_1291.setText(QCoreApplication.translate("MainWindow", u"40  cm", None))
        self.label_1311.setText("")
#if QT_CONFIG(tooltip)
        self.label_6_1.setToolTip(QCoreApplication.translate("MainWindow", u"UP Side Technical View", None))
#endif // QT_CONFIG(tooltip)
        self.label_6_1.setText(QCoreApplication.translate("MainWindow", u"TOP Side", None))
        self.up_side_technical.setText("")
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"40  cm", None))
        self.label_125.setText("")
#if QT_CONFIG(tooltip)
        self.label_119.setToolTip(QCoreApplication.translate("MainWindow", u"UP Side Technical View", None))
#endif // QT_CONFIG(tooltip)
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"BOTTOM Side", None))
        self.down_side_technical.setText("")
#if QT_CONFIG(statustip)
        self.pushButton_28.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_28.setText("")
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText("")
        self.next_img_label_btn.setText("")
        self.prev_img_label_btn.setText("")
        self.zoomIn_btn.setText("")
        self.zoomOut_btn.setText("")
        self.drag_btn.setText("")
        self.polygon_btn.setText("")
        self.bounding_btn.setText("")
        self.heatmap_btn.setText("")
        self.delete_btn.setText("")
        self.image.setText("")
        self.image_up_left.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Up Left", None))
        self.image_up.setText("")
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.image_up_right.setText("")
        self.label_1091.setText(QCoreApplication.translate("MainWindow", u"Up Right", None))
        self.image_left.setText("")
        self.label_81_2.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.image_right.setText("")
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.image_bottom_left.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Bottom Left", None))
        self.image_bottom.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.image_bottom_right.setText("")
        self.label_1321.setText(QCoreApplication.translate("MainWindow", u"Bottom Right", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Defect :", None))
        self.no_defect.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.yes_defect.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.tabWidget_defect.setTabText(self.tabWidget_defect.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Mask", None))
        self.tabWidget_defect.setTabText(self.tabWidget_defect.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.add_label_btn.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Image has no Defect", None))
        self.warning_label_page.setText("")
        self.save_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Coil number :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cam num :", None))
        self.plabel_date_txt.setText("")
        self.plabel_coil_num_txt.setText("")
        self.plabel_cam_txt.setText("")
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
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Data Bases :", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.my_databases_2.setText(QCoreApplication.translate("MainWindow", u"My Databases", None))
        self.create_new_database.setText(QCoreApplication.translate("MainWindow", u"Create New DataBase", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.lineEdit_name_dataset.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Date Today :", None))
        self.today_date.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"User Name Creator:", None))
        self.user_name_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Location :", None))
        self.lineEdit_path_dataset.setText(QCoreApplication.translate("MainWindow", u"D:/", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_8.setText("")
        self.label_14.setText("")
        self.toolButton_select_directory.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Maximum Size Database :", None))
        self.create_database_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Default Dataset :", None))
        self.set_default_database_btn.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.load_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Details of database", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Images", None))
        self.pipeline_pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Pipeline", None))
        self.load_dataset_pbt_btn.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.history_pbt_btn.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.checkBox_2.setText("")
        self.label_12_3.setText(QCoreApplication.translate("MainWindow", u"Binary : ", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.checkBox_3.setText("")
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Localization : ", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.checkBox_4.setText("")
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Classification :", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Save Pipeline", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Refresh All", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Select Data set :", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Defect", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Perfect", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Import Image :", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Select Pipeline", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Piplelines :", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"More details", None))
        self.dfgdr_2.setTitle(QCoreApplication.translate("MainWindow", u"Evaluate Images", None))
        self.binary_list_defect_prev_btn_2.setText("")
        self.binary_list_defect_next_btn_2.setText("")
        self.dfg_2.setTitle(QCoreApplication.translate("MainWindow", u"Orginal Images", None))
        self.binary_list_perfect_prev_btn_3.setText("")
        self.binary_list_perfect_next_btn_3.setText("")
        self.binary_list.setText(QCoreApplication.translate("MainWindow", u"Binary list", None))
        self.binary_training.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.binary_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_11_2.setText(QCoreApplication.translate("MainWindow", u"Dataset Path", None))
        self.binary_list_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.label_12_2.setText(QCoreApplication.translate("MainWindow", u"Annotations Path", None))
        self.binary_list_show_btn.setText(QCoreApplication.translate("MainWindow", u"Show Images", None))
        self.warning_binarylist_page.setText("")
        self.dfg.setTitle(QCoreApplication.translate("MainWindow", u"Perfect Images", None))
        self.binary_list_perfect_prev_btn.setText("")
        self.binary_list_perfect_next_btn.setText("")
        self.dfgdr.setTitle(QCoreApplication.translate("MainWindow", u"Defect Images", None))
        self.binary_list_defect_prev_btn.setText("")
        self.binary_list_defect_next_btn.setText("")
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Algorithm Name :", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Input size :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Input type", None))
        self.input_type_resize.setText(QCoreApplication.translate("MainWindow", u"resize", None))
        self.input_type_split.setText(QCoreApplication.translate("MainWindow", u"split", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Epochs :", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Learning Rate :", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Tuning Epochs :", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Validation Split % :", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Dataset Path :", None))
        self.b_select_dp.setText(QCoreApplication.translate("MainWindow", u"Select dataset", None))
        self.b_delete_ds.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.b_add_ds.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.b_add_ds_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dataset address", None))
        self.b_add_ok.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.b_add_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.binary_train.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.binary_chart_checkbox.setText(QCoreApplication.translate("MainWindow", u"Chart Full View", None))
        self.warning_train_page.setText("")
        self.label_12.setText("")
        self.label_8_2.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_13_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Traning Records", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Tune Epochs", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_86_2.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_134_2.setText(QCoreApplication.translate("MainWindow", u"Tune Epochs", None))
        self.label_85_2.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Batch-Size", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Split-Size", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.label_132_2.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Recall", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.binary_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.binary_clearfilter_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.binary_table_refresh_btn.setText("")
        self.binary_tabel_prev.setText("")
        self.binary_tabel_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.binary_tabel_next.setText("")
        self.binary_tabel_label.setText("")
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
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Select Class", None))
        self.label_111_2.setText(QCoreApplication.translate("MainWindow", u"Total Classes:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Selected Classes:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Total Images :", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Selected Images :", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.localization_train.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
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
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Defect Classes", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Name ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Is Defect", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Defect Group", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Defect Level", None))
        self.classification_add_new_class.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.classification_add_new_class_2.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Show Related Images", None))
        self.classlist_show_related_img_btn.setText(QCoreApplication.translate("MainWindow", u"Show Images", None))
        self.classification_add_new_class_4.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.classlist_msg_label.setText("")
        self.classlist_prev_btn.setText("")
        self.class_list_slider_frame.setText("")
        self.classlist_next_btn.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"new", None))
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
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.classification_train_msg_label.setText("")
        self.label_83543.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_32.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.cls_chart_checkbox.setText(QCoreApplication.translate("MainWindow", u"Chart Full View", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Traning Records", None))
        self.label_1593243.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Tune Epochs", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_86_3.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_134_3.setText(QCoreApplication.translate("MainWindow", u"Tune Epochs", None))
        self.label_85_3.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Batch-Size", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Split-Size", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.label_132_3.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Recall", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Including Class(s)", None))
        self.cls_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.cls_clearfilter_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.cls_table_refresh_btn.setText("")
        self.cls_tabel_prev.setText("")
        self.cls_tabel_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.cls_tabel_next.setText("")
        self.cls_tabel_label.setText("")
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

