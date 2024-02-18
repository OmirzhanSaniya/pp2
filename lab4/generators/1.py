squares_generator = (i * i for i in range(int(input())))
for square in squares_generator:
    print(square)

#or

def generate_squares(n):
    value = 0
    while value < n:
        yield value **2
        value += 1

for square in generate_squares(int(input())):
    print(square)

