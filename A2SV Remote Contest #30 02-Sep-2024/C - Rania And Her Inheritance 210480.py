# Problem: C - Rania And Her Inheritance - https://codeforces.com/gym/545837/problem/C

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())

experts = []
for i in range(1, n + 1):
    experts.append(data[i])

rivalries = []
for i in range(n + 1, n + 1 + m):
    a, b = data[i].split()
    rivalries.append((a, b))

rivalry_pairs = set(rivalries)

best_subset = []

for i in range(1, 1 << n):
    subset = [experts[j] for j in range(n) if (i & (1 << j))]
    subset_set = set(subset)

    valid = True
    for (a, b) in rivalry_pairs:
        if a in subset_set and b in subset_set:
            valid = False
            break

    if valid and len(subset) > len(best_subset):
        best_subset = subset

print(len(best_subset))
for name in sorted(best_subset):
    print(name)
