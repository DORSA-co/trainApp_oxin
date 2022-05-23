import numpy as np
import cv2 as cv2


TEST = 'bbox'  #'bbox' , 'mask

COLOR_MAP_MASK = { 'line':(255,0,0),'point':(0,255,0), 'fill':(255,255,0) }
THINKNESS_MAP_MASK = {'point':-1, 'line':4}

COLOR_MAP_BBOX = { 'rect':(255,0,0),'bbox':(0,255,0), 'gline':(255,255,0), 'point':(0,0,255)}
THINKNESS_MAP_BBOX = {'rect':4, 'gline':4, 'bbox':4}

class maskLbl:
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def __init__(self,img_size, label_color, color_map=COLOR_MAP_MASK, thikness_map = THINKNESS_MAP_MASK):
        self.img_size = img_size
        self.points = []
        self.color_map = color_map
        self.label_color = label_color
        self.thickness_map = thikness_map
        self.status = 'none'
        self.masks = []
        self.edit_mask_idx = -1
        self.edit_point_idx = -1
        self.accept_new_point = True
        self.radius = 10
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def mask_init(self):
        return np.zeros(self.img_size + (3,), dtype=np.uint8)

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def __denormal_pt__(self,pt):
        return int(pt[0] * self.img_size[1]), int(pt[1] * self.img_size[0])

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def click(self,pt):
        pt = self.__denormal_pt__(pt)
        x,y = pt
        if self.status == 'none': #this codition is for draw new mask
            self.status = 'drawing'
            #check if pt is near to a rect corner mode should be 'editing' and store bbox idx and x and y idx
            for idex,(lbl,cnt) in enumerate(self.masks):
                for i,corner in enumerate(cnt):
                    corner = corner[0] #beacuse shape of cnt is (n,1,2)
                    if ( (x-corner[0])**2 + (y-corner[1])**2)**0.5 < 20:
                        self.status = 'editing'
                        self.edit_mask_idx = idex
                        self.edit_point_idx = i
                        break


        if self.status=='drawing' and self.accept_new_point:#this condition is for drawing mask ( add point )
            self.add_points(pt)
            self.accept_new_point = False

        if self.status == 'editing':
            self.edit_mask(pt)




    def release(self):
        if self.status == 'editing':
            self.status = 'none'
        self.accept_new_point = True

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def clear_points(self):
        self.points=[]
        self.status='none'
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def delete_point_or_mask(self,pt):


        # print('delet')

        pt = self.__denormal_pt__(pt)
        if len(self.points)>0 and  self.status=='drawing':
            self.points.pop()
            if len(self.points)==0:
                self.status = 'none'
        else:
            self.masks.sort(key=lambda b: cv2.contourArea(b[1]))
            for i in range(len(self.masks)):
                cnt = self.masks[i][1]
                if cv2.pointPolygonTest(cnt, pt, False)>=0:
                    self.masks.pop(i)
                    break

    # ______________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________
    def update_label(self, label, pt):
        pt = self.__denormal_pt__(pt)
        self.masks.sort(key=lambda b: cv2.contourArea(b[1]))
        for i in range(len(self.masks)):
            cnt = self.masks[i][1]
            if cv2.pointPolygonTest(cnt, pt, False) >= 0:
                self.masks[i][0] = label
                break

    # ______________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________
    def clicked_in_defect(self, pt):
        pt = self.__denormal_pt__(pt)
        for i in range(len(self.masks)):
            cnt = self.masks[i][1]
            if cv2.pointPolygonTest(cnt, pt, False) >= 0:
                return True
        return False

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def add_points(self,pt):
        #check fot countror closed or not
        if len(self.points)>=2:
            first_pts = self.points[0]
            x1,y1 = first_pts
            x2,y2 = pt
            dis = ((x2-x1)**2 + (y1-y2)**2)**0.5
            if dis < 30:
                pt = (x1,y1)
                self.status = 'none'



        #check if new point is so near to last points , dont append it
        if len(self.points)>=1:
            last_x,last_y = self.points[-1]
            x,y = pt
            if ((x-last_x)**2 + (y-last_y)**2)**0.5 >20:
                self.points.append(pt)

        else:
            self.points.append(pt)


    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def edit_mask(self,pt):
        x,y = pt
        self.masks[self.edit_mask_idx][1][self.edit_point_idx][0][0] = x
        self.masks[self.edit_mask_idx][1][self.edit_point_idx][0][1] = y


    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def is_drawing_finish(self):
        if self.status == 'none' and len(self.points)>2:
            return True
        return False
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def save(self, label):

        print('label',label)
        #last point is same as first point so we ignore it
        cnt = np.array(self.points[:-1]).reshape((-1,1,2))
        self.masks.append([label,cnt])
        self.status = 'none'
        self.points = []

        # self.masks_name.append(label)


    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def load(self, masks):
        #last point is same as first point so we ignore it
        cnt = np.array(self.points[:-1]).reshape((-1,1,2))
        self.masks = list( map (lambda x:[x[0],np.array(x[1]).reshape(-1,1,2)], masks))
        self.status = 'none'
        self.points = []

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def get(self):
        return  list( map (lambda x:[x[0],np.array(x[1]).reshape(-1,2)], self.masks))

    def get_labels(self):
        return   self.masks

    #______________________________________________________________________________________________________
    #draw no complete mask
    #______________________________________________________________________________________________________
    def draw_nc(self, mask):
        for i in range(len(self.points)-1):
            pt1 = self.points[i]
            pt2 = self.points[i+1]
            cv2.line(mask, pt1,pt2, color = self.color_map['line'], thickness=self.thickness_map['line'] )


        for pt in self.points:
            cv2.circle(mask, pt, self.radius, self.color_map['point'], thickness=self.thickness_map['point'] )

        return mask
    #______________________________________________________________________________________________________
    #draw complete mask
    #______________________________________________________________________________________________________
    def draw_c(self, mask):
        cnt = np.array(self.points)
        cnt = cnt.reshape((-1,1,2))
        cv2.drawContours(mask, [cnt], 0, color=self.color_map['fill'], thickness=-1)
        return mask


    def draw(self):
        masks_img = self.mask_init()
        # print('color lbl',self.label_color[0])
        for lbl, cnt in self.masks:

            # print('lastcolor',self.label_color[lbl])

            cv2.drawContours(masks_img, [cnt], 0, color=self.label_color[lbl], thickness=-1)
            for corner in cnt:
                corner = tuple(corner[0])
                cv2.circle( masks_img, corner, self.radius, color=self.color_map['point'], thickness=-1)

        if len(self.points)>2 and self.points[0]==self.points[-1]:
            masks_img = self.draw_c(masks_img)

        else:
            masks_img = self.draw_nc(masks_img)


        return masks_img



    #______________________________________________________________________________________________________
    #check mouse event and doing coresponding Task
    #______________________________________________________________________________________________________
    def mouse_event(self, status, button, pt):
            if button == 'left_btn' and status in ( 'mouse_press', 'mouse_move'):
                self.click(pt)

            elif button == 'right_btn' and status == 'mouse_press':
                self.delete_point_or_mask(pt)


            elif status == 'mouse_release':
                self.release()















class bboxLbl:
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def __init__(self,img_size, label_color, color_map=COLOR_MAP_BBOX, thikness_map = THINKNESS_MAP_BBOX):
        self.img_size = img_size
        self.points = []
        self.color_map = color_map
        self.label_color = label_color
        self.thickness_map = thikness_map
        self.status = 'none'
        self.bboxs = []
        self.bbox_auto = []
        self.edit_bbox_idex = -1
        self.edit_x_idex = -1
        self.edit_y_idex = -1
        self.radius = 10

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def image_init(self):
        return np.zeros(self.img_size + (3,), dtype=np.uint8)

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def __denormal_pt__(self,pt):
        return int(pt[0] * self.img_size[1]), int(pt[1] * self.img_size[0])
    #______________________________________________________________________________________________________
    #check edit or draw new box
    #______________________________________________________________________________________________________
    def click(self,pt):
        pt = self.__denormal_pt__(pt)
        x,y = pt
        if self.status == 'none':
            self.status = 'drawing'
            #check if pt is near to a rect corner mode should be 'editing' and store bbox idx and x and y idx
            for idex,(lbl,bbox) in enumerate(self.bboxs):
                for i,corner_x in enumerate(bbox[:,0]):
                    for j,corner_y in enumerate(bbox[:,1]):
                        if ( (x-corner_x)**2 + (y-corner_y)**2)**0.5 < 10:
                            self.status = 'editing'
                            self.edit_bbox_idex = idex
                            self.edit_x_idex = i
                            self.edit_y_idex = j
                            break

        if self.status=='drawing':
            self.add_points(pt)

        if self.status == 'editing':
            self.edit_rect(pt)







    #______________________________________________________________________________________________________
    #Update selected corner
    #______________________________________________________________________________________________________
    def edit_rect(self, pt):
        x,y = pt
        #---------[select bound box and label][only bound box][specific row][x]
        self.bboxs[self.edit_bbox_idex][1][self.edit_x_idex,0] = x
        #---------[select bound box and label][only bound box][specific row][y]
        self.bboxs[self.edit_bbox_idex][1][self.edit_y_idex,1] = y






    def add_points(self,pt):
        if len(self.points)<2:
            self.points.append(pt)
        else:
            self.points.pop()
            self.points.append(pt)

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def clear_points(self):
        self.points=[]
        #self.sta=False
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def delete_bbox(self,pt):
        pt = self.__denormal_pt__(pt)
        x,y=pt
        #sort box by area beacuse if two or more boxs have intersect area, we want delete small box first
        self.bboxs.sort(key=lambda b: (b[1][1,0]-b[1][0,0]) * (b[1][1,1]-b[1][0,1]))

        #check pt is inside of which box
        for i in range(len(self.bboxs)):
            (xmin,ymin),(xmax,ymax) = self.bboxs[i][1]
            if xmin<x<xmax and ymin<y<ymax:
                self.bboxs.pop(i)
                break

    # ______________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________
    def update_label(self, label, pt):
        pt = self.__denormal_pt__(pt)
        x, y = pt
        # sort box by area beacuse if two or more boxs have intersect area, we want delete small box first
        self.bboxs.sort(key=lambda b: (b[1][1, 0] - b[1][0, 0]) * (b[1][1, 1] - b[1][0, 1]))

        # check pt is inside of which box
        for i in range(len(self.bboxs)):
            (xmin, ymin), (xmax, ymax) = self.bboxs[i][1]
            if xmin < x < xmax and ymin < y < ymax:
                self.bboxs[i][0] = label
                break

    # ______________________________________________________________________________________________________
    #
    # ______________________________________________________________________________________________________
    def clicked_in_defect(self, pt):
        pt = self.__denormal_pt__(pt)
        x, y = pt
        # sort box by area beacuse if two or more boxs have intersect area, we want delete small box first
        self.bboxs.sort(key=lambda b: (b[1][1, 0] - b[1][0, 0]) * (b[1][1, 1] - b[1][0, 1]))

        # check pt is inside of which box
        for i in range(len(self.bboxs)):
            (xmin, ymin), (xmax, ymax) = self.bboxs[i][1]
            if xmin < x < xmax and ymin < y < ymax:
                return True
        return False

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    # def is_drawing_finish(self):
    #     pass

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def save(self, label):
        if len(self.points)==2 and self.status =='finish':

            #first corner should be top-left and second corner shoud be bottom right
            (x1,y1), (x2,y2) = self.points
            xmin, xmax = min(x1,x2) , max(x1,x2)
            ymin, ymax = min(y1,y2) , max(y1,y2)

            #only add enough big bbox
            if xmax-xmin>5 and ymax-ymin>5:
                bbox = np.array( [[xmin,ymin], [xmax, ymax]] )
                self.bboxs.append([label,bbox])

        if self.status == 'editing':
            #first corner should be top-left and second corner shoud be bottom right
            x1,x2 = self.bboxs[self.edit_bbox_idex][1][:,0]
            y1,y2 = self.bboxs[self.edit_bbox_idex][1][:,1]
            xmin,xmax = min(x1,x2), max(x1,x2)
            ymin,ymax = min(y1,y2), max(y1,y2)
            self.bboxs[self.edit_bbox_idex][1][0]=[xmin,ymin]
            self.bboxs[self.edit_bbox_idex][1][1]=[xmax,ymax]

        self.status ='none'
        self.points = []



    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def finish_drawing(self):
        if len(self.points) == 2:
            self.status ='finish'
        else:
            self.points = []
            self.status ='none'
        #self.points = []

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def is_drawing_finish(self):
        return self.status == 'finish'
    #______________________________________________________________________________________________________
    #draw no complete mask
    #______________________________________________________________________________________________________
    def draw_nc(self, img):
        pt1,pt2 = self.points
        cv2.rectangle( img, pt1, pt2, color=self.color_map['rect'], thickness=self.thickness_map['rect'] )
        return img
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________


    def draw(self):
        bbox_img = self.image_init()

        for lbl, bbox in self.bboxs:
            pt1,pt2 = bbox
            cv2.rectangle(bbox_img, tuple(pt1), tuple(pt2), color=self.label_color[lbl], thickness=self.thickness_map['bbox'])

            #draw corner points
            for x in bbox[:,0]:
                for y in bbox[:,1]:
                    cv2.circle(bbox_img, (x,y),self.radius, color=self.color_map['point'],thickness=-1)

        if len(self.points)==2:
            bbox_img = self.draw_nc(bbox_img)


        return bbox_img

    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def mouse_event(self, status, button, pt):
            if button == 'left_btn' and status in ( 'mouse_press', 'mouse_move'):
                self.click(pt)

            elif button == 'right_btn' and status == 'mouse_press':
                self.delete_bbox(pt)


            elif button == 'left_btn' and status == 'mouse_release':
                #self.save_bbox('1')
                self.finish_drawing()

    # def get(self):
    #     return  list( map (lambda x:[x[0],np.array(x[1]).reshape(-1,2)], self.bboxs))
    # #____


    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def load(self, bboxs):
        bboxs = np.array(bboxs)
        self.bboxs = list(bboxs)
        self.status ='none'
        self.points = []


    def get(self):
        return self.bboxs




if __name__ == '__main__':

    if TEST == 'bbox':
        # mouse callback function
        status,gx,gy=0,0,0

        def draw_circle(event,x,y,flags,param):
            global status,gx,gy
            if event == cv2.EVENT_LBUTTONDOWN:
                status = 'lc'
            if event == cv2.EVENT_LBUTTONUP:
                status = 'lcn'

            if event == cv2.EVENT_RBUTTONDOWN:
                status = 'rc'
            if event == cv2.EVENT_RBUTTONUP:
                status = ''

            gx,gy = x,y


        # Create a black image, a window and bind the function to window
        img = np.zeros((512,700,3), np.uint8)
        img+=200
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)
        bbox_lbl = bboxLbl((512,700), {'a1':(0,0,255), 'a2':(0,120,150)})

        res = np.copy(img)
        while(1):
            cv2.imshow('image',res)
            if status=='lc':
                bbox_lbl.click((gx,gy))
                bboxs_img = bbox_lbl.draw_bboxs()
                res = cv2.addWeighted(img,0.5, bboxs_img,0.5,1)

            if status =='lcn':
                bbox_lbl.save(np.random.choice(['a1','a2']))
                bboxs_img = bbox_lbl.draw_bboxs()
                res = cv2.addWeighted(img,0.5, bboxs_img,0.5,1)

                #status = ''

            if status =='rc':
                bbox_lbl.delete_bbox((gx,gy))
                bboxs_img = bbox_lbl.draw_bboxs()
                res = cv2.addWeighted(img,0.5, bboxs_img,0.5,1)
                #mask_label.delete_point_or_mask((gx,gy))
                #mask = mask_label.draw_mask()
                #res = cv2.addWeighted(img,0.5, mask,0.5,1)
                status = ''
            if cv2.waitKey(8) & 0xFF == 27:
                break
        cv2.destroyAllWindows()


















    if TEST == 'mask':
        # mouse callback function
        status,gx,gy=0,0,0

        def draw_circle(event,x,y,flags,param):
            global status,gx,gy
            if event == cv2.EVENT_LBUTTONDOWN:
                status = 'lc'
            if event == cv2.EVENT_LBUTTONUP:
                status = 'lcn'

            if event == cv2.EVENT_RBUTTONDOWN:
                status = 'rc'
            if event == cv2.EVENT_RBUTTONUP:
                status = ''

            gx,gy = x,y


        # Create a black image, a window and bind the function to window
        img = np.zeros((512,700,3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)
        mask_label = maskLbl((512,700), {'a1':(0,0,255), 'a2':(0,120,150)})

        res = np.copy(img)
        while(1):
            cv2.imshow('image',res)

            if status=='lc':
                mask_label.click((gx,gy))



                #status = ''
                if mask_label.is_drawing_finish():
                    mask_label.save(np.random.choice(['a1','a2']))
                mask = mask_label.draw()
                res = cv2.addWeighted(img,0.5, mask,0.5,1)


            if status=='lcn':
                #print(mask_label.is_drawing_finish())
                mask_label.release()


            if status =='rc':
                mask_label.delete_point_or_mask((gx,gy))
                mask = mask_label.draw()
                res = cv2.addWeighted(img,0.5, mask,0.5,1)
                status = ''
            if cv2.waitKey(8) & 0xFF == 27:
                break
        cv2.destroyAllWindows()