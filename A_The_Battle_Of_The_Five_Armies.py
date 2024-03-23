sol = list(map(int, input().split()))
cap = list(map(int, input().split()))
b = 0
l = 0
for i in range(3):
    b += sol[i] * cap[i]
for i in range(3, 5):
    l += sol[i] * cap[i]

if b > l:
    print("WIN")
elif l > b:
    print("LOSE")
else:
    print("DRAW")
