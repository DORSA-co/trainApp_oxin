
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
from main_UI import UI_main_window 
import api
from Sheet_loader_win.data_loader_UI import data_loader

import cv2
from platform import python_version



ui, _ = loadUiType("UI/welcome_page.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class UI_welcome_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

    def __init__(self):

        super(UI_welcome_window, self).__init__()

        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.line_username.setText('root2')
        self.line_password.setText('root')
        self.seuccess_image=cv2.imread('UI/images/success.png')
        self.eror_image=cv2.imread('UI/images/warning.png')
        # self.label_9.setStyleSheet('background-color:Transparent;')
        # self.eror_image='asd'
        # print('asdwdawd',self.eror_image)
   
        self.load_dataset_parms()
        self.load_programs()
        self.check_btn.clicked.connect(self.load_dataset_parms)
        self.run_btn.clicked.connect(self.test)

        self.timer_run = QTimer(self)
        self.timer_run.timeout.connect(self.timer_run_program)
        self.timer_run.start(1000) 
        self.timer=2
        # self.eror = False
        

    def test(self):
        self.load_dataset_parms()
        self.load_programs()
        self.timer_run_program()

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

        try:
            python_ver=python_version()
            self.label_4.setText(python_ver)
            
            self.set_image_label(self.label_3, self.seuccess_image)
    
        except:
            
            self.label_4.setText('python Eror')
            self.set_image_label(self.label_3,self.eror_image)
            self.timer=-1 
            # self.run_btn.setDisabled(True)
            self.eror=True

        try:
            import tensorflow as tf
            tf_ver=tf. __version__
            self.label_12.setText(tf_ver)
            self.set_image_label(self.label_5, self.seuccess_image)


        except:
            
            self.label_6.setText('Tensor Eror')
            self.set_image_label(self.label_5, self.eror_image) 
            self.timer=-1 
            self.eror=True 

        try:
            gpu_names=tf.test.gpu_device_name()
            if gpu_names!='':
                self.label_8.setText(gpu_names)
                self.set_image_label(self.label_7, self.seuccess_image)
            else:
                self.label_8.setText('Gpu Not Found')
                self.set_image_label(self.label_7, self.eror_image)

        except:
            
            self.label_8.setText('Gpu Eror')
            self.set_image_label(self.label_7, self.eror_image) 
            self.timer=-1      


        # try:
        try:
            self.other_libs()
        except:
            self.label_10.setText('Packages Eror')



    def other_libs(self):
        import io
        file1 = io.open("requirements.txt", mode="r", encoding='utf-16-le')
        print(file1)
        Lines = file1.readlines()
        cou=0
        count = 0
        import importlib
        lis=[]
        # Strips the newline character
        for line in Lines:
            count += 1
            libs=(line.strip().split("="))[0]
            print(libs)
            # try:
            #     eval('import {}'.format(libs))
            # except:
            #     cou+=1
            #     print(cou)

            
            spam_spec = importlib.util.find_spec(libs)
            found = spam_spec is not None
            print(found)

            if not found:

                lis.append(line)


        print('lis',lis)
        self.label_10.setToolTip(str(lis))
        if len(lis)>5:
            self.label_10.setText('Packages Not found')
            self.set_image_label(self.label_9, self.eror_image) 
        else :
            self.label_10.setText('Packages Done')
            self.set_image_label(self.label_9, self.seuccess_image) 


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
            # self.timer_run.stop()
            # self.run_btn.setDisabled(True)
            self.eror=True
            print('self.eror',self.eror)
            self.timer=-1



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
            self.eror=False
        else:
            self.show_eror_sql.setText(str(str(eror_count)+' '+eror_text))
            self.show_eror_sql.setStyleSheet("color:red")
            # self.timer_run.stop()
            self.check_btn.setDisabled(True)
            # self.run_btn.setDisabled(True)
            self.eror=True
            print(self.eror,self.eror)
        str1=''    
        # for i in check_list:
        #     str1 = str1 + '\n'+ str(check_list[i])   

        # self.textEdit_sql.setText(str(str1))




    def timer_run_program(self):

        if self.timer>0:

            self.run_btn.setText(str('Run Train App  ('+str(self.timer)+')'))
            self.timer-=1
        else :
            self.timer_run.stop()
            print('else',self.eror)
            if self.eror==False:

                self.run_btn.setText(str('Run Train App  ('+str(self.timer)+')'))
                # ui, _ = loadUiType("UI/oxin.ui")
                # self.asdw = U_main_window()
                
                # api = api.API(win2)
                self.close()
                # self.asdw.show()
                # self.load_sheets_win = data_loader()
                # print(self.asdw)
                # self.load_sheets_win.show()
                b=hasan()
                # sys.exit()
                b.a()
                # self.asdw.show()
                # app = QtWidgets.QApplication(sys.argv) 
                # openIcon_p = QtGui.QPixmap(win2)
                
            

    

class hasan():
    def a(self):
        print('asdaw')
        os.system('python .\main_UI.py')




if __name__ == "__main__":
    app = QApplication()
    win = UI_welcome_window()
    win.show()
    sys.exit(app.exec())
