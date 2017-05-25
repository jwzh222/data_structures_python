#!/usr/bin/env python
# encoding: utf-8



L = [4,3,5,6,2,5,1,9]

def f1(L, l, r):
    if (l>=r):
        return 0
    star = L[l]
    swap = l+1
    i = swap
    while i <= r:
        if (L[i]<=star):
            L[swap],L[i] = L[i],L[swap]
            swap += 1
        elif (L[i]>star):
            L[swap],L[i] = L[i],L[swap]
        i += 1

    L[l], L[swap-1] = L[swap-1], L[l]
    print L

    f1(L,l,swap-2)
    f1(L,swap,r)


def f (L):
    l = 0
    r = len(L)-1
    if r <= 0:
        return 0
    f1(L,l,r)

print L
f(L)
print L

