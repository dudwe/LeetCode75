from typing import List
"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

Pivot is where all to the left and all to the right of a number sum to the same value N

[1,7,3,6,5,6]

[1,8,11,17,22,28]

At a given point we need to find the sum on the left and right

sum_right= 1+7+3+6+5+6 = 28
sum_left = 0

idx nums[idx] s_l s_r
0      1       0   27
1      7       1   20
2      3       8   17
3      6       11  11  -> We have answer
4
5

Hence we maintain the sum_left and sum_right
we update that as we loop over and return idx if we have a solution
Else return -1 
O(n) Time complexity
O(1) Space

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_right = sum(nums)
        sum_left = 0

        prev = 0
        for idx, val in enumerate(nums):
            sum_right -= val
            sum_left += prev
            prev = val
            if sum_left == sum_right:
                return idx

        return -1