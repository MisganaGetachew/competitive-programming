# Problem: B - New Year Transportation - https://codeforces.com/gym/532332/problem/B


n, t = map(int, input().strip().split())
portals = list(map(int, input().strip().split()))


cur = 1

while cur < t:
    cur += portals[cur - 1]

# Check if we have reached the target cell
if cur == t:
    print("YES")
else:
    print("NO")
