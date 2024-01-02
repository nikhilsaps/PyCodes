# finding th lcm of two number
num1=int(input("enter the number  "))
num2=int(input("enter the number  "))

hcm=num1*num2

lst = []
while hcm>0:
    if hcm % num1 == 0:
        if hcm % num2 == 0:
            lst.append(hcm)
    hcm-=1
print(min(lst))



