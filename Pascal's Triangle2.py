#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/9 下午8:12
# @Author  : Huang HUi
# @Site    : 
# @File    : Pascal's Triangle2.py
# @Software: PyCharm

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res=[[1] for i in range(numRows)]
        for i in range(1,numRows):
            if i==1:
                res[i]=[1,1]
            else:
                for j in range(1,len(res[i-1])):
                    res[i].append(res[i-1][j]+res[i-1][j-1])
                res[i].append(1)

        return res


if __name__ == '__main__':
    Solution().generate(5)
