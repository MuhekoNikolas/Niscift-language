


from ._ClassesReprMeta import _ClassesReprMeta

class _Undefined(metaclass=_ClassesReprMeta):
    def __init__(self, ctx):
        self.isCallable = False 
        self.ctx = ctx

    def __repr__(self):
        return 'undefined'


class _None(metaclass=_ClassesReprMeta):
    def __init__(self, ctx):
        self.isCallable = False 
        self.ctx = ctx

    def __repr__(self):
        return 'None'