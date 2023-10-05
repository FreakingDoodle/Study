
#транспонирование матрицы
F = [[2, 3],
[5, 7],
[8, 1]]

F_T = [[0, 0, 0],
[0, 0, 0]]

for q in range(len(F)):
    for w in range(len(F[0])):
        F_T[w][q] = F[q][w]
for q in F_T:
    print(q)
#умножение матриц
a = [[1, 1, 0],
     [1, 0, 2]]
     
b = [[1, 0, 2, 1],
     [2, 1, 2, 0],
     [1, 1, 0, 3]]
m = len(a)                                            
n = len(b)                                            
k = len(b[0])
c = [[None for __ in range(k)] for __ in range(m)]   
for i in range(m):
    for j in range(k):       
        c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))
  
print(c)
# определение ранга
def rank_of_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rank = min(rows, cols)
    for row in range(rank):
        if matrix[row][row] != 0:
            for i in range(row + 1, rows):
                multiplier = matrix[i][row] / matrix[row][row]
                for j in range(row, cols):
                    matrix[i][j] -= multiplier * matrix[row][j]
        else:
            reduce_rank = True
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    matrix[row], matrix[i] = matrix[i], matrix[row]
                    reduce_rank = False
                    break
            if reduce_rank:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][cols - 1]  
    return rank
matrix = [[10, 20, 10], [-20, -30, 10], [30, 50, 0]]
print("Матрица:")
for row in matrix:
    print(row)

print("Ранг матрицы:", rank_of_matrix(matrix))
