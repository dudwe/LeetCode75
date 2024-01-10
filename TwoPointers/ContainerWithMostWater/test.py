import unittest
from TwoPointers.ContainerWithMostWater.ContainerWithMostWater import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(49, sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(1, sol.maxArea([1, 1]))


if __name__ == '__main__':
    unittest.main()
