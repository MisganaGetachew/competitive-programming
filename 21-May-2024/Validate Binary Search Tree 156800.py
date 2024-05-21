# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, min, max):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            left = validate(node.left, min, node.val)
            right = validate(node.right, node.val, max)
            return left and right
        return validate(root, -inf, inf )