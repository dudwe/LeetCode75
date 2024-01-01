"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

Solution Brute Force
Find the shortest string

Find all factors for the length of the shortest string

For each factor in decreasing order:
    Check if the factor string divides into str2
    If Yes, check if this divides into the str1 as well
    If Yes return as the is is the largest gcd

return ""

Runtime: O(min(m,n) * (m+n))
We check all factors of the min length string O(min(m,n))
For each valid factor we then check if it is a valid divisor O(m+n)
Hence we get O(min(m,n) * (m+n))
Space: O(n) We compute temporary strings to check as we go


Optimized GCD Solution:

Verify that a divisible string exists:
We can check this by checking if
str1+str2 = str2+str1 , if so then we have a some sort of repeated pattern and thus a GCD exists
If not, no GCD exists

e.g.

str1 = ABCABCABC,  str2 = ABCABC

str1+str2 = ABCABCABCABCABC
str2+str1 = ABCABCABCABCABC

Hence str1+str2 = str2+str1, so we know a GCD of some kind exists here

In contrast:
LEET CODE

LEETCODE != CODELEET

So no GCD is possible to find here

If we find a that the appended patterns match, we just find the gcd,
Then take this on the appended string
And return

Proof by contradiction means that no smaller solution is possible here


Runtime: O(m+n) We just check gcd and return the first one we find
Space: O(m+n) We create the appended string when we check
"""


class Solution:

    def check_valid_factor(self, factor_string: str, str1: str, str2: str) -> bool:
        temp = [factor_string] * int(len(str2) / len(factor_string))
        temp_string = ''.join(temp)
        if str2 != temp_string:
            return False

        temp = [factor_string] * int(len(str1) / len(factor_string))
        temp_string = ''.join(temp)
        if str1 != temp_string:
            return False

        return True

    def gcdOfStringsBrute(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        N = len(str2)
        M = len(str1)

        for x in range(N, 0, -1):
            if N % x == 0 and M % x == 0:
                factor_string = str2[:x]
                if self.check_valid_factor(factor_string, str1, str2):
                    return factor_string

        return ""
    def gcdOfStringsOptimal(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        N = len(str2)
        M = len(str1)

        if str1+str2 != str2+str1:
            return ""

        #Find the gcd
        for x in range(N, 0, -1):
            if N % x == 0 and M % x == 0:
                return str2[:x]
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return self.gcdOfStringsOptimal(str1, str2)
