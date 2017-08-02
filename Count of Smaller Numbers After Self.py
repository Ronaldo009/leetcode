#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/27 下午3:41
# @Author  : Huang HUi
# @Site    : 
# @File    : Count of Smaller Numbers After Self.py
# @Software: PyCharm

class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sorted(enum[:half]), sorted(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i + j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i + j] = right[j]
                        j += 1
            return enum

        smaller = [0] * len(nums)
        sorted(list(enumerate(nums)))
        return smaller





if __name__ == '__main__':
    a=[5,2,6,1]

    print(Solution().countSmaller(a))
