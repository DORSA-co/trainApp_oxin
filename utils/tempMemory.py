


from struct import pack

from cv2 import add



class manageSelectedImage:

    def __init__(self,):
        self.selects_list = [] #memories
        self.selects_dict = {} #memories

    #Ceate a dictionary temp memory by name
    def clear(self):
        self.selects_list = [] #memories
        self.selects_dict = {} #memories


    def add(self, sheet_id, side, selection):
        if self.selects_dict.get(sheet_id) is None:
            self.selects_dict[sheet_id] = {}
        
        if self.selects_dict[sheet_id].get(side) is None:
            self.selects_dict[sheet_id][side] = []
        
        #side = self.__check_side__(side)
        selection = tuple( selection )
        if [sheet_id, side, selection] not in self.selects_list:
            self.selects_list.append( [sheet_id, side, selection] )

        self.selects_dict[sheet_id][side] += [selection]
        self.selects_dict[sheet_id][side] = list(dict.fromkeys(self.selects_dict[sheet_id][side]))
        
    

    def get_all_selections_dict(self,):
        return self.selects_dict
    
    def get_all_selections_list(self,):
        return self.selects_list

    def get_sheet_side_selections(self, sheet_id, side):
        return self.selects_dict.get(sheet_id, {}).get(side, [] )
        

    def remove_by_index(self,idxs):
        for idx in idxs:
            subject = self.selects_list[idx]
            
            self.selects_dict[subject[0]][subject[1]].remove(subject[2])
            self.selects_list.remove( subject )



    def remove_by_value(self, sheet_id, side, selection):
        selection = tuple(selection)

        self.selects_dict[sheet_id][side].remove(selection)

        self.selects_list.remove([sheet_id, side, selection ])



class manageLabel:
    
    def __init__(self,):
        self.labels_dict = {'mask':{}, 'bbox':{}} #memories

    #Ceate a dictionary temp memory by name
    def clear(self):
        self.labels_dict = {'mask':{}, 'bbox':{}} #memories


    def add(self, img_path, labels, label_type):
        self.labels_dict[label_type][img_path] = labels
        
    

    def get_all(self,):
        return self.labels_dict
    


    def get_label(self, label_type, img_path):
        return self.labels_dict.get(label_type, {}).get(img_path, [] )



    def remove_by_value(self, label_type, img_path):

        self.labels_dict[label_type][img_path] = []
