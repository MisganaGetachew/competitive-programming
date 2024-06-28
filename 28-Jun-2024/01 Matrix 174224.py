# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
  
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col  = len(mat), len(mat[0])
        res = [[0 for i in range(col)] for j in range(row)]
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        u = deque()
        visited = set()
        for i in range(row):
            for j in range(col):     
                if not mat[i][j]:
                    u.append((i,j))
                    visited.add((i,j))

        count = 1
        while u:
            for _ in range(len(u)):
                r, c = u.popleft()
                for dx, dy in dir:
                    X = dx + r
                    Y = dy + c
                    if X < 0 or X > row - 1 or Y < 0 or Y > col  - 1:
                        continue
                    if (X,Y) not in visited:
                        # print(mat[X][Y])
                        res[X][Y] = count
                        u.append((X,Y))
                        visited.add((X,Y))

            count += 1        
       
        return res



