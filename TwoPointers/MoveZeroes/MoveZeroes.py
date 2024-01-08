"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

Move Zeroes to the end of alist

[0,1,0,3,12]
[1,3,12,0,0]

Naive:
O(n^2)
We loop over and move all to the end 1 at a time

Optimal
slow sits at the first zero
fast move until we see a non zero
    on non zero, flip slow and fast values
    move slow until at next zero
    fast+=1
continue until we reach the end#


O(n) Solution we scan two pointers form left to right
O(1) Memory in place

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        while slow < len(nums) and nums[slow] != 0:
            slow += 1

        fast = slow + 1

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                while slow < len(nums) and nums[slow] != 0:
                    slow+=1
            fast+=1
