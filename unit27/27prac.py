with open('hello.txt', 'r') as filed:
    count = 0
    words = filed.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1
print(count)