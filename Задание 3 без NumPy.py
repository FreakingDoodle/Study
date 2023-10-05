matrix = [
    [-1,  2, -5],
    [ 3,  4,  1],
    [ 0,  1,  2]
]
 
matrix = [[sum(e1 * e2 for e1, e2 in zip(row, column))
           for column in zip(*matrix)] for row in matrix]
print(*matrix, sep="\n")
