import unittest
import sorting


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.a0 = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8]
        self.a1 = [8, 1, 2, 5, 1, 4, 3, 6, 7, 5]
        self.a2 = [8, 7, 6, 5, 5, 4, 3, 2, 1, 1]

    def test_bubble_sort(self):
        self.assertEqual(sorting.bubble_sort(self.a0), self.a0)
        self.assertEqual(sorting.bubble_sort(self.a1), self.a0)
        self.assertEqual(sorting.bubble_sort(self.a2), self.a0)
        self.assertEqual(sorting.bubble_sort([]), [])

    def test_selection_sort(self):
        self.assertEqual(sorting.selection_sort(self.a0), self.a0)
        self.assertEqual(sorting.selection_sort(self.a1), self.a0)
        self.assertEqual(sorting.selection_sort(self.a2), self.a0)
        self.assertEqual(sorting.selection_sort([]), [])

    def test_insertion_sort(self):
        self.assertEqual(sorting.insertion_sort(self.a0), self.a0)
        self.assertEqual(sorting.insertion_sort(self.a1), self.a0)
        self.assertEqual(sorting.insertion_sort(self.a2), self.a0)
        self.assertEqual(sorting.insertion_sort([]), [])

    def test_merge_sort(self):
        self.assertEqual(sorting.merge_sort(self.a0), self.a0)
        self.assertEqual(sorting.merge_sort(self.a1), self.a0)
        self.assertEqual(sorting.merge_sort(self.a2), self.a0)
        self.assertEqual(sorting.merge_sort([]), [])

    def test_quick_sort(self):
        self.assertEqual(sorting.quick_sort(self.a0), self.a0)
        self.assertEqual(sorting.quick_sort(self.a1), self.a0)
        self.assertEqual(sorting.quick_sort(self.a2), self.a0)
        self.assertEqual(sorting.quick_sort([]), [])
