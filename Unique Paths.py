#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/30 下午2:36
# @Author  : Huang HUi
# @Site    : 
# @File    : Unique Paths.py
# @Software: PyCharm

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0] * n for x in range(m)]
        dp[0][0] = 1
        for x in range(m):
            for y in range(n):
                if x + 1 < m:
                    dp[x + 1][y] += dp[x][y]
                if y + 1 < n:
                    dp[x][y + 1] += dp[x][y]
        return dp[m - 1][n - 1]

        # if m<n:
        #     m,n=n,m
        #
        # res=[0]*n
        # res[0]=1
        # for i in range(m):
        #     for j in range(n-1):
        #         res[j+1]+=res[j]
        # return res[n-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(3,7))

