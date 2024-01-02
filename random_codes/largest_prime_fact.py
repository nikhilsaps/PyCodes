#finding the largest prime factor of a given number

a=int(input("enter the  number to fidn its prime fact"))
gcd=[]
flag=0
d=a-1
while(d>=2):
    if a%d ==0:
        gcd.append(d)
    d-=1

print(gcd)
for x in gcd:
    d2=x-1
    while(d2>=2):
        if x%d2==0:
            flag=1
            break
        d2-=1
    if flag==0:
        print(x)
        break

