# Problem: B - Rudolph and Cut the Rope  - https://codeforces.com/gym/525787/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    ct = 0
    for i in range(n):
        a, b = list(map(int, input().split()))
        if a > b:
            ct += 1
    print(ct)
