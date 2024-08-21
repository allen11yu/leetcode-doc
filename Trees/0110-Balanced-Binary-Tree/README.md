# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

For this problem, we want to check if the given binary tree is balanced, which is defined as left and right subtrees of every node differ in height by no more than 1. We can use
recursive DFS to compare the difference of each subtree. Once the difference is greater than 1, we can set the `nonlocal` variable to `False`. The variable is initially set to `True`, and it will only be set to `False` if the given binary tree is unbalanced (i.e. difference > 1).


---
Runtime: O(N), where each node was visited.

Space: O(h), where `h` is the height of the binary tree. O(h) may be further denoted as O(log(N)) for a balanced binary tree and O(N) for a unbalanced binary tree. 