# Level 2
# Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is
# supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

data =list(input("enter the data "))
num = 0
letter = 0
for  x in data:
    print(type(x),x,x.isdigit())
    if(x.isdigit()):
        num+=1
    elif (x.isalpha()):
        letter+=1

print(f"Num: {num} and Letter: {letter}")

#
# Solution: python
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha(): 
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])