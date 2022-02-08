from PySide6.QtCore import *
from consts.mouse_events import EVENTS_TYPE




WIDGET_NAME = {'down_side_technical', 'down',
               'up_side_technical', 'up'}



class Mouse:

    def __init__(self):
        self.status = ''
        self.x = 0
        self.y = 0
        self.rx = 0
        self.ry = 0

    def mouse_event(self, widget, function):
        def func(e):
            
            self.x, self.y = e.x(), e.y()
            self.rx, self.ry = self.x /  widget.width() , self.y /  widget.height() 

            self.rx = min(max(self.rx,0),1)
            self.ry = min(max(self.ry,0),1)

            self.status = EVENTS_TYPE[e.type()]
            widget_name = widget.objectName()
            function( widget_name)
    
        return func


    def connet(self, widget, function):
        widget.mouseMoveEvent = self.mouse_event(widget, function)

        #return func

    def connet_dbclick(self, widget, function):
        widget.mouseDoubleClickEvent = self.mouse_event(widget, function)


    def get_position(self):
        return self.x, self.y

    def get_relative_position(self):
        return self.rx,self.ry
    
    def get_status(self):
        return self.status
