# n = int(input())
# text = input()

n = 7
text = 'Python is a programming language that lets you work quickly'
words = text.split()

if len(words) < n:
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)
