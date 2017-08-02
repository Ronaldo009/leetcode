#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 下午6:31
# @Author  : Huang HUi
# @Site    : 
# @File    : Rotate List.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None or k==0:
            return head

        count=1
        node = head
        while node.next!=None:
            count+=1
            node=node.next
        if k%count==0:
            return head

        k=k%count
        fast=head
        slow=head
        i=0
        while i<k:
            fast=fast.next
            i+=1
        while fast.next!=None:
            slow=slow.next
            fast=fast.next

        res=slow.next
        fast.next=head
        slow.next=None

        return res.val




if __name__ == '__main__':
    a=ListNode(1)
    b=a.next=ListNode(2)
    c=b.next=ListNode(3)
    d=c.next=ListNode(4)
    e=d.next=ListNode(5)

    print(Solution().rotateRight(a,7))



