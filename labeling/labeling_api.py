
import database_utils
<<<<<<< HEAD
from functools import partial

class labeling_API:
    
    def __init__(self, ui,defects_name,defects_info):
        self.ui = ui
        self.db = database_utils.dataBaseUtils()
        self.defects_name=defects_name
        self.defects_info=defects_info

        self.btn_connector()

        # self.first_time=True

=======





class labeling_API:
    
    def __init__(self, ui):
        self.ui = ui
        self.db = database_utils.dataBaseUtils()

        self.get_contet()
        self.btn_connector()

    def get_contet(self):

        self.defects_name,self.defects_info=self.db.get_defects()
>>>>>>> r_abtahi

    def btn_connector(self):

        self.ui.comboBox_defects.addItems(self.defects_name)
<<<<<<< HEAD
        self.ui.comboBox_defects.currentIndexChanged.connect(partial(self.show_content))
        self.ui.save_btn.clicked.connect(partial(self.ret_selcted_label))
        self.ui.cancel_btn.clicked.connect(partial(self.ui.close_win))




    def show_content(self,e):

        # print('asd.,',e)

        record=self.defects_info[e]
        # print('record',record)
        self.ui.updte_table(record)

    def ret_selcted_label(self):

        self.select_label=self.ui.comboBox_defects.currentText()

        return self.select_label
=======

        print('sadwqdqwdcedfefe')

        self.ui.comboBox_defects.currentTextChanged.connect(self.show_content)

    def show_content(self,e):

        print(e)
>>>>>>> r_abtahi
