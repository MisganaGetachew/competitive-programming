# Problem: C - The Lakes - https://codeforces.com/gym/535309/problem/C

from collections import deque
t = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(t):
    r, c = map(int, input().split())

    grid = []
    for i in range(r):
        grid.append(list(map(int, input().split())))
    visited = set()

    def bfs(x, y):
        queue = deque([(x, y)])
        visited.add((x, y))
        volume = 0

        while queue:
            cx, cy = queue.popleft()
            volume += grid[cx][cy]

            for dx, dy in directions:
                X, Y = cx + dx, cy + dy
                if 0 <= X < r and 0 <= Y < c and (X, Y) not in visited and grid[X][Y] > 0:
                    visited.add((X, Y))
                    queue.append((X, Y))

        return volume
    vol = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] > 0 and (i, j) not in visited:
                vol = max(vol, bfs(i, j))
    print(vol)