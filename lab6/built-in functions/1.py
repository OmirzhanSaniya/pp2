from functools import reduce

numbers = input()

list = [int(num) for num in numbers.split()]

result = reduce(lambda x, y: x * y, list)

print(result)

#or

numbers = input()

list = [int(num) for num in numbers.split()]

print(eval("*".join(str(x) for x in list)))
