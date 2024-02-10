# Please generate a random float where the value is between 10 and 100 using Python math module.
import math
import random
#
# a=random.randint(1,100)
#
# random_float =math.sqrt(a)
# print(random_float)

# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.


print(random.sample([x*1.1 for x in range(10)],5))