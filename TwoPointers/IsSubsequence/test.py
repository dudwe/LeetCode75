import unittest
from TwoPointers.IsSubsequence.IsSubsequence import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()

        self.assertEqual(True, sol.isSubsequence("abc","ahbgdc"))

    def test_two(self):
        sol = Solution()

        self.assertEqual(False, sol.isSubsequence("axc","ahbgdc"))



if __name__ == '__main__':
    unittest.main()
