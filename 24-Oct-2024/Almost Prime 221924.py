# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n=int(input())
a=[0]*(n+1)
for i in range(2,n):
	if a[i]==0:
		for j in range(2*i,n+1,i):
			a[j]+=1
print(a.count(2))