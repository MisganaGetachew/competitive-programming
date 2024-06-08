# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = TreeNode()
        def solve(node):
            nonlocal ans
            if not node:
                return False

            left = solve(node.left)
            right = solve(node.right)
            
            this_node = node.val == p.val or node.val == q.val

            total = left + right + this_node

            if total == 2:
                ans = node
            
            return total != 0
        solve(root)  
        return ans