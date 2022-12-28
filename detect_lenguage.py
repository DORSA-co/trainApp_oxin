from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
# from pyqt5_plugins import *
import sqlite3
from sqlite3 import Error

from PySide6.QtCore import *

from PySide6.QtWidgets import *
def language():
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()       
    cur.execute('select * from language')
    rec = cur.fetchall()
    conn.commit()
    conn.close()    
    return str(rec[0][0])

def main_window(self):
    self.label_6.setText('شمای تکنیکال بالا')
    self.label_7.setText('شمای تکنیکال پایین')
    self.Data_auquzation_btn.setText('داده برداری')
    self.label_btn.setText('لیبل گذاری')
    self.tuning_btn.setText('تنظیمات الگوریتم ها')
    self.pbt_btn.setText('ایجاد و تست')
    self.titleLeftApp.setText('صبا')
    self.titleLeftDescription.setText('    آموزش      ')
    self.btn_about_us.setText('درباره ما')
    self.creditsLabel.setText('')
    self.btn_about_us.setText('درباره ما')
    self.btn_about_us.setText('درباره ما')
    self.btn_about_us.setText('درباره ما')
    self.btn_about_us.setText('درباره ما')
    self.btn_about_us.setText('درباره ما')
    self.btn_about_us.setText('درباره ما')
    # self.tabWidget_2.setCurrentIndex(1)
    self.label_4.setText(': تاریخ')
    self.label_10.setText(': شماره ورق')
    self.label_5.setText(': شماره دوربین')
    self.label_14.setText(': کل تصاویر لیبل زده شده ')
    self.label_15.setText(': تصاویر دارای مشکل')
    self.label_16.setText(': آیدی کاربر')
    self.label_27.setText(': عیب')
    self.yes_defect.setText('بله')
    self.label_21.setText('لیبل ها')
    self.pushButton_3.setText('ذخیره')
    self.no_defect.setText('خیر')
    self.no_defect.setText('خیر')
    self.no_defect.setText('خیر')
    self.label_22.setText('تصویر بدون عیب میباشد')
    self.load_dataset_pbt.setText('بارگذاری دیتاست')
    self.pipeline_pbt.setText('ایجاد پایپ لاین')
    self.history_pbt.setText('تاریخچه')
    self.label_120.setText('اتنخاب الگوریتم')
    self.label_121.setText('باینری')
    self.label_122.setText('جایابی')
    self.label_123.setText('دسته بندی')
    self.label_121.setText('باینری')
    self.label_22.setText('تصویر بدون عیب میباشد')
    self.binary_list.setText('باینری لیست')
    self.binary_training.setText('آموزش باینری')
    self.binary_history.setText('تاریخچه')
    self.label_137.setText('نام الگوریتم')
    self.label_138.setText('تعداد دور')
    self.label_139.setText('اندازه بچ')
    self.label_140.setText('نرخ یادگیری')
    self.pushButton_17.setText('تنظیمات حافظه')
    self.pushButton_16.setText('تنظیمات دیتابیس')
    self.pushButton_15.setText('تنظیمات کاربر')
    self.pushButton_9.setText('تنظیمات الگوریتم ها')
    self.btn_software_setting.setText('تنظیمات نرم افزار')
    self.pushButton_15.setText('تنظیمات کاربر')


    self.label_51.setText('لطفا وارد شوید')
    self.label_43.setText('نام کاربری')
    self.label_44.setText('رمز عبور')
    self.label_121.setText('باینری')


