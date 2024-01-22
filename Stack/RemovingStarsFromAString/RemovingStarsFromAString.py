"""
2390. Removing Stars From a String
https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

leet**cod*e -> lecoe we pop et and d

Hence this is a stack based problem


O(n) memory
O(n) time complexity
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)