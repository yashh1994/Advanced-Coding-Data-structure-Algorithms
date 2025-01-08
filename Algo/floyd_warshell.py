
def shortest_distance(matrix):
    n = len(matrix)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != -1 and matrix[k][j] != -1:
                    if matrix[i][j] == -1:
                        matrix[i][j] = matrix[i][k]+matrix[k][j]
                    else:
                        matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
    return matrix


matrix = [
    [0, 3, -1, 7],
    [8, 0, 2, -1],
    [5, -1, 0, 1],
    [2, -1, -1, 0]
]

result = shortest_distance(matrix=matrix)

for row in result:
    print(row)