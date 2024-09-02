# Problem: A - Weird Balance - https://codeforces.com/gym/545837/problem/A

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)

    if len(count) == 1:
        if  (len(a) > 1 or not a[0]):
            print("NO")
        else:
            print("YES")
            print(*a)

        continue

    a.sort(reverse=True)

    if a[0] == a[1]:
        for i in range(2, n):
            if a[i] != a[1]:
                a[i], a[1] = a[1], a[i]
                break

    if a[0] == a[1]:
        print("NO")
    else:
        print("YES")
        print(*a)