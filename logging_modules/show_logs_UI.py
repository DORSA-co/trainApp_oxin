import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6 import QtCore as sQtCore
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from help_UI import help
import os
from backend import date_funcs
import texts
import texts_codes
import cv2

import subprocess
sys.path.append('../oxin_help')

SHAMSI_DATE = False

ui, _ = loadUiType("UI/show_logs.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class show_logs(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self, log_mainfolderpath='./app_logs', lang='en'):
        super(show_logs, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        title = "SENSE-Log Viewer"
        self.setWindowTitle(title)
        # annotated image
        self.activate_()
        self.center()
        self._old_pos = None

        self.help_win = None
        
        self.language = lang
        self.log_mainfolderpath = log_mainfolderpath

        self.spinBox_fromMonth.valueChanged.connect(self.change_day_range)
        self.spinBox_toMonth.valueChanged.connect(self.change_day_range)

        self.set_date()

        self.checkBox_allDates.stateChanged.connect(self.enable_disable_date)
        self.checkBox_allLevels.stateChanged.connect(self.enable_disable_levels)
        self.checkBox_allTypes.stateChanged.connect(self.enable_disable_types)

        self.search_btn.clicked.connect(self.search_logs)
        self.refresh_btn.clicked.connect(self.refresh_logs)
        self.export_btn.clicked.connect(self.export_logs)

        self.search_logs()

        self.help_process = None

    def mousePressEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)
        self.helpButton.clicked.connect(self.show_help)

    def minimize(self):
        self.showMinimized()
    
    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def show_help(self):
        if self.help_process is not None and self.help_process.poll() is None:
            self.help_process.terminate()
        text = texts.Titles['show_logs'][self.language]
        self.help_process = subprocess.Popen(
                        ['/bin/python3', '../oxin_help/help_UI.py',
                        self.language,
                        text
                        ]
                    )

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
    
    def set_warning(self, text, level=1):
        """Show warning with time delay 2 second , all labels for show warning has been set here"""

        if text != None:
            if level == 1:
                self.message_label.setText(" " + text + " ")
                self.message_label.setStyleSheet(
                    "background-color:#20a740;border-radius:2px;color:white"
                )

            if level == 2:
                self.message_label.setText(
                    texts.WARNINGS["WARNING"][self.language] + text
                )
                self.message_label.setStyleSheet(
                    "background-color:#FDFFA9;border-radius:2px;color:black"
                )

            if level >= 3:
                self.message_label.setText(texts.ERRORS["ERROR"][self.language] + text)
                self.message_label.setStyleSheet(
                    "background-color:#D9534F;border-radius:2px;color:black"
                )
            QTimer.singleShot(2000, lambda: self.set_warning(None))
        else:
            self.message_label.setText("")
            self.message_label.setStyleSheet("")

    def enable_disable_date(self):
        s = not self.checkBox_allDates.isChecked()
        self.spinBox_fromYear.setEnabled(s)
        self.spinBox_fromMonth.setEnabled(s)
        self.spinBox_fromDay.setEnabled(s)
        self.spinBox_toYear.setEnabled(s)
        self.spinBox_toMonth.setEnabled(s)
        self.spinBox_toDay.setEnabled(s)

    def enable_disable_levels(self):
        s = not self.checkBox_allLevels.isChecked()
        self.checkBox_levelInfo.setEnabled(s)
        self.checkBox_levelWarning.setEnabled(s)
        self.checkBox_levelError.setEnabled(s)
        self.checkBox_levelCritical.setEnabled(s)
        self.checkBox_levelException.setEnabled(s)

    def enable_disable_types(self):
        s = not self.checkBox_allTypes.isChecked()
        self.checkBox_typesLogin.setEnabled(s)
        self.checkBox_typesPLC.setEnabled(s)
        self.checkBox_typesCameras.setEnabled(s)
        self.checkBox_typesLabeling.setEnabled(s)
        self.checkBox_typesTraining.setEnabled(s)
        self.checkBox_typesDatabase.setEnabled(s)
        self.checkBox_typesOthers.setEnabled(s)
        self.checkBox_typesLevel2.setEnabled(s)

    def set_date(self):
        date = date_funcs.get_date(persian=SHAMSI_DATE)
        year, month, day = date.split('/')

        year = int(year)
        month = int(month)
        day = int(day)

        self.spinBox_fromYear.setMinimum(year - 5)
        self.spinBox_fromYear.setMaximum(year + 5)
        self.spinBox_fromYear.setValue(year)

        self.spinBox_toYear.setMinimum(year - 5)
        self.spinBox_toYear.setMaximum(year + 5)
        self.spinBox_toYear.setValue(year)

        self.spinBox_fromMonth.setValue(month)
        self.spinBox_toMonth.setValue(month)

        self.spinBox_fromDay.setValue(day)
        self.spinBox_toDay.setValue(day)

    def change_day_range(self):
        btn = self.sender()
        btnName = btn.objectName()
        days = date_funcs.get_n_month_days(btn.value(), persian=SHAMSI_DATE)
        if btnName == 'spinBox_fromMonth':
            self.spinBox_fromDay.setMaximum(days)
        if btnName == 'spinBox_toMonth':
            self.spinBox_toDay.setMaximum(days)

    def search_logs(self):
        last_flag = self.comboBox_linesFL.currentText() == texts.Titles['from_last']['fa'] or \
            self.comboBox_linesFL.currentText() == texts.Titles['from_last']['en']
        log_folders = sorted(os.listdir(self.log_mainfolderpath), reverse=last_flag)

        if not self.checkBox_allDates.isChecked():
            from_date = str(self.spinBox_fromYear.value()) + '-' + str(self.spinBox_fromMonth.value()).rjust(2, '0') + '-' + str(self.spinBox_fromDay.value()).rjust(2, '0')
            to_date = str(self.spinBox_toYear.value()) + '-' + str(self.spinBox_toMonth.value()).rjust(2, '0') + '-' + str(self.spinBox_toDay.value()).rjust(2, '0')
            if from_date > to_date:
                self.set_warning(text=texts.WARNINGS['invalid_date_range'][self.language], level=2)
                return
            log_folders = list(filter(lambda log_folder: from_date <= log_folder <= to_date, log_folders))
        
        max_lines = self.spinBox_lineNumbers.value()
        line_counter = 0
        buffer = []
        text = ''
        for log_folder in log_folders:
            log_files = sorted(os.listdir(os.path.join(self.log_mainfolderpath, log_folder)), reverse=last_flag)
            for log_file in log_files:
                if line_counter > max_lines:
                    break
                with open(os.path.join(self.log_mainfolderpath, log_folder, log_file), 'r') as f:
                    if not last_flag:
                        l = f
                    else:
                        l = reversed(list(f))
                    for line in l:
                        if line.startswith('-'):
                            if not buffer:
                                continue
                            if last_flag:
                                buffer.reverse()
                            line_counter += len(buffer)
                            if line_counter > max_lines:
                                break
                            buffer.append(line)
                            text += ''.join(buffer)
                            buffer = []
                        else:
                            level_match = False
                            type_match = False
                            if not self.checkBox_allLevels.isChecked():
                                level = line.split(' ')[0]
                                if self.checkBox_levelInfo.isChecked() and level == 'INFO':
                                    level_match = True
                                if self.checkBox_levelWarning.isChecked() and level == 'WARNING':
                                    level_match = True
                                if self.checkBox_levelError.isChecked() and level == 'ERROR':
                                    level_match = True
                                if self.checkBox_levelCritical.isChecked() and level == 'CRITICAL':
                                    level_match = True
                                if self.checkBox_levelException.isChecked() and level not in ['INFO', 'WARNING', 'ERROR', 'CRITICAL']:
                                    level_match = True
                            else:
                                level_match = True

                            if not self.checkBox_allTypes.isChecked():
                                type = line[line.find("(")+1:line.find(")")][:2]
                                if self.checkBox_typesLogin.isChecked() and type == texts_codes.Types['Login/Logout']:
                                    type_match = True
                                if self.checkBox_typesPLC.isChecked() and type == texts_codes.Types['PLC']:
                                    type_match = True
                                if self.checkBox_typesCameras.isChecked() and type == texts_codes.Types['Camera/Imaging']:
                                    type_match = True
                                if self.checkBox_typesLabeling.isChecked() and type == texts_codes.Types['Labeling']:
                                    type_match = True
                                if self.checkBox_typesTraining.isChecked() and type == texts_codes.Types['Training']:
                                    type_match = True
                                if self.checkBox_typesDatabase.isChecked() and type == texts_codes.Types['Database']:
                                    type_match = True
                                if self.checkBox_typesOthers.isChecked() and type == texts_codes.Types['Others']:
                                    type_match = True
                                if self.checkBox_typesLevel2.isChecked() and type == texts_codes.Types['Level2']:
                                    type_match = True
                            else:
                                type_match = True

                            if level_match and type_match:
                                buffer.append(line)
                            
        self.logs_textEdit.setText(text)

    def refresh_logs(self):
        self.checkBox_allDates.setCheckState(Qt.CheckState.Checked)
        self.checkBox_allLevels.setCheckState(Qt.CheckState.Checked)
        self.checkBox_allTypes.setCheckState(Qt.CheckState.Checked)
        self.spinBox_lineNumbers.setValue(100)
        self.comboBox_linesFL.setCurrentText('From Last')
        self.search_logs()

    def export_logs(self):
        text = self.logs_textEdit.toPlainText()
        path = QFileDialog.getSaveFileName(self, "Save file", "", ".log")
        path = path[0] + path[1]
        with open(path, 'w') as f:
            f.write(text)

if __name__ == "__main__":
    app = QApplication()
    win = show_logs()
    win.show()
    sys.exit(app.exec())