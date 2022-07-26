# Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If root lies between p and q that means they belong in different subtrees and root is LCA
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        # Searching in Left Subtree
        if root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Searching in right Subtree
        return self.lowestCommonAncestor(root.right, p, q)
      
# Solution:
# Runtime: 102 ms, faster than 70.18% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.7 MB, less than 68.08% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
