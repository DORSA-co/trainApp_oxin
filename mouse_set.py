from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
def mouse(self):
    labels=[self.Data_auquzation_btn]
    for i in range(len(labels)):
        self.Data_auquzation_btn.setCursor(Qt.UpArrowCursor)