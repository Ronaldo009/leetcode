#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/30 下午2:16
# @Author  : Huang HUi
# @Site    : 
# @File    : Climbing Stairs.py
# @Software: PyCharm

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fib(n)

    def fib(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.fib(n-1)+self.fib(n-2)

if __name__ == '__main__':
    print(Solution().climbStairs(15))
