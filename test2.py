# import sys
# from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)


# class MouseTracker(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.setMouseTracking(True)

#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Mouse Tracker')
#         self.label = QLabel(self)
#         self.label.resize(200, 40)
#         self.show()

#     def mouseMoveEvent(self, event):
#         self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))
#         self.hi()

#     def hi(self):
#         print('hi')
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MouseTracker()
#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtCore import (QEvent, QTimer, Qt)
# from PyQt5.QtWidgets import (QApplication, QMenu, QWidget)
# from PyQt5.QtGui import QPainter


# class Widget(QWidget):
#     def __init__(self, parent=None):
#         super(Widget, self).__init__(parent)
#         #Initialize data

#         #Mouse double-click False
#         self.justDoubleClicked = False
#         #Key, output text, prompt message is empty
#         self.key = ""
#         self.text = ""
#         self.message = ""
#         #Set the initial size and position of the window
#         self.resize(400, 300)
#         self.move(100, 100)
#         #Set Title
#         self.setWindowTitle("Events")
#         #Slot function executed after 1 second of timer
#         QTimer.singleShot(1000, self.giveHelp)
#         # To avoid the impact of window size redrawing events, you can change parameter 0 to 3000 (3 seconds) and run it to understand what this line of code means.

#     def giveHelp(self):
#         self.text = "Click here to trigger the tracking mouse function"
#         # Redraw the event, which triggers the paintEvent function.
#         self.update()

#     '''Re-implement Close Event'''
#     def closeEvent(self, event):
#         print("Closed")

#     '''Re-implement Context Menu Events'''
#     def contextMenuEvent(self, event):
#         #Instantiate menu, add submenu one two and add shortcut function, associate slot function
#         menu = QMenu(self)
#         oneAction = menu.addAction("&One")
#         twoAction = menu.addAction("&Two")
#         oneAction.triggered.connect(self.one)
#         twoAction.triggered.connect(self.two)

#         #If message is empty, execute
#         if not self.message:
#             #Add a dividing line to the menu
#             menu.addSeparator()
#             #Add from menu 3, associated slot function
#             threeAction = menu.addAction("Thre&e")
#             threeAction.triggered.connect(self.three)
#         #Menu bar appears at mouse position
#         menu.exec_(event.globalPos())

#     '''Context Menu Slot Function'''
#     def one(self):
#         self.message = "Menu option One"
#         self.update()

#     def two(self):
#         self.message = "Menu option Two"
#         self.update()

#     def three(self):
#         self.message = "Menu option Three"
#         self.update()

#     '''Re-implement Drawing Events'''
#     def paintEvent(self, event):
#         text = self.text
#         i = text.find("\n\n")
#         if i >= 0:
#             text = text[0:i]

#         # If a keyboard button is triggered, the button information is recorded in the text message.
#         if self.key:
#             text += "\n\n You pressed: {0}".format(self.key)

#         painter = QPainter(self)

#         painter.setRenderHint(QPainter.TextAntialiasing)

#         # Draw the contents of the information text
#         painter.drawText(self.rect(), Qt.AlignCenter, text)

#         # If the message text exists, draw the message centered at the bottom, empty the message text and redraw it after 5 seconds.
#         if self.message:
#             #Displays text, coordinates, alignment at a given coordinate.Text Content
#             painter.drawText(self.rect(), Qt.AlignBottom | Qt.AlignHCenter,
#                              self.message)
#             #Five seconds later triggers a function to empty information and redraw the event
#             QTimer.singleShot(5000, self.clearMessage)
#             QTimer.singleShot(5000, self.update)

#     '''Slot function to empty message text'''
#     def clearMessage(self):
#         self.message = ""

#     '''Re-implement resize window event'''
#     def resizeEvent(self, event):
#         self.text = "Resize the window to: QSize({0}, {1})".format(
#             event.size().width(), event.size().height())
#         self.update()

#     '''Re-implement Mouse Release Event'''
#     def mouseReleaseEvent(self, event):
#         # Do not track mouse movement if mouse release is double-click release
#         if self.justDoubleClicked:
#             self.justDoubleClicked = False
#         # If the mouse releases on click release, the state of the tracking function needs to be changed. If the tracking function is turned on, tracking will occur. If the tracking function is not turned on, tracking will not occur.
#         else:
#             # click the mouse
#             self.setMouseTracking(not self.hasMouseTracking())
#             if self.hasMouseTracking():
#                 self.text = "Turn on mouse tracking.\n" + \
#                             "Please move the mouse!\n" + \
#                             "Click the mouse to turn off this feature"
#             else:
#                 self.text = "Turn off mouse tracking.\n" + \
#                             "Click the mouse to turn this on"
#             self.update()

#     '''Re-implement Mouse Move Event'''
#     def mouseMoveEvent(self, event):
#         #Execute without double mouse click
#         if not self.justDoubleClicked:
#             # Convert window coordinates to screen coordinates
#             globalPos = self.mapToGlobal(event.pos())
#             self.text = """Mouse position:
#             Window coordinates are: QPoint({0}, {1}) 
#             Screen coordinates are: QPoint({2}, {3}) """.format(event.pos().x(), event.pos().y(), globalPos.x(), globalPos.y())
#             self.update()

#     '''Re-implement mouse double-click event'''
#     def mouseDoubleClickEvent(self, event):
#         self.justDoubleClicked = True
#         self.text = "You double-clicked the mouse"
#         self.update()

#     '''Re-implement keyboard press events'''
#     def keyPressEvent(self, event):
#         self.key = ""
#         if event.key() == Qt.Key_Home:
#             self.key = "Home"
#         elif event.key() == Qt.Key_End:
#             self.key = "End"
#         elif event.key() == Qt.Key_PageUp:
#             if event.modifiers() & Qt.ControlModifier:
#                 self.key = "Ctrl+PageUp"
#             else:
#                 self.key = "PageUp"
#         elif event.key() == Qt.Key_PageDown:
#             if event.modifiers() & Qt.ControlModifier:
#                 self.key = "Ctrl+PageDown"
#             else:
#                 self.key = "PageDown"
#         elif Qt.Key_A <= event.key() <= Qt.Key_Z:
#             if event.modifiers() & Qt.ShiftModifier:
#                 self.key = "Shift+"
#             self.key += event.text()
#         #Draw a character if the key has a character and is not empty
#         if self.key:
#             self.key = self.key
#             self.update()
#         #Otherwise continue monitoring the event
#         else:
#             QWidget.keyPressEvent(self, event)

#     '''Re-implement other events, applicable to PyQt In the absence of a handler for this event, Tab Key will not be passed to because it involves focus switching keyPressEvent，Therefore, it needs to be redefined here.'''
#     def event(self, event):
#         #If a key is pressed and the key is tab
#         if (event.type() == QEvent.KeyPress and
#                     event.key() == Qt.Key_Tab):
#             self.key = "stay event()Capture in Tab key"
#             self.update()
#             return True
#         return QWidget.event(self, event)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = Widget()
#     form.show()
#     app.exec_()

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)

class Canvas(QtWidgets.QLabel):
    
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
        
class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()