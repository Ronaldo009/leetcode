#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/16 下午4:27
# @Author  : Huang HUi
# @Site    : 
# @File    : Same Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val !=q.val :
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

if __name__ == '__main__':



    Solution().isSameTree()
