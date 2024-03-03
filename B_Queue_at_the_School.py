n, t = map(int, input().split())
s = list(input())

for j in range(t):
    n = 0

    while n + 1 < len(s):
        if s[n] == 'B':
            if s[n + 1] == 'G':
                s[n], s[n + 1] = s[n + 1], s[n]
                n += 2
        n += 1

print("".join(s))


"""




"""
