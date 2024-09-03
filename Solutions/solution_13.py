# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# # DIGITS 3


n = input("enter the data")
countnum=0
countal=0
for x in n :
    if(x.isnumeric()):
        countnum+=1
    if(x.isalpha()):
        countal+=1
print(countnum)
print(countal)