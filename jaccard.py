import numpy as np

a = []
b = []

mat = np.array([[1,0,0,0,1,0,0,1,1,0],[0,0,0,0,0,0,0,1,0,1],[1,0,1,1,1,0,1,1,0,0],[1,1,1,1,1,1,0,0,0,1]])
jaccard_matrix = mat

print("Original Matrix:")
print(mat)
print('\n\n\n')


def jaccard(row1, row2):
    iter = 0
    j01 = 0
    j10 = 0
    j11 = 0
    while iter < len(row1):
        x = row1[iter]
        y = row2[iter]
        if x == 0 and y == 1:
            j01 += 1
        elif x == 1 and y == 0:
            j10 += 1
        elif x == 1 and y == 1:
            j11 += 1
        iter += 1
    jc = j11 / (j01 + j10 + j11)
    return jc


row_iter = 0
col_iter = 1
while row_iter < len(mat):
    col_iter = 0
    while col_iter < len(mat):
        row1 = mat[row_iter,:]
        row2 = mat[col_iter,:]
        jc = jaccard(row1,row2)
        print(str(row_iter) + ' ' + str(col_iter) + ' ' + str(jc))
        jaccard_matrix[row_iter,col_iter] = jc
        col_iter += 1
    row_iter += 1







