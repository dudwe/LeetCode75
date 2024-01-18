"""
2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

Ordering matters for this

O(n^3) runtime where k = nxn
O(n) memory

We can imporve with a map
let the key by a tple in this case
"""

from typing import List

from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = Counter(tuple(row) for row in grid)
        pairs = 0
        for c in range(len(grid)):
            col = [grid[i][c] for i in range(len(grid))]
            pairs += row_count[tuple(col)]

        return pairs
