from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
import texts
from PySide6.QtWidgets import QMessageBox as sQMessageBox

class save_all_worker(sQObject):
    """this class is worker for image processing Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()
    update_progressbar = sSignal()
    warning = sSignal(str, str, int)
    question = sSignal(str, str)

    def assign_parameters(self, api_obj, count):
        self.api_obj = api_obj
        self.count = count

    def run(self):
        # try:
        for i in range(self.count):
            self.api_obj.move_on_list.next_on_list("selected_imgs_for_label")
            self.api_obj.load_image_to_label_page(fast=True)
            self.save_train_ds()
            self.update_progressbar.emit()
        # print('(((((((((((((:', self.api_obj.image_save_status)
        self.finished.emit()
        # except:
        #     print('Exception')
        #     self.finished.emit()

    def save_train_ds(self):
        masks = self.api_obj.label_bakcend["mask"].get()
        try:
            sheet, pos, img_path = self.api_obj.move_on_list.get_current(
                "selected_imgs_for_label"
            )
        except:
            self.warning.emit(
                texts.WARNINGS["NO_IMAGE_LOADED"][self.api_obj.language], "label", 2
            )
            return

        saved_perfect = self.api_obj.ds.check_saved_perfect(pos=pos)
        saved_defect = self.api_obj.ds.check_saved_defect(pos=pos)
        if self.api_obj.ui.no_defect.isChecked():
            if masks:
                self.warning.emit(
                    texts.WARNINGS["WRONGE_MASK_Format"][self.api_obj.language].format(img_path), "label", 2
                )
                return
            if saved_defect:
                self.api_obj.save_all_question = None
                self.question.emit(
                    texts.WARNINGS["question"][self.api_obj.language],
                    texts.WARNINGS["ALREADY_SAVED_DEFECT_Format"][self.api_obj.language].format(img_path),
                )
                while self.api_obj.save_all_question is None: pass
                if not self.api_obj.save_all_question:
                    return
                else:
                    self.api_obj.ds.delete_from_defect(pos)
                    self.api_obj.ds_json.modify_defect(self.api_obj.ds.defect_path)

            self.api_obj.ds.save_to_perfect(img_path=img_path, pos=pos)
            self.api_obj.ds_json.modify_perfect(self.api_obj.ds.perfect_path)
            self.api_obj.image_save_status[img_path] = True

        elif self.api_obj.ui.yes_defect.isChecked():
            if not masks:
                self.warning.emit(
                    texts.WARNINGS["WRONGE_MASK_Format"][self.api_obj.language].format(img_path), "label", 2
                )
                return
            if saved_perfect:
                self.api_obj.save_all_question = None
                self.question.emit(
                    texts.WARNINGS["question"][self.api_obj.language],
                    texts.WARNINGS["ALREADY_SAVED_PERFECT_Format"][self.api_obj.language].format(img_path),
                )
                while self.api_obj.save_all_question is None: pass
                if not self.api_obj.save_all_question:
                    return
                else:
                    self.api_obj.ds.delete_from_perfect(pos)
                    self.api_obj.ds_json.modify_perfect(self.api_obj.ds.perfect_path)

            mask = self.api_obj.create_mask_from_mask(img_path)
            self.api_obj.ds.save_to_defect(img_path=img_path, pos=pos, mask=mask)
            self.api_obj.ds_json.modify_defect(self.api_obj.ds.defect_path)
            self.api_obj.image_save_status[img_path] = True
        else:
            self.warning.emit(
                texts.WARNINGS["IMAGE_STATUS"][self.api_obj.language], "label", 2
            )
            return

        self.api_obj.ds.save(img_path=img_path, pos=pos, sheet=sheet, masks=masks)
        labels = []
        for mask in masks:
            if mask[0] not in labels:
                labels.append(mask[0])

        image_name = self.api_obj.ds.__file_name__(pos) + self.api_obj.ds.format_image
        self.api_obj.ds_json.add_update_classification(image_name, labels)
