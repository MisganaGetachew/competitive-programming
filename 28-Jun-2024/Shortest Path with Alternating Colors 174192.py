# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1 for i in range(n)]
        red = defaultdict(list)
        blue = defaultdict(list)


        for a, b in redEdges:
            red[a].append(b)

        for a, b in blueEdges:
            blue[a].append(b)
        q = deque()
        q.append([0, 0 , None])
        visit = set()
        visit.add((0, None))
        
        while q:
            node , level, color  = q.popleft()
            if ans[node] == -1:
                ans[node] = level
            if color != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append((nei, level  + 1, "RED"))
            if color != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append((nei, level  + 1, "BLUE"))
        return ans

