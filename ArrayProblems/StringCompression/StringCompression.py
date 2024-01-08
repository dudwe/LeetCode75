"""
443. String Compression
https://leetcode.com/problems/string-compression/

Compress:
if 1 char, then just append the char
if greater than number followed by char
In place algo

Memory : O(1) We use existing data structure and a series of counteres

Runtime O(n) We scan over array with slow and fast pointer
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        current_count = 1
        current_char = chars[0]
        total = 0
        slow = 0
        ptr = 1
        while ptr < len(chars):
            if current_char != chars[ptr]:

                chars[slow] = current_char
                slow += 1
                total += 1
                if current_count > 1:
                    for c in list(str(current_count)):
                        chars[slow] = c
                        slow += 1
                        total += 1
                current_char = chars[ptr]
                current_count = 1
            else:
                current_count += 1
            ptr += 1

        chars[slow] = current_char
        slow += 1
        total += 1
        if current_count > 1:
            for c in list(str(current_count)):
                chars[slow] = c
                slow += 1
                total += 1

        return total


sol = Solution()
sol.compress(["a","a","a","b","b","a","a"])
