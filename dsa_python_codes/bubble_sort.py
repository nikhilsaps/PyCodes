a=[99,1,-2,88,3,4,-1,5]


i=0
while(i<len(a)-1):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
        i=0
    else:
        i+=1

print(a)