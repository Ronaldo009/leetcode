#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/9 上午11:32
# @Author  : Huang HUi
# @Site    : 
# @File    : TencentTest.py
# @Software: PyCharm

# 给定一数组a[N]，我们希望构造数组b [N]，其中b[j]=a[0]*a[1]…a[N-1] / a[j]，在构造过程中，不允许使用除法：

# 要求O（1）空间复杂度和O（n）的时间复杂度；

# 除遍历计数器与a[N] b[N]外，不可使用新的变量（包括栈临时变量、堆空间和全局静态变量等）；


class Solution():
    def makeArray(self,a):
        """

        :param a: List[int]
        :return: List[int]
        """

        length=len(a)
        res=[ 1 for i in range(length)]
        for i in range(1,length):
            res[i]=res[i-1]*a[i-1]
        print(res)
        tem=1
        for i in range(length-2,-1,-1):
            tem=tem*a[i+1]
            res[i]*=tem
        for i in range(length-1,0,-1):
            res[i]*=res[0]
            res[0]*=a[i]
        print(res)

if __name__ == '__main__':
    a=[1,3,5,7,9]
    Solution().makeArray(a)