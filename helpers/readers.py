#!/usr/bin/env python3

d1 = '../d1/p1.txt'
d2 = '../d2/p1.txt'

class AdventReader:
    def __init__(self, file) -> None:
        self.file = file
    
    def read_lines(self, dtype=None):
        content = list()
        with open(self.file, 'r') as fin:
            for line in fin.readlines():
                c = line.strip()
                if len(c) > 0 and dtype is not None:
                    c = dtype(c)
                content.append(c)
        return content
    
    @staticmethod
    def read_all(file, dtype=None):
        content = list()
        with open(file, 'r') as fin:
            for line in fin.readlines():
                c = line.strip()
                if len(c) > 0 and dtype is not None:
                    c = dtype(c)
                content.append(c)
        return content


if __name__ == '__main__':
    ar = AdventReader(d1)
    ar.read_lines(dtype=int)