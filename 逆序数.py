#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 上午11:50
# @Author  : Huang HUi
# @Site    : 
# @File    : 逆序数.py
# @Software: PyCharm


def merge_sort(data):
    if (len(data) <= 1):
        return data
    index = len(data) // 2
    lst1 = data[:index]
    lst2 = data[index:]
    left = merge_sort(lst1)
    right = merge_sort(lst2)
    return merge(left, right)


def merge(lst1, lst2):
    """to merge two list together"""
    list = []
    while (len(lst1) > 0 and len(lst2) > 0):
        data1 = lst1[0]
        data2 = lst2[0]
        if (data1 <= data2):
            list.append(lst1.pop(0))
        else:
            global num
            num = num + 1
            list.append(lst2.pop(0))
    if (len(lst1) > 0):
        list.extend(lst1)
    else:
        list.extend(lst2)
    return list


num = 0
arr = [2, 1, 4, 3]
print(merge_sort(arr))
print(num)