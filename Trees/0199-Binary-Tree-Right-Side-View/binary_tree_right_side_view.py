from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## DFS approach.
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def dfs(root, level):
#             nonlocal res
#             if not root:
#                 return

#             if level == len(res):
#                 res.append(root.val)

#             dfs(root.right, level + 1)
#             dfs(root.left, level + 1)

#         dfs(root, 0)
#         return res


## BFS approach.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        while q:
            rightMost = None
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightMost:
                res.append(rightMost.val)
        return res
