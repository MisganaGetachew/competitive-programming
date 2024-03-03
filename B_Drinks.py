
od = float(input())
p = list(map(float, input().split()))


p = [x / 100 for x in p]


average_percentage = (sum(p) / od) * 100

print("{:.12f}".format(average_percentage))
