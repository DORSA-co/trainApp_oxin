import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

from PyQt5.QtWidgets import QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem,QColor,QFont
import cv2
import os

try:
    import texts
except:
    pass

ui, _ = loadUiType("UI/help.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class help(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self, lang='en'):
        super(help, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        title = "SENSE-Help"
        self.setWindowTitle(title)

        self.activate_()
        self.font_size=self.spinBox_font.value()
        self.language = lang
        self.win_set_geometry()
        self.center()
        self._old_pos = None
        self.statusBar().setMaximumHeight(5)
        self.statusBar().setStyleSheet('background-color:rgb(85, 0, 0);')
        self.set_tree_view()
        
        self.spinBox_font.valueChanged.connect(self.set_font)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        if not self.isMaximized():
            self.move(self.pos() + delta)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    def win_set_geometry(self, left=50, top=300, width=350, height=20):
        height=350
        width=550
        top=10
        left=10
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()
    
    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def set_font(self):
        self.font_size=self.spinBox_font.value()
        style='font-size: {}pt;background-color: rgb(220, 220,220);border-color: rgb(188, 188, 188);'.format(self.font_size)
        # style.relace(''','"')
        self.centralwidget.setStyleSheet(style)
        self.set_tree_view()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        ##print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)
        
    def set_text(self, text):
        self.textEdit.clear()
        self.textEdit.setText(text)
    
    def set_language(self, lang):
        self.language = lang
        texts.set_help_title(self, lang)
        self.set_tree_view()

    def set_tree_view(self):
        self.treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()


        # main_software
        main_software = StandardItem(texts.Titles['Train Software'][self.language], self.font_size+2, set_bold=True)

        # ---------------------------Data Aquization-------------------------------
        Data_Aquization = StandardItem(texts.Titles['Data Auquzation'][self.language], self.font_size+1)
        main_software.appendRow(Data_Aquization)
        Live_tab = StandardItem(texts.Titles['Live'][self.language], self.font_size, color=QColor(155, 0, 0))
        Technical_view_tab = StandardItem(texts.Titles['Technical View'][self.language], self.font_size, color=QColor(155, 0, 0))
        Data_Aquization.appendRow(Live_tab)
        Data_Aquization.appendRow(Technical_view_tab)

        # ---------------------------Label-------------------------------
        Label = StandardItem(texts.Titles['Label'][self.language], self.font_size+1)
        main_software.appendRow(Label)
        austin = StandardItem(texts.Titles['Label'][self.language], self.font_size, color=QColor(155, 0, 0))
        Label.appendRow(austin)
        # ---------------------------Tuning-------------------------------
        tuning = StandardItem(texts.Titles[' Tuning'][self.language], self.font_size+1)
        main_software.appendRow(tuning)
        binary = StandardItem(texts.Titles['Binary'][self.language], self.font_size)
        tuning.appendRow(binary)

        localization = StandardItem(texts.Titles['Localization'][self.language], self.font_size)
        tuning.appendRow(localization)

        classification = StandardItem(texts.Titles['Classification'][self.language], self.font_size)
        tuning.appendRow(classification)

        yolo = StandardItem(texts.Titles['Yolo2'][self.language], self.font_size)
        tuning.appendRow(yolo)

        b_list = StandardItem(texts.Titles['binary_list'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        binary.appendRow(b_list)
        b_training = StandardItem(texts.Titles['binary_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        binary.appendRow(b_training)
        b_history = StandardItem(texts.Titles['binary_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        binary.appendRow(b_history)

        l_training = StandardItem(texts.Titles['localization_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        localization.appendRow(l_training)

        l_history = StandardItem(texts.Titles['localization_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        localization.appendRow(l_history)

        c_list = StandardItem(texts.Titles['classes_list'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        classification.appendRow(c_list)
 
        # c_training = StandardItem(texts.Titles['classification_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        # classification.appendRow(c_training)

        # c_history = StandardItem(texts.Titles['classification_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        # classification.appendRow(c_history)

        y_training = StandardItem(texts.Titles['yolo_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        yolo.appendRow(y_training)

        y_history = StandardItem(texts.Titles['yolo_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        yolo.appendRow(y_history)

        # ---------------------------Pipline Build Test-------------------------------
        pipline_m = StandardItem(texts.Titles['Pipline Build & Test'][self.language], self.font_size+1)
        main_software.appendRow(pipline_m)

        Pipline = StandardItem(texts.Titles['Pipline'][self.language], self.font_size, color=QColor(155, 0, 0))
        pipline_m.appendRow(Pipline)

        load_dataset = StandardItem(texts.Titles['Load Dataset'][self.language], self.font_size, color=QColor(155, 0, 0))
        pipline_m.appendRow(load_dataset)

        History = StandardItem(texts.Titles['history'][self.language], self.font_size, color=QColor(185, 0, 0))
        pipline_m.appendRow(History)


        # ---------------------------User Page-------------------------------
        user_profile = StandardItem(texts.Titles['User Profile'][self.language], self.font_size+1)
        main_software.appendRow(user_profile)

        create_data = StandardItem(texts.Titles['create_new_ds'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(create_data)
        all_dataset = StandardItem(texts.Titles['all_ds'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(all_dataset)
        my_data = StandardItem(texts.Titles['my_ds'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(my_data)
        my_pipline = StandardItem(texts.Titles['pipelines'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(my_pipline)

        # ---------------------------Settings Page-------------------------------
        settings = StandardItem(texts.Titles['settings'][self.language], self.font_size+1)
        main_software.appendRow(settings)
        austin = StandardItem(texts.Titles['settings'][self.language], self.font_size, color=QColor(155, 0, 0))
        settings.appendRow(austin)

        # ---------------------------LoadSheet Page-------------------------------
        load_sheet = StandardItem(texts.Titles['load_sheet'][self.language], self.font_size+1)
        main_software.appendRow(load_sheet)
        austin = StandardItem(texts.Titles['load_sheet'][self.language], self.font_size, color=QColor(155, 0, 0))
        load_sheet.appendRow(austin)

        # ---------------------------Image Enlargement Page-------------------------------
        image_enlargement = StandardItem(texts.Titles['image_enlargement'][self.language], self.font_size+1)
        main_software.appendRow(image_enlargement)
        austin = StandardItem(texts.Titles['image_enlargement'][self.language], self.font_size, color=QColor(155, 0, 0))
        image_enlargement.appendRow(austin)

        # ---------------------------Show Logs Page-------------------------------
        show_logs = StandardItem(texts.Titles['show_logs'][self.language], self.font_size+1)
        main_software.appendRow(show_logs)
        austin = StandardItem(texts.Titles['show_logs'][self.language], self.font_size, color=QColor(155, 0, 0))
        show_logs.appendRow(austin)

        # settings_page = StandardItem(texts.Titles['settings_page'][self.language], self.font_size, color=QColor(155, 0, 0))
        # settings.appendRow(settings_page)

        # # setting_software 
        # setting_software = StandardItem(texts.Titles['Setting Software'][self.language], self.font_size+2, set_bold=True)

        # Dashboard = StandardItem(texts.Titles['page_dashboard'][self.language], self.font_size+1)
        # Camera = StandardItem(texts.Titles['page_camera'][self.language], self.font_size+1)
        # PLC = StandardItem(texts.Titles['page_plc'][self.language], self.font_size+1)
        # Level2 = StandardItem(texts.Titles['page_level2'][self.language], self.font_size+1)
        # Defection = StandardItem(texts.Titles['page_defection'][self.language], self.font_size+1)
        # Calibration = StandardItem(texts.Titles['page_calibration'][self.language], self.font_size+1)
        # Setting = StandardItem(texts.Titles['page_settings'][self.language], self.font_size+1)
        # Storage = StandardItem(texts.Titles['page_storage'][self.language], self.font_size+1)
        # User = StandardItem(texts.Titles['page_users'][self.language], self.font_size+1)

        # PLC = StandardItem('PLC', self.font_size+1)
        # PLC = StandardItem('Storage', self.font_size+1)
        # Level2 = StandardItem('Level2', self.font_size+1)
        # Defection = StandardItem('Defection', self.font_size+1)
        # Calibration = StandardItem('Calibration', self.font_size+1)
        # PLC = StandardItem('User', self.font_size+1)
        # Setting = StandardItem('Setting', self.font_size+1)
        # setting_software.appendRows([Dashboard, Camera, PLC,Calibration,Level2,Defection,Storage,User,Setting])


        rootNode.appendRow(main_software)

        self.treeView.setModel(treeModel)
        self.treeView.expandAll()
        self.treeView.doubleClicked.connect(self.getValue)

    def getValue(self, val):
        self.set_help(val.data())

    def set_help(self, name):
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Train Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

        help_image = None
        text = ''
        if name==texts.Titles['Live'][self.language]:
            help_image = cv2.imread(texts.HELPS_ADDRESS['LIVE_PAGE'][self.language])
            text = texts.HELPS['LIVE_PAGE'][self.language]
        elif name ==texts.Titles['Technical View'][self.language]:
            text = texts.HELPS['TECHNICAL_PAGE'][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS['TECHNICAL_PAGE'][self.language])
        elif name==texts.Titles['Label'][self.language]:
            text = texts.HELPS['LABEL_PAGE'][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS['LABEL_PAGE'][self.language])
        # elif name=='page_user_profile':
        #     stack_name = self.stackedWidget_2.currentWidget().objectName()
        elif name ==texts.Titles['create_new_ds'][self.language] :
            text = texts.HELPS['PROFILE_CREATEDS_PAGE'][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS['PROFILE_CREATEDS_PAGE'][self.language])
        elif name ==texts.Titles['all_ds'][self.language] :
            text = texts.HELPS['PROFILE_ALLDS_PAGE'][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS['PROFILE_ALLDS_PAGE'][self.language])
        elif name ==texts.Titles['my_ds'][self.language]:
            text = texts.HELPS['PROFILE_MYDS_PAGE'][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS['PROFILE_MYDS_PAGE'][self.language])
        elif name ==texts.Titles['pipelines'][self.language]:
            text = texts.HELPS['PROFILE_MYPIP_PAGE'][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS['PROFILE_MYPIP_PAGE'][self.language])
        elif name==texts.Titles['Pipline'][self.language]:
            text = texts.HELPS["PBT_PIPLINE_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["PBT_PIPLINE_PAGE"][self.language])
        elif name==texts.Titles['Load Dataset'][self.language]:
            text = texts.HELPS["PBT_LOADDATASET_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["PBT_LOADDATASET_PAGE"][self.language])
        elif name==texts.Titles['History'][self.language]:
            text = texts.HELPS["PBT_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["PBT_HISTORY_PAGE"][self.language])
        elif name == texts.Titles['binary_list'][self.language]:
            text = texts.HELPS["BINARYLIST_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["BINARYLIST_PAGE"][self.language])
        elif name == texts.Titles['binary_training'][self.language]:
            text = texts.HELPS["BINARY_TRAINING_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["BINARY_TRAINING_PAGE"][self.language])
        elif name == texts.Titles["binary_history"][self.language]:
            text = texts.HELPS["BINARY_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["BINARY_HISTORY_PAGE"][self.language])
        elif name == texts.Titles['localization_training'][self.language]:
            text = texts.HELPS["LOC_TRAINING_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["LOC_TRAINING_PAGE"][self.language])
        elif name == texts.Titles['localization_history'][self.language]:
            text = texts.HELPS["LOC_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["LOC_HISTORY_PAGE"][self.language])
        elif name == texts.Titles['yolo_training'][self.language]:
            text = texts.HELPS["YOLO_TRAINING_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["YOLO_TRAINING_PAGE"][self.language])
        elif name == texts.Titles['yolo_history'][self.language]:
            text = texts.HELPS["YOLO_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["YOLO_HISTORY_PAGE"][self.language])
        elif name == texts.Titles['classes_list'][self.language]:
            text = texts.HELPS["CLASSLIST_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["CLASSLIST_PAGE"][self.language])
        # elif name=='page_Classification':
        #     stack_name = self.stackedWidget_classification.currentWidget().objectName()
        # if stack_name == 'page_classification_class_list':
        #         pass
        # elif stack_name == 'page_classification_training':
        #         pass
        # elif stack_name == 'page_classification_history':
        #         pass
        elif name == texts.Titles['settings'][self.language]:
            text = texts.HELPS["SETTINGS_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["SETTINGS_PAGE"][self.language])
        elif name == texts.Titles['load_sheet'][self.language]:
            text = texts.HELPS["LOADSHEET_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["LOADSHEET_PAGE"][self.language])
        elif name == texts.Titles['image_enlargement'][self.language]:
            text = texts.HELPS["IMAGEENLARGEMENT_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["IMAGEENLARGEMENT_PAGE"][self.language])
        elif name == texts.Titles['show_logs'][self.language]:
            text = texts.HELPS["SHOWLOGS_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["SHOWLOGS_PAGE"][self.language])


#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Setting Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

        if name == texts.Titles['page_dashboard'][self.language]:
                text = texts.HELPS["page_dashboard"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_dashboard"][self.language])

        if name == texts.Titles['page_camera'][self.language]:
                text = texts.HELPS["page_camera"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_camera"][self.language])

        if name == texts.Titles['page_defection'][self.language]:
                text = texts.HELPS["page_defection"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_defection"][self.language])

        if name == texts.Titles['page_level2'][self.language]:
                text = texts.HELPS["page_level2"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_level2"][self.language])

        if name == texts.Titles['page_calibration'][self.language]:
                text = texts.HELPS["page_calibration"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_calibration"][self.language])

        if name == texts.Titles['page_settings'][self.language]:
                text = texts.HELPS["page_settings"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_settings"][self.language])

        if name == texts.Titles['page_users'][self.language]:
                text = texts.HELPS["page_users"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_users"][self.language])

        if name == texts.Titles['page_storage'][self.language]:
                text = texts.HELPS["page_storage"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_storage"][self.language])
       
        if name == texts.Titles['page_plc'][self.language]:
                text = texts.HELPS["page_plc"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["page_plc"][self.language])
        self.set_help_image(help_image, text)

    def set_help_image(self, help_image, text):
        if help_image is not None:
            self.textEdit.setText(text)
            image = QImage(help_image, help_image.shape[1], help_image.shape[0], help_image.strides[0],
                    QImage.Format_BGR888)
            self.label.setPixmap(QPixmap.fromImage(image))


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)




if __name__ == "__main__":
    app = QApplication()
    win = help(lang='en')
    win.show()
    win.win_set_geometry(width=300, height=900)
    sys.exit(app.exec())