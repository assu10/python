## 반복문으로 회문 판별

# word = input('input a word.')
#
# is_palindrome = True
#
# for i in range(len(word) // 2):     # // : 버림나눗셈 (소수점 이하 버림)
#     if word[i] != word[-1-i]:
#         is_palindrome = False
#         break
#
# print(is_palindrome)


## 시퀀스 뒤집기로 회문 판별

# word = input('input a word.')
# print(word == word[::-1])       # [시작:끝:증가폭]


## 리스트와 reversed 로 회문 판별

# word = 'level'
# print(list(reversed(word)) == list(word))


## join 메서드와 reversed 사용하여 회문 판별

word = 'level'
print(word == ''.join(reversed(word)))