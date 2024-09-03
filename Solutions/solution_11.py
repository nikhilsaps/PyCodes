
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

def main():
    n= [x for x in input("enter the cs binary : ").split(",")]
    
    for binary in n :
        sum=0
        count=0
        for digit in binary[::-1] :
            sum= sum+int(digit)*2**count
            count+=1
        if sum%5==0:
            print (binary, sum )


if __name__=="__main__":
    main()