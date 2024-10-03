# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def PostOrder(self, root, ans):
        if root:
            for node in root.children:
                self.PostOrder(node, ans)
            ans.append(root.val)
    def postorder(self, root):
        ans = []
        self.PostOrder(root, ans)
        return ans 