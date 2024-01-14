import unittest
from SlidingWindow.MaxAverageSubArray.MaxAverageSubarray import Solution



class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(12.75000, sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))

    def test_two(self):
        sol = Solution()
        self.assertEqual(5.00000, sol.findMaxAverage([5], 1))





if __name__ == '__main__':
    unittest.main()
