#program to find the lcm of 2 number

a =int(input("enter the number"))
b =int(input("enter the number"))
factor_of_a=[]
factor_of_b=[]
d=a
while(d>1):
    if a%d==0:
        factor_of_a.append(d)
    d-=1
d=b
while(d>1):
    if b%d==0:
        factor_of_b.append(d)
    d-=1
#common factor
c=[]
for x in factor_of_a:
    for y in factor_of_b:
        if x==y:
            c.append(y)
print(max(c))