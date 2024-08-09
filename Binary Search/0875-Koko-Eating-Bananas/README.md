# [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)

For this problem, we can apply binary search to improve the brute force solution. The runtime for the brute force solution is `O(max(P) * P)`, where P is piles.
By applying binary search, the runtime complexity improved to `O(log(max(P)) * P)`.

Even a little optimization will have a significant impact on performance.
---
Runtime: O(log(max(P)) * P), apply binary search optimization.

Space: O(1), use of pointer and temp variables.