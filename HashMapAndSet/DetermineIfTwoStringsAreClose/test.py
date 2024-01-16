import unittest
from HashMapAndSet.DetermineIfTwoStringsAreClose.DetermineIfTwoStringsAreClose import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(True, sol.closeStrings("abc", "bca"))

    def test_two(self):
        sol = Solution()
        self.assertEqual(False, sol.closeStrings("a", "aa"))

    def test_three(self):
        sol = Solution()
        self.assertEqual(True, sol.closeStrings("cabbba", "abbccc"))


if __name__ == '__main__':
    unittest.main()
