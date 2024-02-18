import math

x = int(input())

print(math.radians(x))

#or

x = int(input())

y = math.pi

r = (y*x)/180

r = format(r, '.6f')

print(r)