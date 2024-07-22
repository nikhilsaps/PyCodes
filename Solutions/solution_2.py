# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def main():
    fact=1
    x=int(input("enter the number :")) 

    for  y in range(1,x+1):
        fact=fact*y
    print(fact)



if __name__ =="__main__":
    main()