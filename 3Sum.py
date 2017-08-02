#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 下午5:23
# @Author  : Huang HUi
# @Site    : 
# @File    : 3Sum.py
# @Software: PyCharm

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        tmp=[]
        i=0
        nums.sort()
        while i<len(nums)-2:
            k=i+1
            j=len(nums)-1
            while k<j:
                stack=[nums[i],nums[k],nums[j]]
                if sum(stack)==0:
                    if stack not in tmp:
                        tmp.append(stack)
                    k+=1
                    j-=1

                elif sum(stack)>0:
                    j-=1
                else:
                    k+=1
            i+=1

        return tmp


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))









