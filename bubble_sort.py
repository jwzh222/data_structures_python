#!/usr/bin/env python
# encoding: utf-8

def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]


if __name__ == '__main__':
    a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    bubble_sort(a_list)
    print a_list
