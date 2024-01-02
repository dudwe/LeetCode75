"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Solution:
Track each vowel we encounter
Add this to a temporary string at the start
Iterate over s again with a pointer, replace each encountered vowel with the corresponding vowel in the temp string

O(n) Runtime - We loop over word twice
O(n) Memory  - Worst case we store the string in aux set


Optimize:
We loop over the list twice, we also use additional storage
We can optimize to a one loop solution by using a while loop

Scan left and right until l > r
move left and right until both at a vowel
Swap
Continue going

O(n) time and memory, but we are using one loop and one list
"""


class Solution:
    def reverseVowelsBrute(self, s: str) -> str:
        temp_string = ""
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for x in s:
            if x in vowels:
                temp_string = x + temp_string
        ptr = 0
        s = list(s)
        for idx, letter in enumerate(s):
            if letter in vowels:
                s[idx] = temp_string[ptr]
                ptr += 1

        return ''.join(s)

    def reverseVowelsOptimal(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        l = 0
        r = len(s) - 1

        s = list(s)
        while l < r:
            while l < len(s) and s[l] not in vowels:
                l += 1
            while r >= 0 and s[r] not in vowels:
                r -= 1
            if r <= l:
                break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)

    def reverseVowels(self, s: str) -> str:
        return self.reverseVowelsOptimal(s)
