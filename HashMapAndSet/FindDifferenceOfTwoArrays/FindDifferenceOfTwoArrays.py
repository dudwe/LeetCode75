"""
2215. Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

Create two sets
Return the set difference forleft and right
O(n) time complexity
O(n) memory
"""
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        left = set(nums1)
        right = set(nums2)

        return [list(left - right), list(right-left)]

