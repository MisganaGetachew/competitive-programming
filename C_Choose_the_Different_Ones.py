test = int(input())

for _ in range(test):

    len_a, len_b, k = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    count_a = 0
    count_b = 0
    for i in range(k+1):
        if i in a:
            count_a += 1
        if i in b:
            count_b += 1

    if count_b + count_a >= k and count_a == k/2:
        print("YES")
    else:
        print("NO")
