"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

Use Two pointers
s_ptr
t_ptr

aebec
abc

aebbbbabc

abc

We just move until we get a c


move s when s=t
Else keep moving t

If s is at end true else False

O(1) Memory  O(n) time complexity
"""
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_ptr = 0
        t_ptr = 0

        while s_ptr<len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr+=1
                t_ptr+=1
            else:
                t_ptr+=1
        return s_ptr == len(s)
