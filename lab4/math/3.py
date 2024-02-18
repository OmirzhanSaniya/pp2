import math

sides = int(input())
lengthside = int(input())

pi = math.pi

areapolygon = int((sides * lengthside**2)/(4*(math.tan(pi/sides))))

print(areapolygon)