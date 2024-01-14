"""


1004. Max Consecutive Ones III#
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

Solution:
We need to keep a window l,r
We move r when:
    nums[r] == 1
    if nums[r] == 0 and zero_count < k
We move l while zero_count == k and nums[r] == 0:
    if nums[l] == 0:
        zero_count -=1
    l+=1
In each step, compute the window length against the max length

O(n) runtime
O(1) memory


"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zero_count = 0
        max_window = 0
        while r < len(nums):

            if nums[r] == 0 and zero_count < k:
                zero_count +=1
                r+=1
            elif nums[r] == 1:
                r+=1
            else:
                while zero_count  >= k:
                    if nums[l] == 0:
                        zero_count -=1
                    l+=1
            max_window = max(max_window,r-l)

        return max_window

