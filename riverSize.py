matrix = [
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]
]

d_visited = {}
def check_valid(i,j, matrix):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or d_visited.get((i,j)) == 1:
        return False
    else:
        return True

def possible_move(i, j, matrix):
    ans = []
    if check_valid(i, j-1, matrix) and matrix[i][j-1] == 1:
        ans.append((i, j-1))
    if check_valid(i, j+1, matrix) and matrix[i][j+1] == 1:
        ans.append((i, j+1))
    if check_valid(i-1, j, matrix) and matrix[i-1][j] == 1:
        ans.append((i-1, j))
    if check_valid(i+1, j, matrix) and matrix[i+1][j] == 1:
        ans.append((i+1, j))
    return ans

def riverSize(matrix):
    ans = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(i,j)
            if d_visited.get((i,j)) == None:
                d_visited[(i,j)] = 1
            else:
                continue

            if matrix[i][j] == 1:
                possible_ = [(i,j)]
                size = 0
                while possible_:
                    first = possible_.pop()
                    size += 1
                    d_visited[(first[0], first[1])] = 1
                    possible_ += possible_move(first[0], first[1], matrix)
                ans.append(size)

    return ans

print(riverSize(matrix))
