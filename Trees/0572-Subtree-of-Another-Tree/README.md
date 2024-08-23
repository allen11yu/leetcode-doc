# [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/)

The goal for this problem is to check if given binary tree `subRoot` is a subtree of another binary tree `root`. To achieve this, we can use the `isSameTree()` as a helper function.
In the main function `isSubtree()`, we can run recursive DFS on each node and check if the trees are equal. Note that, if `subRoot` is `NULL`, it is still considered as equal, but not vice versa.


Coding note:
- Since we want either left or right subtrees to be equal to `subRoot`, we want to use the `or` operator.

---
Runtime: O(M * N), where each node was visited in `root` and compared to each node of `subRoot`.

Space: O(h), where `h` is the height of the binary tree. O(h) may be further denoted as O(log(M) + log(N)) for a balanced binary tree and O(M + N) for a unbalanced binary tree. 