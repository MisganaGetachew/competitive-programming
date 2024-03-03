def find_four_values(n, target, values):
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if values[i] + values[j] + values[k] + values[l] == target:
                        return [i + 1, j + 1, k + 1, l + 1]
    return "IMPOSSIBLE"


# Input reading
n, target = map(int, input().split())
values = list(map(int, input().split()))

# Find and print the result
result = find_four_values(n, target, values)
print(*result)
