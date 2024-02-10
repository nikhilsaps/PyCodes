# Level 2
# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the
# following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9


data =list(input("enter the number"))
lower=0
upper=0
for x in data:
    if x.islower():
        lower+=1
    elif x.isupper():
        upper+=1
    else :
        pass


print(f"lower {lower} and upper :{upper}")

#
# Solution: python
# s = input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s: 
#     if c.isupper():
#         d["UPPER CASE"+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"]) print("LOWERCASE", d["LOWER CASE"])