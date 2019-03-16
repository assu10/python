## 반복문으로 N-gram 출력

# text = 'Hello'
#
# # 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복
# for i in range(len(text)-1):
#     print(text[i], text[i+1], sep='')


## 단어 N-gram 출력

# text = 'this is python script'
# words = text.split()
#
# for i in range(len(words)-1):
#     print(words[i], words[i+1])


## zip 으로 2-gram 만들기(문자)

# text = 'hello'
#
# two_gram = zip(text, text[1:])
# print(list(two_gram))       # [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]
#
# for i in two_gram:
#     print(i[0], i[1], sep='')


## zip 으로 2-gram 만들기(단어)

# text = 'this is python script'
# words = text.split()
# print(list(zip(words, words[1:])))      # [('this', 'is'), ('is', 'python'), ('python', 'script')]


## zip과 리스트 표현식으로 3-gram

text = 'hello'
step_1 = [text[i:] for i in range(3)]
print(step_1)       # ['hello', 'ello', 'llo']

step_2 = list(zip(step_1))
print(step_2)       # [('hello',), ('ello',), ('llo',)]

step_2_2 = list(zip(*step_1))
print(step_2_2)     # [('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]

step_1_1 = list(zip(*[text[i:] for i in range(3)]))
print(step_1_1)     # [('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]