import unittest


def min_range(listeners, towers):
    largest = 0
    t1 = towers[0]
    i = 0
    for listener in listeners:
        d1 = abs(listener - t1)
        if d1 <= largest:
            continue
        if i + 1 < len(towers):
            t2 = towers[i + 1]
            d2 = abs(t2 - listener)
            if d2 <= d1:
                t1 = t2
                d1 = d2
                i += 1
        if d1 > largest:
            largest = d1
    return largest


class Daily707(unittest.TestCase):

    def test_one(self):
        self.assertEqual(min_range([2], [0]), 2)

    def test_given(self):
        self.assertEqual(min_range([1, 5, 11, 20], [4, 8, 15]), 5)


if __name__ == '__main__':
    unittest.main()
