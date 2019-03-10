from pprint import pprint

## for 반복문으로 배열 출력하기

# a = [[10,20], [30,40], [50,60]]
#
# for x,y in a:
#     print(x,y)



## while 반복문으로 배열 출력하기

# a = [[10,20], [30,40], [50,60]]
#
# i = 0;
# while i < len(a):
#     x,y = a[i]
#     print(x,y)
#     i += 1



## for 반복문으로 2차원 리스트 만들기

# a = []
#
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
#
# print(a)



## 리스트 표현식으로 2차원 리스트 만들기

# a = [[0 for j in range(2)] for i in range(3)]
# print(a)    # [[0, 0], [0, 0], [0, 0]]
#
# b = [[0]*2 for i in range(3)]
# print(b)    # [[0, 0], [0, 0], [0, 0]]



## jagged list (톱니형 리스트) 만들기

# a = [3,1,3,2,5]
# b = []
#
# for i in a:
#     line = []
#     for j in range(i):
#         line.append(0)
#     b.append(line)
#
# print(b)    # [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]
#
#
# c = [[0] * i for i in [3,1,3,2,5]]
# print(c)    # [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]



## sorted로 2차원 리스트 정렬

# students = [
#     ['john', 'C', 19],
#     ['maria', 'A', 25],
#     ['andrew', 'B', 7]
# ]
#
# print(sorted(students, key=lambda studentd: studentd[1]))                   # [['maria', 'A', 25], ['andrew', 'B', 7], ['john', 'C', 19]]
# print(sorted(students, key=lambda studentd: studentd[1], reverse=True))     # [['john', 'C', 19], ['andrew', 'B', 7], ['maria', 'A', 25]]
# print(sorted(students, key=lambda studentd: studentd[2]))                   # [['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]]
# print(sorted(students, key=lambda studentd: studentd[2], reverse=True))     # [['maria', 'A', 25], ['john', 'C', 19], ['andrew', 'B', 7]]



# 2차원 리스트의 할당과 복사

# a = [[10,20], [30,40]]
# b = a
# b[0][0] = 500
# print(a)        # [[500, 20], [30, 40]]
# print(b)        # [[500, 20], [30, 40]]
#
# c = [[10,20], [30,40]]
# d = c.copy()
# d[0][0] = 500
# print(c)        # [[500, 20], [30, 40]]
# print(d)        # [[500, 20], [30, 40]]



## deepcopy

# import copy
#
# a = [[10,20], [30,40]]
# b = copy.deepcopy(a)
# b[0][0] = 500
# print(a)        # [[10, 20], [30, 40]]
# print(b)        # [[500, 20], [30, 40]]


a = [[0,0,0]*3]
print(a)
