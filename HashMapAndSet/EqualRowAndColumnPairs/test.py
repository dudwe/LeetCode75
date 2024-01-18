import unittest
from HashMapAndSet.EqualRowAndColumnPairs.EqualRowAndColumPairs import Solution

class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual(1, sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))

    def test_two(self):
        sol = Solution()
        self.assertEqual(3, sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


if __name__ == '__main__':
    unittest.main()
