# Implement a stack that has the following methods:
#
# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack.
# If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently.
# If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

import unittest


class TestDaily746(unittest.TestCase):

    def test_base(self):
        s = Stack()
        s.push(1)
        self.assertEqual(1, s.max())
        s.push(2)
        self.assertEqual(2, s.max())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.max())
        self.assertEqual(1, s.pop())


class StackElement:
    def __init__(self, val, next):
        self.val = val
        self.next = next
        if next and next.val > val:
            self.max = next.val
        else:
            self.max = val

class Stack:

    def __init__(self):
        self.stack: StackElement = None

    def max(self):
        return self.stack.max

    def push(self, val):
        self.stack = StackElement(val, self.stack)

    def pop(self):
        val = self.stack.val
        self.stack = self.stack.next
        return val


