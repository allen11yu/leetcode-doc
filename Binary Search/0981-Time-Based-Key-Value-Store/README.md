# [981. Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/description/)

For this problem, we can apply binary search to improve the brute force solution, which is iterating through the values and get the value that holds the most recent or equal timestamp. The runtime for the brute force solution is `O(N)`, where N is the number of values within a key.
By appying binary search we can improve the search time to `O(log(N))`.

---
Runtime: O(log(N)), apply binary search optimization.

Space: O(N), use of hashmap to store time based key value pairs.