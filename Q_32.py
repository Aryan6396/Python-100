# Program to add two matrices

A = [[1,5,7],
     [3,9,8],
     [8,8,1]]

B = [[5,7,4],
     [3,6,9],
     [2,0,2]]

res = [[0,0,0],
       [0,0,0],
       [0,0,0]]

# print(len(A[0]))

for i in range(len(B)):
    for j in range(len(B[0])):
        res[i][j] = A[i][j] + B[i][j]

for r in res:
    print(r)