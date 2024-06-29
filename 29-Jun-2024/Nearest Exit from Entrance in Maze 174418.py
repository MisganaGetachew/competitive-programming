# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def outbound(X, Y, maze):
            return X < 0 or X >= len(maze) or Y < 0 or Y >= len(maze[0])
        
        visited = set()
        q = deque()
        q.append((entrance, 0))
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        entrance_tuple = tuple(entrance)
        visited.add(entrance_tuple)
        
        while q:
            (r, c), step = q.popleft()
            
            for dx, dy in dir:
                X = dx + r
                Y = dy + c
                
                if outbound(X, Y, maze):
                    continue
                
                if (X, Y) == entrance_tuple:
                    continue
                
                if maze[X][Y] == "+":
                    continue
                
                if (X, Y) not in visited:
                    if X == 0 or X == len(maze) - 1 or Y == 0 or Y == len(maze[0]) - 1:
                        return step + 1
                    
                    q.append(((X, Y), step + 1))
                    visited.add((X, Y))
                    
        return -1
