#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/23 下午3:22
# @Author  : Huang HUi
# @Site    : 
# @File    : Binary Tree Inorder Traversal.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        node = root
        mystack = []
        result = []
        while mystack or node:
            while node:
                mystack.append(node)
                node = node.left

            node = mystack.pop()
            result.append(node.val)
            node = node.right

        return result

