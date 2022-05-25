import json
import os
from backend import pathStructure,date_funcs
import database_utils


BASIC_INFO = 'basic'
DATASET_NAME = 'dataset_name'
DATE_CREATED = 'date_created'
DATE_MODIFIED = 'date_modify'
MAX_SIZE = 'max_size'
PATH = 'path'
USER_ID = 'user_id'
USER_NAME = 'user_name'
BINARY = 'binary'
COUNT_DEFECT = 'count_defect'
COUNT_PERFECT = 'count_perfect'
CLASSIFICATION = 'classification'
NONE_CLASS = 'None'


class dataset_json():

    def read(self, path):
        with open(path) as jfile:
            file = json.load(jfile)
        return file


    def create_json_dataset(self,parms):

        self.set_user(parms[USER_NAME]) 
        self.set_user_id(parms[USER_ID]) 
        self.set_dataset_name(parms[DATASET_NAME]) 
        self.set_path(parms[PATH],parms[DATASET_NAME]) 
        self.set_max_size(parms[MAX_SIZE]) 
        self.set_create_date(parms['date']) 
        self.set_modify_date('-') 
        self.set_count_defect(0) 
        self.set_count_perfect(0) 
        self.set_parms_classification(NONE_CLASS,0)




        self.dataset_details[BASIC_INFO]=self.main_parms
        self.dataset_details[CLASSIFICATION]=self.classification_details
        self.dataset_details[BINARY]=self.binary_details

            # return {'user_name':user_name,'user_id':user_id,'dataset_name':dataset_name,'path':path,'max_size':max_size}
        path=os.path.join(parms[PATH],parms[DATASET_NAME])
        self.write(os.path.join(path,str(parms[DATASET_NAME]+'.json')))
        try:
            pathStructure.create_dataset_stracture(path)
        except:
            path
    def write(self,path):    
        print('write',path)
        with open(str(path), 'w') as f:
            json.dump(self.dataset_details, f,indent=4, sort_keys=True)
            # json.dump(self.classification, f,indent=4, sort_keys=True)

    def __init__(self,):
        self.db=database_utils.dataBaseUtils()
        self.dataset_details = {}
        self.main_parms={}
        # self.classification={}
        self.classification_details = {}
        self.binary_details = {}

        self.user_name_database=''
        
    def set_user_name_database(self,name):
        self.user_name_database=name
    #--------------------------------------------------------
    #
    #--------------------------------------------------------
    def set_user(self, name):
        self.main_parms[USER_NAME] = name

    def set_user_id(self, user_id):
        self.main_parms[USER_ID] = user_id


    def set_dataset_name(self, name):
        self.main_parms[DATASET_NAME] = name

    def set_path(self, path,name):
        self.main_parms[PATH] = str(path+name)

    def set_max_size(self, max_size):
        self.main_parms[MAX_SIZE] = max_size
    
    def set_create_date(self,date):
        self.main_parms[DATE_CREATED] = date_funcs.get_date()
    
    def set_modify_date(self,date):
        self.main_parms[DATE_MODIFIED] = date
    
    def set_count_defect(self,num):
        self.binary_details[COUNT_DEFECT] = num
    
    def set_count_perfect(self,num):
        self.binary_details[COUNT_PERFECT] = num

    def set_classification_parms(self,defects_list):

        self.classification_details['defects_list'] = list(defects_list)

    def set_parms_classification(self,name,count):

        self.classification_details[name] = count

    ######################################
    #  Modify        ///////////////

    def modify_defect(self,reset=False):
        file=self.read_modify()
        count=file[BINARY][COUNT_DEFECT]
        if reset:
            count=-1
        file[BINARY][COUNT_DEFECT]=count+1
        print('modify',file)
        try:
            file=self.modify_date(file)
        except:
            print('eror modify date')
            pass
        self.write_modify(file)
    
    def modify_perfect(self,reset=False):
        file=self.read_modify()
        count=file[BINARY][COUNT_PERFECT]
        if reset:
            count=-1
        file[BINARY][COUNT_PERFECT]=count+1
        try:
            file=self.modify_date(file)
        except:
            pass
        self.write_modify(file)
    
    def add_update_classification(self,name,AI=True,number=0):
        count=number
        file=self.read_modify()

        if count !=0:
            AI=False

        if str(name) in file[CLASSIFICATION].keys():
            if AI:
                print('ai')
                print((file[CLASSIFICATION][name]['count']))
                count=int(file[CLASSIFICATION][name]['count'])
                count_dict={'count':count+1}
                file[CLASSIFICATION][name]=count_dict
            else :
                count_dict={'count':count}
                file[CLASSIFICATION][name]=count_dict

        else :
            count_dict={'count':count}
            name_dict={name:count_dict}
            file[CLASSIFICATION].update(name_dict)
            print(file)
            # self.add_update_classification(name,AI,count)
        self.write_modify(file)


    def read_modify(self):
        print('user_name',self.user_name_database)
        default_name = self.db.get_default_dataset(self.user_name_database)
        print('default_name',default_name)
        path = self.db.get_path_dataset(default_name)
        path=os.path.join(path,default_name)
        print(PATH,path)
        with open(path+'.json') as jfile:
            file = json.load(jfile)
        return file


    def modify_date(self,file):
        file[BASIC_INFO][DATE_MODIFIED]=date_funcs.get_datetime()
        return file


    def write_modify(self,file):
        path = os.path.join(file[BASIC_INFO][PATH],file[BASIC_INFO][DATASET_NAME])
        with open(str(path+'.json'), 'w') as f:
            json.dump(file, f,indent=4, sort_keys=True)


    





if __name__=='__main__':

    j = dataset_json()
    j.set_user_name_database('ali')
    i=1
    # j.add_update_classification('ads3',number=11)
    # for i in range(100):
    # j.modify_defect()
    j.modify_perfect()