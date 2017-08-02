#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/26 下午3:17
# @Author  : Huang HUi
# @Site    : 
# @File    : Candy.py
# @Software: PyCharm

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        count=len(ratings)
        result=[0 for i in range(count)]
        re=[]
        for i in range(1,count):
            if ratings[i]<=ratings[i+1] and ratings[i]<ratings[i-1]:
                re.append(i)
                result[i]=result[i]+1






