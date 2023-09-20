from unittest import TestCase

from datatool.lcs import lcs_solve_length, lcs_solve


class TimeTest(TestCase):
    def test_lcs_length(self):
        self.assertEqual(lcs_solve_length("abcde", "axcxe"), 3)

    def test_lcs(self):
        self.assertEqual(lcs_solve("abedc", "axec"), ['a', 'e', 'c'])
