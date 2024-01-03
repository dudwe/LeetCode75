import unittest
from ArrayProblems.ReverseWordsInAString.ReverseWordsInAString import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual("blue is sky the", sol.reverseWords("the sky is blue"))

    def test_two(self):
        sol = Solution()
        self.assertEqual("world hello", sol.reverseWords("  hello world  "))


if __name__ == '__main__':
    unittest.main()
