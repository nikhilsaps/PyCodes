# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


n=  int(input("enter the number : "))
sum=[]
for  x in range(4):
     sum.append(str(n+10**x))
print(sum)