# Question: https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Solution: Iterative
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result
        
        stack = [root]
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            stack = stack + curr.children[::-1]
        return result
        
# Verdict:
# Runtime: 98 ms, faster than 20.71% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.2 MB, less than 65.07% of Python3 online submissions for N-ary Tree Preorder Traversal.

# -----------------------------------------------------------------------------------------------------

# Solution: Recursive:
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def traverse(root):
            if root is None:
                return
            result.append(root.val)
            for child in root.children:
                traverse(child)
        traverse(root)
        return result

# Verdict:
# Runtime: 93 ms, faster than 27.69% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.3 MB, less than 48.40% of Python3 online submissions for N-ary Tree Preorder Traversal.
