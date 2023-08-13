# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_logs.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1163, 735)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout.addWidget(self.rightButtons)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #b7baab;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, -1, 3, 3)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(340, 0))
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.groupBox_3.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.checkBox_allDates = QCheckBox(self.groupBox_3)
        self.checkBox_allDates.setObjectName(u"checkBox_allDates")
        self.checkBox_allDates.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_allDates)

        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.spinBox_fromYear = QSpinBox(self.groupBox_3)
        self.spinBox_fromYear.setObjectName(u"spinBox_fromYear")
        self.spinBox_fromYear.setEnabled(False)
        self.spinBox_fromYear.setStyleSheet(u"QSpinBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.horizontalLayout_3.addWidget(self.spinBox_fromYear)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox_fromMonth = QSpinBox(self.groupBox_3)
        self.spinBox_fromMonth.setObjectName(u"spinBox_fromMonth")
        self.spinBox_fromMonth.setEnabled(False)
        self.spinBox_fromMonth.setStyleSheet(u"QSpinBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")
        self.spinBox_fromMonth.setMinimum(1)
        self.spinBox_fromMonth.setMaximum(12)

        self.horizontalLayout_4.addWidget(self.spinBox_fromMonth)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.spinBox_fromDay = QSpinBox(self.groupBox_3)
        self.spinBox_fromDay.setObjectName(u"spinBox_fromDay")
        self.spinBox_fromDay.setEnabled(False)
        self.spinBox_fromDay.setStyleSheet(u"QSpinBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")
        self.spinBox_fromDay.setMinimum(1)
        self.spinBox_fromDay.setMaximum(31)

        self.horizontalLayout_6.addWidget(self.spinBox_fromDay)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.spinBox_toYear = QSpinBox(self.groupBox_3)
        self.spinBox_toYear.setObjectName(u"spinBox_toYear")
        self.spinBox_toYear.setEnabled(False)
        self.spinBox_toYear.setStyleSheet(u"QSpinBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.horizontalLayout_8.addWidget(self.spinBox_toYear)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.spinBox_toMonth = QSpinBox(self.groupBox_3)
        self.spinBox_toMonth.setObjectName(u"spinBox_toMonth")
        self.spinBox_toMonth.setEnabled(False)
        self.spinBox_toMonth.setStyleSheet(u"QSpinBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")
        self.spinBox_toMonth.setMinimum(1)
        self.spinBox_toMonth.setMaximum(12)

        self.horizontalLayout_9.addWidget(self.spinBox_toMonth)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.spinBox_toDay = QSpinBox(self.groupBox_3)
        self.spinBox_toDay.setObjectName(u"spinBox_toDay")
        self.spinBox_toDay.setEnabled(False)
        self.spinBox_toDay.setStyleSheet(u"QSpinBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")
        self.spinBox_toDay.setMinimum(1)
        self.spinBox_toDay.setMaximum(31)

        self.horizontalLayout_10.addWidget(self.spinBox_toDay)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.groupBox_5.setFont(font2)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_allLevels = QCheckBox(self.groupBox_5)
        self.checkBox_allLevels.setObjectName(u"checkBox_allLevels")
        self.checkBox_allLevels.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_allLevels.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_allLevels)

        self.line_2 = QFrame(self.groupBox_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.checkBox_levelInfo = QCheckBox(self.groupBox_5)
        self.checkBox_levelInfo.setObjectName(u"checkBox_levelInfo")
        self.checkBox_levelInfo.setEnabled(False)
        self.checkBox_levelInfo.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_levelInfo)

        self.checkBox_levelWarning = QCheckBox(self.groupBox_5)
        self.checkBox_levelWarning.setObjectName(u"checkBox_levelWarning")
        self.checkBox_levelWarning.setEnabled(False)
        self.checkBox_levelWarning.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_levelWarning)

        self.checkBox_levelError = QCheckBox(self.groupBox_5)
        self.checkBox_levelError.setObjectName(u"checkBox_levelError")
        self.checkBox_levelError.setEnabled(False)
        self.checkBox_levelError.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_levelError)

        self.checkBox_levelCritical = QCheckBox(self.groupBox_5)
        self.checkBox_levelCritical.setObjectName(u"checkBox_levelCritical")
        self.checkBox_levelCritical.setEnabled(False)
        self.checkBox_levelCritical.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_levelCritical)

        self.checkBox_levelException = QCheckBox(self.groupBox_5)
        self.checkBox_levelException.setObjectName(u"checkBox_levelException")
        self.checkBox_levelException.setEnabled(False)
        self.checkBox_levelException.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_levelException)


        self.horizontalLayout_12.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_allTypes = QCheckBox(self.groupBox_6)
        self.checkBox_allTypes.setObjectName(u"checkBox_allTypes")
        self.checkBox_allTypes.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBox_allTypes)

        self.line_3 = QFrame(self.groupBox_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.checkBox_typesLogin = QCheckBox(self.groupBox_6)
        self.checkBox_typesLogin.setObjectName(u"checkBox_typesLogin")
        self.checkBox_typesLogin.setEnabled(False)
        self.checkBox_typesLogin.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesLogin)

        self.checkBox_typesPLC = QCheckBox(self.groupBox_6)
        self.checkBox_typesPLC.setObjectName(u"checkBox_typesPLC")
        self.checkBox_typesPLC.setEnabled(False)
        self.checkBox_typesPLC.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesPLC)

        self.checkBox_typesCameras = QCheckBox(self.groupBox_6)
        self.checkBox_typesCameras.setObjectName(u"checkBox_typesCameras")
        self.checkBox_typesCameras.setEnabled(False)
        self.checkBox_typesCameras.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesCameras)

        self.checkBox_typesLabeling = QCheckBox(self.groupBox_6)
        self.checkBox_typesLabeling.setObjectName(u"checkBox_typesLabeling")
        self.checkBox_typesLabeling.setEnabled(False)
        self.checkBox_typesLabeling.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesLabeling)

        self.checkBox_typesTraining = QCheckBox(self.groupBox_6)
        self.checkBox_typesTraining.setObjectName(u"checkBox_typesTraining")
        self.checkBox_typesTraining.setEnabled(False)
        self.checkBox_typesTraining.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesTraining)

        self.checkBox_typesDatabase = QCheckBox(self.groupBox_6)
        self.checkBox_typesDatabase.setObjectName(u"checkBox_typesDatabase")
        self.checkBox_typesDatabase.setEnabled(False)
        self.checkBox_typesDatabase.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesDatabase)

        self.checkBox_typesOthers = QCheckBox(self.groupBox_6)
        self.checkBox_typesOthers.setObjectName(u"checkBox_typesOthers")
        self.checkBox_typesOthers.setEnabled(False)
        self.checkBox_typesOthers.setStyleSheet(u"QCheckBox:disabled  {\n"
"	color: rgb(70, 70, 70);\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_typesOthers)


        self.horizontalLayout_12.addWidget(self.groupBox_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 60))
        self.groupBox_4.setFont(font1)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.spinBox_lineNumbers = QSpinBox(self.groupBox_4)
        self.spinBox_lineNumbers.setObjectName(u"spinBox_lineNumbers")
        self.spinBox_lineNumbers.setMinimum(1)
        self.spinBox_lineNumbers.setMaximum(500)
        self.spinBox_lineNumbers.setValue(100)

        self.horizontalLayout_11.addWidget(self.spinBox_lineNumbers)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.comboBox_linesFL = QComboBox(self.groupBox_4)
        self.comboBox_linesFL.addItem("")
        self.comboBox_linesFL.addItem("")
        self.comboBox_linesFL.setObjectName(u"comboBox_linesFL")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_linesFL.sizePolicy().hasHeightForWidth())
        self.comboBox_linesFL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.comboBox_linesFL)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.search_btn = QPushButton(self.groupBox)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.search_btn)

        self.refresh_btn = QPushButton(self.groupBox)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.refresh_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.export_btn = QPushButton(self.groupBox)
        self.export_btn.setObjectName(u"export_btn")

        self.verticalLayout_5.addWidget(self.export_btn)

        self.message_label = QLabel(self.groupBox)
        self.message_label.setObjectName(u"message_label")

        self.verticalLayout_5.addWidget(self.message_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logs_textEdit = QTextEdit(self.groupBox_2)
        self.logs_textEdit.setObjectName(u"logs_textEdit")
        self.logs_textEdit.setEnabled(True)
        self.logs_textEdit.setStyleSheet(u"color: black;")
        self.logs_textEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.logs_textEdit)


        self.horizontalLayout.addWidget(self.groupBox_2)


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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search bar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Date", None))
        self.checkBox_allDates.setText(QCoreApplication.translate("MainWindow", u"All Dates", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"From Date:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Year:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Month:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Day:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To Date:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Year:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Month:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Day:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Levels", None))
        self.checkBox_allLevels.setText(QCoreApplication.translate("MainWindow", u"All Levels", None))
        self.checkBox_levelInfo.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.checkBox_levelWarning.setText(QCoreApplication.translate("MainWindow", u"WARNING", None))
        self.checkBox_levelError.setText(QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.checkBox_levelCritical.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None))
        self.checkBox_levelException.setText(QCoreApplication.translate("MainWindow", u"EXCEPTION", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Types", None))
        self.checkBox_allTypes.setText(QCoreApplication.translate("MainWindow", u"All Types", None))
        self.checkBox_typesLogin.setText(QCoreApplication.translate("MainWindow", u"Login/Logout (01)", None))
        self.checkBox_typesPLC.setText(QCoreApplication.translate("MainWindow", u"PLC (02)", None))
        self.checkBox_typesCameras.setText(QCoreApplication.translate("MainWindow", u"Cameras/Imaging (03)", None))
        self.checkBox_typesLabeling.setText(QCoreApplication.translate("MainWindow", u"Labeling (04)", None))
        self.checkBox_typesTraining.setText(QCoreApplication.translate("MainWindow", u"Training (05)", None))
        self.checkBox_typesDatabase.setText(QCoreApplication.translate("MainWindow", u"Database (06)", None))
        self.checkBox_typesOthers.setText(QCoreApplication.translate("MainWindow", u"Others (07)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Lines", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Lines", None))
        self.comboBox_linesFL.setItemText(0, QCoreApplication.translate("MainWindow", u"From Last", None))
        self.comboBox_linesFL.setItemText(1, QCoreApplication.translate("MainWindow", u"From First", None))

        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.message_label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
    # retranslateUi

