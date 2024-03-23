n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

left = 0
right = 0
ans = []
while left < len(l1) and right < len(l2):
    if l1[left] <= l2[right]:
        ans.append(l1[left])
        left += 1
    else:
        ans.append(l2[right])
        right += 1
ans.extend(l1[left:])
ans.extend(l2[right:])
print(*ans)
