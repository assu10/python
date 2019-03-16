with open('words.txt', 'r') as file:
    words = file.readlines()

#print(words)    # ['apache\n', 'decal\n', 'did\n', 'neep\n', 'noon\n', 'refer\n', 'river']

for word in words:
    word = word.strip('\n')
    if word == word[::-1]:
        print(word)
