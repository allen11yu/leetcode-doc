# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

For this problem, we want to find the diameter of a given binary tree. The diameter is computed as the length of the longest path between any two nodes.
So to find the diameter, we can add the height of left and right subtrees together and record the maximum sum. Note that, the height of subtrees may vary, so we need
to maximize the height of the left and right subtrees.

Note on coding:
- `nonlocal x`, allow the variable with same name to be updated within a nested function. The value from the nearest enclosing block is taken.

---
Runtime: O(N), where each node was visited.

Space: O(h), where `h` is the height of the binary tree. O(h) may be further denoted as O(log(N)) for a balanced binary tree and O(N) for a unbalanced binary tree. 