n = int(input())

for _ in range(n):
    s = input()
    j = 0
    c = "codeforces"
    count = 0
    for i in range(10):
        if s[i] == c[j]:
            j += 1
        else:
            count += 1
            j += 1
    print(count)