from pickle import NONE
from matplotlib.pyplot import draw
import numpy as np
import cv2
import os
import json
from consts.consts import MOVEMENTS_KEYS, THINKNESS_MAP, COLOR_MAP
from backend import pathStructure
from Sheet import Sheet


TOP = "TOP"
BOTTOM="BOTTOM"
HORIZONTAL = 3
VERTICAL = 4

IMAGE_SHAPE = (1200, 1920)


class sheetOverView:
    def __init__(
        self,
        sheet,
        side,
        sheet_shape,
        sheet_grid,
        actives_camera=(1, 12),
        color_map=COLOR_MAP,
        thickness_map=THINKNESS_MAP,
        oriation=VERTICAL,
    ):
        self.show_bboxes = False
        self.sheet = sheet
        # self.sheet.get_main_path() = path
        # self.sheet_id = sheet_id
        self.side = side
        self.sheet_shape = sheet_shape
        self.sheet_grid = sheet_grid
        self.actives_camera = actives_camera
        self.oriation = oriation
        self.color_map = color_map
        self.thickness_map = thickness_map
        self.json_postfix = '_imgProcessing'
        self.json_format = '.json'

        assert self.sheet_shape[0] / self.sheet_grid[0] == int(
            self.sheet_shape[0] / self.sheet_grid[0]
        ), "error thechnical grid sheep doesn't match with shape"
        assert self.sheet_shape[1] / self.sheet_grid[1] == int(
            self.sheet_shape[1] / self.sheet_grid[1]
        ), "error thechnical grid sheep doesn't match with shape"

        self.cell_shape = (
            int(self.sheet_shape[0] / self.sheet_grid[0]),
            int(self.sheet_shape[1] / self.sheet_grid[1]),
        )
        print(self.sheet_shape, self.sheet_grid, self.cell_shape)
        assert (
            self.cell_shape[0] % 2 == 1 and self.cell_shape[1] % 2 == 1
        ), "cell shape should be odd"

        self.n = 0

        print(self.cell_shape)

        self.pt = (0, 0)
        self.real_imgs = []
        self.real_idxs = []
        self.real_res = 0

        self.sheet_img = self.init_img(self.color_map["sheet"])
        self.result_img = self.init_img(self.color_map["sheet"])
        self.sheet_img = self.draw_slines(self.sheet_img, -1)
        self.sheet_img = self.draw_discamera(self.sheet_img, self.actives_camera)
        self.result_img = np.copy(self.sheet_img)
        self.is_fit = False

        self.update_line(self.sheet_grid[0])

        self.select_layer = self.init_img((0, 0, 0))
        self.update_pointer((0, 0))

    def init_img(self, color):
        img = np.ones((self.sheet_shape[0], self.sheet_shape[1], 3), dtype=np.uint8)
        img[:, :] *= np.array(self.__rgb2bgr__(color), np.uint8)
        return img

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def update_line(self, n):
        if n == -1:
            self.n += 1
        else:
            self.n = n
        self.result_img = self.draw_noscaned(self.result_img, self.n)

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def update_defect(self):
        for c in range(1, self.actives_camera[1]+1):
            for f in range(1, self.sheet.get_nframe()+1):
                json_path = pathStructure.sheet_image_path(
                    self.sheet.get_main_path()+self.json_postfix,
                    self.sheet.get_id(),
                    self.side,
                    c,
                    f,
                    self.json_format
                )
                if os.path.exists(json_path):
                    with open(json_path) as jfile:
                        file = json.load(jfile)
                        status = file['status']
                else:
                    status = 'black'
                self.sheet_img = self.draw_defect(self.sheet_img, [c-1, f-1], status)

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def update_pointer_keyboard(self, key):
        self.update_pointer(None, key=key)

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def update_pointer(self, pt, key=None):
        self.is_fit = False
        x, y = 0, 0
        if pt is None and key is not None:  # for keyboard press keys event
            x, y = self.pt
            x += int(self.cell_shape[0] * MOVEMENTS_KEYS[key][0])
            y += int(self.cell_shape[1] * MOVEMENTS_KEYS[key][1])

        else:  # for mouse drag event
            x, y = int(pt[0] * (self.sheet_shape[1] - 1)), int(
                pt[1] * (self.sheet_shape[0] - 1)
            )

        cell_h, cell_w = self.cell_shape
        first_cam, last_cam = self.actives_camera
        first_cam -= 1

        start_w = first_cam * cell_w
        end_w = last_cam * cell_w - 1
        start_h = 0
        end_h = self.sheet_shape[0] - 1

        x = min(max(x, start_w + cell_w // 2), end_w - cell_w // 2)
        y = min(max(y, start_h + cell_h // 2), end_h - cell_h // 2)

        self.pt = (x, y)
        # print('pt',self.pt)
        self.update_real_imgs()

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def update_selected(self, selecteds):
        self.select_layer = self.init_img((200, 200, 200))
        for s in selecteds:
            self.select_layer = self.draw_selected(self.select_layer, s)
        # return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
        self.result_img = self.update_sheet_img()

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def update_sheet_img(self):
        # res = self.__add__(self.sheet_layer, self.selec)
        res = cv2.addWeighted(self.sheet_img, 0.5, self.select_layer, 0.5, 1)
        # res = self.__add__(res, self.line_layer)
        return res

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def __rgb2bgr__(self, inpt):
        if type(inpt) == type((1,)):
            r, g, b = inpt
            return (b, g, r)

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def __get_mask__(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def __add__(self, img1, img2):
        msk2 = self.__get_mask__(img2)
        msk1 = 255 - msk2

        img1 = cv2.bitwise_and(img1, img1, mask=msk1)
        img2 = cv2.bitwise_and(img2, img2, mask=msk2)
        return cv2.add(img1, img2)

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def pointer2rect(self, pt):
        x, y = pt
        xmin = x - self.cell_shape[1] // 2
        xmax = x + self.cell_shape[1] // 2
        ymin = y - self.cell_shape[0] // 2
        ymax = y + self.cell_shape[0] // 2
        return (xmin, ymin), (xmax, ymax)

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def draw_pointer(self, img, pt):
        # res = np.copy(img)
        corner1, corner2 = self.pointer2rect(pt)
        res = cv2.rectangle(
            img,
            corner1,
            corner2,
            self.__rgb2bgr__(self.color_map["pointer"]),
            self.thickness_map["pointer"],
        )
        return res

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def clean_pointer(self, img, pt):
        res = np.copy(img)
        corner1, corner2 = self.pointer2rect(pt)
        res = cv2.rectangle(res, corner1, corner2, (0, 0, 0), thickness=-1)

        return res

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________

    def draw_slines(self, img, n=-1):
        DASH_N = 30
        res = np.copy(img)
        if n == -1:
            if self.oriation == HORIZONTAL:
                n = (self.sheet_shape[1] // self.cell_shape[1]) + 1
            if self.oriation == VERTICAL:
                n = (self.sheet_shape[0] // self.cell_shape[0]) + 1

        if self.oriation == HORIZONTAL:
            for i in range(1, n):
                x1 = self.cell_shape[1] * i
                x2 = self.cell_shape[1] * i
                y1 = 0
                y2 = self.sheet_shape[0]

                self.draw_dline(img, (x1, y1), (x2, y2))

        if self.oriation == VERTICAL:
            for i in range(1, n):
                x1 = 0
                x2 = self.sheet_shape[1]
                y1 = self.cell_shape[0] * i
                y2 = self.cell_shape[0] * i

                self.draw_dline(img, (x1, y1), (x2, y2))

        return img

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def draw_dline(self, img, pt1, pt2):
        dash_size = 5
        x1, y1 = pt1
        x2, y2 = pt2

        if self.oriation == VERTICAL:

            for i in range(x1, x2, dash_size * 2):
                img = cv2.line(
                    img,
                    (i, y1),
                    (i + dash_size, y2),
                    self.__rgb2bgr__(self.color_map["sline"]),
                    thickness=self.thickness_map["sline"],
                    lineType=cv2.LINE_AA,
                )

        if self.oriation == HORIZONTAL:
            for i in range(y1, y2, dash_size * 2):
                img = cv2.line(
                    img,
                    (x1, i),
                    (x2, i + dash_size),
                    self.__rgb2bgr__(self.color_map["sline"]),
                    thickness=self.thickness_map["sline"],
                    lineType=cv2.LINE_AA,
                )
        return img

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def draw_discamera(self, img, active_grids):
        s, e = active_grids
        if self.oriation == VERTICAL:
            s *= self.cell_shape[1]
            s -= self.cell_shape[1]
            e *= self.cell_shape[1]
            img[:, :s] = self.color_map["none"]
            img[:, e:] = self.color_map["none"]

        if self.oriation == HORIZONTAL:
            s *= self.cell_shape[0]
            e *= self.cell_shape[0]
            img[:s] = self.color_map["none"]
            img[e:] = self.color_map["none"]
        return img

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def draw_noscaned(self, img, scanned_frame):
        if self.oriation == VERTICAL:
            s = scanned_frame * self.cell_shape[0]
            img[
                s:,
            ] = self.color_map["none"]

        if self.oriation == HORIZONTAL:
            s = scanned_frame * self.cell_shape[1]
            img[:, s:] = self.color_map["none"]
        return img

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def draw_selected(self, img, coordinate):
        i, j = coordinate
        i-=1
        j-=1
        if self.oriation == HORIZONTAL:
            xmin = i * self.cell_shape[1]
            xmax = (i + 1) * self.cell_shape[1]
            ymin = j * self.cell_shape[0]
            ymax = (j + 1) * self.cell_shape[0]

        if self.oriation == VERTICAL:
            xmin = i * self.cell_shape[1] + 1
            xmax = (i + 1) * self.cell_shape[1]
            ymin = j * self.cell_shape[0]
            ymax = (j + 1) * self.cell_shape[0]

        # select_img = np.copy(img)
        img = cv2.rectangle(
            img,
            (xmin, ymin),
            (xmax, ymax),
            self.__rgb2bgr__(self.color_map["select"]),
            thickness=-1,
        )


        # res = cv2.addWeighted(img, 0.7, select_img, 0.3, 1)
        return img

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def draw_defect(self, img, coordinate, status):
        i, j = coordinate
        if self.oriation == HORIZONTAL:
            xmin = i * self.cell_shape[1]
            xmax = (i + 1) * self.cell_shape[1]
            ymin = j * self.cell_shape[0]
            ymax = (j + 1) * self.cell_shape[0]

        if self.oriation == VERTICAL:
            xmin = i * self.cell_shape[1] + 1
            xmax = (i + 1) * self.cell_shape[1]
            ymin = j * self.cell_shape[0]
            ymax = (j + 1) * self.cell_shape[0]

        # select_img = np.copy(img)
        if status == 'False':
            img = cv2.rectangle(
                img,
                (xmin, ymin+1),
                (xmax, ymax-1),
                self.__rgb2bgr__(self.color_map["perfect"]),
                thickness=-1,
            )
        elif status == 'True':
            img = cv2.rectangle(
                img,
                (xmin, ymin+1),
                (xmax, ymax-1),
                self.__rgb2bgr__(self.color_map["defect"]),
                thickness=-1,
            )
        
        elif status == 'black':
            img = cv2.rectangle(
                img,
                (xmin, ymin+1),
                (xmax, ymax-1),
                self.__rgb2bgr__(self.color_map["black"]),
                thickness=-1,
            )

        # res = cv2.addWeighted(img, 0.7, select_img, 0.3, 1)
        return img

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def reset_real_imgs(self):
        self.real_imgs = []
        self.real_idxs = []
        self.real_res = 0


    def set_show_bboxes(self):
        self.show_bboxes = True


    def update_real_imgs(self):
        # try:
        x, y = self.pt
        center_cam = x // self.cell_shape[1]
        center_frame = y // self.cell_shape[0]
        start_cam = center_cam - 1
        end_cam = center_cam + 1
        # -----------
        start_frame = center_frame - 1
        end_frame = center_frame + 1
        # print('start_frame',start_frame,'end_frame',end_frame)
        # -------------------------------------------
        # -------------------------------------------
        start_cam = min(
            max(start_cam, 0), self.actives_camera[1] - 3
        )
        end_cam = min(max(end_cam, start_cam + 2), self.actives_camera[1]-1)
        # -----------
        start_frame = min(max(start_frame, 0), self.sheet_grid[0] - 3)
        end_frame = min(max(end_frame, start_frame + 2), self.sheet_grid[0] - 1)
        # print(start_frame,end_frame)
        # -------------------------------------------
        # -------------------------------------------

        new_idxs = []
        new_imgs = []
        for idx_cam in range(start_cam, end_cam+1):
            for idx_frame in range(start_frame, end_frame+1):
                idx = (idx_cam, idx_frame)
                new_idxs.append(idx)

                if (
                    idx in self.real_idxs
                ):  # if image corespond to this idx loaded befor,
                    list_idx = self.real_idxs.index(idx)
                    new_imgs.append(self.real_imgs[list_idx])

                else:
                    # res_path = os.path.join(
                    #     self.sheet.get_main_path(),
                    #     self.side,
                    #     str(idx_cam),
                    #     str(idx_frame) + '.jpg'
                    # )
                    a = idx_cam
                    # if idx_cam >= 12:
                    #     a = 1
                    img_path = pathStructure.sheet_image_path(
                        self.sheet.get_main_path(),
                        self.sheet.get_id(),
                        self.side,
                        a+1,
                        idx_frame+1,
                        self.sheet.get_image_format(),
                    )
                    json_path = pathStructure.sheet_image_path(
                        self.sheet.get_main_path()+self.json_postfix,
                        self.sheet.get_id(),
                        self.side,
                        a+1,
                        idx_frame+1,
                        self.json_format
                    )
                    img = cv2.imread(img_path, 0)
                    if img is None:  # if image doesnt exist, black image substitute
                        img = np.zeros(IMAGE_SHAPE, np.uint8)
                    else:
                        img = cv2.resize(img, (IMAGE_SHAPE[1], IMAGE_SHAPE[0]))
                    if self.show_bboxes:
                        if os.path.exists(json_path):
                            with open(json_path) as jfile:
                                file = json.load(jfile)
                                bboxes = file['bboxes']

                                for cntr in bboxes:
                                    x1, y1 = cntr[0]
                                    x2, y2 = cntr[1]
                                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                    new_imgs.append(img)

        # print(new_idxs)
        self.real_idxs = new_idxs
        self.real_imgs = new_imgs
        # except:
        #     print("error load image")

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def get_real_img(self):
        h_img, w_img = self.real_imgs[0].shape[:2]
        gridn = int(len(self.real_imgs) ** 0.5)  # 9 images are 3x3
        res_h, res_w = h_img * gridn, w_img * gridn

        # merge images together
        res_img = np.zeros((res_h, res_w, 3), np.uint8)
        for n in range(len(self.real_imgs)):
            i = n // gridn
            j = n - gridn * i
            res_img[
                j * h_img : (j + 1) * h_img, i * w_img : (i + 1) * w_img
            ] = cv2.merge((self.real_imgs[n], self.real_imgs[n], self.real_imgs[n]))
        x, y = self.pt
        start_x_idx, start_y_idx = np.array(self.real_idxs).min(
            axis=0
        )  # start idx_x and idx_y of images that concatinate in res_img
        # conver position of mouse in technical sheet image to normalized position of mouse in res_img
        px = (
            (x % self.cell_shape[1]) / (self.cell_shape[1] - 1)
            + x // self.cell_shape[1]
            - start_x_idx
        )
        py = (
            (y % self.cell_shape[0]) / (self.cell_shape[0] - 1)
            + y // self.cell_shape[0]
            - start_y_idx
        )
        # denormalized position of mouse in res_img
        px = int(px * w_img)
        py = int(py * h_img)
        # calc ROI on res_img
        x1, y1 = px - w_img // 2, py - h_img // 2
        x1 = min(max(x1, 0), res_w - w_img)
        y1 = min(max(y1, 0), res_h - h_img)
        
        y2 = y1 + h_img
        x2 = x1 + w_img

        crop = res_img[y1:y2, x1:x2]
        # -------------------
        return cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def fit(self, pt):

        real_img_x, real_img_y = (
            pt[0],
            pt[1],
        )  # normalize position of  mouse clicl event in real_img_window
        real_img_x, real_img_y = real_img_x - 0.5, real_img_y - 0.5

        x, y = self.pt
        cx = x / (self.cell_shape[1] - 1)
        cy = y / (self.cell_shape[0] - 1)

        cx = cx + real_img_x
        cy = cy + real_img_y

        idx_x = int(cx)
        idx_y = int(cy)

        new_x = int(idx_x * (self.cell_shape[1]) + self.cell_shape[1] // 2)
        new_y = int(idx_y * (self.cell_shape[0]) + self.cell_shape[0] // 2)

        self.pt = (new_x, new_y)
        self.is_fit = True

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def get_sheet_img(self):
        res = self.draw_pointer(np.copy(self.result_img), self.pt)
        return res
        return cv2.cvtColor(self.result_img, cv2.COLOR_BGR2RGB)


    def get_pos(self):
        pt_norm_x = self.pt[0] / self.sheet_shape[1]
        pt_norm_y = self.pt[1] / self.sheet_shape[0]

        return (pt_norm_x, pt_norm_y)


    def get_current_img_position(self):
        if self.is_fit:
            x, y = self.pt
            cam = x // self.cell_shape[1]
            frame = y // self.cell_shape[0]
            return cam+1, frame+1

        return -1, -1


    def get_side(self):
        return self.side.lower()


if __name__ == "__main__":

    sheet = Sheet(id = 1,
                sheet_id=996,
                main_path='/home/reyhane/PycharmProjects/trainApp_oxin8/oxin_image_grabber',
                image_format='.png',
                heat_number=0,
                ps_number=1111,
                pdl_number=2222,
                width=480,
                length=1000,
                thickness=None,
                date='1400/12/25',
                time='12:25:00',
                user='ali',
                nframe=15,
                cameras=[1, 12],)

    img = np.zeros((1920, 1200, 3), dtype=np.uint8)

    sheet_view = sheetOverView(
        sheet=sheet,
        side=TOP,
        sheet_shape=(51*sheet.get_nframe(), 41*12),
        sheet_grid=(sheet.get_nframe(), 12),
        oriation=VERTICAL,
    )

    # sheet_view = sheetOverView(
    #     path="110",
    #     side=TOP,
    #     sheet_shape=(int(252 * 2.76), 252),
    #     sheet_grid=(30, 12),
    #     oriation=VERTICAL,
    #     actives_camera=(0, 8),
    # )

    selected = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]
    sheet_view.update_selected(selected)
    # selected = [[0, 0], [1, 1]]
    # sheet_view.update_selected(selected)

    # sheet_view.update_line(6)

    cv2.imshow("res", sheet_view.result_img)
    cv2.waitKey(0)
    # """
    # img = sheet_view.draw_sline(img,1)
    # img = sheet_view.draw_pointer(img, (100,200))
    # """
    # # import time
    # # all_t = 0
    # # for _ in range(100):
    # #     t = time.time()
    # #     sheet_view.update_line(0)
    # #     sheet_view.update_line(1)
    # #     sheet_view.update_line(2)

    # #     sheet_view.update_defect([[(11,2), (0.2,0.3), (0.5,0.6)]])
    # #     #img = sheet_view.update_line(2)
    # #     sheet_view.update_line()
    # #     selected = [[1,4],[0,0],[1,2]]
    # #     sheet_view.update_selected(selected)

    # #     sheet_view.update_pointer((0.2,0.3))
    # #     #sheet_view.update_real_imgs()
    # #     real_img = sheet_view.get_real_img()
    # #     cv2.imshow('img real', cv2.resize(real_img, None , fx=0.2, fy=0.1))
    # #     cv2.waitKey(0)
    # #     img = sheet_view.get_sheet_img()
    # #     t = time.time() - t
    # #     all_t+=t

    # # #print(all_t/100)
    # # cv2.imshow('res', cv2.cvtColor( img, cv2.COLOR_RGB2BGR))
    # # cv2.waitKey(0)
