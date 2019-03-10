input = "51900;83000;158000;367500;250000;59200;128500;1304000"

arrInput = input.split(';')
arrInput = list(map(int, arrInput))
arrInput.sort(reverse=True)

for i in range(len(arrInput)):
    print('{:>9,}'.format(arrInput[i]))
