from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
import texts
from Loading_page import loading

class loading_worker(sQObject):
    finished = sSignal()

    def __init__(self) -> None:
        super().__init__()

        self.loading_page = loading.Loading_UI()

    def show_win(self, text):
        print('start'*10)
        self.loading_page.set_text(text)

        self.loading_page.show()

    def close_win(self):
        print('close'*10)
        self.loading_page.close_win()
        self.finished.emit()