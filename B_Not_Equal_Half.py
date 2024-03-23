n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if sum(arr[:n]) != sum(arr[n:2*n]):
    ans = " ".join(map(str, arr[:n] + arr[n:2*n]))
    print(ans)
else:
    print(-1)
