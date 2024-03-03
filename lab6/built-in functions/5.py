def all_elements_true():
    t = tuple(map(bool, input().split()))
    return all(t)


print(all_elements_true())

#or

def all_elements_true():
    t = tuple(map(lambda x: x == 'True', input().split()))
    return all(t)


print(all_elements_true())
