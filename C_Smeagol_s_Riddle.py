from collections import Counter
n = int(input())

for _ in range(n):
    s = input()
    count = 0
    length = len(s)

    if length % 2 != 0:
        right = length // 2 - 1
        i = length // 2 + 1
        while i < length and right >= 0:
            if s[i] != s[right]:
                count += 1
            right -= 1
            i += 1
    else:
        right = length // 2 - 1
        i = length // 2

        while i < length and right >= 0:
            if s[i] != s[right]:
                count += 1
            right -= 1
            i += 1

    print(count)
