from collections import Counter

x = list(input())
y = list(input())
z = list(input())


x_s = Counter(x)
y_s = Counter(y)
z_s = Counter(z)
diagonal1 = Counter([x[0], y[1], z[2]])
diagonal2 = Counter([x[2], y[1], z[0]])


ind_heads = set()
heads = set()

for val, freq in diagonal1.items():
    if freq == 3:
        ind_heads.add(val)
    elif freq == 2:
        heads.add(val)

for val, freq in diagonal2.items():
    if freq == 3:
        ind_heads.add(val)
    elif freq == 2:
        heads.add(val)

for val, freq in x_s.items():
    if freq == 3:
        ind_heads.add(val)
    elif freq == 2:
        heads.add(val)

for val, freq in y_s.items():
    if freq == 3:
        ind_heads.add(val)
    elif freq == 2:
        heads.add(val)

for val, freq in z_s.items():
    if freq == 3:
        ind_heads.add(val)
    elif freq == 2:
        heads.add(val)

print(len(ind_heads))
print(len(heads))
