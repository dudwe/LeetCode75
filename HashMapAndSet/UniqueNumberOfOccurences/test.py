import unittest
from HashMapAndSet.UniqueNumberOfOccurences.UniqueNumberOfOccurrences import Solution


class MyTestCase(unittest.TestCase):
    def test_one(self):
        sol = Solution()
        self.assertEqual(True, sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(False, sol.uniqueOccurrences([1, 2]))

    def test_three(self):
        sol = Solution()
        self.assertEqual(True, sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

if __name__ == '__main__':
    unittest.main()
