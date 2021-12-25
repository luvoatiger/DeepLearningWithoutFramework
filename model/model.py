class Model(object):
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset
        self.is_training = False
        if not hasattr(self, 'rand_std'):
            self.rand_std = 0.039

    def __str__(self):
        return f"{self.name}/{self.dataset}"

    def exec_all(self, epoch_count=10, batch_size=10, learning_rate=0.001, report=0, show_cnt=3):
        self.train(epoch_count, batch_size, learning_rate, report)
        self.test()
        if show_cnt > 0:
            self.visualize(show_cnt)