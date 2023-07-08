
import numpy as np
import random
import string
RANDOM=True

class connection_level2():

    def __init__(self):
        # self.ui_obj=ui_obj
        self.sheet_id = 900

    def ret_sheet_details(self):
        ret,details=self.connect()
        return ret,details
    
    def calculate_camera_and_projector(self):

        #calculate number of camera and projector
        ret, details=self.ret_sheet_details() 
        if ret:
            # cameras=round(details['width']/250)     # this should be change 
            # projector =int(details['width'] /14)
            cameras=np.random.choice([4, 6, 8, 10, 12])
            cameras=12
            projector=6
            # speed = np.random.choice([-1, 0, 1], p=[0.1, 0.1, 0.8])
            speed = 1
            return cameras, projector ,speed, details
 
        else:
            return 0, 0, None

    def get_number_camera_projector(self):
        cameras,projectors,_=self.calculate_camera_and_projector()
        return cameras,projectors

    def get_full_info(self):
        cameras, projectors, speed, details=self.calculate_camera_and_projector()
        return cameras, projectors ,speed, details

    def connect(self):
        # Should add connection function here and get details
        try:
            details={}
            if RANDOM:
                details.update({"sheet_id": str(self.sheet_id) + ''.join(random.choices(string.ascii_letters + string.digits, k = 2))})
                details.update({"pdl_number": np.random.randint(100,1000)})
                details.update({"heat_number": np.random.randint(100,1000)})
                details.update({"ps_number": np.random.randint(100,1000)})
                details.update({"width": np.random.randint(2950, 3050)})
                details.update({"length": np.random.randint(1000,10000)})
                details.update({"thickness": np.random.randint(10,50)})
                self.details=details
                self.sheet_id += 1
                # #print(details)
                return True,details
        except:
            return False,None


if __name__=='__main__':

    conn=connection_level2()
    cameras,projectors,details = conn.get_full_info()
    #print(cameras,projectors,details )
        