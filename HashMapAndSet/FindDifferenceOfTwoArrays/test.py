import unittest
from HashMapAndSet.FindDifferenceOfTwoArrays.FindDifferenceOfTwoArrays import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual([[1, 3], [4, 6]], sol.findDifference([1, 2, 3], [2, 4, 6]))

    def test_two(self):
        sol = Solution()
        self.assertEqual([[3], []], sol.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
