from BPlusTree import BPlusTree


class ProjectDB(object):
    def __init__(self):
        self.file = None

    def open(self, file_name, mode):
        self.file = open(file_name, mode)

    def close(self):
        self.file.close()