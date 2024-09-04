# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for neig in range (len(isConnected)):
                if isConnected[start][neig] and neig not in visited:
                    dfs(neig)

        provinces = 0
        visited = set()
        for node in range(len(isConnected)):
            if node not in visited:
                provinces += 1
                dfs(node)
        return provinces