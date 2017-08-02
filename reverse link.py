#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 下午2:51
# @Author  : Huang HUi
# @Site    : 
# @File    : reverse link.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def reverse(self,head):
        node=ListNode(0)
        while head:
            next=head.next
            head.next=node.next
            node.next=head
            head=next

        return node.next










if __name__ == '__main__':
    a = ListNode(1)
    b = a.next = ListNode(2)
    c = b.next = ListNode(3)
    d = c.next = ListNode(4)
    e = d.next = ListNode(5)
    print(Solution().reverse(a))