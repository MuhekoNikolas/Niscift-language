



class _Float(object):
    def __init__(self, value, isNegative=False, ctx=None):
        self.value = value
        self.isNegative = isNegative
        self.ctx = ctx

    def __add__(self, val):

        if isinstance(val, _Float):
            return self.value + val.value
        
        return self.value + val
    
    def __iadd__(self, val):
        self.value += val
        return self
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"{self.value}"
    
