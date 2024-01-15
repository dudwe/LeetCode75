import unittest
from SlidingWindow.LongestSubArrayofOnes.LongestSubArrayofOnes import Solution




class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(3, sol.longestSubarray([1,1,0,1]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(5, sol.longestSubarray([0,1,1,1,0,1,1,0,1]))

    def test_three(self):
        sol = Solution()
        self.assertEqual(2, sol.longestSubarray([1,1,1]))





if __name__ == '__main__':
    unittest.main()
