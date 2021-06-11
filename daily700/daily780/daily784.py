# Given a 2D matrix of characters and a target word, write a function that
# returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
#
# For example, given the following matrix:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column.
# Similarly, given the target word 'MASS', you should return true, since it's the last row.

import unittest

m = [['F', 'A', 'C', 'I'],
     ['O', 'B', 'Q', 'P'],
     ['A', 'N', 'O', 'B'],
     ['M', 'A', 'S', 'S'],
     ]


class Daily784(unittest.TestCase):
    def test_base(self):
        self.assertFalse(find_word("hest", m))

    def test_found(self):
        self.assertTrue(find_word("FOAM", m))
        self.assertTrue(find_word("MASS", m))

    def test_notfound(self):
            self.assertFalse(find_word("MASH", m))


def find_word(word, m):
    for (dr, dc) in [(1, 0), (0, 1)]:
        for r0 in range(len(m) - dr * len(word) + dr):
            for c0 in range(len(m[r0]) - dc * len(word) + dc):
                if check(word, m, r0, c0, dr, dc):
                    print("found", r0, c0, dr, dc)
                    return True
    return False


def check(word, m, r0, c0, dr, dc):
    for i, c in enumerate(word):
        if m[r0 + i * dr][c0 + i * dc] != c:
            return False
    return True
