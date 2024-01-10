# Level 2
# Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example:
# 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.



def bin_to_number(bin_list):
    index =len(bin_list)
    num=0
    while (index> 0):
        num=num+2**index
        index-=1
    return num

binary_input= input("enter the binary number").split()


print(bin_to_number(binary_input))


