import unittest
from SlidingWindow.MaxConsecOnes.MaxConsecOnes import Solution




class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(6, sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))

    def test_two(self):
        sol = Solution()
        self.assertEqual(10, sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))





if __name__ == '__main__':
    unittest.main()
