# Level 1
# Question: Write a program which can compute the factorial of a given numbers.
# sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def main():
    num=int(input("enter the number"))
    fact=1
    for i in range(1,num+1):
        fact =fact *i

    print(fact)


if __name__=="__main__":
    main()


# Solution: ```python
# def fact(x):
#   if x == 0:
#       return 1
#   return x * fact(x - 1)
# x=int(input())
# print(fact(x)) ```