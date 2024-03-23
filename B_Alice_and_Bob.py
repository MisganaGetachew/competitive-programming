t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())
    i = 0
    j = 0
    st = ""
    c_a = 0
    c_b = 0
    while i < n and j < m:
        if a[i] < b[j] and c_a < k:
            st += a[i]
            c_a += 1
            c_b = 0
            i += 1
        elif a[i] > b[j] and c_b < k:
            st += b[j]
            c_b += 1
            c_a = 0
            j += 1
        else:
            if c_a < k:
                st += a[i]
                c_a += 1
                c_b = 0
                i += 1
            elif c_b < k:
                st += b[j]
                c_b += 1
                c_a = 0
                j += 1

    print(st)
