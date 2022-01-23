import numpy as np
import cv2 as cv

status = False
gx,gy=0,0
def draw_circle(event,x,y,flags,param):
    global status, gx,gy
    gx,gy=x,y
    if event == cv.EVENT_LBUTTONDOWN:
        status = True
        
    elif event == cv.EVENT_LBUTTONUP: 
        status = False
        #cv.circle(img,(x,y),100,(255,0,0),-1)



img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    _img = np.copy(img)
    if status:
        cv.rectangle( _img, (gx-10,gy-10), (gx+10,gy+10), (0,0,255))
    cv.imshow('image',_img)
    #if cv.waitKey(1) & 0xFF == 27:
    #    break
cv.destroyAllWindows()