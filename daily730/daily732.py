import unittest

# An imminent hurricane threatens the coastal town of Codeville.
# If at most two people can fit in a rescue boat,
# and the maximum weight limit for a given boat is k,
# determine how many boats will be needed to save everyone.

# For example, given a population with weights
# [100, 200, 150, 80] and a boat limit of 200,
# the smallest number of boats required will be three.


class TestDaily732(unittest.TestCase):

    def test_base(self):
        self.assertEqual(3, boats_needed(200, [100, 200, 150, 80]))

def boats_needed(boat_limit, weights):
    if len(weights) == 0:
        return 0
    weights.sort()
    if weights[-1] > boat_limit:
        raise Exception("The boat limit is lower than the heaviest person")
    boats = 0
    low = 0
    high = len(weights) - 1
    while low < high:
        if weights[low] + weights[high] <= boat_limit:
            low += 1
        high -= 1
        boats += 1
    if low == high:
        boats += 1
    return boats