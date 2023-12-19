from pickle import NONE
from matplotlib.pyplot import draw
import numpy as np
import cv2
import os
import json
from consts.consts import MOVEMENTS_KEYS, THINKNESS_MAP, COLOR_MAP
from backend import pathStructure
from Sheet import Sheet
from backend.Annotation import Annotation

TOP = "TOP"
BOTTOM="BOTTOM"
HORIZONTAL = 3
VERTICAL = 4

IMAGE_SHAPE = (1024, 1792)
PIP_INPUT_SHAPE = (256, 256)

class sheetOverView:
    def __init__(
        self,
        sheet:Sheet,
        side: str,
        technical_sheet_shape,
        sheet_grid,
        dataset_annotation_path,
        actives_camera=(1, 12),
        color_map=COLOR_MAP,
        thickness_map=THINKNESS_MAP,
        oriation=VERTICAL,
        loading_callback = None
    ):
        self.show_bboxes = False
        self.sheet = sheet
        # self.sheet.get_main_path() = path
        # self.sheet_id = sheet_id
        self.side = side
        self.technical_sheet_shape = technical_sheet_shape
        self.sheet_grid = sheet_grid
        self.actives_camera = actives_camera
        self.oriation = oriation
        self.color_map = color_map
        self.thickness_map = thickness_map
        self.dataset_annotation_path = dataset_annotation_path

        assert self.technical_sheet_shape[0] / self.sheet_grid[0] == int(
            self.technical_sheet_shape[0] / self.sheet_grid[0]
        ), "error thechnical grid sheep doesn't match with shape"
        assert self.technical_sheet_shape[1] / self.sheet_grid[1] == int(
            self.technical_sheet_shape[1] / self.sheet_grid[1]
        ), "error thechnical grid sheep doesn't match with shape"

        self.cell_shape = (
            int(self.technical_sheet_shape[0] / self.sheet_grid[0]),
            int(self.technical_sheet_shape[1] / self.sheet_grid[1]),
        )
        # #print(self.technical_sheet_shape, self.sheet_grid, self.cell_shape)
        assert (
            self.cell_shape[0] % 2 == 1 and self.cell_shape[1] % 2 == 1
        ), "cell shape should be odd"

        self.n = 0
        self.pt = (0, 0)
        self.real_imgs = []
        self.real_idxs = []
        self.real_res = 0
        self.single_image_shape = IMAGE_SHAPE
        self.viewport_size = IMAGE_SHAPE #size of crop image frome full image to show into real image
        self.loading_callback = loading_callback
        
        self.set_zoom_scale(1)
        self.sheet_img = self.init_img(self.color_map["sheet"])
        self.result_img = self.init_img(self.color_map["sheet"])
        self.sheet_img = self.draw_slines(self.sheet_img, -1)
        self.sheet_img = self.draw_discamera(self.sheet_img, self.actives_camera)
        self.result_img = np.copy(self.sheet_img)
        self.is_fit = False
        self.labeled_images = []
        self.intensity = 20

        self.update_line(self.sheet_grid[0])

        self.select_layer = self.init_img((0, 0, 0))
        self.labeled_layer = self.init_img((200, 200, 200))
        self.update_pointer((0, 0))
        #-----------------------------------------News
        self.sheet_full_image = self.initsheet_full_image()

    def set_loading_callback(self, func):
        self.loading_callback = func

    def set_zoom_scale(self, scale):
        self.scale = scale
        self.viewport_size = int(self.single_image_shape[0] / scale) , int(self.single_image_shape[1] / scale)
        self.viewport_pointer_size = int( self.cell_shape[0] / scale) , int( self.cell_shape[1] / scale) #size of rectangle pointer
 
    def load_custom_images_from_file(self, frame_idx:int, cam_idx:int):
        img_path = pathStructure.sheet_image_path(
                    self.sheet.get_main_path(),
                    self.sheet.get_id(),
                    self.side,
                    cam_idx,
                    frame_idx,
                    self.sheet.get_image_format(),
                )

        img_path_operator = pathStructure.sheet_image_path_operator(
                    self.sheet.get_main_path(),
                    self.sheet.get_id(),
                    self.side,
                    cam_idx,
                    frame_idx,
                    self.sheet.get_image_format(),
                )


        img = None  
        if os.path.exists(img_path):
                img = cv2.imread(img_path, 0)
        elif os.path.exists(img_path_operator):
                img = cv2.imread(img_path_operator, 0)

        if img is not None:
            
            annotation_path  = pathStructure.get_image_annotation_path(self.dataset_annotation_path,
                                                    self.sheet.get_id(),
                                                    side = self.side,
                                                    camera_numbers=cam_idx,
                                                    n_frame=frame_idx,
                                                    )
            
            if os.path.exists(annotation_path):
                annotation = Annotation()
                annotation.read(annotation_path)
                masks = annotation.get_masks()
                self.labeled_images.append(
                    {
                        'camera': cam_idx,
                        'frame': frame_idx,
                        'img': img.copy(),
                        'masks': masks,
                    }
                )

                self.draw_selected(self.labeled_layer, (cam_idx, frame_idx), color=(200,0,0))
                

            if self.single_image_shape is None:
                self.single_image_shape = img.shape[:2]

            i = cam_idx - self.actives_camera[0]
            j = frame_idx - 1
            self.append_single_image_into_full_image(img, i, j)
        else:
            print(f'Warning: image of camera{cam_idx} and frame{frame_idx} not exist')

    def draw_labels(self, state=True):
        for label_img in self.labeled_images:
            img = label_img['img'].copy()
            
            if state:
                masks = label_img['masks']
                cnts = list( map( lambda x:x.get_mask_contour(), masks) )
                #layer_label = np.zeros_like(img)
                img = cv2.drawContours(img, cnts, -1, 255, thickness=3)

                # cv2.addWeighted(img, )
            

            self.append_single_image_into_full_image(
                img=img,
                i = label_img['camera' ] - self.actives_camera[0],
                j = label_img['frame'] - 1, 
            )





    def initsheet_full_image(self) -> np.ndarray :
        """generate an black image of full sheet image (all in one)

        Returns:
            np.ndarray: _description_
        """
        first_cam, last_cam = self.sheet.get_cameras()
        frame_counts = self.sheet.get_nframe()

        #SHOULD  BE MODIFY:
        #frame_counts = int(frame_counts/10)
        ###################
        camera_counts = last_cam - first_cam + 1
        
        single_h, single_w = self.single_image_shape
        return np.zeros( (single_h*frame_counts, single_w*camera_counts ), dtype=np.uint8)

    def draw_defect_bbox_on_single_image(self, cam_idx:int, frame_idx:int, bboxes: list) -> np.ndarray:
        """draws defects bounding boxes on single image

        Args:
            img (np.ndarray): orginal image
            cam_idx (int): number of camera . start from 1
            frame_idx (int): frame number. start from 1

        Returns:
            np.ndarray: result image
        """
        i = cam_idx - 1
        j = frame_idx - 1
        h, w = IMAGE_SHAPE
        img = self.sheet_full_image[j*h: (j+1)*h,
                              i*w: (i+1)*w
                              ]

        for cntr in bboxes:
            x1, y1 = cntr[0]
            x2, y2 = cntr[1]
            #SHOULD BE CHANGE (image is gray scale)
            res = cv2.rectangle(img, (x1, y1), (x2, y2), 255, 2)
 
    def append_single_image_into_full_image(self, img:np.ndarray, i:int, j:int):
        """puts a singlee image in correct position of full sheet image

        Args:
            img (np.ndarray): single image
            i (int): horizentaly index. always start from 0
            j (int): verticaly index. always start from 0
        """
        h,w = img.shape
        self.sheet_full_image[j*h: (j+1)*h,
                              i*w: (i+1)*w
                              ] = img

    def init_img(self, color):
        img = np.ones((self.technical_sheet_shape[0], self.technical_sheet_shape[1], 3), dtype=np.uint8)
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
    def update_defect(self, c, f):
        json_path = pathStructure.sheet_suggestions_json_path(
            '',
            self.sheet.get_id(),
            self.side, 
            c, 
            f
        )
        if os.path.exists(json_path):
            with open(json_path) as jfile:
                file = json.load(jfile)
                status = file['status']
                bboxes = file['bboxes']
        else:
            status = 'black'
            bboxes = []
        self.sheet_img = self.draw_defect(self.sheet_img, [c-1, f-1], status)
        if bboxes:
            self.draw_defect_bbox_on_single_image(c, f, bboxes)

    def update_defect_from_model(self, c, f):
        json_path = pathStructure.sheet_annotation_path_operator(
            self.sheet.get_main_path,
            self.sheet.get_id(),
            self.side,
            c,
            f
        )

        info_path = pathStructure.sheet_info_path_operator(
            self.sheet.get_main_path,
            self.sheet.get_id(),
        )

        if os.path.exists(json_path):
            with open(json_path) as jfile:
                file = json.load(jfile)
                status = str(any(file['binary']))
                binary_indices = list(filter(lambda i_x: file['binary'][i_x]==1 , range(len(file["binary"]))))
                bboxes = []

                if os.path.exists(info_path):
                    with open(info_path) as info_file:
                        info = json.load(info_file)
                        if 'image_shape' in info.keys():
                            image_shape = info['image_shape']
                        else:
                            image_shape = IMAGE_SHAPE
                        if 'pipline_input_shape' in file.keys():
                            pip_input_shape = info['pipline_input_shape']
                        else:
                            pip_input_shape = PIP_INPUT_SHAPE

                        nx = image_shape[1]//pip_input_shape[0]
                        for i in binary_indices:
                            x1 = (i % nx) * pip_input_shape[0]
                            y1 = (i // nx) * pip_input_shape[0]
                            bboxes.append(((x1, y1), (x1+pip_input_shape[0], y1+pip_input_shape[1])))
        else:
            status = 'False'
            bboxes = []

        self.sheet_img = self.draw_defect(self.sheet_img, [c-1, f-1], status)
        if bboxes:
            self.draw_defect_bbox_on_single_image(c, f, bboxes)

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
            x += int(self.viewport_pointer_size[0] * MOVEMENTS_KEYS[key][0])
            y += int(self.viewport_pointer_size[1] * MOVEMENTS_KEYS[key][1])

        else:  # for mouse drag event
            x, y = int(pt[0] * (self.technical_sheet_shape[1] - 1)), int(
                pt[1] * (self.technical_sheet_shape[0] - 1)
            )

        # cell_h, cell_w = self.cell_shape
        # first_cam, last_cam = self.actives_camera
       

        # start_w = (first_cam-1) * cell_w #pointer shouldent be out of actives cameras
        # end_w = last_cam * cell_w - 1
        # start_h = 0
        # end_h = self.technical_sheet_shape[0] - 1

        # x = min(max(x, start_w), end_imw - self.viewport_pointer_size[1])
        # y = min(max(y, start_h), end_h - self.viewport_pointer_size[0])

        self.pt = self.clip_pt((x,y)) #this show top-left corner of viewport pointer
        self.update_real_imgs()
    

    def clip_pt(self, pt):
        """check upper and lower limit of pt

        Args:
            pt (_type_): _description_

        Returns:
            _type_: _description_
        """
        x,y = pt
        cell_h, cell_w = self.cell_shape
        first_cam, last_cam = self.actives_camera
       

        start_w = (first_cam-1) * cell_w #pointer shouldent be out of actives cameras
        end_w = last_cam * cell_w 
        start_h = 0
        end_h = self.technical_sheet_shape[0] 

        x = min(max(x, start_w), end_w - self.viewport_pointer_size[1])
        y = min(max(y, start_h), end_h - self.viewport_pointer_size[0])
        return x,y

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def update_selected(self, selecteds):
        self.select_layer = self.init_img((200, 200, 200))
        for s in selecteds:
            self.select_layer = self.draw_selected(self.select_layer, s)
        # return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
        self.result_img = self.update_sheet_img()

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________


    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def update_sheet_img(self):
        # res = self.__add__(self.sheet_layer, self.selec)
        res = cv2.addWeighted(self.sheet_img, 0.5, self.select_layer, 0.5, 1)
        res = cv2.addWeighted(res, 0.5, self.labeled_layer, 0.5, 1)
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
        xmin = x
        xmax = x + self.viewport_pointer_size[1]
        ymin = y
        ymax = y + self.viewport_pointer_size[0]
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
        #DASH_N = 30
        #res = np.copy(img)
        if n == -1:
            if self.oriation == HORIZONTAL:
                n = (self.technical_sheet_shape[1] // self.cell_shape[1]) + 1
            if self.oriation == VERTICAL:
                n = (self.technical_sheet_shape[0] // self.cell_shape[0]) + 1

        if self.oriation == HORIZONTAL:
            for i in range(1, n):
                x1 = self.cell_shape[1] * i
                x2 = self.cell_shape[1] * i
                y1 = 0
                y2 = self.technical_sheet_shape[0]

                self.draw_dline(img, (x1, y1), (x2, y2))

        if self.oriation == VERTICAL:
            for i in range(1, n):
                x1 = 0
                x2 = self.technical_sheet_shape[1]
                y1 = self.cell_shape[0] * i
                y2 = self.cell_shape[0] * i

                self.draw_dline(img, (x1, y1), (x2, y2))

            
            for i_cam in range(self.actives_camera[0], self.actives_camera[1]):
                y1 = 0
                x1 = i_cam * self.cell_shape[1]
                y2 = self.technical_sheet_shape[0]
                cv2.line(img, (x1, y1), (x1, y2), color=self.color_map["sline"], thickness=1)

        return img

    # ______________________________________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________________________________
    def draw_dline(self, img, pt1, pt2,):
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
    def draw_selected(self, img, coordinate, color=None):
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
        
        if color is None:
            color = self.__rgb2bgr__(self.color_map["select"])

        # select_img = np.copy(img)
        img = cv2.rectangle(
            img,
            (xmin, ymin),
            (xmax, ymax),
            color,
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
        pass


    def set_show_bboxes(self):
        self.show_bboxes = True


    def update_real_imgs(self):
        # try:
        pass

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def get_real_img(self, eq=True, intensity = 20):
        norm_x, norm_y = self.get_pos()
        h,w = self.sheet_full_image.shape
        x = int(norm_x * w)
        y = int(norm_y * h) 
        
        crop = np.copy(self.sheet_full_image[ y:y+self.viewport_size[0], 
                                     x:x+ self.viewport_size[1]])

        if eq:
            crop = self.balance_hist(crop, intensity)
        
        return crop


    def balance_hist(self, img, intensity):
        img = img.astype(np.int16)
        img = img + intensity
        img = np.clip(img, 0, 255).astype(np.uint8)

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(100, 100))
        return clahe.apply(img)
        # -------------------
        
    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def fit(self, pt):
        
        real_img_x, real_img_y = pt[0],pt[1]
        
        # normalize position of  mouse clicl event in real_img_window
        real_img_x, real_img_y = real_img_x / self.scale, real_img_y/ self.scale
        

        x, y = self.pt
        
        cx = x / (self.cell_shape[1] )
        cy = y / (self.cell_shape[0] )

        cx = cx + real_img_x
        cy = cy + real_img_y

        idx_x = int(cx)
        idx_y = int(cy)

        new_x = int(idx_x * (self.cell_shape[1]))
        new_y = int(idx_y * (self.cell_shape[0]))


      
        # real_img_x, real_img_y = int(real_img_x ), int(real_img_y )
        

        # x, y = self.pt
        
        # cx = x / (self.cell_shape[1] )
        # cy = y / (self.cell_shape[0] )

        # cx = cx + real_img_x
        # cy = cy + real_img_y

        # idx_x = int(cx)
        # idx_y = int(cy)

        # new_x = int(idx_x * (self.cell_shape[1]))
        # new_y = int(idx_y * (self.cell_shape[0]))


        self.pt = self.clip_pt((new_x, new_y))
        self.is_fit = True

    # _____________________________________________________________________________________________________________________________
    #
    # _____________________________________________________________________________________________________________________________
    def get_sheet_img(self):
        res = self.draw_pointer(np.copy(self.result_img), self.pt)
        return res
        return cv2.cvtColor(self.result_img, cv2.COLOR_BGR2RGB)

    def get_pos(self)-> tuple:
        """returns normalized coordinate on thechnical sheet

        Returns:
            tuple: norm_x, norm_y
        """

        pt_norm_x = self.pt[0] / (self.cell_shape[1] * (self.actives_camera[1] - self.actives_camera[0] + 1))#self.technical_sheet_shape[0]
        pt_norm_y = self.pt[1] / self.technical_sheet_shape[0]
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

    def get_current_cam(self,):
        return self.pt[0] // self.cell_shape[1] + 1


if __name__ == "__main__":

    sheet = Sheet(id = 1,
                sheet_id=996,
                main_path='/home/reyhane/PycharmProjects/trainApp_oxin8/oxin_image_grabber',
                image_format='.png',
                heat_id=0,
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

    img = np.zeros((1792, 1024, 3), dtype=np.uint8)

    sheet_view = sheetOverView(
        sheet=sheet,
        side=TOP,
        technical_sheet_shape=(51*sheet.get_nframe(), 41*12),
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

    # # ##print(all_t/100)
    # # cv2.imshow('res', cv2.cvtColor( img, cv2.COLOR_RGB2BGR))
    # # cv2.waitKey(0)
