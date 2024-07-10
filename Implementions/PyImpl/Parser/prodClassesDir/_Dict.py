
from ._NoneTypes import _Undefined

class _Dict(dict):
    def __init__(self, contents, ctx):
        self.contents = contents
        self.ctx = ctx

    def __setitem__(self, key, item):
        if type(key).__name__ != "str":
            raise TypeError("Dict Indexes must be of type: String.")
        
        self.contents[key] = item

    def __getitem__(self, key):
        if type(key).__name__ != "str":
            return _Undefined(self.ctx)
        
        thisContentKeys = self.contents.keys()

        if key in thisContentKeys:
            return self.contents[key]
        else:
            return _Undefined(self.ctx)

    def __repr__(self):
        return repr(self.contents)
    
    @property
    def __dict__(self):
        return self.contents

    def __len__(self):
        return len(self.contents)

    def __delitem__(self, key):
        del self.contents[key]

    def clear(self):
        return self.contents.clear()

    def copy(self):
        return self.contents.copy()

    def has_key(self, k):
        return k in self.contents

    def update(self, *args, **kwargs):
        return self.contents.update(*args, **kwargs)

    def keys(self):
        return self.contents.keys()

    def values(self):
        return self.contents.values()

    def items(self):
        return self.contents.items()

    def pop(self, *args):
        return self.contents.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.contents, dict_)

    def __contains__(self, item):
        return item in self.contents

    def __iter__(self):
        return iter(self.contents)

    def __unicode__(self):
        return unicode(repr(self.contents))