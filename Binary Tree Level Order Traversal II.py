#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/8 下午8:04
# @Author  : Huang HUi
# @Site    : 
# @File    : Binary Tree Level Order Traversal II.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        self.preorder(root,0,res)
        res.reverse()
        print(res)

    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)



if __name__ == '__main__':
    aa=TreeNode(1)
    bb=aa.left=TreeNode(2)
    cc=aa.right=TreeNode(3)
    bb.left = None
    bb.right = None
    cc.left = TreeNode(4)
    cc.right = TreeNode(5)
    Solution().levelOrderBottom(aa)


