from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal

class storage_worker(sQObject):
    """this class is worker for storage Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()

    def assign_parameters(self, storage_api_obj):
        self.s_api = storage_api_obj

    def run(self):
        try:
            self.s_api.update_charts()
            self.s_api.check_disks()
            self.finished.emit()
        except:
            self.finished.emit()