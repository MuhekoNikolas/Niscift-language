

class _ClassesReprMeta(type):
    def __repr__(cls):
        return f'{cls.__repr__(cls)}'