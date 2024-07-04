# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph =  defaultdict(list)
        visited = set()
        q = deque()
        q.append((target.val, 0))
        visited.add(target.val)

        def dfs(root):
            if root == None:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        ans = []
        while q:
            node, step = q.popleft()
            # if k > step:
            #     return ans
            if k == step:
                ans.append(node) 
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append((n, step + 1))          

        return ans
