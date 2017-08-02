#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 下午6:06
# @Author  : Huang HUi
# @Site    : 
# @File    : Longest Common Prefix.py
# @Software: PyCharm

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        if len(strs)==1 :
            return strs
        res=[]
        min_=strs[0]
        for i in range(len(strs)):
            if min_>strs[i]:
                min_=strs[i]
        for i in range(len(min_)):
            count=0
            for j in range(len(strs)):
                if min_[i] in strs[j][i]:
                    count+=1
            if count==len(strs):
                res.append(min_[i])
            else:
                break
        return ''.join(res)







if __name__ == '__main__':
    a=["abc","abcc","asc","abcd"]
    b=["c","c"]
    print(Solution().longestCommonPrefix(b))
