

   

from ._ClassesReprMeta import _ClassesReprMeta

class _True(metaclass=_ClassesReprMeta):
    def __init__(self, ctx):
        self.ctx = ctx
    
    def __repr__(self):
        return "True"

class _False(metaclass=_ClassesReprMeta):
    def __init__(self, ctx):
        self.ctx = ctx
    
    def __repr__(self):
        return "False"