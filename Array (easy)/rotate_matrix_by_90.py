#You are given an n x n 2D matrix representing an image, 
#rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, 
# which means you have to modify the input 2D matrix directly. 
#DO NOT allocate another 2D matrix and do the rotation.
#Brute Force
def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            result[j][(n-1)-i] = matrix[i][j]

    return result


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
output = rotate_matrix(matrix)
print(output)
#optimal
def rotate_matrix_by_ninety(matrix2):
    n = len(matrix2)
    for i in range(0,n-1):
        for j in range(i+1,n):
            matrix2[i][j],matrix2[j][i] = matrix2[j][i],matrix2[i][j]

    for i in range(0,n):
        matrix2[i].reverse()

    return matrix2

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
output2 = rotate_matrix_by_ninety(matrix2)
print(output2)