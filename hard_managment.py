import os
from pathlib import Path
import shutil
import threading

dirpath='D:/1'
dirname=dirpath

class HardManagment():

    def __init__(self,path):
        
        self.dirpath=path

        self.is_running=False
        self.working=False
    
    def set_path(self,path):

        self.dirpath=path

    def get_files_sort_date(self):

        try:

            paths = sorted(Path(self.dirpath).iterdir(), key=os.path.getmtime)
            # paths.reverse()
            return paths[-1]

        except:
            return ['']

    # #print(paths[-1])

    def get_storage_drive(self):
        #example c:

        total, used, free = shutil.disk_usage(self.dirpath)
        free_per=free*100/total
        used_per=used*100/total
        # #print(free_per, used_per)
        # self.start()
        return ({'free_per':free_per,'user_per':used_per})

    def remove_files_until_condition(self,Percentage_condotion=98):

        percentages=self.get_storage_drive()
        # #print(percentages['free_per'])

        # #print(self.working,self.is_running)

        if self.working==False:

            while not self.is_running:
                # #print('asdw')
                percentages=self.get_storage_drive()

                if int(percentages['free_per'])<int(Percentage_condotion):

                    try:

                        # #print('asdw')

                        path=self.get_files_sort_date()

                        self.remove_last_files(path)

                    except:
                        
                        break

                    self.working=True
                else:
                    self.is_running=True
            self.working=False

    def remove_last_files(self,path):

        try:
            shutil.rmtree(path)
        except OSError as e:
            pass
        try:
            os.remove(path)
        except:
            pass



    def start(self,Percentage_condotion):
        # if not self.is_running:
        self._timer = threading.Timer(2, self.remove_files_until_condition)
        # #print('check')
        self._timer.start()
            # self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


if __name__=='__main__':

    hm=HardManagment('D:/1')
    hm.get_storage_drive()
    # hm.remove_files_until_condition(97)
    # hm.remove_last_files()
    # path=hm.get_files_sort_date()
    # #print(path)
    hm.start(97)
    # hm.get_storage_drive()