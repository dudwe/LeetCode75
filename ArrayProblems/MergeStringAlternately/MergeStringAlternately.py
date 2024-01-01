"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

Solution:

Use two pointers to track word1 and word2
Flip between both until we reach the end of one
THen append the remainder of the other to our output
Return the output

O(n+m) Runtime O(1) Memory as we are doing a loop over both lists once and storing our solution in a new list
(no additional space)


Alternative:
We can use one pointer to achieve the same solution
ptr = 0
add word1[ptr]
add word2[ptr]
ptr+=1
continue until we reach end of one list
append the other if needed

O(n+m) Runtime
O(1) memory
"""

import typing


class Solution:
    def mergeAlternately_One_Pointer(self, word1: str, word2: str) -> str:
        ptr = 0
        output = ""
        while ptr < len(word1) and ptr < len(word2):
            output += word1[ptr]
            output += word2[ptr]
            ptr += 1

        if ptr < len(word1):
            output += word1[ptr:]
        if ptr < len(word2):
            output += word2[ptr:]

        return output

    def mergeAlternately_Two_Pointer(self, word1: str, word2: str) -> str:
        ptr_a = 0
        ptr_b = 0
        flip = True
        output = ""
        while ptr_a < len(word1) and ptr_b < len(word2):
            if flip:
                output += word1[ptr_a]
                ptr_a += 1
            else:
                output += word2[ptr_b]
                ptr_b += 1
            flip = not flip

        if ptr_a < len(word1):
            output += word1[ptr_a:]
        if ptr_b < len(word2):
            output += word2[ptr_b:]

        return output

    def mergeAlternately(self, word1: str, word2: str) -> str:
        return self.mergeAlternately_One_Pointer(word1, word2)
