# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

t = int(input())
for _ in range(t):
     n = int(input())
     arr = list(map(int, input().split()))
     ans = max(arr)
     for i in range(n-1):
          temp = max(arr[i], arr[i+1])
          ans = min(ans, temp)
     print(ans - 1)
 