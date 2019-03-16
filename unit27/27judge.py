with open('27judge_txt.txt', 'r') as file:
    line = file.readline()

words = line.split()
for word in words:
    if 'c' in word:
        print(word.strip('.,'))