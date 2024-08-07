# [704. Binary Search](https://leetcode.com/problems/binary-search/description/)

For this problem, we are implementing a basic binary search. Binary Search is like finding a word in a dictionary: we start in the middle, and move to the left or right section depending on the word. If the word is bigger, then we move to the **smaller** left section. If the word is smaller, then we move to the **bigger** right section. In order to apply binary search, the list must be **sorted**.

When coding it up, make sure to avoid errors like the overflow error. One way to find the mid point is `(l + r) // 2`. For languages like Java, this operation may lead to integer overflow. In some cases, both `nums[l]` and `nums[r]` will be maximum integers, hence adding them together will lead to overflow (i.e. too large for system to handle). So, another way to find the mid point without potential overflow is `l + ((l + r) // 2)`.

---
Runtime: O(log N), cut the list in half after each iteration.

Space: O(1), use of three variables: left, right, and mid.