"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

We use a stack,
pop when current and stack.peek is <= curr
elif continue if stack.peek > curr  and curr is opposite to stack.peek
else we append

stack = []
for a in asteroids:
    explode = False
    while stack:
        if in the same direciton or <-  -> :
            stack.append(a)
            break
        if collision direction and explosion
            explostion = True
            break
        else:
            stack.pop()

    if not explode:
        stack.append(a)



O(n) memory
O(n) time
"""

from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            explode = False

            while stack:
                if (stack[-1] >= 0 and a >= 0) or (stack[-1] < 0 and a < 0) or (stack[-1] <= 0 <= a):
                    break
                if abs(stack[-1])>=abs(a):
                    if abs(stack[-1]) == abs(a):  #dual explosion
                        stack.pop()
                    explode = True
                    break
                else:
                    stack.pop()

            if not explode:
                stack.append(a)

        return stack
