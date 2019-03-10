# col 가로, row 세로
col, row = map(int, input().split())

# 리스트로 인풋 받기
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "*":     # 현재 위치가 지뢰인 경우
            continue
        else:
            matrix[i][j] = 0
            for y in range(i-1, i+2):       # 세로
                for x in range(j-1, j+2):   # 가로
                    if y < 0 or x < 0 or y >= row or x >= col:
                        continue
                    else:
                        if matrix[y][x] == "*":
                            if matrix[i][j] == ".":
                                matrix[i][j] = 1
                            else:
                                matrix[i][j] += 1


print(matrix)