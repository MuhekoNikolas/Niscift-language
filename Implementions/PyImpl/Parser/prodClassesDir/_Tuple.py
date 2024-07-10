

class _Tuple:
    def __init__(self, contents=[], ctx=None):
        self.contents = contents
        self.ctx = ctx

    def __repr__(self):
        return f"({f'{self.contents}'[1:-1]})"

    def __len__(self):
        return len(self.contents)
    
    def ____getParsedContents_____(self):
        _thisParsedContents = []

        for x in self.contents:
            if type(x).__name__ in ["_Array", "_Tuple"]:
                _thisParsedContents.append(x.____getParsedContents_____())
            else:
                _thisParsedContents.append(x.value)

        return _thisParsedContents
    
    def __getitem__(self, index):
        return self.contents[index]
    
    def __setitem__(self, index, value):
        raise("Cannot mutate tuple object.")