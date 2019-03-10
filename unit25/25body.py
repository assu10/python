x = {'a':10, 'b':20, 'c':30}

# for key, value in x.items():
#     print(key, value)


# for key in x.keys():
#     print(key)


# for value in x.values():
#     print(value)

keys = ['a', 'b', 'c', 'd']

# {'a': None, 'b': None, 'c': None, 'd': None}
# x = {key:value for key,value in dict.fromkeys(keys).items()}
# print(x)


# {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# x = {key:0 for key in dict.fromkeys(keys)}
# print(x)


# {10: 0, 20: 0, 30: 0}
# x = {value:0 for value in {'a':10, 'b':20, 'c':30}.values()}
# print(x)


# {10: 'a', 20: 'b', 30: 'c'}
# x = {value:key for key,value in {'a':10, 'b':20, 'c':30}.items()}
# print(x)


# {'a': 10, 'c': 30}
# x = {'a':10, 'b':20, 'c':30}
# x = {key:value for key,value in x.items() if value != 20}
# print(x)


