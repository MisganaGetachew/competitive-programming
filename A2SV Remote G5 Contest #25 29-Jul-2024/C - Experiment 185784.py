# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C

n = int(input())
events = []

for _ in range(n):
    si, ti, bi = map(int, input().split())
    events.append((si, bi))
    events.append((ti + 1, -bi))
events.sort()

current_rooms = 0
max_rooms = 0

for time, change in events:
    current_rooms += change
    if current_rooms > max_rooms:
        max_rooms = current_rooms

print(max_rooms)
