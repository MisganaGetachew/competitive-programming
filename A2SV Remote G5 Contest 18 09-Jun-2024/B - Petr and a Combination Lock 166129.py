# Problem: B - Petr and a Combination Lock - https://codeforces.com/gym/528793/problem/B

n = int(input())
arr = [int(input()) for _ in range(n)]


def rec(idx, run_sum):
    if idx == n:
        return run_sum % 360 == 0

    return rec(idx + 1, run_sum + arr[idx]) or rec(idx + 1, run_sum - arr[idx])


print("YES" if rec(0, 0) else "NO")



