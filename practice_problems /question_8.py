# Level 2
# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the
# output should be: bag,hello,without,world

data_list= input("enter the comma separated value ").split(",")
data_list.sort()
print(",".join(data_list))


# Solution: python
# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items)) 