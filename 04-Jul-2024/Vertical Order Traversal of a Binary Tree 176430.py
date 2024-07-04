# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = defaultdict(list)
        ans = []
        q = deque()
        q.append((root, 0,  0))
        while q: 
            node, x,  y = q.popleft()
        
            values[y].append((x, node.val)) 
            if node.left:
                q.append((node.left, x + 1, y - 1))
            if node.right:
                q.append((node.right, x + 1, y + 1)) 
        val = sorted(values)
        for key in val:
            ans.append([i[1] for i in sorted(values[key])])
        # print(val)
        return ans


         