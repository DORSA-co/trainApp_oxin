
from PySide6.QtCore import QEvent
from PySide6 import QtCore
EVENTS_TYPE={

    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release',
    QEvent.Type.MouseButtonDblClick: 'mouse_dclick',
}


BUTTONS = {

    QtCore.Qt.LeftButton:'left_btn',
    QtCore.Qt.RightButton:'right_btn'
}