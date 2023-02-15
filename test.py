import os
import texts

def search_logs(self):
    last_flag = self.comboBox_linesFL.currentText() == 'Last'
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
    text = ''
    match_flag = True
    for log_folder in log_folders:
        log_files = sorted(os.listdir(os.path.join(self.log_mainfolderpath, log_folder)), reverse=last_flag)
        for log_file in log_files:
            if line_counter >= max_lines:
                break
            with open(os.path.join(self.log_mainfolderpath, log_folder, log_file), 'r') as f:
                if not last_flag:
                    l = zip(f, f)
                else:
                    l = reversed(list(zip(f, f)))
                for line, dash in l:
                    if line_counter >= max_lines:
                            break
                    if not self.checkBox_allLevels.isChecked():
                        match_flag = False
                        level = line.split(' ')[0]
                        if self.checkBox_levelInfo.isChecked() and level == 'INFO':
                            match_flag = True
                        if self.checkBox_levelWarning.isChecked() and level == 'WARNING':
                            match_flag = True
                        if self.checkBox_levelError.isChecked() and level == 'ERROR':
                            match_flag = True
                        if self.checkBox_levelCritical.isChecked() and level == 'CRITICAL':
                            match_flag = True
                        if self.checkBox_levelException.isChecked() and level not in ['INFO', 'WARNING', 'ERROR', 'CRITICAL']:
                            match_flag = True
                    if match_flag:
                        text += line
                        text += dash
                        line_counter += 1

    self.logs_textEdit.setText(text)