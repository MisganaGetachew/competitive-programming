# Problem: C - Parity Sort - https://codeforces.com/gym/527307/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    newarr = arr.copy()
    newarr.sort()
    cnt = 0
    for i in range(n):
        if (newarr[i] % 2 == 0 and arr[i] % 2 == 0) or (newarr[i] % 2 != 0 and arr[i] % 2 != 0):
            cnt += 1

    if cnt == n:
        print("YES")

    else:
        print("NO")
