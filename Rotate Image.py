#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/26 下午2:16
# @Author  : Huang HUi
# @Site    : 
# @File    : Rotate Image.py
# @Software: PyCharm
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        newMatrix=[]
        for i in range(n):
            for j in range(m):
                newMatrix=matrix[i][j]
                matrix[i][j]=matrix[m-1-j][i]
                newMatrix=matrix[i][m-1-j]
                matrix[i][m-1-j]=newMatrix


        print(matrix)


if __name__ == '__main__':
    a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    Solution().rotate(a)