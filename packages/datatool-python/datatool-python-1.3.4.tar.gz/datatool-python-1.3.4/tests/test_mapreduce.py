from unittest import TestCase

from datatool.mapreduce import map_multi, reduce_multi, mapreduce_multi


class MapreduceTest(TestCase):
    def test_map_multi(self):
        self.assertListEqual(
            map_multi(
                [1, 2, 3],
                map_func=lambda x: x**2,
                threads_num=2
            ),
            [1, 4, 9]
        )

    def test_reduce_multi(self):
        self.assertEqual(
            reduce_multi(
                [1, 2, 3],
                reduce_func=lambda a, b: a + b,
                threads_num=2
            ),
            6
        )

    def test_mapreduce_multi(self):
        self.assertEqual(
            mapreduce_multi(
                [1, 2, 3],
                map_func=lambda x: x**2,
                reduce_func=lambda a, b: a + b,
                threads_num=2
            ),
            14
        )
