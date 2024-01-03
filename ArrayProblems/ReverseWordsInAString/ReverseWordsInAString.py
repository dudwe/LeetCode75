"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Solution:
Basic Approach:
Built a list of words
Return the list in reverse
O(n) Runtime and Space complexity

Note that in Python strings are immutable, so the additional work does not apply here

Hypothetically, in a mutable string language we would need to make use of points and look for each word.
When we find a word on the left and right, we swap them
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []

        current_word = ""
        for idx,val in enumerate(s):
            if val == " ":
                if current_word:
                    word_list.append(current_word)
                    current_word = ""
            else:
                current_word+=val
        if s[-1] != " ":
            word_list.append(current_word)

        return ' '.join(reversed(word_list))

