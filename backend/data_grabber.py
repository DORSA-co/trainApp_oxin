import numpy as np
import cv2



COLOR_MAP = { 'sheet':(200,200,200), 'none':(20,20,20), 'pointer':(255,0,0), 'sline':(0,0,255), 'select':(0,255,0), 'defect':(200,20,0) }
THINKNESS_MAP = {'pointer':2, 'sline':1}


class sheetOverView():
    
    
    def __init__(self, h,w,nh=12,nw=50,color_map=COLOR_MAP, thickness_map=THINKNESS_MAP):
        self.w = w
        self.h = h
        self.nw = nw
        self.nh = nh
        self.color_map = color_map
        self.thickness_map = thickness_map
        
        self.cell_w = int(self.w / self.nw)
        self.cell_h = int(self.h / self.nh)
        
        self.sheet_layer = self.init_img(self.color_map['none'])
        self.line_layer  = self.init_img((0,0,0))
        self.defect_layer = self.init_img((0,0,0))
        self.select_layer = self.init_img((0,0,0))
        self.pointer_layer = self.init_img((0,0,0))
        
        
        self.n=0
        
        self.img = self.init_img(self.color_map['none'])
        self.res = np.copy(self.img)
    
    
    def init_img(self, color):
        img = np.ones((self.h, self.w, 3), dtype=np.uint8)
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
        self.pointer_layer = self.init_img((0,0,0))
        self.pointer_layer = self.draw_pointer(self.pointer_layer, pt)
        #return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def update_selected(self,selecteds):
        self.select_layer = self.init_img((0,0,0))
        for s in selecteds:
            self.select_layer = self.draw_selected(self.select_layer, s) 
        #return cv2.cvtColor( self.res, cv2.COLOR_BGR2RGB)
        
    def get_img(self):
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
        res = np.copy(img)
        x,y = pt
        xmin = x - self.cell_w // 2
        xmax = x + self.cell_w // 2
        ymin = y - self.cell_h // 2
        ymax = y + self.cell_h // 2
        
        #print('0',xmin,xmax,ymin,ymax, self.w, self.h)
        if xmin < 0:
            xmax = abs(xmin) + xmax
            xmin = 0
            #print('1',xmin,xmax,ymin,ymax)
        if xmax >= self.n*self.cell_w:
            xmin = xmin - (xmax - self.n*self.cell_w + 1) 
            xmax = self.n*self.cell_w - 1
            #print('2',xmin,xmax,ymin,ymax)
            
        if ymin < 0:
            ymax = abs(ymin) + ymax
            ymin = 0
            #print('3',xmin,xmax,ymin,ymax)
        if ymax >= self.h:
            ymin = ymin - (ymax - self.h + 1) 
            ymax = self.h - 1
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
            n= (self.w // self.nw) + 1
        for i in range(1,n):
            #x1 = i * self.cell_w
            #x2 = i * self.cell_w
            #y1 = 0 
            #y2 = self.h
            
            for j in range(0,DASH_N+1,2):
                
                x1 = i * self.cell_w
                x2 = i * self.cell_w
                y1 = j * ( self.h // DASH_N )
                y2 = (j+1) * ( self.h // DASH_N )
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
            
            x1 = n * self.cell_w - self.thickness_map['sline'] // 2
            x2 = n * self.cell_w - self.thickness_map['sline'] // 2
            y1 = j * ( self.h // DASH_N )
            y2 = (j+1) * ( self.h // DASH_N )
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
        x1 = n * self.cell_w
        x2 = (n+1) * self.cell_w
        res[:, x1:x2] = np.array(self.__rgb2bgr__( self.color_map['sheet'] ))
        return res
    
    
    #______________________________________________________________________________________________________________________________
    #    
    #______________________________________________________________________________________________________________________________
    def draw_selected(self,img,coordinate):
        i,j = coordinate
        xmin = i * self.cell_w 
        xmax = (i+1) * self.cell_w
        ymin = j * self.cell_h
        ymax = (j+1) * self.cell_h
        
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

        xmin = int(self.cell_w*xmin + self.cell_w*i )
        xmax = int(self.cell_w*xmax + self.cell_w*i )
        ymin = int(self.cell_h*ymin + self.cell_h*j )
        ymax = int(self.cell_h*ymax + self.cell_h*j )
        

        res= cv2.rectangle( res,
                            (xmin,ymin),
                            (xmax,ymax),
                            self.__rgb2bgr__( self.color_map['defect']),
                            thickness=-1)
        
        return res
    
        
if __name__ == '__main__':
    
    img = np.zeros((252,1260,3), dtype=np.uint8)
    sheet_view = sheetOverView(h=252,w=1260,nh=12,nw=30)
    
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
        
        
        sheet_view.update_pointer((300,50))
        
        
        img = sheet_view.get_img()
        t = time.time() - t
        all_t+=t
        
    print(all_t/100)
    cv2.imshow('res', cv2.cvtColor( img, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
