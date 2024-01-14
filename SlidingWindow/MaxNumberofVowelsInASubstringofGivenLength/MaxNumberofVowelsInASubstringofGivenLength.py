"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

Find max number of vowel letters in a substring of s with length k

Naive:
Iterate over the list from 0->len(s) -k
    Compute number of vowels in section
    compare to max_vowels

O(n^2) Runtime

Sliding Window:
Compute initial window
total_vowels = number of vowels from 0->k
max_vowels = total_vowels

for i in range k+1->len(n):
    decrement_total_vowels if n[i - k+1] is in vowels
    update total_vowels if n[i] in vowels
    update max_vowels if total_vowels > max_vowels

O(n) runtime
O(1) memory
"""
from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        total_vowels = 0
        for letter in s[:k]:
            if letter in vowels:
                total_vowels+=1
        max_vowels = total_vowels

        for i in range(k,len(s)):
            if s[i] in vowels:
                total_vowels +=1
            if s[i-k] in vowels:
                total_vowels-=1
            max_vowels = max(max_vowels,total_vowels)


        return max_vowels



