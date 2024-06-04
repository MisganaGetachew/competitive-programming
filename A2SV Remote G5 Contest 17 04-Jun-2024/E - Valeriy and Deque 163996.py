# Problem: E - Valeriy and Deque - https://codeforces.com/gym/527307/problem/E

from collections import deque
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
q = int(data[1])
arr = list(map(int, data[2:n+2]))
queries = list(map(int, data[n+2:n+2+q]))


r = deque(arr)


operations = []
for _ in range(n-1):
    a = r.popleft()
    b = r.popleft()
    operations.append((a, b))
    if a > b:
        r.appendleft(a)
        r.append(b)
    else:
        r.appendleft(b)
        r.append(a)

fixed_state = list(r)


results = []
for m in queries:
    if m <= n-1:
        results.append(operations[m-1])
    else:
        index = (m - n) % (n - 1) + 1
        results.append((fixed_state[0], fixed_state[index]))


for result in results:
    print(result[0], result[1])
