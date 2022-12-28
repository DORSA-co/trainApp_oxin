
import database_utils
from functools import partial

class labeling_API:
    """This is a API class for labeling. It contains  main functionality of labeling.

    :param ui: An instance of labeling class.
    :type ui: labeling
    :param defects_name: List of defect classes names.
    :type defects_name: list
    :param defects_info: List of defect classes informations.
    :type defects_info: list
    """    
    def __init__(self, ui,defects_name,defects_info):
        """Constructor method.
        """
        # Set ui.
        self.ui = ui
        # Set defects name.
        self.defects_name=defects_name
        # Set defect info.
        self.defects_info=defects_info
        # Connect labeling window widgets.
        self.btn_connector()

        # self.first_time=True


    def btn_connector(self):
        """Connect labeling window widgets to approprate slots.
        """
        # Add defects name into combobox.
        self.ui.comboBox_defects.addItems(self.defects_name)
        self.show_content(0)
        # Change table content as combobox index changes.
        self.ui.comboBox_defects.currentIndexChanged.connect(partial(self.show_content))
        # Connect save button to save selected defect class.
        self.ui.save_btn.clicked.connect(partial(self.ret_selcted_label))
        # Connect cancel button to close window.
        self.ui.cancel_btn.clicked.connect(partial(self.ui.close_win))


    def show_content(self,e):
        """Show information of current selected defect class from combobox into table.

        :param e: Current index of combobox.
        :type e: int
        """
        # print('asd.,',e)

        record=self.defects_info[e]
        # print('record',record)
        self.ui.updte_table(record)

    def ret_selcted_label(self):
        """Return name of the current selected defect class.

        :return: Current text of combobox.
        :rtype: str
        """
        self.select_label=self.ui.comboBox_defects.currentText()

        return self.select_label
