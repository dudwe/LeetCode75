"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
Solution:

Naive:
    We compute each for each index  O(n^2)

Optimize:
    [1,2,3,4]
    left [1,2,6,24]
    right[4,12,24,24]

    [1,2,3,4]

    idx  left  right
    0     -      24
    1     1      12
    2     2      4
    3     6      -

    Therefore:
    For idx 1, n-1 product except setlf pef_i = left[i-1] * right [-(i+1)]

    O(n) Memory
    O(n) Runtime

To Optimize Further we can do this in place
We can use an auxilary variable to total mult and a single output array

So compute the left:
[1,2,3,4]
[1,1,2,6]

Set R = 1
Then scan backwards and update:
ans[i] = ans[i] * R
R *= nums[i]

[]



"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        #[1,1,2,6]
        print(ans)
        r = 1
        for i in  range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * r
            r *=nums[i]

        '''
        [1,1,2,6] r = 1
        [1,1,2,6] r = 4
        [1,1,8,6] r = 12
        [1,12,8,6]r = 24
        [24,12,8,6]
        '''
        return ans
