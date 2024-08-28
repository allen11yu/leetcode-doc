# [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)

The goal for this problem is to store the value of the nodes that belong to the right most side of a binary tree. Note that, a left child may also be apart of the right most view, when right child does not exist. This problem can be solve using DFS or BFS. For DFS, we will always go to right child first and use left child as last resort. For BFS, we will keep track of the right most node so far.


Coding note:
- May pass in parameter to DFS recursive function. In this case, the `level` variable is used to determine whether to append the node value to the result list. 

---
Runtime: O(N) for DFS and BFS, where each node was visited.

Space: O(h) for DFS and O(N) for BFS, where `h` is the height of the binary tree. O(h) may be further denoted as O(log(N)) for a balanced binary tree and O(N) for a unbalanced binary tree. 