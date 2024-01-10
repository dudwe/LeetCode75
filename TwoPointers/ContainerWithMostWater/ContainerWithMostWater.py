"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

Brute Force:
Need to find the max area, so we compute every possible combination from left and right

area = 0
for x in range(0,n)
    for y in range(x+1,n)
        area = max(area,(y-x) * min(height[y],height[x]))

O(n^2) Solution


Optimize:
We can skip some of the operations
We can make local decision to compute the local height

So some sort of two pointer solution

left = 0
right = 0

move left if height[left] < height[right]

otherwise move right

Continue until left >= right

O(1) Memory
O(n) time complexity
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right-left) * (min(height[left],height[right])))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return area

