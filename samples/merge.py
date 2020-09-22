#!/usr/bin/env python3

#
# merge sort
#
A = [1, 3, 5, 8, 13, 2, 4, 6, 8, 10]
#
#    p             q               r
#

p = 0
q = 5
r = 10 
n1 = q - p + 1
n2 = r - q

L = []
R = []

for i in range(1, n1):
    L.append(A[p + i - 1])

for j in range(0, n2):
    R.append(A[q + j])

i = 0 
j = 0 

_A = []

FAKE_AMOUNT=1000

for k in range(p, r):
    if(len(L) <= i and len(R) <= j):
        break
    elif(len(L) <= i):
        _A.append(R[j])
        continue
    elif(len(R) <= j):
        _A.append(L[i])
        continue

    l = L[i]
    r = R[j]
    if(l <= r): 
        _A.append(l) # assign the smaller stack head and increment the pointer of the stack
        i = i + 1
    else:
        _A.append(r)
        j = j + 1

print(_A)
