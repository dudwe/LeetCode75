import unittest
from ArrayProblems.MergeStringAlternately.MergeStringAlternately import Solution


class MyTestCase(unittest.TestCase):
    def test_one(self):
        sol = Solution()
        self.assertEqual("apbqcr", sol.mergeAlternately("abc", "pqr"))

    def test_two(self):
        sol = Solution()
        self.assertEqual("apbqrs", sol.mergeAlternately("ab", "pqrs"))

    def test_three(self):
        sol = Solution()
        self.assertEqual("apbqcd", sol.mergeAlternately("abcd", "pq"))

if __name__ == '__main__':
    unittest.main()
