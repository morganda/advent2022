#!/usr/bin/env python3

from string import ascii_letters

from readers import AdventReader

priorities = dict()

def set_priorities():
    p = 1
    for i in ascii_letters:
        priorities[i] = p
        p += 1

def getCommonChar(lists):
    lookups = list()
    for s in range(len(lists) - 1):
        lookup = dict()
        for c in lists[s]:
            lookup[c] = 1
        lookups.append(lookup)
    seek = lists[-1]
    for s in seek:
        match = True
        for lookup in lookups:
            if s not in lookup:
                match = False
                break
        if match:
            return s
    return None

def getPriority(rucksack):
    partition = int(len(rucksack) / 2)
    c1 = rucksack[0:partition]
    c2 = rucksack[partition:]
    i = getCommonChar((c1, c2))
    return priorities[i]

def getBadgePriority(rucksacks):
    r = getCommonChar(rucksacks)
    return priorities[r]

def main():
    lines = AdventReader().read_all("/Users/morgana/src/advent2022/d3/p1.txt")
    sum = 0
    for line in lines:
        sum += getPriority(line)
    print(f"p1: {sum}")

    i = 0
    j = 2
    sum = 0
    while j < len(lines):
        sum += getBadgePriority(lines[i:j+1])
        i += 3
        j += 3
    print(f"p2: {sum}")


if __name__ == '__main__':
    set_priorities()
    main()