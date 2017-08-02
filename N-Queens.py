#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 下午3:04
# @Author  : Huang HUi
# @Site    : 
# @File    : N-Queens.py
# @Software: PyCharm
import copy
class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def check(row, col):  # check if the kth queen can be put in column j!
            for i in range(row):
                if board[i] == col or abs(row - i) == abs(board[i] - col):
                    return False
            return True

        def dfs(row, valuelist):
            if row == n:
                res.append(valuelist)
                return

            for col in range(n):
                if check(row, col):
                    board[row] = col
                    s = '.' * n
                    dfs(row + 1, valuelist + [s[:col] + 'Q' + s[col + 1:]])

        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return res




if __name__ == '__main__':
    print(Solution().solveNQueens(4))


