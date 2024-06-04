# Problem: B - Different String - https://codeforces.com/gym/527307/problem/B

from collections import Counter
t = int(input())

for _ in range(t):
    s = input()

    c = Counter(s)

    if len(c.keys()) > 1:
        print("YES")
        print(s[1::] + s[0])
    else:
        print("NO")
