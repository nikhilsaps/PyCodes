# Level 2
# Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example:
# 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.



def bin_to_number(bin_list):
    index =len(bin_list)-1
    num=0
    for x in bin_list:
        num =num +int(x)*(2**index)
        index -= 1
    return num


binary_input= list(input("enter the binary number").split(","))

for x in binary_input:
    if (bin_to_number(list(x))%5==0):
        print(x)

#
# Solution: ```python
# value = []
# items=[x for x in input().split(‘,’)]
# for p in items:
#     intp = int(p, 2) if not intp%5: value.append(p)
# print(‘,’.join(value)) ```