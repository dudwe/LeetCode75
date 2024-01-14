import unittest
from SlidingWindow.MaxNumberofVowelsInASubstringofGivenLength.MaxNumberofVowelsInASubstringofGivenLength import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(3, sol.maxVowels("abciiidef", 3))

    def test_two(self):
        sol = Solution()
        self.assertEqual(2, sol.maxVowels("aeiou", 2))

    def test_three(self):
        sol = Solution()
        self.assertEqual(2, sol.maxVowels("leetcode", 3))


if __name__ == '__main__':
    unittest.main()
