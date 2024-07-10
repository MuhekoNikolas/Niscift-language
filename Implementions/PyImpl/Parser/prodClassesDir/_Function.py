

from ._Callable import _Callable

class _Function(_Callable):
    def __init__(self, ctx):
        super().__init__()
        pass

    def ____call____(self, arguments=[]):
        print(arguments, "joijoijoj")
        return 2