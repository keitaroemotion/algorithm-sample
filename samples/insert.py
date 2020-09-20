#!/usr/bin/env python3

set = [5, 2, 4, 6, 1, 3]

for j in range(1, len(set)):
    key = set[j]
    i   = j - 1
    while (i >= 0 and set[i] > key):
        set[i+1] = set[i]
        i        = i - 1
    set[i+1] = key

print(set)
