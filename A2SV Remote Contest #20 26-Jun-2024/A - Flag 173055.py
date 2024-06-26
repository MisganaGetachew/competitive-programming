# Problem: A - Flag - https://codeforces.com/gym/531416/problem/A

def grid():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    for i in range(n):
        temp = grid[i][0]
        for j in range(m):
            if temp != grid[i][j]:
                return False
        if i > 0 and grid[i][0] == grid[i-1][0]:
            return False
    return True


if grid():
    print("YES")
else:
    print("NO")
