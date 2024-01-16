from typing import List
from collections import Counter

"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

Number of occurneces for each value is unique 
Create a Counter dict
Then check each value by creating a set

O(n) space and time complexity
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter_d = Counter(arr)
        enc = set()
        for val in counter_d.values():
            if val in enc:
                return False
            enc.add(val)

        return True
