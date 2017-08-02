#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 下午4:59
# @Author  : Huang HUi
# @Site    : 
# @File    : Min Stack.py
# @Software: PyCharm

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q=[]
        self.min=[]
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        if not self.min or x<self.min[-1]:

            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()
        if self.q[-1]==self.min[-1]:
            self.min.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]