from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QMovie, Qt
import sys

ui, _ = loadUiType('Loading_page/loading.ui')

class Loading_UI(QWidget, ui):
    global widgets
    widgets = ui

    def __init__(self, lang) -> None:
        super(Loading_UI, self).__init__()
        self.setupUi(self)

        self.center()

        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.movie = QMovie("Loading_page/loading6.gif")
        self.gif_label.setMovie(self.movie)

        if lang == 'en':
            self.set_text('Please Waite ...')
        else:
            self.set_text('لطفا منتظر بمانید...')
  
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
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        win = Loading_UI(sys.argv[1])
    else:
        win = Loading_UI('en')
    win.show()
    sys.exit(app.exec())