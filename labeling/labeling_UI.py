import enum
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
import pandas as pd

from PyQt5.QtGui import QPainter
from labeling import labeling_api
# import labeling_api
ui, _ = loadUiType("UI/labeling.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class labeling(QMainWindow, ui):
    """This is a class for labeling user interface. It helps users to select defect class for defective regions.  
    """
    global widgets
    widgets = ui
    x=0

    def __init__(self):
        """Constructor method.
        """
        super(labeling, self).__init__()
        # Set ui.
        self.setupUi(self)
        # Set flags. window is frameless and always stay on top of other windows.
        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        # Find and save position of window.
        self.pos_ = self.pos()
        # Connect buttons.
        self.activate_()
        # Set geometry of window.
        self.win_set_geometry()
        # Set old position to None.
        self._old_pos = None

        self.comboBox_defects.setEditable(True) 
        self.comboBox_defects.completer().setCompletionMode(QCompleter.PopupCompletion) 
        self.comboBox_defects.setInsertPolicy(QComboBox.NoInsert) 

    def mousePressEvent(self, event):
        """Reimplemented function to receive mouse press events.

        :param event: Received event for mouse press.
        :type event: QMouseEvent
        """
        # Update old position if mouse left button pressed.
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        """Reimplemented function to receive mouse release events.

        :param event: Received event for mouse release.
        :type event: QMouseEvent
        """
        # Set old position to None if mouse left button released.
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        """Reimplemented function to receive mouse move events.

        :param event: Received event for mouse move.
        :type event: QMouseEvent
        """
        # Move window as mouse move if old position is not None.
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def activate_(self):
        """Connect buttons clicked signal to approprate slots.
        """
        # Connect cancel button to slot that close window.
        self.cancel_btn.clicked.connect(self.close_win)
        # Connect save button to slot that minimize window.
        self.save_btn.clicked.connect(self.minimize)
        # self.maxiButton.clicked.connect(self.maxmize_minimize)

    def win_set_geometry(self,left=100, top=600, width=250, height=130):
        """Set geometry of window.

        :param left: X position of window, defaults to 100
        :type left: int, optional
        :param top: Y position of window, defaults to 600
        :type top: int, optional
        :param width: Width of window, defaults to 250
        :type width: int, optional
        :param height: Height of window, defaults to 130
        :type height: int, optional
        """
        self.setGeometry(left, top, width, height)

    def minimize(self):
        """Minimize window.
        """
        self.showMinimized()

    def close_win(self):
        """Close window.
        """
        self.close()

    def set_combobox(self,defects_list):
        """Set items of combobox.

        :param defects_list: List of defect classes that should set to combobox.
        :type defects_list: list
        """
        self.comboBox_defects.addItems(defects_list)
    
    def set_on_top(self):
        """ Set window FramelessWindowHint and WindowStaysOnTopHint flags.
        """
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        # self.show()
        print('set_on_top')

    def updte_table(self,records):
        """Set defect class information into table.

        :param records: Defect class information.
        :type records: dict
        """
        # self.clear_table()                                                  #cleare table

        self.tableWidget_defects.setRowCount(1)           #set row count

        self.hh_Labels=['name', 'defect_ID', 'is_defect', 'groupp','level']
        self.tableWidget_defects.setHorizontalHeaderLabels(self.hh_Labels)
        table_item = QTableWidgetItem(str(records))

        print('roeasdawd',records[self.hh_Labels[1]])

        # Set informations to each columns.
        for row in range(len(self.hh_Labels)):
            
            table_item = QTableWidgetItem(records[self.hh_Labels[row]])
            # table_item.setData(Qt.DisplayRole, record)
            self.tableWidget_defects.setItem(0,row,table_item)
        #     print('eror')

    def get_label_name(self):
        """Get current selected defect classs from combobox.

        :return: Current selected defect classs
        :rtype: str
        """
        return self.comboBox_defects.currentText()


#api = labeling_api.labeling_API(win)



if __name__ == "__main__":
    app = QApplication()
    win = labeling()
    api = labeling_api.labeling_API(win)
    win.show()
    sys.exit(app.exec())
    