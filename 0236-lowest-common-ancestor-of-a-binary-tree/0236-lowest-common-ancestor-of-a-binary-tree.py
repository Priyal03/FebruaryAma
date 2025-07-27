# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent = {root: None}
        stack = [root]

        while p not in parent or q not in parent:
            current = stack.pop()
            if current.left:
                parent[current.left] = current
                stack.append(current.left)
            if current.right:
                parent[current.right] = current
                stack.append(current.right)

        pAncestors = set()

        while p:
            pAncestors.add(p)
            p = parent[p]

        while q not in pAncestors:
            q = parent[q]

        return q
