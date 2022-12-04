#!/usr/bin/env python3

from readers import AdventReader

def parse_pair(pair_in):
    raw_assignments = pair_in.split(",")
    assignments = list()
    for ra in raw_assignments:
        d, r = ra.split("-")
        assignments.append((int(d), int(r)))
    return assignments

def contained(p1, p2):
    if p1[0] >= p2[0] and p1[1] <= p2[1] or \
            p2[0] >= p1[0] and p2[1] <= p1[1]:
        return True
    return False

def overlap(p1, p2):
    if p1[0] >= p2[0] and p1[0] <= p2[1] or \
            p1[1] >= p2[0] and p1[1] <= p2[1] or \
            p2[0] >= p1[0] and p2[0] <= p1[1] or \
            p2[1] >= p1[0] and p2[1] <= p1[1]:
        return True
    return False

def main():
    lines = AdventReader.read_all("/Users/morgana/src/advent2022/d4/p1.txt")
    contain_count = 0
    overlap_count = 0
    for line in lines:
        pair = parse_pair(line)
        if contained(*pair):
            contain_count += 1
        if overlap(*pair):
            overlap_count += 1
    print(f"p1: {contain_count}")
    print(f"p2: {overlap_count}")


if __name__ == '__main__':
    main()