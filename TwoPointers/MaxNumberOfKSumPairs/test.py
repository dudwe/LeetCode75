import unittest
from TwoPointers.MaxNumberOfKSumPairs.MaxNumberOfKSumPairs import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(2, sol.maxOperations([1,2,3,4],5))

    def test_two(self):
        sol = Solution()
        self.assertEqual(1, sol.maxOperations([3,1,3,4,3],6))


    def test_three(self):
        sol = Solution()
        self.assertEqual(3, sol.maxOperations([1,2,2,3,3,4,5,6],6))


if __name__ == '__main__':
    unittest.main()
