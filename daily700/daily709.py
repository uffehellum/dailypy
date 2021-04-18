import unittest

def paths(a):
    p = [0] * len(a[0])
    p[0] = 1
    for r in a:
        x = 0
        for i, v in enumerate(r):
            if v == 0:
                x += p[i]
            else:
                x = 0
            p[i] = x
    return x

class TestDaily709(unittest.TestCase):

    def test_base(self):
        v = paths(
            [[0, 0, 1],
             [0, 0, 1],
             [1, 0, 0]])
        self.assertEqual(v, 2)

