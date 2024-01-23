class ROW:
    def __init__(self, t):
        self.cells = t

    @classmethod
    def new(cls, t):
        return cls(t)
