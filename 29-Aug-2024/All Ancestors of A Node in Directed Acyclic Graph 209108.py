# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
            
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        ancestors = [set() for _ in range(n)]
        
        def dfs(node, start):
            for neighbor in graph[node]:
                if start not in ancestors[neighbor]:
                    ancestors[neighbor].add(start)
                    dfs(neighbor, start)
        
        for node in range(n):
            dfs(node, node)
        
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
        return result
        