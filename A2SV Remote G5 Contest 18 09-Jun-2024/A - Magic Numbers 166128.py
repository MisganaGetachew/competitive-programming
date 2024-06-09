# Problem: A - Magic Numbers - https://codeforces.com/gym/528793/problem/A

nums = (input())
res = True
i = 0
while i < len(nums):
    if nums[i:i+3] == "144":
        i += 3
    elif nums[i:i+2] == "14":
        i += 2
    elif nums[i] == "1":
        i += 1
    else:
        res = False
        break

if res:
    print("YES")
else:
    print("NO")
