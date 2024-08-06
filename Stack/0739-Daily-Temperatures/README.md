# [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

The key idea for this problem is monotonic stack. Monotonic stack is a stack data structure that maintains elements in a specific order, either increasing or decreasing.

For example, a monotonic increasing stack may have elements: `(bottom) [2, 3, 4, 5] (top)`. Each new element is greater than or equal to the element before it. Similarly, a montonic decreasing stack may have elements: `(bottom) [5, 4, 3, 2] (top)`. Each new element is greater than or equal to the element before it (i.e. element on top of the stack).

In this problem, we want to update `result[i]` (i.e. the number of days after the ith day before a warmer temperature appears on a future day.) whenever a higher temperature is spotted. To find `i`, we can save the index of each element using a tuple (e.g. (temperature, index)). This way, the stack will always be in a decreasing order, hence a montonic decreasing stack.

---
Runtime: O(N), iterate through the `temperatures` list with length N.

Space: O(N), use of data structures to store N temperatures and number of days till warmer temperature.
