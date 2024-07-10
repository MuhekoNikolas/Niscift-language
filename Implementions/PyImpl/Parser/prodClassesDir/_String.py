

class _String(str):
    def __new__(self, value, ctx):
        self.ctx = ctx
        self.value = value
        return super(_String, self).__new__(self, value)