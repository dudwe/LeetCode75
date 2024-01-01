import unittest
from ArrayProblems.KidsWithTheGreatestNumberOfCandies.KidsWithGreatestNumberOfCandies import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual([True,True,True,False,True] , sol.kidsWithCandies([2,3,5,1,3], 3))

    def test_two(self):
        sol = Solution()
        self.assertEqual([True,False,False,False,False] , sol.kidsWithCandies([4,2,1,1,2], 1))

    def test_three(self):
        sol = Solution()
        self.assertEqual([True,False,True], sol.kidsWithCandies([12,1,12], 10))


if __name__ == '__main__':
    unittest.main()
