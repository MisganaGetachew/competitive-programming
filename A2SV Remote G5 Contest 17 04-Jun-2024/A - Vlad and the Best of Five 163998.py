# Problem: A - Vlad and the Best of Five - https://codeforces.com/gym/527307/problem/A

t = int(input())

for _ in range(t):
    s = input()
    A = 0
    B = 0

    for i in s:
        if i == "A":
            A += 1
        else:
            B += 1
    if A > B:
        print("A")
    else:
        print("B")
