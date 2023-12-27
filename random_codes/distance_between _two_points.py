# to fidn  the distance between 2 point  we need  4 coordinates
import math

x1= int(input("enter the  value of x1"))
x2= int(input("enter the  value of x2"))
y1= int(input("enter the  value of x3"))
y2= int(input("enter the  value of x4"))

distance = math.sqrt(((x1**2)-(x2**2))+((y1**2)-(y2**2)))
print(distance)