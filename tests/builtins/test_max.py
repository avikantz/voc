from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class MaxTests(TranspileTestCase):

    def test_max(self):
        self.assertCodeExecution("""
            samples = [
                [1, 5, 3, 2, 4, 9, 12],
                ["foo", "bar"],
                ["foo", "bar", "other"],
                ["ackbar", "balrog", "klingon", "ewok"],
                [(1, 2), (3, 4), (5, 6, 7)]
            ]
            for seq in samples:
                try:
                    print(max(seq))
                except Exception as e:
                    print(e)
            """, run_in_function=False)


class BuiltinMaxFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["max"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]
