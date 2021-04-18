import unittest

parens = [
    '((%d %s %d) %s %d) %s %d',
    '(%d %s (%d %s %d)) %s %d',
    '%d %s ((%d %s %d) %s %d)',
    '%d %s (%d %s (%d %s %d))',
    '(%d %s %d) %s (%d %s %d)'
]
ops = '+-*/'

def v4(p, o1, o2, o3, a):
    try:
        return eval(p % (a[0], o1, a[1], o2, a[2], o3, a[3]))
    except ZeroDivisionError:
        return 0

def is24(a):
    return any (1 for o1 in ops
                for o2 in ops
                for o3 in ops
                for p in parens
                if v4(p, o1, o2, o3, a) == 24)


class Daily706(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(is24([5, 2, 7, 8]), True)

    def test_twos(self):
        self.assertEqual(is24([2, 2, 2, 3]), True)


if __name__ == '__main__':
    unittest.main()
