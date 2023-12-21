#bubble sort program

l=[1,4,3,5,-1,6,8,-99]
i=0

while i<len(l)-1:
    if l[i]>l[i+1]:
        temp= l[i]
        l[i]=l[i+1]
        l[i+1]=temp
        i=0
    else:
        i+=1

print(l)

