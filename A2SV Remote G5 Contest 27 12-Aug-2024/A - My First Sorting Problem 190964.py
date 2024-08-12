# Problem: A - My First Sorting Problem - https://codeforces.com/gym/541399/problem/A

t = int(input())

for _ in range(t):
     num1, num2 = map(int, input().split())
    #  print("working")
     print (min(num1, num2), max(num1, num2))