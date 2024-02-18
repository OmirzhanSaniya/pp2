def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2


for square in squares(int(input()), int(input())):
    print(square)