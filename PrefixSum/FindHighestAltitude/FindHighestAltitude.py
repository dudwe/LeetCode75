"""
1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

Solution:
iterate with a variable to store current altitude
O(n) Runtime, O(1) Memory
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        max_alt = start
        for g in gain:
            start+=g
            max_alt = max(max_alt,start)
        return max_alt