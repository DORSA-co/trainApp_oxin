
import database_utils





class labeling_API:
    
    def __init__(self, ui):
        self.ui = ui
        self.db = database_utils.dataBaseUtils()

        self.get_contet()
        self.btn_connector()

    def get_contet(self):

        self.defects_name,self.defects_info=self.db.get_defects()

    def btn_connector(self):

        self.ui.comboBox_defects.addItems(self.defects_name)

        print('sadwqdqwdcedfefe')

        self.ui.comboBox_defects.currentTextChanged.connect(self.show_content)

    def show_content(self,e):

        print(e)
