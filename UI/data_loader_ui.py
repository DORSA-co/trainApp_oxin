# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_loader.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 440)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(90,50,90);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 32))
        self.frame_4.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 20))
        self.label_2.setLineWidth(0)
        self.label_2.setPixmap(QPixmap(u"../trainApp_oxin/images/images/whitew.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(-5)
        self.label_2.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(846, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.miniButton = QPushButton(self.frame_4)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.frame_4)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon1)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.frame_4)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 5)
        self.tableWidget_dataset = QTableWidget(self.frame_3)
        if (self.tableWidget_dataset.columnCount() < 5):
            self.tableWidget_dataset.setColumnCount(5)
        if (self.tableWidget_dataset.rowCount() < 1):
            self.tableWidget_dataset.setRowCount(1)
        self.tableWidget_dataset.setObjectName(u"tableWidget_dataset")
        self.tableWidget_dataset.setStyleSheet(u"	background-color: Transparent;")
        self.tableWidget_dataset.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.tableWidget_dataset.setDragDropOverwriteMode(False)
        self.tableWidget_dataset.setSortingEnabled(True)
        self.tableWidget_dataset.setRowCount(1)
        self.tableWidget_dataset.setColumnCount(5)

        self.verticalLayout_4.addWidget(self.tableWidget_dataset)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 113))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 5, 2)
        self.detail_dataset = QLineEdit(self.groupBox_2)
        self.detail_dataset.setObjectName(u"detail_dataset")
        self.detail_dataset.setEnabled(False)
        self.detail_dataset.setMinimumSize(QSize(0, 84))

        self.verticalLayout_10.addWidget(self.detail_dataset)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 2)
        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(481, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_6)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_search = QTabWidget(self.groupBox)
        self.widget_search.setObjectName(u"widget_search")
        self.widget_search.setCursor(QCursor(Qt.ArrowCursor))
        self.widget_search.setStyleSheet(u"\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"	color:black;\n"
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
"	color:rgb(20,0,200);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"	color:black;\n"
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
""
                        "QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
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
        self.id_page = QWidget()
        self.id_page.setObjectName(u"id_page")
        self.verticalLayout_5 = QVBoxLayout(self.id_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_8 = QFrame(self.id_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.list_show_id = QListWidget(self.frame_8)
        self.list_show_id.setObjectName(u"list_show_id")

        self.verticalLayout_9.addWidget(self.list_show_id)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lineEdit_7 = QLineEdit(self.frame_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(150, 27))

        self.horizontalLayout_13.addWidget(self.lineEdit_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.btn_id_search = QPushButton(self.frame_8)
        self.btn_id_search.setObjectName(u"btn_id_search")
        self.btn_id_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_id_search, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.widget_search.addTab(self.id_page, "")
        self.heat_id_page = QWidget()
        self.heat_id_page.setObjectName(u"heat_id_page")
        self.verticalLayout_6 = QVBoxLayout(self.heat_id_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.heat_id_page)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.list_heat_id = QListWidget(self.heat_id_page)
        self.list_heat_id.setObjectName(u"list_heat_id")

        self.verticalLayout_6.addWidget(self.list_heat_id)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.heat_id_page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.heat_id_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(150, 5))

        self.horizontalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.coil_search = QPushButton(self.heat_id_page)
        self.coil_search.setObjectName(u"coil_search")
        self.coil_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.coil_search, 0, Qt.AlignRight)

        self.widget_search.addTab(self.heat_id_page, "")
        self.psn_page = QWidget()
        self.psn_page.setObjectName(u"psn_page")
        self.verticalLayout_7 = QVBoxLayout(self.psn_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.psn_page)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.list_ps_number = QListWidget(self.psn_page)
        self.list_ps_number.setObjectName(u"list_ps_number")

        self.verticalLayout_7.addWidget(self.list_ps_number)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.psn_page)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.lineEdit_4 = QLineEdit(self.psn_page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(150, 5))

        self.horizontalLayout_10.addWidget(self.lineEdit_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.pushButton_6 = QPushButton(self.psn_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.pushButton_6, 0, Qt.AlignRight)

        self.widget_search.addTab(self.psn_page, "")
        self.PDLN_page = QWidget()
        self.PDLN_page.setObjectName(u"PDLN_page")
        self.verticalLayout_8 = QVBoxLayout(self.PDLN_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_9 = QFrame(self.PDLN_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.list_pdl_number = QListWidget(self.frame_9)
        self.list_pdl_number.setObjectName(u"list_pdl_number")

        self.verticalLayout_11.addWidget(self.list_pdl_number)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.lineEdit_5 = QLineEdit(self.frame_9)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(150, 5))

        self.horizontalLayout_11.addWidget(self.lineEdit_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.coil_search_3 = QPushButton(self.frame_9)
        self.coil_search_3.setObjectName(u"coil_search_3")
        self.coil_search_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.coil_search_3, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.widget_search.addTab(self.PDLN_page, "")

        self.verticalLayout_3.addWidget(self.widget_search)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 48))
        self.frame_7.setMaximumSize(QSize(16777203, 37))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(90, 32))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(206, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.open_folder_image = QPushButton(self.frame_7)
        self.open_folder_image.setObjectName(u"open_folder_image")
        self.open_folder_image.setMaximumSize(QSize(97, 32))
        self.open_folder_image.setFont(font1)
        self.open_folder_image.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.open_folder_image)

        self.load_btn = QPushButton(self.frame_7)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setMaximumSize(QSize(66, 32))
        self.load_btn.setFont(font1)
        self.load_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.load_btn)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_12.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMaximumSize(QSize(16777215, 5))
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.widget_search.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Details of Dataset :    ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search By :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Available ID Numbers :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ID  :", None))
        self.btn_id_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.widget_search.setTabText(self.widget_search.indexOf(self.id_page), QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Availabl eHEAT Numbers :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number :", None))
        self.coil_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.widget_search.setTabText(self.widget_search.indexOf(self.heat_id_page), QCoreApplication.translate("MainWindow", u"HEAT", None))
#if QT_CONFIG(tooltip)
        self.widget_search.setTabToolTip(self.widget_search.indexOf(self.heat_id_page), QCoreApplication.translate("MainWindow", u"heat number", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Available Product Schedule Numbesr :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Order Number :", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.widget_search.setTabText(self.widget_search.indexOf(self.psn_page), QCoreApplication.translate("MainWindow", u"PSN", None))
#if QT_CONFIG(tooltip)
        self.widget_search.setTabToolTip(self.widget_search.indexOf(self.psn_page), QCoreApplication.translate("MainWindow", u"Product Schedule Number", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Available Product Drift Line Numbers :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number :", None))
        self.coil_search_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.widget_search.setTabText(self.widget_search.indexOf(self.PDLN_page), QCoreApplication.translate("MainWindow", u"PDLN", None))
#if QT_CONFIG(tooltip)
        self.widget_search.setTabToolTip(self.widget_search.indexOf(self.PDLN_page), QCoreApplication.translate("MainWindow", u"Product Drift Line Number", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.open_folder_image.setText(QCoreApplication.translate("MainWindow", u"Open Images", None))
        self.load_btn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
    # retranslateUi

