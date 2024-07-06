# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        deg = [0] * numCourses
        for crs, preq in prerequisites:
            graph[preq].append(crs)
            deg[crs] += 1
        prc = 0
        q = deque([i for i in range(numCourses) if deg[i] == 0])
        while q:
          node = q.popleft()
          prc += 1
          for ne in graph[node]:
                deg[ne]  -= 1
                if deg[ne] == 0:
                    q.append(ne)
        return prc == numCourses


            