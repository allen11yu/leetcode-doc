# [100. Same Tree](https://leetcode.com/problems/same-tree/description/)

The goal for this problem is to check if two given binary trees(p and q) are equal. For two binary trees to be equal, the trees must have the same structure and node value.
Here, we can use recursive DFS to achieve this. We keep calling the `isSameTree()` for left and right children, as long as the values are equal. When the current node reaches `NULL`, all the function calls on the stack will return `True`. However, if a mismatch is found, the function will immediately return `False` without waiting for the current node to reach `NULL`.

Coding note:
- Since we want both left and right subtrees to be equal, we want to use the `and` operator.

---
Runtime: O(N), where each node was visited.

Space: O(h), where `h` is the height of the binary tree. O(h) may be further denoted as O(log(N)) for a balanced binary tree and O(N) for a unbalanced binary tree. 