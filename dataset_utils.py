
import json
import os
from backend import pathStructure,date_funcs
import database_utils
class dataset_json():

    def read(self, path):
        with open(path) as jfile:
            file = json.load(jfile)
        return file


    def create_json_dataset(self,parms):

        _, defects_info = self.db.get_defects()

        self.set_user(parms['user_name'])
        self.set_user_id(parms['user_id']) 
        self.set_dataset_name(parms['dataset_name']) 
        self.set_path(parms['path'])
        self.set_max_size(parms['max_size']) 
        self.set_create_date(parms['date']) 
        self.set_modify_date('-') 
        self.set_count_defect(0) 
        self.set_count_perfect(0) 
        self.set_parms_classification(defects_info)




        self.dataset_details['basic']=self.main_parms
        self.dataset_details['classification']=self.classification_details
        self.dataset_details['binary']=self.binary_details

            # return {'user_name':user_name,'user_id':user_id,'dataset_name':dataset_name,'path':path,'max_size':max_size}
        path=parms['path']
        self.write(os.path.join(path,str(parms['dataset_name']+'.json')))
        # try:
        #     pathStructure.create_dataset_stracture(path)
        # except:
        #     path
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
        self.main_parms['user_name'] = name

    def set_user_id(self, user_id):
        self.main_parms['user_id'] = user_id


    def set_dataset_name(self, name):
        self.main_parms['dataset_name'] = name

    def set_path(self, path):
        self.main_parms['path'] = str(path)

    def set_max_size(self, max_size):
        self.main_parms['max_size'] = max_size
    
    def set_create_date(self,date):
        self.main_parms['date_created'] = date_funcs.get_date()
    
    def set_modify_date(self,date):
        self.main_parms['date_modify'] = date
    
    def set_count_defect(self,num):
        self.binary_details['count_defect'] = num
    
    def set_count_perfect(self,num):
        self.binary_details['count_perfect'] = num

    def set_classification_parms(self,defects_list):

        self.classification_details['defects_list'] = list(defects_list)

    def set_parms_classification(self,defects_info):

        for defect in defects_info:
            self.classification_details[defect['defect_ID']] = []

    ######################################
    #  Modify        ///////////////

    def modify_defect(self,reset=False):
        file=self.read_modify()
        count=file['binary']['count_defect']
        if reset:
            count=-1
        file['binary']['count_defect']=count+1
        print('modify',file)
        try:
            file=self.modify_date(file)
        except:
            print('eror modify date')
            pass
        self.write_modify(file)
    
    def modify_perfect(self,reset=False):
        file=self.read_modify()
        count=file['binary']['count_perfect']
        if reset:
            count=-1
        file['binary']['count_perfect']=count+1
        try:
            file=self.modify_date(file)
        except:
            pass
        self.write_modify(file)
    
    def add_update_classification(self,path, labels):
        file=self.read_modify()

        for label in labels:
            file['classification'][label].append(path)

        # if str(name) in file['classification'].keys():
        #     if AI:
        #         print('ai')
        #         print((file['classification'][name]['count']))
        #         count=int(file['classification'][name]['count'])
        #         count_dict={'count':count+1}
        #         file['classification'][name]=count_dict
        #     else :
        #         count_dict={'count':count}
        #         file['classification'][name]=count_dict
        #
        # else :
        #     count_dict={'count':count}
        #     name_dict={name:count_dict}
        #     file['classification'].update(name_dict)
        #     print(file)
        #     # self.add_update_classification(name,AI,count)
        self.write_modify(file)


    def read_modify(self):
        print('user_name',self.user_name_database)
        default_id = self.db.get_default_dataset(self.user_name_database)
        default_name = self.db.get_dateset_name(default_id)
        print('default_name',default_name)
        path = self.db.get_path_dataset(default_id)
        path=os.path.join(path, default_name)
        print('path', path)
        with open(path+'.json') as jfile:
            file = json.load(jfile)
        return file


    def modify_date(self,file):
        file['basic']['date_modify']=date_funcs.get_datetime()
        return file


    def write_modify(self,file):
        path = os.path.join(file['basic']['path'],file['basic']['dataset_name'])
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