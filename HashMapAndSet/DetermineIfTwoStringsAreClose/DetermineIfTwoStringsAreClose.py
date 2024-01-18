"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

We can make strings by doing the following:
1. Swap
2. Transform all letters from x to y so long as the letters exist in both lists

False when:
len(word1) != len(word2)
Any value in counter dict for word1 is NOT in word2 -> Means we cant do a flip

True if every occurence of word1 has an equivlaent in word2

We dont actully need to use swap

Hence:
Compute Counter for word1 and word2
Flip word2 so key=number of occurences value is number of letters we can use for this
Check each letter in counter_1 against the flipped_dict
Return true or false depending on if we have match ornot
at each match decrement flipped

O(n) Memory and Time Complexity

"""
from collections import Counter,defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False



        counter_w1 = Counter(word1)
        counter_w2 = Counter(word2)

        if counter_w1.keys() != counter_w2.keys():
            return False

        flipped_dict = defaultdict(int)
        for val in counter_w2.values():
            flipped_dict[val] +=1

        for val in counter_w1.values():
            if flipped_dict[val] == 0:
                return False
            else:
                flipped_dict[val] -= 1

        return True