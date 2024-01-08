import unittest
from ArrayProblems.StringCompression.StringCompression import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        data = ["a","a","b","b","c","c","c"]
        self.assertEqual(6, sol.compress(data))
        self.assertEqual(list("a2b2c3c"), data)
    def test_two(self):
        sol = Solution()
        data = ["a"]
        self.assertEqual(1, sol.compress(data))
        self.assertEqual(list("a"), data)

    def test_three(self):
        sol = Solution()
        data = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.assertEqual(4, sol.compress(data))
        self.assertEqual(list("ab12bbbbbbbbb"), data)

if __name__ == '__main__':
    unittest.main()
