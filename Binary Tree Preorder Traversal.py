#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/16 下午4:46
# @Author  : Huang HUi
# @Site    : 
# @File    : Binary Tree Preorder Traversal.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        mystack=[]
        node=root
        result=[]

        while node or mystack:
            while node:
                mystack.append(node)
                result.append(node.val)
                node=node.left

            node=mystack.pop()
            node=node.right

        return result






