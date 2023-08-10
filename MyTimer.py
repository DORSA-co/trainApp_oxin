from ast import arg
from curses.ascii import SI
from time import sleep
import PySide6
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from typing import Optional
import threading
import time

class MyTimer(QObject):
    timeout = Signal()

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None:
        super().__init__(parent)
        self.stop_thread = False

    def create_thread(self, msec: int) -> None:
        self.thread = threading.Thread(target=self.timer, args=(msec, ))

    def start_thread(self) -> None:
        self.thread.start()

    def join_thread(self) -> None:
        self.stop_thread = True
        self.thread.join()

    def start(self, msec: int) -> None:
        self.stop_thread = False
        self.create_thread(msec)
        self.start_thread()

    def stop(self) -> None:
        self.join_thread()

    def timer(self, msec: int):
        while True:
            if self.stop_thread:
                break
            t1 =time.time()
            sleep(msec/1000)
            
            if self.stop_thread:
                break
            self.timeout.emit()
            print(time.time()-t1)