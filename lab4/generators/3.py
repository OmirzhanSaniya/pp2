def generate_3_4(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for thfo in generate_3_4(int(input())):
    print(thfo)            

num3_4 = ", ".join(str(thfo) for thfo in generate_3_4(int(input())))

print(num3_4)