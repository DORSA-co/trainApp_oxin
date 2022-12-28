from PySide6.QtCore import *

EVENTS_TYPE={

    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release',
    QEvent.Type.MouseButtonDblClick: 'mouse_dclick'
}



WIDGET_NAME = {'down_side_technical', 'down',
               'up_side_technical', 'up'}



class Keyboard:

    def __init__(self):
        self.key = ''


    def connet(self, ui, keys, functions, page_name):
        ui.connet_keyboard( keys,functions, page_name)


