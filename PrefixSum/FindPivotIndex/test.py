import unittest
from PrefixSum.FindPivotIndex.FindPivotIndex import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(3, sol.pivotIndex([1,7,3,6,5,6]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(-1, sol.pivotIndex([1,2,3]))


    def test_three(self):
        sol = Solution()
        self.assertEqual(0, sol.pivotIndex([2,1,-1]))


if __name__ == '__main__':
    unittest.main()
