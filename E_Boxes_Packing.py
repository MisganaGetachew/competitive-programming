n = int(input())
size = list(map(int, input().split()))
size.sort()
count = [0]*5001
visible = 0
for i in range(n):
    if count[size[i]-1] > 0:
        count[size[i]-1] -= 1
    else:
        visible += 1
    count[size[i]] += 1
print(visible)
