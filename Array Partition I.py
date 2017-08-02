#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 下午4:52
# @Author  : Huang HUi
# @Site    : 
# @File    : Array Partition I.py
# @Software: PyCharm

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sums=0
        i=0
        while i <len(nums):
            sums+=nums[i]
            i+=2

        return sums
