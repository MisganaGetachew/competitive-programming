r = input()
count = 0
temp = 0

for char in r:
    if char == "O":
        temp += 1
        count = max(count, temp)
    else:
        temp = 0

print(count)
