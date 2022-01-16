
from PySide6.QtCore import *
from backend import data_grabber

EVENTS_TYPE={

    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release'
}


class API:

    def __init__(self,ui):
        self.ui = ui
        
        self.ui.down_side_technical.mouseMoveEvent = self.mouseevent(self.ui.down_side_technical)
        self.ui.down_side_technical.mouseReleaseEvent = self.mouseevent(self.ui.down_side_technical)

        self.ui.up_side_technical.mouseMoveEvent = self.mouseevent(self.ui.up_side_technical)
        self.ui.up_side_technical.mouseReleaseEvent = self.mouseevent(self.ui.up_side_technical)

        self.load_sheet()
    
    def mouseevent(self,widget):

        def func(e):
            
            x = e.x() / widget.width()
            y = e.y() / widget.height()
            x = min(max(x,0),1)
            y = min(max(y,0),1)
            self.x=x
            self.y=y
            self.status = EVENTS_TYPE[e.type()]
            self.widget_name = widget.objectName()
            # print(self.x,self.y,self.widget_name,self.status)


            if self.widget_name=="down_side_technical" and self.status=="mouse_move":
                self.update_sheet_real_img('down',(self.x,self.y))


    


        return func


    def update_sheet_real_img(self,side,pt):
        if side=="down":
            self.obj_sheet_down.update_pointer(pt)
            real_img = self.obj_sheet_down.get_real_img()
            self.update_sheet_img()
            self.ui.set_crop_image(real_img)



    def load_sheet(self):
        self.obj_sheet_up=data_grabber.sheetOverView('G:\oxin_image_grabber/001',
                                                data_grabber.UP,(1000,298),(20,12),actives_camera=(0,12),
                                                oriation=data_grabber.VERTICAL)

        self.obj_sheet_down=data_grabber.sheetOverView('G:\oxin_image_grabber/001',
                                                data_grabber.DOWN,(1000,298),(20,12),actives_camera=(0,12),
                                                oriation=data_grabber.VERTICAL)

        self.obj_sheet_down.update_line(20)
        self.obj_sheet_up.update_line(20)
        self.update_sheet_img()


    def update_sheet_img(self):
        img=self.obj_sheet_down.get_sheet_img()
        self.ui.set_img_sheet(img,"down")


    def sheet_top_img():
        pass


