# Problem: A - Odd One Out - https://codeforces.com/gym/525787/problem/A

from collections import Counter
t = int(input())

for _ in range(t):
    c = Counter(list(map(int, input().split())))

    for val, freq in c.items():
        if freq == 1:
            print(val)
            break
