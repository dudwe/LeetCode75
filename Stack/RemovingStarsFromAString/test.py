import unittest
from Stack.RemovingStarsFromAString.RemovingStarsFromAString import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual("lecoe", sol.removeStars("leet**cod*e"))

    def test_two(self):
        sol = Solution()
        self.assertEqual("", sol.removeStars("erase*****"))


if __name__ == '__main__':
    unittest.main()
