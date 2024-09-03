# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


n=  input("enter the data :")
countup=0
countdown=0
for x in n:
    if x.isupper() : 
        countup+=1
    if x.islower():
        countdown+=1
print(countup)
print(countdown)