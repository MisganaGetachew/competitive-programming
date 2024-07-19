# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
nums = list(map(int, input().split()))

pos_sum = 0
small_odd = float('inf')

for num in nums:
    if num >= 0:
        pos_sum += num
    if abs(num) % 2 == 1:
        small_odd = min(small_odd, abs(num))

if pos_sum % 2 == 1:
    print(pos_sum)
else:
    print(pos_sum - small_odd)
