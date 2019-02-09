k = int(input())

for i in range(k):
    for j in range(1, k*2):
        if (k-j) > i or (j-k) > i:
            print('-', end='')
        else:
            print('*', end='')

    print()

# height = 3
# for i in range(height):
#     for j in reversed(range(height)):
#         if j > i:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     for j in range(height):
#         if j < i:
#             print('*', end='')
#     print()