#checking if number si prime or not
a=int(input("enter the number"));

d=a-1
flag=0
while(d>=2):
    if a%d==0:
        flag=1
        break
    d-=1

if flag ==0 :
    print("prime")