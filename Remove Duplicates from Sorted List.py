#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/23 下午3:06
# @Author  : Huang HUi
# @Site    : 
# @File    : Remove Duplicates from Sorted List.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node=head
        while node:
            while node.next and node.val==node.next.val:
                node.next=node.next.next
            node=node.next
        return node

if __name__ == '__main__':
    a=ListNode(1)
    b=a.next=ListNode(2)
    b.next=ListNode(2)
    c=b.next.next=ListNode(3)
    c.next=ListNode(3)
    print(Solution().deleteDuplicates(a))





