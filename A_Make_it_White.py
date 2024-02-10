testcase = int(input())

for i in range(testcase):

    n = int(input())
    s = input()
    pos = []
    for i in range(n):
        if s[i] == "B":
            pos.append(i)
    print(max(pos) - min(pos) + 1)
