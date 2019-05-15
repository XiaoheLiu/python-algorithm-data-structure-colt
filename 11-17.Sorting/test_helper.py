import unittest
import helper


class TestHelper(unittest.TestCase):

    def test_min_index(self):
        self.assertEqual(helper.min_index([5, 2, 1, 3], 1), 2)

    def test_merge(self):
        a1 = [1, 3]
        a2 = [5, 7]
        a3 = [2, 4]
        self.assertEqual(helper.merge(a1, a2), [1, 3, 5, 7])
        self.assertEqual(helper.merge(a3, a1), [1, 2, 3, 4])
        self.assertEqual(helper.merge([2], a1), [1, 2, 3])
