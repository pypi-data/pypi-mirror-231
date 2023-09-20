from unittest import TestCase

import numpy as np
import pandas as pd

from datatool.utils import as_iter_chunks, as_chunks, as_grid


class UtilsTest(TestCase):
    def test_as_chunks(self):
        it = iter(range(12))
        result = [chunk for chunk in as_chunks(it, 5)]
        self.assertListEqual(
            result,
            [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11]]
        )

    def test_as_iter_chunks(self):
        it = iter(range(12))
        result = [list(chunk) for chunk in as_iter_chunks(it, 5)]
        self.assertListEqual(
            result,
            [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11]]
        )

    def test_as_grid(self):
        it1 = range(3)
        it2 = range(2)
        grid = list(as_grid(it1, it2))
        self.assertListEqual(
            grid,
            [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        )
