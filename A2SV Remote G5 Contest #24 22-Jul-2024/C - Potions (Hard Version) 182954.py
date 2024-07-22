# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

from heapq import heappush, heappop
n = int(input())
lst = map(int, input().split())
heap = []
health = 0
for num in lst:
    health += num
    heappush(heap, num)
    if health < 0:
        health -= heappop(heap)
print(len(heap))
