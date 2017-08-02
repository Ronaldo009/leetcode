#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/9 下午2:36
# @Author  : Huang HUi
# @Site    : 
# @File    : Trapping Rain Water.py
# @Software: PyCharm

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count=0
        n=max(height)
        print(height)




        for i in range(n-1):
            for k in height:
                print(k)
                while k == 0:

                    height.remove(k)
                break
            for v in range(len(height) - 1, -1, -1):
                while height[v] == 0:
                    height.remove(height[v])
                break

            for x in height:
                print(len(height))
                print(x)
                if x==0:
                    count+=1
                    height.remove(x)

            for j in range(len(height)):
                if height[j]!=0:
                    height[j]-=1
            print(height)
        print(count)

if __name__ == '__main__':
    aa=[0,0,1,0,2,1,0,1,3,2,1,2,1]
    Solution().trap(aa)




