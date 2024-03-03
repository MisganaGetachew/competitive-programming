n = int(input())

nums = list(map(int, input().split()))

less = []
great = []
equal = []
count = 0
for i in nums:
    if i < 0:
        less.append(i)
    elif i > 0:
        great.append(i)
    else:
        equal.append(i)

if great:
    pass
else:
    great.append(less.pop())
    great.append(less.pop())

if len(less) % 2 == 0:
    less.append(great.pop())

# for i in range(3):
less = [str(i) for i in less]
great = [str(i) for i in great]
equal = [str(i) for i in equal]


print(len(less), " ".join(less))
print(len(great), " ".join(great))
print(len(equal), " ".join(equal))
# print(great)

# print(len(great), map(str, less)"".join(great))
# # print(len(equal), "".join(equal))
