t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    frodo_list = list(map(int, input().split()))
    sam_list = list(map(int, input().split()))
    
    frodo_list.sort()
    sam_list.sort(reversed=True)
    l = 0
    r1 = n-1
    r2 = m-1
    ans = []
    while(l<=r1):
        if abs(frodo_list[l]-sam_list[r1]) > abs(frodo_list[l]-sam_list[r2]):














# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     frodo_list = list(map(int, input().split()))
#     sam_list = list(map(int, input().split()))

#     frodo_list.sort()  
#     sam_list.sort(reverse=True)  

#     max_difference = 0

#     for i in range(n // 2):
#         difference = sam_list[i] - frodo_list[i]
#         max_difference += difference

    
#     print(max_difference * 2)
