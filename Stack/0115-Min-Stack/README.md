# [155. Min Stack](https://leetcode.com/problems/min-stack/description/)

The key idea for this problem is to have two stacks. One regular stack that allow for `push()`, `pop()`, `top()` of passed values. Another "minimal" stack for storing the minimal value at each point of `push()`, hence enabling the `getMin()` function.

For example, say we have a list of operations:

- `push(1)`
- `push(2)`
- `push(0)`

The regular stack will consists of: `(bottom) [1, 2, 0] (top)`

The minimal stack will consists of: `(bottom) [1, 1, 0] (top)`

This is because at each `push(val)`, `val` is compared to the top of the minimal stack. Hence, the smaller value will be pushed to the minimal stack. That being said, everytime `getMin()` is called, the top of the minimal stack will always be the minimal value.

Now if `getMin()` is called, the function will return `0`, which is the minimal value.

---
Runtime: O(1), each operation is constant.

Space: O(N), append N values to the stack.

