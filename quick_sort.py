#!/usr/bin/env python
# encoding: utf-8


def quick_sort_helper(l,left, right):
    if((right-left)>0):
        key = l[left]
        flag = left
        for i in range(left+1,right+1):
            if(l[i] < key):
                l[i], l[flag] = l[flag], l[i]
                flag +=1
        if (flag == left):
            flag +=1
        print l
        quick_sort_helper(l, left, flag-1)
        quick_sort_helper(l, flag, right)

def quick_sort(l):
    quick_sort_helper(l,0,len(l)-1)


b_list = [54, 26, 93, 17, 77]
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)
