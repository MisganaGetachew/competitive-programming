# Problem: B - Powering the Hero (easy version) - https://codeforces.com/gym/541399/problem/B

import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    cards = map(int, input().split())
    bonuses = []
    power = 0
    for num in cards:
        if num != 0:
            heapq.heappush(bonuses, -num)
        else:
            if bonuses:
                power += -heapq.heappop(bonuses)
    print(power)
