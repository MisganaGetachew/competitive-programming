# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(root, curr):
            if root.left == None and root.right == None :
                return curr * 10 + root.val
            res = 0
            if root.left != None:
                res += rec(root.left, curr * 10 + root.val)
            if root.right != None:
                res += rec(root.right, curr * 10 + root.val )
            
            return res
        return rec(root, 0)
            