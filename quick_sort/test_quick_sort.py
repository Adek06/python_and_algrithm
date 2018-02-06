import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    """ test quick_sort.py """

    def test_sort(self):
        ''' return sort list '''

        sort_list = quick_sort([6, 3, 2, 1, 4, 9, 8, 7, 5], 0, 8)
        self.assertEqual(sort_list, [1,2,3,4,5,6,7,8,9])

unittest.main()