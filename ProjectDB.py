from BPlusTree import BPlusTree


class ProjectDB(object):
    def __init__(self, file):
        self.file = file
        self.bptree = BPlusTree(10)

    def start(self):
        pass

    def close(self):
        pass