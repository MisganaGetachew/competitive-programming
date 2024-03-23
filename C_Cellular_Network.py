n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

r = 0
city_ptr = 0
tower_ptr = 0

while city_ptr < n:
    while tower_ptr < m - 1 and abs(cities[city_ptr] - towers[tower_ptr + 1]) <= abs(cities[city_ptr] - towers[tower_ptr]):
        tower_ptr += 1

    r = max(r, abs(cities[city_ptr] - towers[tower_ptr]))
    city_ptr += 1

print(r)
