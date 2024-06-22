# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph  = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        stack = [source]

        while stack:
            val =  stack.pop()
            if val == destination:
                return True
            if val in visited:
                continue
            visited.add(val)
            for neigh in graph[val]:
                    if neigh not in visited:
                            stack.append(neigh)
        return False
                    