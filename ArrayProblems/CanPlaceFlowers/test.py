import unittest
from ArrayProblems.CanPlaceFlowers.CanPlaceFlowers import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(True, sol.canPlaceFlowers([1,0,0,0,1], 1))

    def test_two(self):
        sol = Solution()
        self.assertEqual(False, sol.canPlaceFlowers([1,0,0,0,1], 2))

    def test_three(self):
        sol = Solution()
        self.assertEqual(False, sol.canPlaceFlowers([1,0,1,0,1], 1))

    def test_four(self):
        sol = Solution()
        self.assertEqual(True, sol.canPlaceFlowers([0,0,0,0,0], 3))

    def test_five(self):
        sol = Solution()
        self.assertEqual(False, sol.canPlaceFlowers([0,0,0,0,0], 4))

    def test_six(self):
        sol = Solution()
        self.assertEqual(False, sol.canPlaceFlowers([0,1,0], 1))

if __name__ == '__main__':
    unittest.main()
