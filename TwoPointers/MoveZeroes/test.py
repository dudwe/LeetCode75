import unittest
from TwoPointers.MoveZeroes.MoveZeroes import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        data = [0, 1, 0, 3, 12]
        sol.moveZeroes(data)
        self.assertEqual([1, 3, 12, 0, 0], data)

    def test_two(self):
        sol = Solution()
        data = [0]
        sol.moveZeroes(data)
        self.assertEqual([0], data)


    def test_three(self):
        sol = Solution()
        data = [0,0,0]
        sol.moveZeroes(data)
        self.assertEqual([0,0,0], data)

    def test_four(self):
        sol = Solution()
        data = [0,1,0]
        sol.moveZeroes(data)
        self.assertEqual([1,0,0], data)

if __name__ == '__main__':
    unittest.main()
