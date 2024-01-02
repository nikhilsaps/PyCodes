s= "is the worls is love fake no fae fake"
l=s.split(" ")
l.sort()
d={}
print(set(l))
for x in set(l):
    count=0
    for y in l:
        if x== y:
            count +=1
    d[x]=count

print(d)

