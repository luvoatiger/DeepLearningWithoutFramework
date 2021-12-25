class Dataset(object):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __str__(self):
        return f"{self.name}({self.mode}, {self.tr_xs}+{self.te_xs}+{len(self.va_xs)})"

    @property
    def train_count(self):
        return len(self.tr_xs)