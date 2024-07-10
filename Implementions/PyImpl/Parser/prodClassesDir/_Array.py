
from collections.abc import MutableSequence

class _Array(MutableSequence):

    def __init__(self, contents=None, ctx=None):
        self.contents = []
        self.ctx = ctx
        
        if contents is not None:
            if isinstance(contents, list):
                self.contents[:] = contents

            elif isinstance(contents, _Array):
                self.contents[:] = contents.contents[:]

            else:
                self.contents = list(contents)

    def ____getParsedContents_____(self):
        _thisParsedContents = []

        for x in self.contents:
            if type(x).__name__ in ["_Array", "_Tuple"]:
                _thisParsedContents.append(x.____getParsedContents_____())
            else:
                _thisParsedContents.append(x.value)

        return _thisParsedContents

    def __repr__(self):
        return """{}""".format(repr(self.contents))

    def __lt__(self, other):
        return self.contents < self.__cast(other)

    def __le__(self, other):
        return self.contents <= self.__cast(other)

    def __eq__(self, other):
        return self.contents == self.__cast(other)

    def __gt__(self, other):
        return self.contents > self.__cast(other)

    def __ge__(self, other):
        return self.contents >= self.__cast(other)

    def __cast(self, other):
        return other.contents if isinstance(other, _Array) else other

    def __contains__(self, value):
        return value in self.contents

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return self.__class__(self.contents[idx])
        else:
            return self.contents[idx]

    def __setitem__(self, idx, value):
        self.contents[idx] = value

    def __delitem__(self, idx):
        del self.contents[idx]

    def __add__(self, other):
        if isinstance(other, _Array):
            return self.__class__(self.contents + other.contents)

        elif isinstance(other, type(self.contents)):
            return self.__class__(self.contents + other)

        return self.__class__(self.contents + list(other))

    def __radd__(self, other):
        if isinstance(other, _Array):
            return self.__class__(other.contents + self.contents)

        elif isinstance(other, type(self.contents)):
            return self.__class__(other + self.contents)

        return self.__class__(list(other) + self.contents)

    def __iadd__(self, other):
        if isinstance(other, _Array):
            self.contents += other.contents

        elif isinstance(other, type(self.contents)):
            self.contents += other

        else:
            self.contents += list(other)

        return self

    def __mul__(self, nn):
        return self.__class__(self.contents * nn)

    __rmul__ = __mul__

    def __imul__(self, nn):
        self.contents *= nn
        return self

    def __copy__(self):
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)

        # Create a copy and avoid triggering descriptors
        inst.__dict__["contents"] = self.__dict__["contents"][:]

        return inst

    def append(self, value):
        self.contents.append(value)

    def insert(self, idx, value):
        self.contents.insert(idx, value)

    def pop(self, idx=-1):
        return self.contents.pop(idx)

    def remove(self, value):
        self.contents.remove(value)

    def clear(self):
        self.contents.clear()

    def copy(self):
        return self.__class__(self)

    def count(self, value):
        return self.contents.count(value)

    def index(self, idx, *args):
        return self.contents.index(idx, *args)

    def reverse(self):
        self.contents.reverse()

    def sort(self, /, *args, **kwds):
        self.contents.sort(*args, **kwds)

    def extend(self, other):
        if isinstance(other, _Array):
            self.contents.extend(other.contents)

        else:
            self.contents.extend(other)