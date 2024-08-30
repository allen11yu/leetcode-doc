# [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)

The goal for this problem is to count the good nodes within a given binary tree. A good node is a node, where its value is greater than or equal to the maximum value on the path so far. We can solve this problem with recursive DFS, using additional parameter `maxVal` for comparisons.

---
Runtime: O(N), where each node was visited.

Space: O(h), where `h` is the height of the binary tree. O(h) may be further denoted as O(log(N)) for a balanced binary tree and O(N) for a unbalanced binary tree. 