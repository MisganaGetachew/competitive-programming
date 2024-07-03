# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * n  
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
                indegree[rightChild[i]] += 1

        
        if any(d > 1 for d in indegree):
            return False

        
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root == -1:
                    root = i
                else: 
                    return False

        if root == -1:
            return False

       
        visited = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False  
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != -1:
                    queue.append(neighbor)
        return len(visited) == n