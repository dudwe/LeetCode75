"""


1004. Max Consecutive Ones III#
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
Longest sub array containing only 1s after deleting one element
Solution:
We need to keep a window l,r
We move r when:
    nums[r] == 1
    if nums[r] == 0 and not contains_one
We move l while contains_one  and nums[r] == 0:
    if nums[l] == 0:
        contains_one = False
    l+=1
Our array always will delete one element, so we just compute max(max_val,r-l-1)
In each step, compute the window length against the max length

O(n) runtime
O(1) memory


"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        contains_one = False
        max_window = 0
        while r < len(nums):
            if nums[r] == 0 and not contains_one:
                contains_one = True
                r+=1
            elif nums[r] == 1:
                r+=1
            else:
                while nums[l] != 0:
                    l+=1
                contains_one = False
                l+=1


            max_window = max(max_window,r-l-1)

        return max_window

