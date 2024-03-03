matrix = [input().split(),
          input().split(),
          input().split(),
          input().split(),
          input().split()
          ]
rows = 0
cols = 0
for row in range(5):
    for col in range(5):
        if str(matrix[row][col]) == "1":
            rows = row
            cols = col
            break


opp = abs(2 - rows) + abs(2 - cols)


# while rows != 2 and cols != 2:

#     if rows > 2:
#         rows -= 1
#         opp += 1

#     elif cols > 2:
#         cols -= 1
#         opp += 1

#     elif rows < 2:
#         rows += 1
#         opp += 1

#     elif cols < 2:
#         cols += 1
#         opp += 1

print(opp)
# print(cols)
