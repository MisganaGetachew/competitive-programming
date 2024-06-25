# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]

        def bipart(i):
            color[i] = 0
            stack = [i]
            while stack:
                node = stack.pop()
                for neigh in graph[node]:
                    if color[neigh] == color[node]:
                        return False
                    if color[neigh] == -1 :
                        stack.append(neigh)
                        color[neigh] = 1 - color[node]
            return True

        for i in range(len(graph)):
            if color[i] == -1 and not bipart(i):
                return False
        return True