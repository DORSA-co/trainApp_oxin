from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pandas as pd

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,30,600,400)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 90))  
        qp.setBrush(br)   
        qp.drawRect(QtCore.QRec(self.begin, self.end))       

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        

    # def mouseReleaseEvent(self, event):
    #     self.begin = event.pos()
    #     self.end = event.pos()
    #     self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())

# class Window(QMainWindow):

#     def __init__(self):

#         super().__init__()
#         self.image = QImage('1.jpg')
#         #self.showFullScreen()
#         self.startPos = None
#         self.rect = QRect()
#         self.drawing = False

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton and not self.drawing:
#             self.startPos = event.pos()
#             self.rect = QRect(self.startPos, self.startPos)
#             self.drawing = True
#             self.update()

#     def mouseMoveEvent(self, event):
#         if self.drawing == True:
#             self.rect = QRect(self.startPos, event.pos())
#             self.update()

#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.drawing = False

#     def paintEvent(self, event):

#         pen = QtGui.QPen()
#         pen.setWidth(3)
#         pen.setColor(QtGui.QColor(255, 0, 0))

#         brush = QtGui.QBrush()
#         brush.setColor(QtGui.QColor(255, 0, 0))
#         brush.setStyle(Qt.SolidPattern)

#         painter = QPainter(self)
#         painter.drawImage(0, 0, self.image)
#         painter.setBrush(brush)
#         painter.setPen(pen)
#         if not self.rect.isNull():
#             painter.drawRect(self.rect)
#         painter.end()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = Window()
#     # window.show()
#     # app.aboutToQuit.connect(app.deleteLater)
#     sys.exit(app.exec())