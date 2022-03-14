


class tempMemory:

    def __init__(self,):
        self.mems = {}

    
    def add_mem(self, name):
        self.mems[ name ] = {}
    
    def add_feqatures(self, mem_name, f_names):
        for name in f_names:
            self.mems[ mem_name ][name] = []


    #def add_feature(self, mem_name, f_name):

    def add( self, name, fname, data):
        self.mems[name][fname].append(data)

    def clear_all(self, name):
        for key in self.mems[ name ].keys():
            self.memsp[name][key] = []


    def get_feature(self, name, fname):
        return self.mems[ name ][fname]

    def get(self, name, fname, idx):
        return self.mems[ name ][fname][idx]