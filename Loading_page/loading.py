from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QMovie, Qt
import sys

ui, _ = loadUiType('Loading_page/loading.ui')

class Loading_UI(QWidget, ui):
    global widgets
    widgets = ui

    def __init__(self) -> None:
        super(Loading_UI, self).__init__()
        self.setupUi(self)

        self.center()

        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.movie = QMovie("Loading_page/loading1.gif")
        self.gif_label.setMovie(self.movie)

        self.set_text('Please Waite ...')
  
        self.startAnimation()

    def set_text(self, text):
        self.label.setText(text)

    def close_win(self):
        self.close()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())

    def startAnimation(self):
        self.movie.start()
  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()


if __name__ == "__main__":
    app = QApplication()
    win = Loading_UI()
    win.show()
    sys.exit(app.exec())