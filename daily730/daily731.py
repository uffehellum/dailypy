import unittest

# Given a array of numbers representing the stock
# prices of a company in chronological order,
# write a function that calculates the maximum profit
# you could have made from buying and selling that stock once.
# You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5,
# since you could buy the stock at 5 dollars and
# sell it at 10 dollars.


class TestDaily731(unittest.TestCase):

    def test_base(self):
        self.assertEqual(5, max_profit([9, 11, 8, 5, 7, 10]))


def max_profit(prices):
    if len(prices) == 0:
        return 0
    max = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        if price - lowest > max:
            max = price - lowest
    return max