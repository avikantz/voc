from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class MaxTests(TranspileTestCase):

    def test_tuple(self):
        self.assertCodeExecution("""
            try:
                print(max((1, 5), (2, 4), (12, 14)))
                print(max(("ackbar", "balrog"), ("klingon", "ewoks"), ("zalthor", "zathura")))
                print(max((1, 4), (1, 2)))
            except Exception as e:
                print(e)
            """, run_in_function=False)

    def test_max(self):
        self.assertCodeExecution("""
            try:
                print(max(1, 5, 3, 2, 4, 9, 12))
                print(max("foo", "bar"))
                print(max("foo", "bar", "other"))
                # print(max("foo", "bar", 1729))
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
        'test_tuple'
    ]
