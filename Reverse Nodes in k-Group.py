#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 下午12:13
# @Author  : Huang HUi
# @Site    : 
# @File    : Reverse Nodes in k-Group.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self,head):
        node=ListNode(0)
        while head:
            next=head.next
            head.next=node.next
            node.next=head
            head=next

        return node.next

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1 or k==0 or not head:
            return head
        newHead=ListNode(0)
        newHead.next=head
        start=newHead
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None:
                    return newHead.next









if __name__ == '__main__':
    a = ListNode(1)
    b = a.next = ListNode(2)
    c = b.next = ListNode(3)
    d = c.next = ListNode(4)
    e = d.next = ListNode(5)
    print(Solution().reverseKGroup(a,2))
