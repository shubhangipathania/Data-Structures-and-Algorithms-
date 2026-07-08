#Given an m x n integer matrix matrix, if an element is 0, 
# set its entire row and column to 0's.
#You must do it in place.
#optimal 
def set_matrix_zero(matrix):
    rows= len(matrix)
    cols= len(matrix[0])
    rowstrack = [0 for _ in range(0,rows)]
    colstrack = [0 for _ in range(0,cols)]
    for i in range(0,rows):
        for j in range(0,cols):
            if (matrix[i][j] == 0):
                rowstrack[i] = -1
                colstrack[j] = -1

    for i in range(0,rows):
        for j in range(0,cols):
            if(rowstrack[i] == -1 or colstrack[j] == -1):
                matrix[i][j] = 0 

    return matrix

matrix = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
output = set_matrix_zero(matrix)
print(output)