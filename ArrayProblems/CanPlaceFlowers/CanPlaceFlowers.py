"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

Solution:
Find the maximum placements we can do
Then compare that against n

To find the maximum possilbe placements

Use a while loop,
IF we are at 0:
    find valid on left
    find valid on right

    if valid:
        update count
        update arr
        increment ptrs

Time O(n) Single scan over list
Space O(1) For aux vars


To optimize, stop if max_placements = n
"""

import typing
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_placements = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                left = i == 0 or flowerbed[i - 1] == 0
                right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if left and right:
                    flowerbed[i] = 1
                    max_placements += 1
                    if max_placements == n:
                        return True

        return max_placements >= n
