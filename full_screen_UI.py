
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtGui import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import os

ui, _ = loadUiType("UI/full_screen.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class full_screen_window(QMainWindow, ui):
    """
    this class initializes a confirm/message window for user. it has two buttons, yes or no, to accept or deny the operation will be done

    Inputs:
        ui: login UI object
        language: the main language for window and messages (in string)

    Outputs: None
    """
    
    global widgets
    widgets = ui


    def __init__(self, type):
        super(full_screen_window, self).__init__()

        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # removing the window frame and attache it to top
        self.pos_ = self.pos()
        self._old_pos = None
        self.setWindowFlags(flags)

        self.activate_()
        self.win_set_geometry()
        self.center()
        self._old_pos = None 

        if type=='single':
            self.stackedWidget.setCurrentWidget(
                self.page_single
            )
        elif type=='top':
            self.stackedWidget.setCurrentWidget(
                self.page_top
            )
        if type=='bottom':
            self.stackedWidget.setCurrentWidget(
                self.page_bottom
            )
        if type=='all':
            self.stackedWidget.setCurrentWidget(
                self.page_all
            )

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
        self.move(self.pos() + delta)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)
        # self.helpButton.clicked.connect(self.show_help)

    def win_set_geometry(self, left=100, top=600, width=800, height=600):
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()
    
    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        #print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)

    #def show_help(self):
    #    if not self.help_win:
    #        self.help_win = help()
    #    self.help_win.set_text('neighbouring page')
    #    self.help_win.show()


    
if __name__ == "__main__":
    app = QApplication()
    win = full_screen_window()
    win.show()
    sys.exit(app.exec())
    
