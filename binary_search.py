#!/usr/bin/env python
# encoding: utf-8



def binary_search(l, num):
    if len(l) == 0:
        return False
    if len(l) == 1:
        return l[0] == num
    mid = len(l)/2
    if (l[mid] == num):
        return True
    if (l[mid] < num):
        return binary_search(l[mid+1:], num)
    if (l[mid] > num):
        return binary_search(l[:mid], num)


def binary_search1(l, num):
    left = 0
    right = len(l)-1
    while(left<=right):
        mid = (left+right)/2
        if(l[mid] == num):
            return True
        elif(l[mid] < num):
            left = mid+1
        else:
            right = mid-1
    return False



test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search1(test_list, 3))
print(binary_search1(test_list, 13))
