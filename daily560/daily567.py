import unittest


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def f(a, b):
        return a

    return pair(f)

def cdr(pair):
    def f(a, b):
        return b

    return pair(f)


class Daily567(unittest.TestCase):


    def test_car(self):
        self.assertEqual(car(cons(3, 4)), 3)

    def test_cdr(self):
        self.assertEqual(cdr(cons(3, 4)), 4)


if __name__ == '__main__':
    unittest.main()
