DEBUG=False

class moveOnList:

    def __init__(self):

        self.lists={}
        self.idxs={}

    def add(self, mylist, name):
        self.lists[name] = mylist
        self.idxs [name] = 0

    
    def check(self,name):
        if name in self.lists.keys():
            return True
        return False


    def build_next_func(self, name):   
        def next_on_list():
            self.idxs[name]+=1
            self.idxs[name]=min(self.idxs[name],len(self.lists[name])-1)

            if DEBUG:
                print("*"*50,self.idxs[name],len(self.lists[name]))
        return next_on_list


    def build_prev_func(self, name):  
        def prev_on_list():
            self.idxs[name]-=1
            self.idxs[name]=max(self.idxs[name],0)
            
            if DEBUG:
                print("*"*50,self.idxs[name],len(self.lists[name]))

        return prev_on_list


    def next_on_list(self,name):
        self.idxs[name]+=1
        #self.idxs[name]=min(self.idxs[name],len(self.lists[name])-1)
        if self.idxs[name] >= len(self.lists[name]) :
            self.idxs[name] = 0

        if DEBUG:
            print("*"*50,self.idxs[name],len(self.lists[name]))


    def prev_on_list(self,name):
        self.idxs[name]-=1
        #self.idxs[name]=max(self.idxs[name],0)
        if self.idxs[name] < 0:
            self.idxs[name] = len(self.lists[name])-1

        if DEBUG:
            print("*"*50,self.idxs[name],len(self.lists[name]))


    def get_current(self,name):
        mylist = self.lists[ name ] 
        idx = self.idxs[name]
        return mylist[idx]


    def get_list(self,name):
        mylist = self.lists[ name ] 
        return mylist

    def get_count(self,name):
        mylist = self.lists[ name ] 
        return len( mylist )




class moveOnImagrList:

    def __init__(self, sub_directory='', step=4):
        """this class is used to create a iterable list of imageswith ability to get next/prev items

        :param sub_directory: subdirectory of images, defaults to ''
        :type sub_directory: str, optional
        :param step: step to get next/prev on list, this also determins n returning current items of the list, defaults to 4
        :type step: int, optional
        """

        self.lists = {}
        self.lists_annots={}
        self.idxs={}
        self.sub_directory = sub_directory
        self.step = step

    def add_sub_directory(self, sub_directory):
        self.sub_directory = sub_directory

        
    def add(self, mylist, name, mylist_annots=[]):
        self.lists[name] = mylist
        self.lists_annots[name] = mylist_annots
        self.idxs [name] = 0

    
    def check(self,name):
        if name in self.lists.keys():
            return True
        return False

    def build_next_func(self, name):
        """this function is used to build next function for iterable list to get next items

        :param name: list name
        :type name: _type_
        """

        def next_on_list():
            if self.idxs[name] + self.step < len(self.lists[name]):
                self.idxs[name] += self.step
            
            #self.idxs[name]=min(self.idxs[name],len(self.lists[name])-1)

            if DEBUG:
                print("*"*50,self.idxs[name],len(self.lists[name]))
        return next_on_list


    def build_prev_func(self, name):
        """this function is used to build prev function for iterable list to get prev items

        :param name: list name
        :type name: _type_
        """

        def prev_on_list():
            if self.idxs[name] - self.step >= 0:
                self.idxs[name] -= self.step
            #self.idxs[name]=max(self.idxs[name],0)
            
            if DEBUG:
                print("*"*50,self.idxs[name],len(self.lists[name]))

        return prev_on_list


    def get_current(self,name):
        mylist = self.lists[ name ] 
        idx = self.idxs[name]
        return idx, mylist[idx]

    
    def get_n_current(self, name, get_annots=False):
        """this function is used to get n current images from list

        :param name: list name
        :type name: str
        :param get_annots: boolean to determine whther to also return image annotations, defaults to False
        :type get_annots: bool, optional
        :return: _description_
        :rtype: _type_
        """

        mylist = self.lists[ name ]
        mylist_annots = self.lists_annots[name]
        #print(self.lists_annots)
        idx = self.idxs[name]
        list = []
        list_annots = []
        for i in range(idx, idx+self.step):
            if i < len(self.lists[name]):
                list.append(mylist[i])
                if get_annots:
                    list_annots.append(mylist_annots[i])

        if not get_annots:
            return list

        else:
            return list, list_annots


    def get_list(self,name):
        mylist = self.lists[ name ] 
        return mylist

    def get_count(self,name):
        mylist = self.lists[ name ] 
        return len( mylist )




if __name__ == '__main__':
    l = ['a1', 'a2', 'a3', 33, 'a4', 'a5']
    obj = moveOnImagrList(sub_directory='')
    obj.add(l,'coils')

    next_f = obj.build_next_func('coils')
    prev_f = obj.build_prev_func('coils')
    
    next_f()
    next_f()
    prev_f()
    prev_f()
    
    
    #print(obj.get_current('coils'))