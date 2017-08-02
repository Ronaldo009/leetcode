#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/16 下午5:22
# @Author  : Huang HUi
# @Site    : 
# @File    : Count of Range Sum.py
# @Software: PyCharm

class FenwickTree(object):
    def __init__(self,n):
        self.n=n
        self.sums=[0]*(n+1)

    def lowbit(self,x):
        return x & -x

    def add(self,x,val):
        while x<=self.n:
            self.sums[x]+=val
            x+=self.lowbit(x)
    def sum(self,x):
        res=0
        while x>0:
            res+=self.sums[x]
            x-=self.lowbit(x)
        return res



class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        sums=nums[:]
        for x in range(1,len((sums))):
            sums[x]+=sums[x-1]
        osums=sorted(set(sums))
        ft=FenwickTree(len(osums))






