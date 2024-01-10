# Level 1
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
# contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: [‘34’, ‘67’,
# ‘55’, ‘33’, ‘12’, ‘98’] (‘34’, ‘67’, ‘55’, ‘33’, ‘12’, ‘98’)

input_str=input("enter the comma separated value")

print((input_str.split(',')))
print(tuple(input_str.split(',')))

# Solution: python
# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)
