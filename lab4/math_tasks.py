#1
import math
d =int(input())
r=math.radians(d)
print("input degree",d)
print ("output radian",r)

#2
import math
a=int(input())
b=int(input())
h=int(input())
s=(a+b)/2 * h
print (s)

#3
import math

def regular_polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

num_sides = int(input())
side_length = float(input())

area = regular_polygon_area(num_sides, side_length)
print(area)

#4
a=int(input())
b=int(input())
def area(a,b):
    return float(a*b)

print (area(a,b))
