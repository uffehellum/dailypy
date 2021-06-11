import unittest


def fixed_point(a):
    return next((i for i, v in enumerate(a) if i == v), False)
    # for i, v in enumerate(a):
    #     if i == v:
    #         return i
    # return False


class Daily708Test(unittest.TestCase):

    def test_none(self):
        self.assertEqual(fixed_point([1, 5, 7, 8]), False)

    def test_two(self):
        self.assertEqual(fixed_point([-6, 0, 2, 40]), 2)