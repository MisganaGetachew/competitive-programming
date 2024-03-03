# Read the number of requests
n = int(input())

file_counts = {}


for _ in range(n):
    name = input()

    if name not in file_counts:
        file_counts[name] = 1
        print("OK")
    else:

        while f"{name}{file_counts[name]}" in file_counts:
            file_counts[name] += 1

        file_counts[f"{name}{file_counts[name]}"] = 1
        print(f"{name}{file_counts[name]}")
