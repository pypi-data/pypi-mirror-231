import warnings
from unittest import TestCase

import numpy as np
import pandas as pd

from datatool.cuda.base import (
    get_cuda_type, get_cuda_struct, dataframe_to_records
)
from datatool.cuda.cluster import clusterize


try:
    import pycuda
except ImportError:
    warnings.warn("Could not run CudaClusterTest "
                  "because pycuda is not installed")
else:
    class CudaBaseTest(TestCase):
        def test_get_cuda_type(self):
            self.assertEqual(
                get_cuda_type(np.dtype("u4")),
                "uint"
            )
            self.assertEqual(
                get_cuda_type(np.dtype("i4")),
                "int"
            )
            self.assertEqual(
                get_cuda_type(np.dtype("u4"), "a"),
                "uint a"
            )
            self.assertEqual(
                get_cuda_type(np.dtype("u1")),
                "char"
            )
            self.assertEqual(
                get_cuda_type(np.dtype("i1")),
                "signed char"
            )
            self.assertEqual(
                get_cuda_type(np.dtype("S16")),
                "char[16]"
            )

        def test_get_cuda_struct(self):
            dtype = np.dtype([('x', 'u4'), ('y', 'i4'), ('z', 'S8')])
            self.assertEqual(
                get_cuda_struct(dtype),
                'struct {\nuint x;\nint y;\nchar z[8];\n}'
            )

        def test_dataframe_to_records(self):
            df = pd.DataFrame({
                'key': ['text' for _ in range(11)],
                'x': list(range(11)),
                'y': [0] * 11
            })

            items = dataframe_to_records(
                df,
                column_dtypes=[
                    ('key', 'S4'),
                    ('x', np.uint8),
                    ('y', np.uint16),
                ]
            )
            self.assertEqual(items.nbytes, 77)

            items = dataframe_to_records(
                df,
                column_dtypes=[
                    ('key', 'S4'),
                    ('x', np.uint8),
                    ('y', np.uint16),
                ],
                align=True
            )
            self.assertEqual(items.nbytes, 88)

    class CudaClusterTest(TestCase):
        def test_cluster(self):
            items = np.array(
                [('text', i, 0) for i in range(11)],
                dtype=np.dtype(
                    [('key', 'S4'), ('x', np.uint8), ('y', np.uint16)],
                    align=True
                )
            )
            code = """
            __device__ int edge(const Item* item1, const Item* item2) {
                return (item1->x == 2 * item2->x) || (item2->x == 2 * item1->x);
            }
            """
            clusters = clusterize(items, code)

            self.assertTrue(np.array_equal(
                clusters,
                np.array([0, 1, 1, 3, 1, 5, 3, 7, 1, 9, 5], dtype=np.uint32)
            ))

        def test_cluster_pandas(self):
            df = pd.DataFrame({
                'key': ['text' for _ in range(11)],
                'x': list(range(11)),
                'y': [0] * 11
            })

            items = dataframe_to_records(
                df,
                column_dtypes=[
                    ('key', 'S4'),
                    ('x', np.uint8),
                    ('y', np.uint16),
                ],
                align=True
            )

            code = """
            __device__ int edge(const Item* item1, const Item* item2) {
                return (item1->x == 2 * item2->x) || (item2->x == 2 * item1->x);
            }
            """
            clusters = clusterize(items, code)

            self.assertTrue(np.array_equal(
                clusters,
                np.array([0, 1, 1, 3, 1, 5, 3, 7, 1, 9, 5], dtype=np.uint32)
            ))
