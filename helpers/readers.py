#!/usr/bin/env python3

d1 = '../d1/p1.txt'
d2 = '../d2/p1.txt'

class AdventReader:
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
