from matplotlib.pyplot import draw
import numpy as np
import cv2
import os 


COLOR_MAP = { 'sheet':(200,200,200), 'none':(20,20,20), 'pointer':(255,0,0), 'sline':(0,0,255), 'select':(0,255,0), 'defect':(200,20,0) }
THINKNESS_MAP = {'pointer':2, 'sline':1}

UP = "UP"
DOWN="DOWN"
HORIZONTAL=3
VERTICAL=4

IMAGE_SHAPE = (1200,1920)

class sheetOverView():
    
    
    def __init__(self,
                 path,
                 side,
                 sheet_shape,
                 sheet_grid,
                 actives_camera=(0,12), 
                 color_map=COLOR_MAP,
                 thickness_map=THINKNESS_MAP,
                 oriation=VERTICAL):
        
        self.path = path
        self.side = side
        self.sheet_shape = sheet_shape
        self.sheet_grid = sheet_grid
        self.actives_camera = actives_camera
        self.oriation = oriation
        self.color_map = color_map
        self.thickness_map = thickness_map
        
        self.cell_shape = (int(self.sheet_shape[0] / self.sheet_grid[0]) , 
                           int(self.sheet_shape[1] / self.sheet_grid[1]))

        
        
        self.n=0
        
        
        
        
        self.pt = (0,0)
        self.real_imgs=[]
        self.real_idxs=[]
        self.real_res=0
        
        self.sheet_img = self.init_img(self.color_map['sheet'])
        self.result_img = self.init_img(self.color_map['sheet'])
        self.sheet_img = self.draw_slines(self.sheet_img,-1)
        self.sheet_img = self.draw_discamera(self.sheet_img, self.actives_camera)
        self.result_img = np.copy( self.sheet_img)
    
    
    def init_img(self, color):
        img = np.ones((self.sheet_shape[0], self.sheet_shape[1], 3), dtype=np.uint8)
        img[:,:] *= np.array(self.__rgb2bgr__( color ), np.uint8)
        return img
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_line(self,n):
        if n==-1:
            self.n+=1
        else:
            self.n = n
        self.result_img = self.draw_noscaned(self.result_img,self.n)
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_defect(self,defects):
        for coordinate,pt1,pt2 in defects:
            self.defect_layer = self.draw_defect(self.defect_layer, coordinate, pt1, pt2)
        #self.res = np.copy( self.img )
        #return cv2.cvtColor( self.img, cv2.COLOR_BGR2RGB)
        self.result_img = self.update_result_img()
    
        

    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_pointer(self,pt):
        self.update_real_imgs()
        self.pt = int(pt[0]*self.sheet_shape[1]), int( pt[1]*self.sheet_shape[0])
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_selected(self,selecteds):
        self.select_layer = self.init_img((0,0,0))
        for s in selecteds:
            self.select_layer = self.draw_selected(self.select_layer, s) 
        #return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
        self.result_img = self.update_result_img()
    
    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def update_result_img(self):
        #res = self.__add__(self.sheet_layer, self.selec)
        res = cv2.addWeighted(self.sheet_img,0.7,self.select_layer,0.3,1)
        #res = self.__add__(res, self.line_layer)
        return res
        

    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def __rgb2bgr__(self,inpt):
        if type(inpt)==type((1,)):
            r,g,b = inpt
            return (b,g,r)
    
    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def __get_mask__(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
        return cv2.threshold(gray, 0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def __add__(self,img1,img2):
        msk2 = self.__get_mask__(img2)
        msk1 = 255 - msk2
        
        img1 = cv2.bitwise_and(img1,img1,mask=msk1)
        img2 = cv2.bitwise_and(img2,img2,mask=msk2)
        return cv2.add(img1,img2)
        
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def pointer2rect(self, pt):
        x,y = pt
        xmin = x - self.cell_shape[1] // 2
        xmax = x + self.cell_shape[1] // 2
        ymin = y - self.cell_shape[0] // 2
        ymax = y + self.cell_shape[0] // 2
        
        #print('0',xmin,xmax,ymin,ymax, self.sheet_shape[1], self.sheet_shape[0])
        if xmin < 0:
            xmax = abs(xmin) + xmax
            xmin = 0
            #print('1',xmin,xmax,ymin,ymax)
        if xmax >= self.n*self.cell_shape[1]:
            xmin = xmin - (xmax - self.n*self.cell_shape[1] + 1) 
            xmax = self.n*self.cell_shape[1] - 1
            #print('2',xmin,xmax,ymin,ymax)
            
        if ymin < 0:
            ymax = abs(ymin) + ymax
            ymin = 0
            #print('3',xmin,xmax,ymin,ymax)
        if ymax >= self.sheet_shape[0]:
            ymin = ymin - (ymax - self.sheet_shape[0] + 1) 
            ymax = self.sheet_shape[0] - 1
            #print('4',xmin,xmax,ymin,ymax)
        
        return (xmin,ymin),(xmax, ymax)
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_pointer(self,img, pt):
        #res = np.copy(img)
        corner1,corner2 = self.pointer2rect(pt)  
        res = cv2.rectangle(img,
                            corner1,
                            corner2,
                            self.__rgb2bgr__( self.color_map['pointer']), 
                            self.thickness_map['pointer'])
        return res
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def clean_pointer(self,img, pt):
        res = np.copy(img)
        corner1,corner2 = self.pointer2rect(pt)  
        res = cv2.rectangle(res,
                            corner1,
                            corner2,
                            (0,0,0), 
                            thickness=-1)
        
        return res
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    
    def draw_slines(self, img, n=-1):
        DASH_N = 30
        res = np.copy(img)
        if n == -1:
            if  self.oriation == HORIZONTAL:
                n= (self.sheet_shape[1] // self.cell_shape[1]) + 1
            if self.oriation == VERTICAL:
                n= (self.sheet_shape[0] // self.cell_shape[0]) + 1
        
        if self.oriation==HORIZONTAL:
            for i in range(1,n):
                x1 = self.cell_shape[1] * i
                x2 = self.cell_shape[1] * i
                y1 = 0
                y2 = self.sheet_shape[0] 
                
                self.draw_dline(img, (x1,y1), (x2,y2))
        
        if self.oriation==VERTICAL:
            for i in range(1,n):
                x1 = 0
                x2 = self.sheet_shape[1]
                y1 = self.cell_shape[0] * i
                y2 = self.cell_shape[0] * i
                
                self.draw_dline(img, (x1,y1), (x2,y2))

        return img
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_dline(self, img, pt1,pt2):
        dash_size = 5   
        x1,y1=pt1
        x2,y2=pt2
                
        if self.oriation==VERTICAL:
            
            for i in range(x1,x2,dash_size*2):
                img = cv2.line(img,
                        (i,y1),
                        (i+dash_size,y2),
                        self.__rgb2bgr__(self.color_map['sline']),
                        thickness=self.thickness_map['sline'],
                        lineType=cv2.LINE_AA)
                
            
        if self.oriation==HORIZONTAL:
            for i in range(y1,y2,dash_size*2):
                img = cv2.line(img,
                        (x1,i),
                        (x2,i+dash_size),
                        self.__rgb2bgr__(self.color_map['sline']),
                        thickness=self.thickness_map['sline'],
                        lineType=cv2.LINE_AA)
        return img
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_discamera(self,img,avtive_grids):
        s,e = avtive_grids
        if self.oriation==VERTICAL:
            s *= self.cell_shape[1]
            e *= self.cell_shape[1]
            img[:,:s]=self.color_map['none']
            img[:,e:]=self.color_map['none']
        
    
        if self.oriation==HORIZONTAL:
            s *= self.cell_shape[0]
            e *= self.cell_shape[0]
            img[:s]=self.color_map['none']
            img[e:]=self.color_map['none']
        return img
    
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________       
    def draw_noscaned(self, img, scanned_frame):
        if self.oriation==VERTICAL:
            s = scanned_frame * self.cell_shape[0]
            img[s:,]=self.color_map['none']
        
    
        if self.oriation==HORIZONTAL:
            s = scanned_frame * self.cell_shape[1]
            img[:,s:]=self.color_map['none']
        return img  
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_selected(self,img,coordinate):
        i,j = coordinate
        if self.oriation == HORIZONTAL:
            xmin = i * self.cell_shape[1] 
            xmax = (i+1) * self.cell_shape[1]
            ymin = j * self.cell_shape[0]
            ymax = (j+1) * self.cell_shape[0]
        
        if self.oriation == VERTICAL:
            xmin = i * self.cell_shape[1] 
            xmax = (i+1) * self.cell_shape[1]
            ymin = j * self.cell_shape[0]
            ymax = (j+1) * self.cell_shape[0]
            
        
        #select_img = np.copy(img)
        img = cv2.rectangle(img,
                                   (xmin,ymin),
                                   (xmax,ymax),
                                   self.__rgb2bgr__( self.color_map['select']),
                                   thickness=-1)
        
        #res = cv2.addWeighted(img, 0.7, select_img, 0.3, 1)
        return img
    
    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def draw_defect(self,img,coordinate, pt1,pt2):
        res = np.copy(img)
        xmin, ymin = pt1
        xmax, ymax = pt2
        i,j = coordinate

        xmin = int(self.cell_shape[1]*xmin + self.cell_shape[1]*i )
        xmax = int(self.cell_shape[1]*xmax + self.cell_shape[1]*i )
        ymin = int(self.cell_shape[0]*ymin + self.cell_shape[0]*j )
        ymax = int(self.cell_shape[0]*ymax + self.cell_shape[0]*j )
        

        res= cv2.rectangle( res,
                            (xmin,ymin),
                            (xmax,ymax),
                            self.__rgb2bgr__( self.color_map['defect']),
                            thickness=-1)
        
        return res
    
    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def update_real_imgs(self):
        try:
            x,y = self.pt
            max_frame = -1
            #nx,ny = x//self.cell_shape[1] , y//self.cell_shape[0]
            if self.oriation == VERTICAL:
                ncam = x//self.cell_shape[1]
                nframe = y//self.cell_shape[0]

                max_frame = self.sheet_grid[0]
            
            if self.oriation == HORIZONTAL:
                ncam = y//self.cell_shape[0]
                nframe = x//self.cell_shape[1]

                max_frame = self.sheet_grid[1]

            
            new_idxs=[]
            new_imgs=[]
            
            
            low_nc,up_nc,low_nf,up_nf=0,0,0,0

            low_nc = ncam-1
            up_nc = ncam+1
            low_nf = nframe-1
            up_nf = nframe+1

            #-------------------------------------------
            if low_nc <= self.actives_camera[0]:
                low_nc = self.actives_camera[0]
                up_nc = min( low_nc + 2 , self.actives_camera[1])

            if up_nc >= self.actives_camera[1]:
                up_nc = self.actives_camera[1]
                low_nc = max(up_nc-2 , self.actives_camera[0] )
            #-------------------------------------------
            if low_nf <=0:
                low_nf = 0
                up_nf = low_nf + 2
            if up_nf>= max_frame:
                up_nf = max_frame
                low_nf = max_frame - 2
            
            for nc in range( low_nc, up_nc+1 ):
                for nf in range(low_nf, up_nf+1):
                    idx=(nc,nf)
                    new_idxs.append(idx)
                    
                    if idx in self.real_idxs and False:
                        list_idx = self.real_idxs.index(idx)
                        new_imgs.append( self.real_imgs[list_idx] )
                    
                    else:
                        res_path = os.path.join(
                            self.path,
                            self.side,
                            str(nc+1),
                            str(nf) + '.jpg'
                        )
                        img = cv2.imread( res_path,0 )
                        if img is None:
                            print('*'*100)
                            # print(res_path)
                            print('cant load image {},{}'.format(nf, nc))
                            print('-'*100)
                            img = np.zeros(IMAGE_SHAPE, np.uint8)
                        new_imgs.append(img )
            
            
            self.real_idxs = new_idxs     
            self.real_imgs = new_imgs 
        except:
            print('eror load image')

    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def get_real_img(self):
        h,w=self.real_imgs[0].shape[:2]
        gridn = int( len(self.real_imgs)**0.5 )  #9 images are 3x3
        res_h, res_w = h * gridn, w * gridn
        res_img = np.zeros((res_h,res_w,3), np.uint8)
        
        for n in range(len(self.real_imgs)):
            if self.oriation == VERTICAL:
                i = n//gridn
                j = n - gridn * i
                #print(res_img[ j * res_h: (j+1)*res_h, i * res_w: (i+1)*res_w, 1].shape)
                res_img[ j * h: (j+1)*h, i * w: (i+1)*w, 0] = self.real_imgs[n]
                res_img[ j * h: (j+1)*h, i * w: (i+1)*w, 1] = self.real_imgs[n]
                res_img[ j * h: (j+1)*h, i * w: (i+1)*w, 2] = self.real_imgs[n]

        
        x,y = self.pt
    
        px = x / self.cell_shape[1]
        py = y / self.cell_shape[0]
        idxs = np.array( self.real_idxs)
        if self.oriation == VERTICAL:
            min_x,min_y = idxs.min(axis=0)
        elif self.oriation == HORIZONTAL:
            min_y,min_x = idxs.min(axis=0)
        
        px = px - min_x
        py = py - min_y

        px = int(px * w)
        py = int(py * h)

        x1,x2 = px - w//2, px + w//2
        y1,y2 = py - h//2 , py + h//2
        
        if x1<=0:
            x2 += abs(x1)
            x1=0

        elif x2>=res_w:
            x1 -= (x2 - res_w)
            x2 = res_w
        
        if y1<=0:
            y2 += abs(y1)
            y1=0
        elif y2>= res_h:
            y1 -= (y2-res_h)
            y2 = res_h

        crop = res_img[y1:y2, x1:x2]
        #crop = cv2.resize(res_img, (1920,1200))
        return cv2.cvtColor( crop, cv2.COLOR_BGR2RGB)


    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def get_sheet_img(self):
        res = self.draw_pointer(np.copy(self.result_img), self.pt )
        return res
        return cv2.cvtColor( self.result_img, cv2.COLOR_BGR2RGB)
        
      
    
        
if __name__ == '__main__':
    
    img = np.zeros((1260,252, 3), dtype=np.uint8)
    
    sheet_view = sheetOverView(path='110',
                               side=TOP,
                               sheet_shape=(252,1260),
                               sheet_grid=(12,30),
                               oriation=HORIZONTAL
                               )
    
    sheet_view= sheetOverView(path='110',
                               side=TOP,
                               sheet_shape=(int(252*2.76),252),
                               sheet_grid=(30,12),
                               oriation=VERTICAL,
                               actives_camera=(0,8)
                               )
    
    selected = [[0,0],[1,1],[2,2]]
    sheet_view.update_selected(selected)
    selected = [[0,0],[1,1]]
    sheet_view.update_selected(selected)
    
    sheet_view.update_line(6)
    
    
    cv2.imshow('res', sheet_view.result_img )
    cv2.waitKey(0)
    '''
    img = sheet_view.draw_sline(img,1)
    img = sheet_view.draw_pointer(img, (100,200))
    '''
    # import time
    # all_t = 0
    # for _ in range(100):
    #     t = time.time()
    #     sheet_view.update_line(0)
    #     sheet_view.update_line(1)
    #     sheet_view.update_line(2)
        
    #     sheet_view.update_defect([[(11,2), (0.2,0.3), (0.5,0.6)]])
    #     #img = sheet_view.update_line(2)
    #     sheet_view.update_line()
    #     selected = [[1,4],[0,0],[1,2]]
    #     sheet_view.update_selected(selected)
        
        
    #     sheet_view.update_pointer((0.2,0.3))
    #     #sheet_view.update_real_imgs()
    #     real_img = sheet_view.get_real_img()
    #     cv2.imshow('img real', cv2.resize(real_img, None , fx=0.2, fy=0.1))
    #     cv2.waitKey(0)
    #     img = sheet_view.get_sheet_img()
    #     t = time.time() - t
    #     all_t+=t
        
    # print(all_t/100)
    # cv2.imshow('res', cv2.cvtColor( img, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)
