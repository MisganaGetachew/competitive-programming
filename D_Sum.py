t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    left = 0
    right = n - k
    s = sum(nums[left:right])

    while left < n and right + 1 < n:
        s += nums[right + 1]
        s -= nums[left]
        right += 1
        ans = sum(nums[left:right], s)
    print(ans)
