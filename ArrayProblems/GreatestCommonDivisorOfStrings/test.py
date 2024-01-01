import unittest
from ArrayProblems.GreatestCommonDivisorOfStrings.GreatestCommonDivisorOfStrings import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual("ABC", sol.gcdOfStrings("ABCABC", "ABC"))

    def test_two(self):
        sol = Solution()
        self.assertEqual("AB", sol.gcdOfStrings("ABABAB", "ABAB"))

    def test_three(self):
        sol = Solution()
        self.assertEqual("", sol.gcdOfStrings("LEET", "CODE"))


if __name__ == '__main__':
    unittest.main()
