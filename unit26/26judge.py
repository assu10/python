a,b = map(int, input().split())

a_set = {i for i in range(1,a+1) if a%i == 0}
b_set = {i for i in range(1,b+1) if b%i == 0}

divisor = a_set & b_set

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)