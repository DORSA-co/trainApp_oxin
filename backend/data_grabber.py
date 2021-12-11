import numpy as np
import cv2
import os 


COLOR_MAP = { 'sheet':(200,200,200), 'none':(20,20,20), 'pointer':(255,0,0), 'sline':(0,0,255), 'select':(0,255,0), 'defect':(200,20,0) }
THINKNESS_MAP = {'pointer':2, 'sline':1}

TOP = -1
BOTTOM=-1

class sheetOverView():
    
    
    def __init__(self,
                 path,
                 side,
                 sheet_shape,
                 sheet_grid,
                 color_map=COLOR_MAP,
                 thickness_map=THINKNESS_MAP ):
        
        self.path = path
        self.side = side
        self.sheet_shape = sheet_shape
        self.sheet_grid = sheet_grid
        
        self.color_map = color_map
        self.thickness_map = thickness_map
        
        self.cell_shape = (int(self.sheet_shape[0] / self.sheet_grid[0]) , 
                           int(self.sheet_shape[1] / self.sheet_grid[1]))
        
        
        self.sheet_layer = self.init_img(self.color_map['none'])
        self.line_layer  = self.init_img((0,0,0))
        self.defect_layer = self.init_img((0,0,0))
        self.select_layer = self.init_img((0,0,0))
        self.pointer_layer = self.init_img((0,0,0))
        
        
        self.n=0
        
        self.img = self.init_img(self.color_map['none'])
        self.res = np.copy(self.img)
        
        
        self.pt = (0,0)
        self.real_imgs=[]
        self.real_idxs=[]
        self.real_res=0
        
    
    
    def init_img(self, color):
        img = np.ones((self.sheet_shape[0], self.sheet_shape[1], 3), dtype=np.uint8)
        img[:,:] = self.__rgb2bgr__( color )
        return img
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_line(self,n):
        self.n = n + 1
        self.sheet_layer = self.draw_scaned(self.sheet_layer, n)
        self.line_layer = self.draw_sline(self.line_layer,n+1)
        #return cv2.cvtColor( self.img, cv2.COLOR_BGR2RGB)
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_defect(self,defects):
        for coordinate,pt1,pt2 in defects:
            self.defect_layer = self.draw_defect(self.defect_layer, coordinate, pt1, pt2)
        #self.res = np.copy( self.img )
        #return cv2.cvtColor( self.img, cv2.COLOR_BGR2RGB)
    
        

    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_pointer(self,pt):
        self.pt = pt
        self.pt = int(pt[0]*self.sheet_shape[1]), int( pt[1]*self.sheet_shape[0])
        
        self.pointer_layer = self.init_img((0,0,0))
        self.pointer_layer = self.draw_pointer(self.pointer_layer, self.pt )
        #return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_selected(self,selecteds):
        self.select_layer = self.init_img((0,0,0))
        for s in selecteds:
            self.select_layer = self.draw_selected(self.select_layer, s) 
        #return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
        
    def get_sheet_img(self):
        res = self.__add__(self.sheet_layer, self.defect_layer)
        res = cv2.addWeighted(res,0.7,self.select_layer,0.3,1)
        res = self.__add__(res, self.line_layer)
        res = self.__add__(res, self.pointer_layer)
        
        return cv2.cvtColor( res, cv2.COLOR_BGR2RGB)
        
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def __rgb2bgr__(self,inpt):
        if type(inpt)==type((1,)):
            r,g,b = inpt
            return (b,g,r)
    
    
    def __get_mask__(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
        return cv2.threshold(gray, 0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    
    def __add__(self,img1,img2):
        msk2 = self.__get_mask__(img2)
        msk1 = 255 - msk2
        
        img1 = cv2.bitwise_and(img1,img1,mask=msk1)
        img2 = cv2.bitwise_and(img2,img2,mask=msk2)
        return cv2.add(img1,img2)
        
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_pointer(self,img, pt):
        self.update_real_imgs()
        res = np.copy(img)
        x,y = pt
        print(pt)
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
            
        
        res = cv2.rectangle(res,
                            (xmin,ymin),
                            (xmax, ymax),
                            self.__rgb2bgr__( self.color_map['pointer']), 
                            self.thickness_map['pointer'])
        
        return res
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    
    def draw_slines(self, img, n=-1):
        DASH_N = 30
        res = np.copy(img)
        if n == -1:
            n= (self.sheet_shape[1] // self.sheet_grid[1]) + 1
        for i in range(1,n):
            #x1 = i * self.cell_shape[1]
            #x2 = i * self.cell_shape[1]
            #y1 = 0 
            #y2 = self.sheet_shape[0]
            
            for j in range(0,DASH_N+1,2):
                
                x1 = i * self.cell_shape[1]
                x2 = i * self.cell_shape[1]
                y1 = j * ( self.sheet_shape[0] // DASH_N )
                y2 = (j+1) * ( self.sheet_shape[0] // DASH_N )
                res = cv2.line(res,
                            (x1,y1),
                            (x2,y2),
                            self.__rgb2bgr__(self.color_map['sline']),
                            thickness=self.thickness_map['sline'],
                            lineType=cv2.LINE_AA)
                
    
        return res
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_sline(self, img, n):
        DASH_N = 30
        res = np.copy(img)         
        for j in range(0,DASH_N+1,3):
            
            x1 = n * self.cell_shape[1] - self.thickness_map['sline'] // 2
            x2 = n * self.cell_shape[1] - self.thickness_map['sline'] // 2
            y1 = j * ( self.sheet_shape[0] // DASH_N )
            y2 = (j+1) * ( self.sheet_shape[0] // DASH_N )
            res = cv2.line(res,
                        (x1,y1),
                        (x2,y2),
                        self.__rgb2bgr__(self.color_map['sline']),
                        thickness=self.thickness_map['sline'],
                        lineType=cv2.LINE_AA)
                
    
        return res
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_scaned(self,img,n):
        res = np.copy(img)
        x1 = n * self.cell_shape[1]
        x2 = (n+1) * self.cell_shape[1]
        res[:, x1:x2] = np.array(self.__rgb2bgr__( self.color_map['sheet'] ))
        return res
    
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_selected(self,img,coordinate):
        i,j = coordinate
        xmin = i * self.cell_shape[1] 
        xmax = (i+1) * self.cell_shape[1]
        ymin = j * self.cell_shape[0]
        ymax = (j+1) * self.cell_shape[0]
        
        select_img = np.copy(img)
        select_img = cv2.rectangle(select_img,
                                   (xmin,ymin),
                                   (xmax,ymax),
                                   self.__rgb2bgr__( self.color_map['select']),
                                   thickness=-1)
        
        #res = cv2.addWeighted(img, 0.7, select_img, 0.3, 1)
        return select_img
    
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
        x,y = self.pt
        nx,ny = x//self.cell_shape[1] , y//self.cell_shape[0]
        
        
        new_idxs=[]
        new_imgs=[]
        for i in range( nx-1, nx+2 ):
            for j in range(ny-1, ny+2):
                
                idx=(i,j)
                new_idxs.append(idx)
                
                if idx in self.real_idxs:
                    list_idx = self.real_idxs.index(idx)
                    new_imgs.append( self.real_imgs[list_idx] )
                
                else:
                    img_name = '{},{},{}'.format(i,j,self.side) + '.jpg'
                    img = cv2.imread( os.path.join( self.path, img_name),0 )    
                    new_imgs.append( img )
        self.real_idxs = new_idxs     
        self.real_imgs = new_imgs
    #_____________________________________________________________________________________________________________________________
    #
    #_____________________________________________________________________________________________________________________________
    def get_real_img(self):
        h,w=self.real_imgs[0].shape[:2]
        gridn = int( len(self.real_imgs)**0.5 )
        res_h, res_w = h * gridn, w * gridn
        res_img = np.zeros((res_h,res_w,3), np.uint8)
        
        for n in range(len(self.real_imgs)):
            j = n//gridn
            i = n - gridn * j
            #print(res_img[ j * res_h: (j+1)*res_h, i * res_w: (i+1)*res_w, 1].shape)
            res_img[ j * h: (j+1)*h, i * w: (i+1)*w, 0] = self.real_imgs[n]
            res_img[ j * h: (j+1)*h, i * w: (i+1)*w, 1] = self.real_imgs[n]
            res_img[ j * h: (j+1)*h, i * w: (i+1)*w, 2] = self.real_imgs[n]

        
        x,y = self.pt
        px = int( (x % self.cell_shape[1]) / self.cell_shape[1] * w ) + w
        py = int( (y % self.cell_shape[0]) / self.cell_shape[0] * h ) + h
        crop = res_img[ py - h//2: py + h//2 , px - w//2 : px + w//2 ]
        
        return cv2.cvtColor( crop, cv2.COLOR_BGR2RGB)
            
            
    
        
if __name__ == '__main__':
    
    img = np.zeros((252,1260,3), dtype=np.uint8)
    sheet_view = sheetOverView(path='110',
                               side=TOP,
                               sheet_shape=(252,1260),
                               sheet_grid=(12,30),
                               )
    
    '''
    img = sheet_view.draw_scaned(img,0)
    img = sheet_view.draw_scaned(img,1)
    
    img = sheet_view.draw_defect(img, (0,2), (0.2,0.3), (0.5, 0.6))
    img = sheet_view.draw_defect(img, (1,4), (0.3,0.4), (0.6, 0.9))
    
    img = sheet_view.draw_selected(img,(1,4))
    img = sheet_view.draw_selected(img,(0,2))
    
    img = sheet_view.draw_sline(img,1)
    img = sheet_view.draw_pointer(img, (100,200))
    '''
    import time
    all_t = 0
    for _ in range(100):
        t = time.time()
        sheet_view.update_line(0)
        sheet_view.update_line(1)
        sheet_view.update_line(2)
        
        sheet_view.update_defect([[(0,2), (0.2,0.3), (0.5,0.6)]])
        #img = sheet_view.update_line(2)
        
        selected = [[1,4],[0,0],[1,2]]
        sheet_view.update_selected(selected)
        
        
        sheet_view.update_pointer((0.2,0.3))
        #sheet_view.update_real_imgs()
        real_img = sheet_view.get_real_img()
        cv2.imshow('img real', cv2.resize(real_img, None , fx=0.2, fy=0.1))
        cv2.waitKey(0)
        img = sheet_view.get_sheet_img()
        t = time.time() - t
        all_t+=t
        
    print(all_t/100)
    cv2.imshow('res', cv2.cvtColor( img, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
