import unittest
from PrefixSum.FindHighestAltitude.FindHighestAltitude import Solution


class MyTestCase(unittest.TestCase):
    def test_one(self):
        sol = Solution()
        self.assertEqual(1, sol.largestAltitude([-5,1,5,0,-7]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(0, sol.largestAltitude([-4,-3,-2,-1,4,3,2]))

if __name__ == '__main__':
    unittest.main()
