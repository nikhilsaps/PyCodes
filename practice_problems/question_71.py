# Please write a program to print the running time of execution of “1+1” for 100 times.
from timeit import Timer
import checking

t= Timer(checking.fun)



print(t.timeit())