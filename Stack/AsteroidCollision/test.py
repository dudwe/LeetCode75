import unittest

from Stack.AsteroidCollision.AsteroidCollision import Solution


class MyTestCase(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        self.assertEqual([5, 10], sol.asteroidCollision([5, 10, -5]))

    def test_two(self):
        sol = Solution()
        self.assertEqual([], sol.asteroidCollision([8, -8]))

    def test_three(self):
        sol = Solution()
        self.assertEqual([10], sol.asteroidCollision([10, 2, -5]))

    def test_four(self):
        sol = Solution()
        self.assertEqual([-2,-1,1,2], sol.asteroidCollision([-2, -1, 1, 2]))
