# Problem: A. Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    n = int(input())
    mask = 0
    for i in range(31):
        if (n >> i) & 1:
            mask = 1 << i
            break
    if bin(n).count("1") == 1:
        for i in range(31):
            if not (n >> i) & 1:
                mask |= 1 << i
                break

    print(mask)
