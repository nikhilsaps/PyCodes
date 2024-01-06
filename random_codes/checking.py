a=[4,6,5,7,9,0,2,1,3]

x=0
while(x<len(a)-1):
    if a[x]>a[x+1]:
        a[x],a[x+1]=a[x+1],a[x]
        x=0
    x+=1

print(a)