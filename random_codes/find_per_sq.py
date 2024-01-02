import math
from math import sqrt
def sqrt(n):
    return (math.sqrt(n))

a=int(input("enter the number"))
ans =sqrt(a)
if int(ans)**2==a:
    print("perfect square")
else:
    print("not perfect square")