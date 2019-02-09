# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep='', end=' ')
#
#     print('i:', i, '\\n', sep='')

# for i in range(3):
#     for j in range(7):
#         print('*', end='')
#     print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()