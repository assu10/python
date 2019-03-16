# file = open('hello.txt', 'w')
# file.write('Hello, world!')
# file.close()


# file = open('hello.txt', 'r')
# s = file.read()
# print(s)


# with open('hello.txt', 'r') as file:
#     s = file.read()
#     print(s)


# with open('hello.txt', 'w') as file:
#     for i in range(3):
#         file.write('Hello, world! {0}\n'.format(i))


# lines = ['안녕하세요\n', '파이썬']
# with open('hello.txt', 'w') as file:
#     file.writelines(lines)


# with open('hello.txt', 'r') as file:
#     lines = file.readlines()
# print(lines)


## while 로 파일 내용 줄단위로 읽기

# with open('hello.txt', 'r') as file:
#     line = None
#     while line != '':
#         line = file.readline()
#         print(line.strip('\n'))


## for 반복문으로 파일 내용 줄단위로 읽기

# with open('hello.txt', 'r') as file:
#     for line in file:
#         print(line.strip('\n'))


## pickling

# import pickle
#
# name = 'james'
# age = 36
# address = '경기도 수원'
# scores = {'korean':90, 'english':100}
#
# with open('james.p', 'wb') as file:     # binary mode로 읽기
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)


## unpickling

# import pickle
#
# with open('james.p', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#
#     print(name)
#     print(age)
#     print(address)
#     print(scores)

with open('hello.txt', 'a+') as file:
     for i in range(3):
         file.write('Hesllo, worsld! {0}\n'.format(i))


# with open('hello.txt', 'w+') as file:
#     line = file.readlines()
#     print(line)
