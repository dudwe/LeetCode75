import unittest
from ArrayProblems.ReverseVowelsOfAString.ReverseVowelsOfAString import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual("holle", sol.reverseVowels("hello"))

    def test_two(self):
        sol = Solution()
        self.assertEqual("leotcede", sol.reverseVowels("leetcode"))


if __name__ == '__main__':
    unittest.main()
