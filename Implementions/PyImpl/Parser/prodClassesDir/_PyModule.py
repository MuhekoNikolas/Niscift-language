


class _PyModule():
    def __init__(self, module, ctx):
        self.module = module 
        self.ctx = ctx 

    def __getitem__(self, key):
        thisModuleDict = self.module.__dict__
        thisModuleDictKeys = list(thisModuleDict.keys())
        if key in thisModuleDictKeys:
            return thisModuleDict[key] 
        else:
            return None
        
    def __setitem__(self, key, value):
        temp = {
            "module": self.module, 
            "value": value
        }
        exec(f"module.{key} = value", temp)

    @property
    def __dict__(self):
        return self.module.__dict__
    
    def __vars__(self):
        return vars(self.module)