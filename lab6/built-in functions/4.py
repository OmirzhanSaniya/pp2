import math

def delayed_square_root(num, delay):
    for _ in range(delay * 10000):
        pass
    return math.sqrt(num)

num = int(input())
delay = int(input())
result = delayed_square_root(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")
