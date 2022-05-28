import cv2
from backend.pathStructure import create_sheet_path, sheet_image_path, settings
from simulator import camera_simulator, plc_simulator, PATH
from PySide6.QtGui import QImage, QPixmap

class live_manager:
    def __init__(self, ui, path):
        self.n_camera = 1
        self.n_frame = 1
        self.side = 'TOP'
        self.coil_number = 0
        self.grab = 'False'
        self.ui = ui
        self.path = path

    def save_camera_images(self, cameras):
        plc_simulator()
        camera_simulator()

        while 1:
            plc = open('plc.txt').read().strip()
            if plc == '':
                continue
            coil_number_new = int(plc)
            if coil_number_new != self.coil_number:
                self.n_frame = 1
                self.coil_number = coil_number_new
                create_sheet_path(self.path, self.coil_number)

            # print(coil_number)

            grab_new = open('grab.txt').read().strip()
            if grab_new == '':
                continue
            if grab_new == 'True' and self.grab == 'True':
                continue
            self.grab = grab_new

            # print(grab)

            if self.grab == 'True':
                img = cv2.imread(PATH)
                path = sheet_image_path(self.path, self.coil_number, self.side, self.n_camera, self.n_frame,
                                        settings['image_format'])
                cv2.imwrite(path, img)
                self.n_frame += 1

                self.live(img)

    def live(self, img):
        fs = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
        self.ui.live1.setPixmap(QPixmap.fromImage(fs))
