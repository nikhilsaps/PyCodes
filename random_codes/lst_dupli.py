#dupicate item in list

a=[1,2,3,3,4,6,2]

b=[]
for x in a:
    if x not in b:
        b.append(x)

print(b)

