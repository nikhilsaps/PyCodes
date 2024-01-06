# this is the  code to better under stand the map function
from functools import reduce


def lul(x,y):
    return x+y
l=[1,2,3]
print(reduce(lul,l))

