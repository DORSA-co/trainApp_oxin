from opcua import Client, ua
import os
import texts_codes
import json
try:
    from backend import texts
except:
    # pass
    try:
        import texts
    except:
        pass

import threading

PLC_DEFAULT=[{'id': 25, 'name': 'ProjectorPulseTrig', 'path': 'ns=4;i=2', 'value0': 'True'}, {'id': 26, 'name': 'NCamera', 'path': 'ns=4;i=3', 'value0': '2'}, {'id': 27, 'name': 'MemSoftwareStart', 'path': 'ns=4;i=4', 'value0': 'False'}, {'id': 28, 'name': 'MemDownLimitSwitchIn', 'path': 'ns=4;i=5', 'value0': 'False'}, {'id': 29, 'name': 'MemDownLimitSwitchOut', 'path': 'ns=4;i=6', 'value0': 'False'}, {'id': 30, 'name': 'MemDownProjectorOnOff1', 'path': 'ns=4;i=12', 'value0': 'False'}, {'id': 31, 'name': 'MemDownProjectorOnOff2', 'path': 'ns=4;i=11', 'value0': 'False'}, {'id': 32, 'name': 'MemDownProjectorOnOff3', 'path': 'ns=4;i=10', 'value0': 'False'}, {'id': 33, 'name': 'MemDownProjectorOnOff4', 'path': 'ns=4;i=9', 'value0': 'False'}, {'id': 34, 'name': 'MemDownProjectorOnOff5', 'path': 'ns=4;i=8', 'value0': 'False'}, {'id': 35, 'name': 'MemDownProjectorOnOff6', 'path': 'ns=4;i=7', 'value0': 'False'}, {'id': 36, 'name': 'MemDownValve', 'path': 'ns=4;i=13', 'value0': 'False'}, {'id': 37, 'name': 'DownTemperature', 'path': 'ns=4;i=23', 'value0': '134.55'}, {'id': 38, 'name': 'DownHighThreshold', 'path': 'ns=4;i=24', 'value0': '0.0'}, {'id': 39, 'name': 'DownLowThreshold', 'path': 'ns=4;i=25', 'value0': '0.0'}, {'id': 40, 'name': 'MemUpLimitSwitchIn', 'path': 'ns=4;i=26', 'value0': 'False'}, {'id': 41, 'name': 'MemUpLimitSwitchOut', 'path': 'ns=4;i=27', 'value0': 'False'}, {'id': 42, 'name': 'MemUpProjectorOnOff1', 'path': 'ns=4;i=33', 'value0': 'False'}, {'id': 43, 'name': 'MemUpProjectorOnOff2', 'path': 'ns=4;i=32', 'value0': 'False'}, {'id': 44, 'name': 'MemUpProjectorOnOff3', 'path': 'ns=4;i=31', 'value0': 'False'}, {'id': 45, 'name': 'MemUpProjectorOnOff4', 'path': 'ns=4;i=30', 'value0': 'False'}, {'id': 46, 'name': 'MemUpProjectorOnOff5', 'path': 'ns=4;i=29', 'value0': 
'False'}, {'id': 47, 'name': 'MemUpProjectorOnOff6', 'path': 'ns=4;i=28', 'value0': 'False'}, {'id': 48, 'name': 'MemUpValve', 'path': 'ns=4;i=34', 'value0': 'False'}, {'id': 49, 'name': 'UpTemperature', 'path': 'ns=4;i=35', 
'value0': '27.6'}, {'id': 50, 'name': 'UpHighThreshold', 'path': 'ns=4;i=36', 'value0': '0.0'}, {'id': 51, 'name': 'UpLowThreshold', 'path': 'ns=4;i=37', 'value0': '0.0'}, {'id': 52, 'name': 'MemDistanceSensor', 'path': 'ns=4;i=38', 'value0': 'False'}]






class management():
    """
    this class is used to create and manage opc/plc object

    Args:
        ip: plc ip (in string)
        ui_obj: main ui object
    
    Returns: PLC object
    """

    def __init__(self, ip, ui_obj,logger):
        self.ip=ip
        self.set_file_name('text_plc_parms')
        self.ui_obj = ui_obj
        self.spec_pathes=set_pathes(PLC_DEFAULT)
        self.logger = logger
    

    def connection(self):
        """
        this function is used to connect to plc

        Returns:
            resault: a boolean deermining if connected or not
        """

        ##print('Start Connecting to {}'.format(self.ip))
        self.ui_obj.logger.create_new_log(message=texts.MESSEGES['plc_start_connecting']['en'] + ' ip: ' + str(self.ip), level=1)
        self.client = Client(self.ip)
        # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
        try:
            self.client.connect()
            ##print('Connection Successed')
            return True

        except:
            ##print('Connection Eror')
            return False

    
    def disconnect(self):
        """
        this functino is used to disconnect from plc

        Args: None

        Returns: None
        """

        self.client.disconnect()


    def get_value(self, path):
        """
        this function is used to get value of a logic from plc using its path

        Args:
            path (_type_): plc logic path (in string)

        Returns:
            value: value stored in path, if failed to load, return '-'
            data_value: if failed to load, return message error
        """

        # try:
        var = self.client.get_node(path)
        # #print(var)
        # data_value=var.get_data_value() # get value of node as a DataValue object   this line is not imporant
        value=var.get_value() # get value of node as a python builtin
        # #print('x'*5,value)
        return (value, None)

        # except:
        #     # #print('except')
        #     return '-', texts.ERRORS['plc_path_error'][self.ui_obj.language]


    def set_value(self, path, value):
        """
        this function is used to set/update value of a logic, using its path on plc

        Args:
            path (_type_): path of the logic (in string)
            value (_type_): input value to update (digit or boolean)

        Returns: None
        """

        var = self.client.get_node(path)
        # print(path,'    ',value)
        try:
            if type(value) == int:
                # #print('number')
                data = ua.DataValue(ua.Variant(value, ua.VariantType.Byte))
                var.set_value(data)

            else:
                # #print('value:',value)
                if value=='False':
                    value_=False
                    ##print(value_)
                else:
                    value_=True

                value = ua.DataValue(ua.Variant(value_,ua.VariantType.Boolean))
                var.set_value(value)
            
            self.logger.create_new_log(
                code=texts_codes.SubTypes["plc_write_successfully"],
                message=texts.MESSEGES["plc_write_successfully"]["en"]+' '+str(path)+str(value),
                level=1,
                )

            return True
        
        except:

            self.logger.create_new_log(
                code=texts_codes.SubTypes["plc_write_failed"],
                message=texts.MESSEGES["plc_write_failed"]["en"]+' '+str(path)+str(value),
                level=5,
                )


            return False
            

    def set_file_name(self, name):
        """
        this function is used to set json file name to store plc params

        Arge: None

        Returns: None
        """

        self.text_plc_parms=name  


    def write(self, value):
        """
        this function is used to write plc values on json file

        Args:
            value (_type_): in dict
        """
        
        # #print('write',path)
        path = os.path.join(self.text_plc_parms+'.json')
        # #print('value',value)
        with open(str(path), 'w') as f:
            json.dump(value, f,indent=4, sort_keys=True)

    # def get_pathes(self):

    #     # self.parms=self.db_obj.load_plc_parms()


    # def get_MemDistanceSensor(self):

    #     x=self.parms[0]['path']
    #     #print(x)

    # def set_pathes(self,pathes):

    #     pathes=pathes[0]
    #     tom_info = people_by_name.get("Tom")




    def set_cams_and_prejector(self):
        n_cam=3
        threading.Thread(target=self.set_value,args=(self.spec_pathes['NCamera'], n_cam)).start()

        for proj in range(1,7):
            mode=True
            threading.Thread(target=self.set_value,args=(self.spec_pathes['MemDownProjectorOnOff{}'.format(proj)], str(mode))).start()
            threading.Thread(target=self.set_value,args=(self.spec_pathes['MemUpProjectorOnOff{}'.format(proj)], str(mode))).start()
        print('*'*100)
        return True









def set_pathes(pathes):
    path_dict={}
    # pathes=pathes[0]
    # #print(pathes)
    # value='ProjectorPulseTrig'
    # path_list=
    PLC_items = [
        "ProjectorPulseTrig",
        "NCamera",
        "MemSoftwareStart",
        "MemDownLimitSwitchIn",
        "MemDownLimitSwitchOut",
        "MemDownProjectorOnOff1",
        "MemDownProjectorOnOff2",
        "MemDownProjectorOnOff3",
        "MemDownProjectorOnOff4",
        "MemDownProjectorOnOff5",
        "MemDownProjectorOnOff6",
        "MemDownValve",
        "DownTemperature",
        "DownHighThreshold",
        "DownLowThreshold",
        "MemUpLimitSwitchIn",
        "MemUpLimitSwitchOut",
        "MemUpProjectorOnOff1",
        "MemUpProjectorOnOff2",
        "MemUpProjectorOnOff3",
        "MemUpProjectorOnOff4",
        "MemUpProjectorOnOff5",
        "MemUpProjectorOnOff6",
        "MemUpValve",
        "UpTemperature",
        "UpHighThreshold",
        "UpLowThreshold",
        "MemDistanceSensor",
    ]
    # values=['MemDistanceSensor','NCamera','MemDownValve','MemUpValve','UpTemperature','DownTemperature']
    # tom_info = pathes.get("ProjectorPulseTrig")
    for i, dic in enumerate(pathes):
        if dic['name'] in PLC_items:
            path_dict.update({dic['name']:dic['path']})
    return path_dict









#        parms [{'id': 25, 'name': 'ProjectorPulseTrig', 'path': 'ns=4;i=2', 'value0': 'True'}, {'id': 26, 'name': 'NCamera', 'path': 'ns=4;i=3', 'value0': '2'}, {'id': 27, 'name': 'MemSoftwareStart', 'path': 'ns=4;i=4', 'value0': 'False'}, {'id': 28, 'name': 'MemDownLimitSwitchIn', 'path': 'ns=4;i=5', 'value0': 'False'}, {'id': 29, 'name': 'MemDownLimitSwitchOut', 'path': 'ns=4;i=6', 'value0': 'False'}, {'id': 30, 'name': 'MemDownProjectorOnOff1', 'path': 'ns=4;i=7', 'value0': 'False'}, {'id': 31, 'name': 'MemDownProjectorOnOff2', 'path': 'ns=4;i=8', 'value0': 'False'}, {'id': 32, 'name': 'MemDownProjectorOnOff3', 'path': 'ns=4;i=9', 'value0': 'False'}, {'id': 33, 'name': 'MemDownProjectorOnOff4', 'path': 'ns=4;i=10', 'value0': 'False'}, {'id': 34, 'name': 'MemDownProjectorOnOff5', 'path': 'ns=4;i=11', 'value0': 'False'}, {'id': 35, 'name': 'MemDownProjectorOnOff6', 'path': 'ns=4;i=12', 'value0': 'False'}, {'id': 36, 'name': 'MemDownValve', 'path': 'ns=4;i=13', 'value0': 'False'}, {'id': 37, 'name': 'DownTemperature', 'path': 'ns=4;i=23', 'value0': '134.55'}, {'id': 38, 'name': 'DownHighThreshold', 'path': 'ns=4;i=24', 'value0': '0.0'}, {'id': 39, 'name': 'DownLowThreshold', 'path': 'ns=4;i=25', 'value0': '0.0'}, {'id': 40, 'name': 'MemUpLimitSwitchIn', 'path': 'ns=4;i=26', 'value0': 'False'}, {'id': 41, 'name': 'MemUpLimitSwitchOut', 'path': 'ns=4;i=27', 'value0': 'False'}, {'id': 42, 'name': 'MemUpProjectorOnOff1', 'path': 'ns=4;i=28', 'value0': 'False'}, {'id': 43, 'name': 'MemUpProjectorOnOff2', 'path': 'ns=4;i=29', 'value0': 'False'}, {'id': 44, 'name': 'MemUpProjectorOnOff3', 'path': 'ns=4;i=30', 'value0': 'False'}, {'id': 45, 'name': 'MemUpProjectorOnOff4', 'path': 'ns=4;i=31', 'value0': 'False'}, {'id': 46, 'name': 'MemUpProjectorOnOff5', 'path': 'ns=4;i=32', 'value0': 
# 'False'}, {'id': 47, 'name': 'MemUpProjectorOnOff6', 'path': 'ns=4;i=33', 'value0': 'False'}, {'id': 48, 'name': 'MemUpValve', 'path': 'ns=4;i=34', 'value0': 'False'}, {'id': 49, 'name': 'UpTemperature', 'path': 'ns=4;i=35', 
# 'value0': '27.6'}, {'id': 50, 'name': 'UpHighThreshold', 'path': 'ns=4;i=36', 'value0': '0.0'}, {'id': 51, 'name': 'UpLowThreshold', 'path': 'ns=4;i=37', 'value0': '0.0'}, {'id': 52, 'name': 'MemDistanceSensor', 'path': 'ns=4;i=38', 'value0': 'False'}] # 


if __name__=='__main__':
    




    data=[{'id': 25, 'name': 'ProjectorPulseTrig', 'path': 'ns=4;i=2', 'value0': 'True'}, {'id': 26, 'name': 'NCamera', 'path': 'ns=4;i=3', 'value0': '2'}, {'id': 27, 'name': 'MemSoftwareStart', 'path': 'ns=4;i=4', 'value0': 'False'}, {'id': 28, 'name': 'MemDownLimitSwitchIn', 'path': 'ns=4;i=5', 'value0': 'False'}, {'id': 29, 'name': 'MemDownLimitSwitchOut', 'path': 'ns=4;i=6', 'value0': 'False'}, {'id': 30, 'name': 'MemDownProjectorOnOff1', 'path': 'ns=4;i=7', 'value0': 'False'}, {'id': 31, 'name': 'MemDownProjectorOnOff2', 'path': 'ns=4;i=8', 'value0': 'False'}, {'id': 32, 'name': 'MemDownProjectorOnOff3', 'path': 'ns=4;i=9', 'value0': 'False'}, {'id': 33, 'name': 'MemDownProjectorOnOff4', 'path': 'ns=4;i=10', 'value0': 'False'}, {'id': 34, 'name': 'MemDownProjectorOnOff5', 'path': 'ns=4;i=11', 'value0': 'False'}, {'id': 35, 'name': 'MemDownProjectorOnOff6', 'path': 'ns=4;i=12', 'value0': 'False'}, {'id': 36, 'name': 'MemDownValve', 'path': 'ns=4;i=13', 'value0': 'False'}, {'id': 37, 'name': 'DownTemperature', 'path': 'ns=4;i=23', 'value0': '134.55'}, {'id': 38, 'name': 'DownHighThreshold', 'path': 'ns=4;i=24', 'value0': '0.0'}, {'id': 39, 'name': 'DownLowThreshold', 'path': 'ns=4;i=25', 'value0': '0.0'}, {'id': 40, 'name': 'MemUpLimitSwitchIn', 'path': 'ns=4;i=26', 'value0': 'False'}, {'id': 41, 'name': 'MemUpLimitSwitchOut', 'path': 'ns=4;i=27', 'value0': 'False'}, {'id': 42, 'name': 'MemUpProjectorOnOff1', 'path': 'ns=4;i=28', 'value0': 'False'}, {'id': 43, 'name': 'MemUpProjectorOnOff2', 'path': 'ns=4;i=29', 'value0': 'False'}, {'id': 44, 'name': 'MemUpProjectorOnOff3', 'path': 'ns=4;i=30', 'value0': 'False'}, {'id': 45, 'name': 'MemUpProjectorOnOff4', 'path': 'ns=4;i=31', 'value0': 'False'}, {'id': 46, 'name': 'MemUpProjectorOnOff5', 'path': 'ns=4;i=32', 'value0': 
'False'}, {'id': 47, 'name': 'MemUpProjectorOnOff6', 'path': 'ns=4;i=33', 'value0': 'False'}, {'id': 48, 'name': 'MemUpValve', 'path': 'ns=4;i=34', 'value0': 'False'}, {'id': 49, 'name': 'UpTemperature', 'path': 'ns=4;i=35', 
'value0': '27.6'}, {'id': 50, 'name': 'UpHighThreshold', 'path': 'ns=4;i=36', 'value0': '0.0'}, {'id': 51, 'name': 'UpLowThreshold', 'path': 'ns=4;i=37', 'value0': '0.0'}, {'id': 52, 'name': 'MemDistanceSensor', 'path': 'ns=4;i=38', 'value0': 'False'}]


    x=set_pathes(data)
    ns=4;i=3
    #print(x)