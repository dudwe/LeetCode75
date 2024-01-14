"""
643. Maximum Average Subarray Ihttps://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

Need to find the max average given a window:

Naive:
We loop over the entire array from 0 -> len(nums) - k
Compute average for i -> i+k each time

O(n^2)

Optimal: Sliding Window
Initialize by compute 0->k
for i in range 0-> len(nums-k)
    total = total - nums[i] + nums[i+k]
    max_average = max(total/k, max_average)

retunr max_average

O(n) runtime as we save having to compute each inner K for each iteration
O(1) memory

"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        max_average = total/k
        for i in range(1,len(nums) - k+1):
            total = total - nums[i-1] + nums[i-1+k]
            max_average = max(max_average, total / k)

        return max_average