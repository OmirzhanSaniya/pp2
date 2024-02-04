import itertools

def permutation(str):
    permutations = itertools.permutations(str)
    for permutation in permutations:
        print(''.join(permutation))

permutation(input())