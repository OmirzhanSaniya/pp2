def convert(grams):
    return 28.3495231 * grams

print(convert(int(input())))



def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return False

x, y = solve(int(input()), int(input()))
print(x, y)



import itertools

def permutation(str):
    permutations = itertools.permutations(str)
    for permutation in permutations:
        print(''.join(permutation))

permutation(input())