n = int(input())

for _ in range(n):
    a = int(input())
    at = list(map(int, input().split()))
    c = float('inf')
    at.sort()
    for i in range(1, a):
        c = min(c, at[i] - at[i - 1])
    print(c)
