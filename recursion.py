#def facto(n):
#   if n>0:
#        return n*facto(n-1)
#    else:
#        return 1
#
#a=int(input("enter the  number to find factorial "))
#print(facto(a))

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

a= int(input("enter the  number to  work with "))
for c in range(a):
    print(fibo(c))




