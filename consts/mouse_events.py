
from PySide6.QtCore import QEvent

EVENTS_TYPE={

    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release',
    QEvent.Type.MouseButtonDblClick: 'mouse_dclick'
}