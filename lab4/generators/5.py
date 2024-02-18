def generate_return(n):
    while n >= 0:
        yield n 
        n -=1

for num in generate_return(int(input())):
    print(num)    

#or

def generate_return(n):
    for i in range(n, -1, -1):
        yield i

for num in generate_return(int(input())):
    print(num)