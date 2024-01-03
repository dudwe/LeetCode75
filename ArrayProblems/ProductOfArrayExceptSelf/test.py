import unittest
from ArrayProblems.ProductOfArrayExceptSelf.ProductOfArrayExceptSelf import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual([24,12,8,6], sol.productExceptSelf([1,2,3,4]))

    def test_two(self):
        sol = Solution()
        self.assertEqual([0,0,9,0,0], sol.productExceptSelf([-1,1,0,-3,3]))


if __name__ == '__main__':
    unittest.main()
