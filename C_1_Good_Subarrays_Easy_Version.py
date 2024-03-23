t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # 1 2 3 1 1 2
    l = ans = 0
    for r in range(n):
        while arr[r] < r - l + 1:
            ans += (r - l)
            l += 1
    N = n - l
    print(ans + N * (N + 1) // 2)
