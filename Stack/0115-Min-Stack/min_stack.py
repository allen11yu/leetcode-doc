class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []  # each value added to the stack has a minimal value

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
