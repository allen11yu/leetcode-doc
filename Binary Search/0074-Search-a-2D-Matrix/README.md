# [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

For this problem, we are searching for a target value in a 2D list/matrix. 

Per the problem description,
- Each row in `matrix` is sorted in non-decreasing order.
- The first integer of every row is greater than the last integer of the previous row.

Since the list is sorted, we can apply two binary searches to find the target value. First we apply binary search to find the row, then we apply another binary search to find the target value within that row. During the first binary search, we need to use the 1st integer to determine whether we need to shift to a bigger row or use the last integer to determine whether we need to shift to a smaller row.

Note on coding:
- `len(matrix)` returns the number of rows
- `len(matrix[0])` returns the number of columns
- `matrix[row][columnm]` returns the value

---
Runtime: O(log N), apply 2 binary searches.

Space: O(1), use of pointer variables.