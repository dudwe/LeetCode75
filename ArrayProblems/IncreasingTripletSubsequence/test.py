import unittest
from ArrayProblems.IncreasingTripletSubsequence.IncreasingTripletSubsequence import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(True, sol.increasingTriplet([1,2,3,4,5]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(False, sol.increasingTriplet([5,4,3,2,1]))

    def test_three(self):
        sol = Solution()
        self.assertEqual(True, sol.increasingTriplet([2,1,5,0,4,6]))


if __name__ == '__main__':
    unittest.main()
