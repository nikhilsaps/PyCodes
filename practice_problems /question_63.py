# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by
# console.
# Example: If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# Hints: We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use string.join() to join
# a list of strings.

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
#
fibos=[]
# num = int(input("enter the  number"))
# for x in range(num+1):
#     finos.append(fibo(x))
fibos =[fibo(x) for x in range(int(input("enter the number"))+1)]

print(fibos)