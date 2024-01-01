"""
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

Solution:
Find the maximum
Then compare current val + extraCandies against the max
Return the boolean list

Time: O(n) compute the max and then iterate again
Space: O(1) ignoring returned object, only extra space stores the max
"""
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)

        output = []
        for val in candies:
            output.append(val + extraCandies >= max_candy)
        return output
