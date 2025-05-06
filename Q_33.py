# Program to transpose a matrix
#  solution using for loop

matrix = [[1,4,7],
          [2,5,8],
          [3,6,9]]

transpose = [[0,0,0],
             [0,0,0],
             [0,0,0]]

for i in range(len(matrix)):
    for j in range(len(matrix[2])):
        transpose[j][i] = matrix[i][j]

for t in transpose:
    print(t)        

