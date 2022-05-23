
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
import PySide6.QtGui as PG
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
from PySide6.QtWidgets import QMessageBox as sQMessageBox
from PySide6.QtGui import QPixmap as sQPixmap 
from PySide6.QtGui import QIcon as sQIcon
from PySide6.QtGui import QIntValidator as sQIntValidator
import database_utils


import cv2
from platform import python_version



ui, _ = loadUiType("UI/welcome_page.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

    def __init__(self):

        super(UI_main_window, self).__init__()

        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.line_username.setText('root')
        self.line_password.setText('root')
        self.seuccess_image=cv2.imread('UI/images/success.png')
        self.eror_image=cv2.imread('UI/images/x-mark.png')
        # self.eror_image='asd'
        # print('asdwdawd',self.eror_image)
   
        self.load_dataset_parms()
        self.load_programs()
        self.check_btn.clicked.connect(self.load_dataset_parms)

        self.timer_run = QTimer(self)
        self.timer_run.timeout.connect(self.timer_run_program)
        self.timer_run.start(1000) 
        self.timer=10


        

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)

    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()
        sys.exit()


    def set_image_label(self,label_name, img):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = sQImage(img.data, w, h, bytes_per_line, sQImage.Format_BGR888)


        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

    def load_programs(self):

        # try:
        python_ver=python_version()
        self.label_4.setText(python_ver)
        
        self.set_image_label(self.label_3, self.seuccess_image)
    
        # except:
            
        #     self.label_4.setText('python Eror')
        #     self.set_image_label(self.label_3,self.eror_image)

        try:
            import tensorflow as tf
            tf_ver=tf. __version__
            self.label_6.setText(tf_ver)
            
            self.set_image_label(self.label_5, self.seuccess_image)
        
        except:
            
            self.label_6.setText('Tensor Eror')
            self.set_image_label(self.label_5, self.eror_image)          



    def load_dataset_parms(self):

        user_name=self.line_username.text()
        password=self.line_password.text()

        self.db = database_utils.dataBaseUtils(user_name,password)

        ret=self.db.check_connection()
        if ret:
            self.check_dataset_tables()
        else:
            self.show_eror_sql.setText('Connection Eror')
            self.show_eror_sql.setStyleSheet("color:red") 



    def check_dataset_tables(self):
        # self.db.get_table_names()
        # text = self.lineEdit_sql.text()
        parms=self.db.__dict__
        check_list=[]
        list_parms=list(parms.values())[1:]
        eror_text='All Table exist'
        eror_count=0
        for i in range(len(list_parms)):
            ret=self.db.check_table_exist(list_parms[i])
            print('ret',ret)
            if ret:
                check_list.append(str(list_parms[i]+' : '+ret))
            else:
                check_list.append(str('Eror reading data from :'+list_parms[i]))
                eror_text='Not Found'
                eror_count+=1


        print(check_list)
        listToStr = ' \n'.join(map(str, check_list))
        print(listToStr)
        self.textEdit_sql.setText(listToStr)
        if eror_count==0:
            self.show_eror_sql.setText(eror_text)
            self.show_eror_sql.setStyleSheet("color:green")
        else:
            self.show_eror_sql.setText(str(str(eror_count)+' '+eror_text))
            self.show_eror_sql.setStyleSheet("color:red")
        str1=''    
        # for i in check_list:
        #     str1 = str1 + '\n'+ str(check_list[i])   

        # self.textEdit_sql.setText(str(str1))




    def timer_run_program(self):

        if self.timer>0:

            self.run_btn.setText(str('Run Train App  ('+str(self.timer)+')'))
            self.timer-=1
        else :
            self.run_btn.setText(str('Run Train App  ('+str(self.timer)+')'))
            self.timer_run.stop()






if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    win.show()
    sys.exit(app.exec())
