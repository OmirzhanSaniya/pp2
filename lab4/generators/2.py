def generate_even(n):
    for i in range(0, n):
        if i % 2 == 0 :
            yield i

even_numbers = ", ".join(str(even) for even in generate_even(int(input())))

print(even_numbers)