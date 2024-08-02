import unittest
from min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def test_minStack(self):
        self.min_stack.push(1)
        self.min_stack.push(2)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.getMin(), 0)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 2)
        self.assertEqual(self.min_stack.getMin(), 1)


if __name__ == "__main__":
    unittest.main()
